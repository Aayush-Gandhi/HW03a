import unittest
from unittest.mock import patch

class TestGitHubAPI(unittest.TestCase):

    @patch("requests.get")
    def test_valid_user(self, mock_get):
        # First call: repos
        mock_repos_response = unittest.mock.Mock(
            status_code=200,
            json=lambda: [{"name": "repo1"}]
        )
        # Second call: commits page 1 (5 commits)
        mock_commits_page1 = unittest.mock.Mock(
            status_code=200,
            json=lambda: [{}] * 5
        )
        # Third call: commits page 2 (empty → stop)
        mock_commits_page2 = unittest.mock.Mock(
            status_code=200,
            json=lambda: []
        )

        mock_get.side_effect = [mock_repos_response, mock_commits_page1, mock_commits_page2]

        from src.github_api import get_user_repos_and_commits
        result = get_user_repos_and_commits("someuser")
        self.assertEqual(result, [("repo1", 5)])

    @patch("requests.get")
    def test_user_not_found(self, mock_get):
        # Simulate 404 when fetching repos
        mock_get.return_value = unittest.mock.Mock(
            status_code=404,
            json=lambda: {}
        )

        from src.github_api import get_user_repos_and_commits
        result = get_user_repos_and_commits("invaliduser")
        self.assertEqual(result, [])

    @patch("requests.get")
    def test_repo_with_no_commits(self, mock_get):
        # First call: repos
        mock_repos_response = unittest.mock.Mock(
            status_code=200,
            json=lambda: [{"name": "repo1"}]
        )
        # Second call: commits page 1 (empty)
        mock_commits_page1 = unittest.mock.Mock(
            status_code=200,
            json=lambda: []
        )
        # Third call: commits page 2 (empty again to exit loop cleanly)
        mock_commits_page2 = unittest.mock.Mock(
            status_code=200,
            json=lambda: []
        )

        mock_get.side_effect = [mock_repos_response, mock_commits_page1, mock_commits_page2]

        from src.github_api import get_user_repos_and_commits
        result = get_user_repos_and_commits("someuser")
        self.assertEqual(result, [("repo1", 0)])


if __name__ == "__main__":
    unittest.main()
