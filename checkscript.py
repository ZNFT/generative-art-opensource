import json
import os
import sys

directory = "/Users/matthewcai/Documents/code/nft/generative-art-opensource/output"


attributesMap = {}

for fileName in os.listdir(directory):
    if fileName.endswith(".json"):
        print(fileName)
        data = json.load(open(directory+"/"+fileName))
        attributes = data['attributes']
        attributeArray = []    
        for itemCount, firstItem in enumerate(attributes):
            attributeArray.append(str(firstItem['value']))

        joinedAttributes = '-'.join(attributeArray)
        if joinedAttributes in attributesMap:
            print("issue")
            print(attributesMap[joinedAttributes])
            print(fileName)
        else:
            attributesMap[joinedAttributes] = fileName


