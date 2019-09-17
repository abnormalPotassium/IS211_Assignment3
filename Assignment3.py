import urllib.request
import csv
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('url')
args = parser.parse_args()

rawFile = urllib.request.urlopen(args.url).read()
file = csv.reader(rawFile.decode('utf-8').splitlines())
processedFile = [row[0:3:2] for row in file]

imgHits = [row[0] for row in processedFile if re.search('(?i).(?:jpg|jpeg|gif|png)$', row[0])]
imgTotal = len(imgHits)
total = len(processedFile)
imgPercent = imgTotal/total*100

print(f"Image requests make up {imgPercent}% of all requests.")

browserDict = {"Firefox":0, "Chrome":0, "Safari":0, "InternetExplorer":0}

#It took me quite a while to figure out a good solution to parse the strings because I noticed some strings had multiple browsers in them.
#However I noticed that while a Chrome browser may have Safari in the string, a Safari browser won't have Chrome in the string. There are a few rules like that which I ordered these by.

for row in processedFile:
    if re.search("Firefox", row[1]):
        browserDict["Firefox"] += 1
    elif re.search("Chrome", row[1]):
        browserDict["Chrome"] += 1
    elif re.search("Safari", row[1]):
        browserDict["Safari"] += 1
    elif re.search("MSIE", row[1]):
        browserDict["InternetExplorer"] += 1
    else:
        pass

browserSorted = sorted(browserDict.items(), key=lambda x: x[1], reverse=True)

print(f"The most popular browser today is {browserSorted[0][0]} with {browserSorted[0][1]} requests")