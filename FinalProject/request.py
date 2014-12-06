import requests
import xmldict

#idconverter = {}
#ids = open("snp_omim.txt","r")
#for line in ids:
#    line = line.rstrip('\n')
#    currPair = line.split(" ")
#    idconverter[currPair[0]] = currPair[1]
#ids.close()
#mim = list(idconverter.values())  

#converting dict to html
def prettyTable(dictionary, cssClass=''):
        ''' pretty prints a dictionary into an HTML table(s) '''
        if isinstance(dictionary, str):
            return '<td>' + dictionary + '</td>'
        s = ['<table ']
        if cssClass != '':
            s.append('class="%s"' % (cssClass))
        s.append('>\n')
        for key, value in dictionary.iteritems():
            s.append('<tr>\n  <td valign="top"><strong>%s</strong></td>\n' % str(key))
            if isinstance(value, dict):
                if key == 'picture' or key == 'icon':
                    s.append('  <td valign="top"><img src="%s"></td>\n' % prettyTable(value, cssClass))
                else:
                    s.append('  <td valign="top">%s</td>\n' % prettyTable(value, cssClass))
            elif isinstance(value, list):
                s.append("<td><table>")
                for i in value:
                    s.append('<tr><td valign="top">%s</td></tr>\n' % prettyTable(i, cssClass))
                s.append('</table>')
            else:
                if key == 'picture' or key == 'icon':
                    s.append('  <td valign="top"><img src="%s"></td>\n' % value)
                else:
                    s.append('  <td valign="top">%s</td>\n' % value)
            s.append('</tr>\n')
        s.append('</table>')
        return '\n'.join(s)

matches = open("matchlist.txt", "r")
mim = matches.read()
mim = mim.split('\n')
del mim[-1] #get rid of extra empty ID at end of list

fuzzyFile = open("fuzzyTurtle.html", "w")

print mim
print len(mim)

#make calls to OMIM database
for x in range(len(mim)):
    mimNumber = mim[x]
    url = "http://api.omim.org/api/entry?apiKey=2D38BBD07E6389672AE6469A244285FA6C7209F2&include=all&mimNumber=" + mimNumber
    r = requests.get(url)
    individualXDict =  xmldict.xml_to_dict(r.content)['omim']
    fuzzyFile.write(prettyTable(individualXDict))
    # print(r.content)
    
fuzzyFile.close()  #type 'open fuzzyTurtle.html' to view in browser