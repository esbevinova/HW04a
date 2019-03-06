import requests
import json
import unittest
from unittest.mock import MagicMock as Mock
from unittest.mock import patch


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
    data = r.json()
    return len(data)
'''
class TestGitHubAPI(object):
    def test_commitCount(self):
        assert len(getCommits("esbevinova", "hello_world")) > 0

    def test_getRepos(self):
        assert len(retrieveRep("helloworld")) >0
    
    def test_getCommits(self):
        assert getCommits('hello', 'Hi!') > 0    
 
'''

class MyGreatClassTestCase(unittest.TestCase):

    @patch('requests.get')
    def testGetNumberOfCommits(self, mockedReq):
    #def testGetNumberOfCommits(self, mock_get_commit):
        
        #gc = mock_get_commit()
        #gc.return_value = '[{”hello_world”:1},{”hello_world”:2}]'
        #mockedReq.return_value = MockResponse("[{”sha”:1},{”sha”:2}]")
        user = 'esbevinova'
        repoName = 'hello_world'
        mockedReq.return_value.json.return_value = json.loads('[{"sha":1},{"sha":2}]')
        commits = getCommits(user, repoName)
        self.assertEqual(commits, 2)  


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    #print(f"{user} has {getCommits(user, repoName)} commits")


