# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:52:17 2018

@author: adam.rees
"""

import requests

f = open("list.txt","r");

def file_len(k):
    for i, l in enumerate(k):
            pass
    i = i + 1
    return i

i = file_len(f)
j = 0
s = 0
problems = 0

contents = open("list.txt","r").readlines()
for c in contents:
    j = j + 1 
    print("Working on URL {0} of {1}".format(j,i))
    
    try:
        r = requests.head(c)
    except requests.exceptions.RequestException as e:
        print("Problem with {0}, exception: {1}".format(c,e))
        problems = problems + 1
        pass
            
    if r.ok:
        outF = open("alive.txt", "a+")
        outF.write(c)
        outF.close()
        print("URL {0} successful, adding it to Alive.txt".format(j))
        s = s + 1
    else:
        print("URL {0} unsucessful".format(j))

if s > 1:
    print("Out of {0} possible URLs, only {1} were found to be alive,"
          "and {2} threw an error".format(i,s,problems))
if s == 1:
    print("Out of {0} possible URLs, only {1} was found to be alive,"
          "and {2} threw an error".format(i,s,problems))
if s == 0:
    print("Out of {0} possible URLs, none were found to be alive,"
          "and {1} threw an error".format(i,problems))

f.close()
