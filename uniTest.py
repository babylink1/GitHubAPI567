import unittest
from unittest.mock import patch, Mock
from HW04a import get_github_repositories_and_commits


class TestGitHubRepositoriesAndCommits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_get = patch('HW04a.requests.get').start()

    @classmethod
    def tearDownClass(cls):
        cls.mock_get.stop()

    def setUp(self):
        # 模拟请求成功的默认响应
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.text = '[{"name": "repo1"}, {"name": "repo2"}]'

    def test_successful_request_with_commits(self):
        # 模拟 repo1 和 repo2 含有不同数量提交的响应
        self.mock_get.side_effect = [
            # 对于 repo1
            Mock(status_code=200,
                 text='[{"commit": {"author": {"name": "John"}}}]'),

        ]

        user_id = "testuser"
        results = get_github_repositories_and_commits(user_id)

        # self.assertEqual(
        #     results[0], "Repo: repo1 Number of commits: 1")  # repo1有1个提交


if __name__ == '__main__':
    unittest.main()
