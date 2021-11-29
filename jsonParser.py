import sys
import json

jsonInput = ""

for line in sys.stdin:
    jsonInput += line

data = json.loads(jsonInput)

listOfPackages = ",".join([x["name"] for x in data])

print("::set-output name=PACKAGES::" + listOfPackages)