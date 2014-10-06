'''
Created on Oct 6, 2014

@author: dbhage

Get author lists HTML from gale
'''

import urllib2

working_dir = "/home/dbhage/piperlab/authors_gale/"

url_part_1 = "http://www.galenet.com/servlet/LitIndex/hits?r=s&origSearch=false&o=DocTitle&n=10&l=8&c="
url_part_2 = "&secondary=false&u=LitIndex&t=KW&s=6&BO=is&BA=A.D.&DO=is&DA=A.D."

i=201

while (i <= 237981):

    url = url_part_1 + str(i) + url_part_2
    print (str(i) + ' -> ' + url)
    response = urllib2.urlopen(url)

    with open(working_dir + "file" + str(i) + ".html", "w") as out_file:
        out_file.write(response.read())
    
    i+=10