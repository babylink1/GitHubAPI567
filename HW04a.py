import requests
import json
"Lijuan Liu ,this script for Travis ci practice,11:00am,Oct.9,2023."


def get_github_repositories_and_commits(user_id):
    try:

        repositories_url = f"https://api.github.com/users/{user_id}/repos"

        response = requests.get(repositories_url)

        if response.status_code == 200:

            repositories_data = json.loads(response.text)

            # Initialize a list to store repository names and commit counts
            results = []

            # Iterate through each repository
            for repo_data in repositories_data:
                repo_name = repo_data["name"]

                # API endpoint to retrieve commits for the repository
                commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"

                # Send a GET request to retrieve commits
                commits_response = requests.get(commits_url)
                commits_data = json.loads(commits_response.text)

                # Get the number of commits
                commit_count = len(commits_data)

                # Add repository name and commit count to results
                results.append(
                    f"Repo: {repo_name} Number of commits: {commit_count}")

            return results
        else:
            return ["Error: Unable to retrieve data from GitHub API"]
    except Exception as e:
        return [f"Error: {str(e)}"]


# Example usage:
if __name__ == "__main__":
    user_id = "babylink1"
    results = get_github_repositories_and_commits(user_id)
    for result in results:
        print(result)
