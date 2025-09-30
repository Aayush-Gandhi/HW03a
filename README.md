# HW03a - GitHub API Repository Info

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Aayush-Gandhi/HW03a/tree/HW04c_Mocking.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Aayush-Gandhi/HW03a/tree/HW04c_Mocking)

## Overview
This project queries the GitHub API to retrieve a list of repositories for a given user and the number of commits in each repository.  

It includes:
- A core function (`get_user_repos_and_commits`) implemented in **`src/github_api.py`**  
- A simple demo program (**`demo.py`**) for interactive use  
- Unit tests in **`tests/test_github_api.py`**

---

## Requirements
- Python 3.8+
- `requests`
- `pytest`

Install dependencies:
```bash
pip install -r requirements.txt

## Usage

### Running the Demo
To run the interactive demo which shows repository information for a GitHub user:
```bash
python demo.py
```

Example output for user 'Aayush-Gandhi':
```
Repositories and commit counts:
- Fashion-Era: 2 commits
- First-Spline-3D: 3 commits
- HRMS: 2 commits
- HW03: 14 commits
- Kosol-Clone-Project-: 33 commits
- Magni-Era: 3 commits
- MedVision: 2 commits
- memo-invoice: 7 commits
- NFT-Dashboard: 10 commits
- Shopping-Cart: 4 commits
- SSW-567: 5 commits
```

### Running Tests
To run the unit tests with coverage report:
```bash
PYTHONPATH=$PYTHONPATH:./src pytest test.py -v --cov=src
```

## Function Documentation

### `get_user_repos_and_commits(user_id)`
Returns a list of tuples containing repository names and their commit counts for a given GitHub user.

Parameters:
- `user_id` (str): GitHub username

Returns:
- List of tuples (repo_name, commit_count)



## Running Tests
Run the tests (with mocks, no real API calls):
```bash
pytest -v
