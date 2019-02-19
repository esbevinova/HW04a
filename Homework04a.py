import requests
import json


def getRep(gettingId):
    repos = retrieveRep(gettingId)
    dct = {}
    for repo in repos:
        repository = repo["name"]
        dct[repository] = getCommits(gettingId, repository)
    
    return dct

def retrieveRep(gettingId):
    url = "https://api.github.com/users/" + gettingId + "/repos"
    r = requests.get(url = url)
    data = r.json()
    return data 

def getCommits(gettingId, repoName):
    URL = "https://api.github.com/users/" + gettingId + "/" + repoName + "/commits"
    r = requests.get(url = URL)
    data= r.json()
    return len(data)

class TestGitHubAPI(object):
    def test_commitCount(self):
        assert len(getCommits("esbevinova", "hello_world")) > 0

    def test_getRepos(self):
        assert len(retrieveRep("helloworld")) >0
    
    def test_getCommits(self):
        assert getCommits('hello', 'Hi!') > 0     
    

if __name__ == '__main__':
    user = 'esbevinova'
    repoName = 'hello_world'
    print(f"{user} has {getCommits(user, repoName)} commits")
