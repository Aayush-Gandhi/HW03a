# demo.py
import sys
from src.github_api import get_user_repos_and_commits

def main():
    print("GitHub Repo Commit Counter")
    print("===========================")

    # If username is passed via command line, use it
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        # Otherwise, ask interactively
        try:
            username = input("Enter a GitHub username (or 'q' to quit): ").strip()
        except EOFError:
            print("⚠️ No input detected. Usage: python demo.py <username>")
            sys.exit(1)

    if username.lower() == "q":
        sys.exit(0)

    repos = get_user_repos_and_commits(username)

    if not repos:
        print(f"No repositories found for user '{username}' or user not found.")
    else:
        print(f"\nRepositories and commit counts for '{username}':\n")
        for repo, commits in repos:
            print(f"- {repo}: {commits} commits")

if __name__ == "__main__":
    main()
