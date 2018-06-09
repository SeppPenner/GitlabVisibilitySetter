import requests
import sys
import json

gitlabBaseAddress = "https://gitlab.com/api/v4/"
userName = "YourUserName"
token = "1234567890"

def loadRepositoriesForDefinedUser():
	"Loads all repositories for the defined user id from gitlab.com"
	try:
		totalConnectionString = gitlabBaseAddress + "users/" + str(userName) + "/projects?private_token=" + str(token)
		response = requests.get(totalConnectionString)
		lastPage = loadLastPageOfRepositories(response)
		data = []
		for currentPageNumber in range(1, lastPage + 1):
			print('Loading page ' + str(currentPageNumber))
			resultData = loadPageRepositories(currentPageNumber)
			jsonData = json.loads(resultData)
			for repository in jsonData:
				id = repository['id']
				makeRepositoryPubliclyVisible(id)
			print("---------------------------------------------------")
		print("All gitlab repositories loaded.")
	except:
		print("Unexpected error:", sys.exc_info()[0])

def loadLastPageOfRepositories(response):
	"Finds the last page of the users repositories"
	print(response)
	link = response.headers["Link"]
	lastPageLink = link.split(",")
	startPosition = lastPageLink[2].find("&page=")
	endPosition = lastPageLink[2].find("&per_page=")
	lastPageWithText = lastPageLink[2][startPosition:endPosition]
	lastPage = lastPageWithText.split("=")[1]
	print("Last page is: " + str(lastPage))
	return int(lastPage)

def loadPageRepositories(pageNumber):
	"Loads the repositories for the given page"
	totalConnectionString = gitlabBaseAddress + "users/" + str(userName) + "/projects?page=" + str(pageNumber) + "&per_page=20&private_token=" + str(token)
	response = requests.get(totalConnectionString)
	return response.content
	
def makeRepositoryPubliclyVisible(id):
	"Sets the project status to be publicly visible"
	totalConnectionString = gitlabBaseAddress + "projects/" + str(id) + "?private_token=" + str(token)
	print(totalConnectionString)
	payload = {'visibility': 'public'}
	response = requests.put(totalConnectionString, data=payload)
	print(response)

loadRepositoriesForDefinedUser()