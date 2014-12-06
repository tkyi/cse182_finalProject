import requests

#idconverter = {}
#ids = open("snp_omim.txt","r")
#for line in ids:
#    line = line.rstrip('\n')
#    currPair = line.split(" ")
#    idconverter[currPair[0]] = currPair[1]
#ids.close()
#mim = list(idconverter.values())  

matches = open("matchlist.txt", "r")
mim = matches.read()
mim = mim.split('\n')

print mim
print len(mim)
for x in range(len(mim)):
	mimNumber = mim[x]
	url = "http://api.omim.org/api/entry?apiKey=2D38BBD07E6389672AE6469A244285FA6C7209F2&include=all&mimNumber=" + mimNumber
	r = requests.get(url)
	print(r.content)
	
