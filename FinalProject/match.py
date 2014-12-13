#!/usr/bin/python

num = [] #contains all rsids
snpnum = [] #contains all rsids that match from omimdb
omimmatch = [] #omimids corresponding 

#gets all rs numbers for particular individual
vcf = open("individualX.txt", "r") #opens file for reading
for line in vcf:
	data = line.split( )
	if data[2] is not '.':
		new = data[2] #rsid
		new = new[2:] #removes rs
		num.append(new)

#gets all rs numbers from omimdb
snp = open("snp_omim.txt", "r")
for line in snp:
	data = line.split( )
	new1 = data[0]
	snpnum.append(new1)
snp.close()

#gets matches for rsids
matches =  set(num) & set(snpnum) 
#turns into list
match = list(matches)

#gets all matches and gets the omim numbers to store into omimmatch
snp = open("snp_omim.txt", "r")
for line in snp:
	print line
	data = line.split( )
	print data[0]
	for j in range(len(match)):
		if match[j] == data[0]:
			omimmatch.append(data[1]) #append data
				
#print matches
print snpnum
print match
print omimmatch

#create matchlist of rs ids
matchlist = 'matchlist.txt'
with open(matchlist, 'w') as fout:
	for id in matches:
  		fout.write(id)
  		fout.write("\n")

#create matchlist of omim ids
omim = 'omim.txt'
with open(omim, 'w') as omimout:
	for k in omimmatch:
  		omimout.write(k)
  		omimout.write("\n")
