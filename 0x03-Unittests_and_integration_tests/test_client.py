#!/usr/bin/env python3
"""Test for the client module"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        expected_payload = {"login": org_name, "id": 12345}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL from org"""

        test_repos_url = "https://api.github.com/orgs/testorg/repos"
        payload = {"repos_url": test_repos_url}

        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("testorg")
            self.assertEqual(client._public_repos_url, test_repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient._public_repos returns
        the expected payload"""

        test_payload = [
                        {"name": "repo1"},
                        {"name": "repo2"},
                        {"name": "repo3"}
                        ]

        mock_get_json.return_value = test_payload

        test_url = "https://api/github.com/orgs/testotg/repos"

        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = test_url

            client = GithubOrgClient("testorg")
            result = client.public_repos()

            expected = ["repo1", "repo2", "repo3"]

            self.assertEqual(result, expected)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_licence", False),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({"license": {"key": None}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_client returns the correct license"""

        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
                      {
                       "org_payload": payload[0],
                       "repos_payload": payload[1],
                       "expected_repos": [repo["name"] for repo in payload[1]],
                       "apache2_repos": [
                           repo["name"]
                           for repo in payload[1]
                           if isinstance(repo.get("license"), dict) and
                           repo.get("license").get("key") == "apache-2.0"
                       ],
                       } for payload in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get with payloads"""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock_response = Mock()
            if url == f"https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = None
            return mock_response

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop requests.get patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repos"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering public repos by license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos
                         )
