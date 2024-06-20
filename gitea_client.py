"""Gitea API client."""

import os
import requests


class GiteaAPI:
    """Gitea API client."""

    def __init__(self, username: str, token: str, domain: str, repo_owner: str):
        self.username = username
        self.token = token
        self.domain = domain
        self.repo_owner = repo_owner

    def import_repo_from_github(self, repo_url: str, repo_name: str, is_private: bool):
        """Import a repository from GitHub to Gitea.
        Args:
            repo_url (str): URL of the repository to import.
            repo_name (str): Name of the repository.
            is_private (bool): Whether the repository is private or public.
        """
        data = {
            "auth_username": os.getenv("GITHUB_USERNAME"),
            "auth_password": os.getenv("GITHUB_TOKEN"),
            "clone_addr": repo_url,
            "mirror": False,
            "private": is_private,
            "repo_name": repo_name,
            "repo_owner": self.repo_owner,
            "service": "git",
            "uid": 0,
            "wiki": True,
        }
        response = requests.post(
            url=f"https://{self.domain}/api/v1/repos/migrate",
            auth=(self.username, self.token),
            json=data,
            timeout=10,
        )
        return response

    def delete_repository(self, owner: str, repo_name: str):
        """Delete a repository on Gitea.
        Args:
            owner (str): The owner of the repository.
            repo_name (str): The name of the repository to delete.
        """
        url = f"https://{self.domain}/api/v1/repos/{owner}/{repo_name}"
        headers = {"accept": "application/json", "Authorization": f"token {self.token}"}
        response = requests.delete(url=url, headers=headers, timeout=10)
        return response
