import json
from xml.dom.pulldom import CHARACTERS

with open("dict.json"
          
          ) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
    
# product = jsonObject{'product'}
# overall = jsonObject['overall']
# text = jsonObject['text']

for key, value in jsonFile:
    print("key: ")
    print(key)