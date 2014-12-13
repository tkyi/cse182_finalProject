CSE 182 Final Project README.txt
Fuzzy Turtles Group:
Danny Hsiung
Tiffany Kyi
Veronica Khauv
Sneha Jayaprakash

We have implemented two different pipelines in order to replicate Promethease functionality. Everything was implemented 
using Python.

The first pipeline uses the OMIM database. In match.py SNPs from individualX's VCF file(in txt format) are extracted and 
matched to its mim ID counterpart using the snp_omim.txt found on OMIM. Each entry in the file represents a 1 to 1 mapping 
of SNP ids (rs######) matched to an omim ID (#####). Entries that have a match are outputted to matchlist.txt and are then 
passed into request.py, which makes a RESTful call to the OMIM database, and returns an XML of the entries we queried using 
the omim ID. We then parse the XML into an HTML and output this HTML as fuzzyTurtle.html.
Commands: python request.py
          open fuzzyTurtle.html

Our second pipeline directly queries the SNPedia database. By running searchSnpedia.py, we directly search the SNPedia database
by reading each item in indivdualX's VCF file (in txt format). Each call takes about 5 seconds, and many of individualX's entries
do not have one in the SNPedia database. 
This action takes about 26 hours to complete, and often times it fails. A bunch of entries were outputted into bunchOfSnpediaMatches.txt.
We compiled as many interesting results as we could and manually displayed it in our version of Promethease...GENEius.html. 
Commands: python searchSnpedia.py
          open GENEius.html
