import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

g = Github(os.environ['GIT_KEY'])

REPO_NAME = ''
USER_TO_BE_ADDED='' # Git Username

for repo in g.get_user().get_repos():
    if repo.name == REPO_NAME:
        repo.add_to_collaborators(USER_TO_BE_ADDED)
