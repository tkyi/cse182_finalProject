CSE 182 Final Project README.txt
Fuzzy Turtles Group:
Danny Hsiung
Tiffany Kyi
Veronica Khauv
Sneha Jayaprakash

We have two solutions that replicate the Promethease functionality. Everything was implemented using python.

The first pipeline uses match.py, to extract the SNPs from individualX's VCF file(in txt format), and matches it with the snp_omim.txt entries.
These entries represent a 1 to 1 mapping of SNP ids (rs######) matched to an omim ID (#####). Entries that have a match (matchlist.txt), are then passed into request.py, which makes a RESTful call to the OMIM database, and returns an XML of the entries we queried using the omim ID. We then parse the XML into an HTML, and we output this HTML as fuzzyTurtle.html.

Our second pipeline directly queries the SNPedia database. By running searchSnepedia.py, we directly search the SNPedia databased, by reading each item in indivdualX's VCF file (in txt format). Each call takes about 5 seconds, and many of individualX's entries do not have one in the SNPedia database. 
This action takes about 26 hours to complete, and often times it fails. We compiled as many interesting results as we could, and manually displayed it in our version of Promethease....GENEius.html. 