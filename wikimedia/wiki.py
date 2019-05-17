#!/usr/bin/python3

import requests

class Wikisearch:

    def __init__(self, lieu):
        self.lieu = lieu

    def getPlace(self):
        S = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
                    'action':"opensearch",
                    'search': self.lieu,
                    'format':"json",
                }

        DATA = S.get(url=URL, params=PARAMS).json()
        print(DATA)

endroit = Wikisearch("baguette")
liste_lieu = endroit.getPlace()

#with open("result.json", "x", encoding="utf_8") as json_data:
#        json.dump(PAGES, json_data, indent=4)