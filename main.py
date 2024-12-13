import os
import re
import sys

from github import Github
from github.File import File
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest

# Function to get changed files of a pull request
def get_pr_files(org_repo: str, pr_num : int, github:Github) -> PaginatedList[File]:
    try:
        repo = github.get_repo(org_repo)
        pull_request = repo.get_pull(pr_num)
        files = pull_request.get_files()
        return files

    except Exception as e:
        print(f"Error in retrieving the changed files in the PR : {e}")
        sys.exit(1)

# Function to add a comment on a pull request
def add_comment(org_repo: str, pr_num: int, comment: str, github: Github) -> None:
    try:
        repo = github.get_repo(org_repo)
        issue = repo.get_issue(number=pr_num)
        issue.create_comment(body=comment)

    except Exception as e:
        printf(f"Error adding comment on PR : {e}")

'''
# Function to filter PRs by source branch regex
def get_prs_by_branch_regex(org_repo: str, branch_regex: str, github: Github) -> list[PullRequest]:
    try:
        repo = github.get_repo(org_repo)
        all_prs = repo.get_pulls(state="open")

        source_branch_regex = re.compile(branch_regex)
        filtered_prs = [pr for pr in all_prs if source_branch_regex.match(pr.head.ref)]
        return filtered_prs

    except Exception as e:
        print(f"Error retrieving filtered PRs : {e}")
        sys.exit(1)
'''

def main() -> None:
    '''
    org_repo = os.environ["ORG_REPO"]
    token = os.environ["GITHUB_TOKEN"]

    #github = Github(base_url = "https://github.com/OSrivalli/Legal_check", login_or_token = token)

    #pull_request = get_prs_by_branch_regex(org_repo, source_branch_regex, github)
    #failing_prs = [pr for pr in pull_requests if not are_checks_assing(pr)]

    #if len(failing_prs) > 0:
    #    print(f"Failing PRs")
    #    sys.exit(1)

    add_comment(org_repo, pr_num, pr_comment, github)
    '''
    print("HEllooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    
main()
  
        
