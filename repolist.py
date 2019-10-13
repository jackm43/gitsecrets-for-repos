import os, sys
import subprocess
import getpass
from github import Github

# basic details for auth
get_token = getpass.getpass("Enter GH Personal Access Token:")
GITHUB_TOKEN = Github(get_token)
ORG = ""


#create some empty lists
repo_list = []
repo_name_list = []
ignore_these = [
    #put repos you don't want to scan here
    ''
    ''
]

# pull full name and URL.. want repo_name_list to be used as results.json in sh file in future
# this is here because gitleaks doesnt currently let you ignore archived repos

def get_all_repos():
    for repo in GITHUB_TOKEN.get_organization(ORG).get_repos():
        if not repo.archived:
            x = "{repo.full_name}".format(repo=repo)
            repo_name_list.append(x)
            repo_list.append(repo.clone_url)

def remove_stuff():
    for ignore_these in repo_list:
        repo_list.remove(ignore_these)

def single_repo():
    singlerepo_input = input('Enter repo:')
    singlerepo = ('VGW/' + singlerepo_input)
    for repo in GITHUB_TOKEN.get_organization(ORG).get_repos():
        if not repo.archived and repo.full_name == singlerepo:
                print('Found', singlerepo)
                print('Found clone_url', repo.clone_url)
                repo_list.append(repo.clone_url)
                return repo.clone_url
                
# args on run

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    if action == '--singlerepo':
        single_repo()
        print(single_repo)
    elif action == '--all':
        get_all_repos()

if __name__ == "__main__":
    main()

remove_stuff()

# send vars over to my good friend run.gitleaks_full.sh
print("Sending GitHub links to docker")
os.putenv('URLS', ' '.join(repo_list))
os.putenv('filename', ' '.join(repo_name_list))
subprocess.call('./run_gitleaks_full.sh')