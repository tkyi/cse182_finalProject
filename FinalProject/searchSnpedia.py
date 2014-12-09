
import argparse
from wikitools import wiki  # https://github.com/alexz-enwp/wikitools
from wikitools import page

poopoo = "no page found"
 
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
        return poopoo
    
 
# def _main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('snp', type=str, help='snp like `rs3`')
#     args = parser.parse_args()
 
#     found = search_snpedia(args.snp)
#     print found
 
# if __name__ == '__main__':
#     _main()


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
        # result = search_snpedia("rs55700207")
        # id = "rs4778138"
        result = search_snpedia(id)
        snpediaFile.write(str(id) + "\n")
        snpediaFile.write(result)
        snpediaFile.write("\n\n")
        print result

snpediaFile.close()
