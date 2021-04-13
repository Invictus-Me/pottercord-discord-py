import json
import requests
import random
import os, re, os.path

mainList = []
index = 0
f = open('Members.json','r')
data = json.load(f)
f.close()
MembersList = data["MembersList"]
MembersMedia = data["MembersMedia"]
MembersCaption = data["MembersCaption"]


haya = [":cat:", ':zany_face:',  ':snowflake:', ':clap:', ':heart_eyes:',':stuck_out_tongue_winking_eye:',':smirk_cat:',':smiling_imp:',':smile:',':rofl:',':pleading_face:',':face_with_hand_over_mouth:',':zany_face:']
YimYimList = {
 "default":"https://c.tenor.com/wnKNW5ObcX8AAAAM/shinoa-h%C4%ABragi-owari.gif",
 "kevnana":"https://cdn.discordapp.com/attachments/528123416746655754/826251701136654346/image0-13.png",
 "donut":"https://cdn.discordapp.com/attachments/656068195005759498/826073555363954707/1617021465703.png",
 "icecream":"https://cdn.discordapp.com/attachments/528123416746655754/825742059872452628/image0.png",
 "skyguette":"https://cdn.discordapp.com/attachments/528123416746655754/824077554054332426/image0-8.png", 
 "funeguette":"https://cdn.discordapp.com/attachments/528123416746655754/825632409164447754/1616911034792.png", 
 "cheesecat" : "https://cdn.discordapp.com/attachments/528123416746655754/824077553329111040/image0-8_1.png",
 "attac" : "https://c.tenor.com/WXbj6ZdOGHMAAAAM/shinoa-anime.gif",
 "welcome": "https://media.discordapp.net/attachments/825789253442338816/826115718893928449/NimWelcome.gif"
 }
YimYimIndexes = YimYimList.keys()


def stripCaption(caption):
	index = caption.find('#')
	return caption[:index].strip()

def getNishList():
	mypath = "nishPhotos"
	for root, dirs, files in os.walk(mypath):
		for file in files:
			os.remove(os.path.join(root, file))
	f = open('nishInsta.json',)

	data = json.load(f)
	graphql = data["graphql"]
	user = graphql["user"]

	postsBig = user["edge_owner_to_timeline_media"]
	edges = postsBig["edges"]

	finalList = []
	for i in edges:
		node = i["node"]
		photo = node["display_url"]
		caption = node["edge_media_to_caption"]["edges"][0]["node"]["text"]
		caption = stripCaption(caption)
		r = requests.get(photo)
		name = photo[229:239]
		with open("nishPhotos/"+name + ".jpg", 'wb') as f:
		    f.write(r.content) 
		dictTemp = {}
		dictTemp["image"] = name
		dictTemp["caption"] = caption
		finalList.append(dictTemp)

	return(finalList)

def getSkwiList():
	directory = r'skwiData'
	finalList = [[],[]]
	for filename in os.listdir(directory):
		if filename.endswith(".gif"):

			finalList[0].append(filename[:-4])
			finalList[1].append(os.path.join(directory, filename))
		else:
			continue
	print(finalList)
	return(finalList)

def replaceString(message, index, word):
	temp = message[0:index]
	temp2 = message[index+1:]
	message= temp + word + temp2
	return(message)

def addString(message, index, word):
	temp = message[0:index]
	temp2 = message[index:]
	message= temp + word + temp2
	return(message)

def checkSummer(message):
	listSummah = ['b', 'p', 'l', 's', '.', "'", '?', ' ']
	replace = [['b','l'], ['p','s']]
	index = 0
	listWords = message.split()
	flag = 1
	finalList = []
	for i in listWords:
		for k in i:
			if k not in listSummah:
				flag = 0
	if (flag == 1):
		return("You've sent a Summer Approved message ;P")
			
	for i in listWords:
		temp = i
		print(i)
		index = 0
		allowed = replace[random.randint(0,1)]
		print(allowed)
		for k in range(0,len(i)):
			if index == 0:
					temp = replaceString(temp, k , allowed[0])
			else:
				flag = 0
				temp = replaceString(temp, k , allowed[random.randint(0,1)])
			index = index + 1
		print("i = " , i , "temp = ", temp)
		finalList.append(temp)	
	finalMessage = ""
	print(finalList)

	for k in finalList:
		finalMessage = finalMessage + k + " "
		
	if(flag == 0):
		return (finalMessage)
	else:
		return("You've sent a Summer Approved message ;P")

def getNimArts(word):
	searchWord = word.lower().strip()
	if searchWord in YimYimList.keys():
		return(YimYimList[searchWord])

def getMembers(member):
	listMem = []
	if member.lower().strip() in MembersList:
		listMem.append(MembersMedia[member])
		listMem.append(MembersCaption[member])
	else:
		return( False )
	return listMem

def addMembers(name, url, desc):
	
	MembersList.append(name)
	MembersMedia[name] = url
	MembersCaption[name] = desc
	os.remove('Members.json')
	MembersJson = {}
	MembersJson["MembersList"] = MembersList
	MembersJson["MembersMedia"] = MembersMedia
	MembersJson["MembersCaption"] = MembersCaption

	f = open('Members.json', 'w')
	json.dump(MembersJson, f)
	f.close()

def amandify(message):
	newMessage = message
	for i in range(0, random.randint(1,5)):
		k = random.randint(0, len(newMessage)-1)
		if newMessage[k].isalpha():
			shift = ord(newMessage[k].lower())
			newMessage = addString(newMessage, k , chr(shift + random.randint(-5,5)))
		else:
			continue

	return newMessage

def hayafying(message):
    listM = message.split()
    k = ""
    for i in listM: 
        k += i + ' '+  haya[random.randint(0,len(haya)-1)]
    for i in range(0, random.randint(5,8)):
        k += haya[random.randint(0,len(haya)-1)]
    return (k)
