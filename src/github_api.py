import requests

def get_user_repos_and_commits(user_id):
    """
    Given a GitHub user ID, return a list of tuples (repo_name, commit_count).
    Handles all repos of the user.
    """
    results = []
    try:
        # Get list of repositories for the user
        repo_url = f"https://api.github.com/users/{user_id}/repos"
        repo_response = requests.get(repo_url)
        repo_response.raise_for_status()
        repos = repo_response.json()

        for repo in repos:
            repo_name = repo.get("name", "Unknown")
            commit_count = 0
            page = 1

            # Loop through pages of commits
            while True:
                commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
                params = {"per_page": 100, "page": page}
                commit_response = requests.get(commits_url, params=params)

                if commit_response.status_code != 200:
                    break

                commits = commit_response.json()
                if not commits:
                    break  # stop if no more commits

                commit_count += len(commits)
                page += 1  # next page

            results.append((repo_name, commit_count))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    return results


if __name__ == "__main__":
    user = "Aayush-Gandhi"
    repos_and_commits = get_user_repos_and_commits(user)
    for repo, commits in repos_and_commits:
        print(f"Repo: {repo} Number of commits: {commits}")
