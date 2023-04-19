import sys
import os

myFiles = os.listdir()
brRecs = []
for file in myFiles:
    if ('recB' in file) & ('.txt' in file):
        brRecs.append(file)

print(myFiles)
print(brRecs)
