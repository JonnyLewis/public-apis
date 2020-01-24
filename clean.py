#!/usr/bin/python

import os.path
import re


class apiObject:
    def __init__(self, name, homePage, description, auth, https, cors):
        self.name = name
        self.homePage = homePage
        self.description = description
        self.auth = auth
        self.https = https
        self.cors = cors


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "README.md")

f = open(path, "r")
apis = []

for x in f:
    fields = x.split('|')
    arrayLength = len(fields)
    if ("**[" in x) or ("###" in x) or ("API | Description" in x):
        continue
    if arrayLength >= 2:
        s=x
        m = re.search(r"\[([A-Za-z0-9_]+)\]", s)
        e = re.search(r"\((.*?)\)", s)
        if m:
            api1 = apiObject(m.group(1), e.group(1), fields[2], fields[3], fields[4], fields[5])
            apis.append(api1)

for obj in apis:
    print obj.description

f.close()
