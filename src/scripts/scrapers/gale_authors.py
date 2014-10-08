'''
Created on Oct 6, 2014

@author: dbhage

This script gets the HTML only for all authors (~24000 pages) which can later be parsed to get the names only. 
'''

import urllib2, socket, time

working_dir = "WORKING DIRECTORY"

url_part_1 = "http://www.galenet.com/servlet/LitIndex/hits?r=s&origSearch=false&o=DocTitle&n=10&l=8&c="
url_part_2 = "&secondary=false&u=LitIndex&t=KW&s=6&BO=is&BA=A.D.&DO=is&DA=A.D."

i=1

while (i <= 237981):
    url = url_part_1 + str(i) + url_part_2
    print (str(i) + ' -> ' + url)

    # Get a OpenerDirector instance from build_opener function.
    # Need to use a cookie processor since http cookies must be preserved from request to request
    httpRedirectHandler = urllib2.HTTPRedirectHandler()
    httpCookieProcessor = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(httpRedirectHandler, httpCookieProcessor)
    
    # The following block of code (try ... except...) tries to open the url
    # and read the content. There is a timeout of 10 in case the OpenerDirector.open
    # call hangs. If there is a timeout, socket.timeout is thrown, we sleep for 2 s
    # and then continue the loop without incrementing i (so we try to open the same
    # URL again).
    try:
        response = opener.open(url)
        content = response.read()
        with open(working_dir + "file" + str(i) + ".html", "w") as out_file:
            out_file.write(content)
    except socket.timeout:
        time.sleep(2)
        continue

    # increment i    
    i+=10