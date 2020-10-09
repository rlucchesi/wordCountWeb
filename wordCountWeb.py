# 
# * Author:    Rafael Lucchesi
# * Created:   2020/10/07
#
# Goal: count the number of words on a hardcoded website
#

import urllib.request
from bs4 import BeautifulSoup

output = 0
lineList = [ ]
wordList = [ ]
url = 'https://www.globalrelay.com/'

htmlResponse = urllib.request.urlopen(url)
htmlContent = htmlResponse.read()

soup = BeautifulSoup(htmlContent, features="html.parser")

lineList = soup.text.split('\n')

for line in lineList:
	if len(line) > 0:
		wordList = line.split(' ')
		for word in wordList:
			if len(word) > 0 and (word[0].isalpha() or word[0].isnumeric()):
				output += 1

print(output)