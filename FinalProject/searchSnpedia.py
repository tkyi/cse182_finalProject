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


num = []
snpnum = []
vcf = open("individualX.txt", "r") #opens file for reading
for line in vcf:
    data = line.split( )
    if data[2] is not '.':
        new = data[2]
        num.append(new)

snpediaFile = open("snpediaResults.txt", "w")

for id in num:
    if id != "ID":
        print id
        result = search_snpedia(id)
        if result != errMsg:
            snpediaFile.write(str(id) + "\n") #write to file if match in snpedia
            snpediaFile.write(result)
            snpediaFile.write("\n\n")
        print result

snpediaFile.close()