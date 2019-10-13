# gitsecrets-for-repos

# Requirements / dependancies

Github Personal Access Token with repo.read all

Python3 

Github library for Python

```pip install PyGithub```

Docker

# Usage

Before running, currently you have to run export to get your Github token into the sh script.

```export GITHUB_TOKEN=""```

To scan a single repo:

```python3 repolist.py --singlerepo ```

To scan all repos(this takes a long time):

```python3 repolist.py --all```

Edit run_gitleaks_full.sh `depth` command for how many commits you want to scan. If you want to scan all, remove the line all together

If you are running this on a big EC2 instance you can make the full repo scan go HELLA fast if you edit run_Gitleaks_full.sh to use all your cpu via --threads

# To-do

~~Add options for single repo by entering direct name~~

Improve authentication instead of having to enter PAT in python file & export to use in sh file with docker file

Investigate ECS/lambda usage

Implement single repo scan for on-commit hook on latest scan

Visualisation
