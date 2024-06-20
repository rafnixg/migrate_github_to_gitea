"""Migrate repositories from GitHub to Gitea."""

import os

from gitea_client import GiteaAPI
from github_client import GithubAPI

from dotenv import load_dotenv

load_dotenv()


class MigrationManager:
    """Manager to migrate repositories from GitHub to Gitea."""

    def __init__(self):
        # Check if all required environment variables are set
        if not all(
            [
                os.getenv("GITHUB_USERNAME"),
                os.getenv("GITHUB_TOKEN"),
                os.getenv("GITEA_USERNAME"),
                os.getenv("GITEA_TOKEN"),
                os.getenv("GITEA_DOMAIN"),
                os.getenv("GITEA_REPO_OWNER"),
            ]
        ):
            raise ValueError("Missing environment variables")

        # Initialize API clients
        self.github_api = GithubAPI(
            username=os.getenv("GITHUB_USERNAME"), token=os.getenv("GITHUB_TOKEN")
        )
        self.gitea_api = GiteaAPI(
            username=os.getenv("GITEA_USERNAME"),
            token=os.getenv("GITEA_TOKEN"),
            domain=os.getenv("GITEA_DOMAIN"),
            repo_owner=os.getenv("GITEA_REPO_OWNER"),
        )

    def migrate_repos(self, is_private: bool):
        """Migrate repositories from GitHub to Gitea.
        Args:
            is_private (bool): Whether to migrate private or public repositories.
        """
        repos = self.github_api.get_repos_by_visibility(is_private)
        for repo_url in repos:
            repo_name = repo_url.replace(
                f"https://github.com/{self.github_api.username}/", ""
            )
            if "github.com" in repo_name:
                print(f"Invalid URL: {repo_url}")
                continue
            print(f"Found {repo_name}, importing...")

            response = self.gitea_api.import_repo_from_github(
                repo_url, repo_name, is_private
            )
            if response.status_code == 201:
                print(f"Successfully imported {repo_name}")
            else:
                print(f"Failed to import {repo_name}: {response.text}")

    def migrate_all_repos(self):
        """Migrate all repos"""
        print("Importing Public")
        self.migrate_repos(is_private=False)
        print("Importing Private")
        self.migrate_repos(is_private=True)

    def delete_repos_migrated(self, is_private: bool):
        """Delete all repos migrated"""
        repos = self.github_api.get_repos_by_visibility(is_private)
        for repo_url in repos:
            repo_name = repo_url.replace(
                f"https://github.com/{self.github_api.username}/", ""
            )
            if "github.com" in repo_name:
                print(f"Invalid URL: {repo_url}")
                continue
            print(f"Found {repo_name}, importing...")
            response = self.gitea_api.delete_repository(
                self.gitea_api.repo_owner, repo_name
            )
            if response.status_code == 204:
                print(f"Repository {repo_name} deleted successfully.")
            else:
                print(
                    f"Failed to delete repository {repo_name}. Status code: {response.text}"
                )

    def delete_all_repos_migrated(self):
        """Delete all repos migrated"""
        print("Delete: Public")
        self.delete_repos_migrated(is_private=False)
        print("Delete: Private")
        self.delete_repos_migrated(is_private=True)
