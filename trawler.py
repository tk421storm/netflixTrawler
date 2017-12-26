import re

queueFile=open("queue.html","r")

rawMoviesInstant=[]

with queueFile:
	for line in queueFile:
		if 'Watch \'' in line:
			watchList=[m.start() for m in re.finditer('Watch \'', line)]
			for charNum in watchList:
				rawMoviesInstant.append(line[charNum-600:charNum+50])

rawMoviesDic={}

for rawGarbage in rawMoviesInstant:
	rawMoviesDic[rawGarbage.split('Watch \'')[1].split('\'')[0]]=rawGarbage.split('Watch \'')[0].split('?')[0][-8:]

print rawMoviesDic

moviesToAdd={}
listFile=open("myList.html","r")


with listFile:
	fileLines = list(listFile)

for movie in rawMoviesDic:
	print "checking if "+movie+" is already on my list"
	found=False
	for line in fileLines:
		if movie in line:
			listEntry=[m.start() for m in re.finditer(movie, line)]
			for charNum in listEntry:
				print "found "+movie+" at:"
				print line[charNum-600:charNum+50]
				found=True
	if not found:
		moviesToAdd[movie]=rawMoviesDic[movie]

print moviesToAdd
urlList=""

for movie in moviesToAdd:
	urlList+='http://www.netflix.com/title/'+moviesToAdd[movie]+"\n"

outputFile=open("output.txt","w")
with outputFile:
	outputFile.write(urlList)

print "list of urls to add stored in output.txt"

