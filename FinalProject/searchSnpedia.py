#opens up vcf file and uses rsIds to make calls to SNPedia


import argparse
from wikitools import wiki  # https://github.com/alexz-enwp/wikitools
from wikitools import page

errMsg = "No match found"

#call to snpedia API
def search_snpedia(snp):
    """
    http://snpedia.com/index.php/Bulk
    """
    site = wiki.Wiki("http://bots.snpedia.com/api.php")
    pagehandle = page.Page(site,snp)
    try:
        snp_page = pagehandle.getWikiText()
        return snp_page
    except page.NoPage:
        return errMsg

#retrieving rsIds
num = []
snpnum = []
vcf = open("individualX.txt", "r") #opens file for reading
for line in vcf:
    data = line.split( )
    if data[2] is not '.':
        new = data[2]
        num.append(new)

snpediaFile = open("snpediaResults.txt", "w")

count = 1

#loop through rsIds and make calls to SNPedia
for id in num:
    if id != "ID":
        print id
        result = search_snpedia(id)
        if result != errMsg:
            snpediaFile.write("Match #" + str(count) + ": " + str(id) + "\n") #write to file if match in snpedia
            snpediaFile.write(result)
            snpediaFile.write("\n\n")
            count += 1
        print result

snpediaFile.close()
