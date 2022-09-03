"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
from IPython.display import display
from ipywidgets import IntProgress
import requests

# Data Science libraries
import pandas as pd

import time
from requests import get

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_search(query, page):
    # topic_search_url': 'https://api.github.com/search/topics?q={query}{&page,per_page}',
    base_url = 'https://api.github.com/'
    url = f"{base_url}search/repositories?q={query}&page={page}&per_page=100"
    time.sleep(2)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Something went wrong. Status {response.status_code}')
    else:
        return response.json()

def new_github_urls():
    urls = []
    page = 0
    f = IntProgress(min=0, max=1000, description='Getting URLs')
    display(f)
    while len(urls) <= 900:
        f.value = len(urls)
        page += 1
        items = github_search('stars%3A%3E1&s=forks&type=Repositories', page)['items']
        for item in items:
            urls.append(item['full_name'])
    return urls

# returns a list of github repo names, either from a file on disk or from github using the fetch_github_repos function
def get_github_repos(refresh=False ):
    # If the cached parameter is false, or the csv file is absent, use github
    if refresh == True or os.path.isfile('git_urls.csv') == False:
        # read from github
        repo_list = new_github_urls()
        # and write to the cache file for next time
        df = pd.DataFrame(repo_list, columns=['repos'])
        df.to_csv('git_urls.csv', index=False)
    else:
        # read from the cache file on disk
        df = pd.read_csv("git_urls.csv")
        repo_list = df['repos'].to_list()

    # either way, return the list of repos
    return repo_list

REPOS = get_github_repos()

def github_api_request(url: str) -> Union[List, Dict]:
    time.sleep(0.25)
    print(url)
    response = requests.get(url, headers=headers, timeout=60)
    response_data = response.json()
    if int(response.headers['X-RateLimit-Remaining']) < 10:
        print('Rate-limit exceeded. Slowing down.')
        time.sleep(60)
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    try:
        readme_contents = requests.get(get_readme_download_url(contents)).text
    except:
        readme_contents = ''
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    f = IntProgress(min=0, max=len(REPOS), description='Downloading Data')
    display(f)
    output = []
    for i, repo in enumerate(REPOS):
        f.value = i
        output.append(process_repo(repo))
    return output


# if __name__ == "__main__":
#     data = scrape_github_data()
#     json.dump(data, open("data2.json", "w"), indent=1)


def get_data(refresh=False):
    filename = './data.csv'
    if refresh or not os.path.isfile(filename):
        data = scrape_github_data()
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
    else:
        df = pd.read_csv(filename)
    return df


def wrangle_data():
    df = get_data()

    return df