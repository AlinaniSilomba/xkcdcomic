import requests

#This is out business logic for getting the data from xkcd.com


def GetCurrentComic():
    baseUrl = "https://xkcd.com/info.0.json"
    response = requests.get(baseUrl)
    response.raise_for_status()
    data = response.json()
    return data
    

def GetRandomComic(comicNumber):
    baseUrl = f"https://xkcd.com/{comicNumber}/info.0.json"
    response = requests.get(baseUrl)
    response.raise_for_status() 
    data = response.json()
    return data