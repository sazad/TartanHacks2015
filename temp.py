from __future__ import print_function
import os

directory = "static"
current = "none"
for file in os.listdir(directory):
    print (file)
    keywords = file.replace(".", " ").split(" ")
    for k in keywords:
        print (k)
