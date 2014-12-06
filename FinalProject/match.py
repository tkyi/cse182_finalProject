#!/usr/bin/python

num = []
snpnum = []
vcf = open("individualX.txt", "r") #opens file for reading
for line in vcf:
	data = line.split( )
	if data[2] is not '.':
		new = data[2]
		new = new[2:]
		num.append(new)

snp = open("snp_omim.txt", "r")
for line in snp:
	data = line.split( )
	new = data[1]
	new = new[0:]
	snpnum.append(new)


matches =  set(num) & set(snpnum)
print matches

print len(matches)
print len(snpnum)
print len(num)

matchlist = 'matchlist.txt'
with open(matchlist, 'w') as fout:
	for id in matches:
  		fout.write(id)
  		fout.write("\n")
	
