import unittest
from unittest.mock import patch, Mock

# Import the function under test
from src.github_api import get_user_repos_and_commits


class TestGitHubAPI(unittest.TestCase):
    """Unit tests for get_user_repos_and_commits with mocked GitHub API calls"""

    @patch("requests.get")
    def test_valid_user_with_commits(self, mock_get):
        """
        Simulates a valid GitHub user with one repo and 5 commits.
        Checks that the function correctly counts commits.
        """

        # Mock repo list response
        mock_repos_response = Mock(status_code=200, json=lambda: [{"name": "repo1"}])

        # Mock commits: page 1 has 5 commits, page 2 is empty (end of commits)
        mock_commits_page1 = Mock(status_code=200, json=lambda: [{}] * 5)
        mock_commits_page2 = Mock(status_code=200, json=lambda: [])

        # Responses in the order the function calls requests.get
        mock_get.side_effect = [mock_repos_response, mock_commits_page1, mock_commits_page2]

        result = get_user_repos_and_commits("someuser")
        self.assertEqual(result, [("repo1", 5)])


    @patch("requests.get")
    def test_user_not_found(self, mock_get):
        """
        Simulates a 404 response when fetching repos for an invalid user.
        Function should return an empty list.
        """

        mock_get.return_value = Mock(status_code=404, json=lambda: {})

        result = get_user_repos_and_commits("invaliduser")
        self.assertEqual(result, [])


    @patch("requests.get")
    def test_repo_with_no_commits(self, mock_get):
        """
        Simulates a repo that exists but has zero commits.
        Function should return commit count as 0.
        """

        # Mock repo list response
        mock_repos_response = Mock(status_code=200, json=lambda: [{"name": "repo1"}])

        # Mock commits: immediately empty
        mock_commits_page1 = Mock(status_code=200, json=lambda: [])
        mock_commits_page2 = Mock(status_code=200, json=lambda: [])

        mock_get.side_effect = [mock_repos_response, mock_commits_page1, mock_commits_page2]

        result = get_user_repos_and_commits("someuser")
        self.assertEqual(result, [("repo1", 0)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
