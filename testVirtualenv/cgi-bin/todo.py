#!/usr/bin/env python3

import os
import yaml

myFile = open('cgi-bin/yaml.txt', 'r')
myDict = yaml.load(myFile)
myFile.close()


print("Content-type: text/html")
print("")
myDictKeys = myDict.keys()
print(myDictKeys)
print("    ")
print("Dictionary Reference for yaml.txt : ")
print(myDict)
print("")
print("<h1>To-Do List</h1>")

for header in myDictKeys:

    print("<li>")
    print(myDictKeys[header])
    print("</li>")
    
    for listItems in myDictKeys:


        print("<li>")
        print(myDict[header][listItems])
        print("</li>")
