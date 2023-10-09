import unittest
from unittest.mock import patch, Mock
from HW04a import get_github_repositories_and_commits


class TestGitHubRepositoriesAndCommits(unittest.TestCase):

    @patch('HW04a.requests.get')
    def test_successful_request(self, mock_get):
        # Mock a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '[{"name": "repo1"}, {"name": "repo2"}]'

        # Mock the response for repo1 with some commits
        mock_get.side_effect = [
            mock_get.return_value,  # For repo1
            # For repo2
            Mock(status_code=200,
                 text='[{"commit": {"author": {"name": "John"}}}]'),
        ]

        user_id = "testuser"
        results = get_github_repositories_and_commits(user_id)

        self.assertEqual(len(results), 2)
        self.assertEqual(
            results[0], "Repo: repo1 Number of commits: 1")  # Now repo1 has 1 commit
        self.assertEqual(
            results[1], "Repo: repo2 Number of commits: 1")  # Repo2 also has 1 commit

    @patch('HW04a.requests.get')
    def test_failed_request(self, mock_get):
        # Mock a failed response
        mock_get.return_value.status_code = 404

        user_id = "testuser"
        results = get_github_repositories_and_commits(user_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0], "Error: Unable to retrieve data from GitHub API")


if __name__ == '__main__':
    unittest.main()
