# Basics of Coding R/Python
# 1. Using Comments R/Python
# 2. Executing Commands R/Python
# 3. Importing Packages R/Python
# 4. Getting Data into python
# 5. Saving Output R/Python
# 6. Accessing Records and Variables R/Python

#**********************************************************************
#USING COMMENTS IN PYTHON

# This is a inline sample comment.
'''
This is a multiline
sample comment.
'''
#IMPORTING PACKAGES IN PYTHON

import re
import os

# GETTING DATA INTO PYTHON

import requests
import json
response_API =
requests.get(```https://api.covid19india.org/state_district_wise.json```)
#print(response_API.status_code)

#SAVING OUTPUT R PYTHON

import sys
stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w")

# ACCESSING RECORDS AND VARIABLES PYTHON

#creating class
class student:
# constructor
def __init__(self, name, rollno):
# instance variable
self.name = name
self.rollno = rollno
def display(self):
# using self to access
# variable inside class
print("hello my name is:", self.name)
print("my roll number is:", self.rollno)
# Driver Code
# object created
s = student('HARRY', 1001)
# function call through object
s.display()
# accessing variable from
# outside the class
print(s.name)
