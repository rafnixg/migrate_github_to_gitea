"""GitHub API Client"""

import requests


class GithubAPI:
    """Github API client."""

    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"

    def get_repos(self):
        """Get all repositories from the authenticated user."""
        url = f"{self.base_url}/user/repos?per_page=200&visibility=all"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {self.token}",
        }
        response = requests.get(url=url, headers=headers, timeout=10)
        if response.status_code == 200:
            return [repo["html_url"] for repo in response.json()]
        else:
            print(f"Error fetching repositories: {response.status_code}")
            return []

    def get_repos_by_visibility(self, is_private: bool):
        """Get all repositories from the authenticated user by visibility.
        Args:
            is_private (bool): Whether to fetch private or public repositories.
        """
        url = f"{self.base_url}/user/repos?per_page=200"
        url_visibility = f"{url}&visibility={'private' if is_private else 'public'}"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {self.token}",
        }
        response = requests.get(url=url_visibility, headers=headers, timeout=10)
        if response.status_code == 200:
            return [repo["html_url"] for repo in response.json()]
        else:
            print(f"Error fetching repositories: {response.status_code}")
            return []
