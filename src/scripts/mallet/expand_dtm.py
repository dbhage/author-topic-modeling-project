'''
Created on Sep 29, 2014

@author: dbhage

Expand a document-term matrix into a folder with individual files containing words
'''

from util.string import replace_uhmlauts
dtm_file_name = "" #"PATH TO DTM FILE"
folder_name = "OUTPUT FOLDER"

with open(dtm_file_name, 'r') as fd:

    i=0
    header = None
    
    for line in fd:
        if i==0:
            i+=1
            header = line.split(',')
            header = map(replace_uhmlauts, header)
            continue
        
        # row
        row = line.split(',')

        # get file name and offset
        # account for comma(s) in file name
        m=1
        while (1):
            try:
                int(row[m])
                fname = ""
                for n in range(0,m): 
                    fname += row[n]
                fname = fname.replace('"', '')
                offset = m-1
                break
            except ValueError:
                m+=1
                
        print (fname)
        
        with open(folder_name + '/' + fname, 'w') as output_fd:
            for j in range(1, len(header)):
                word = header[j]
                count = int(row[j + offset])
                if count > 0:
                    output_fd.write((word + ' ') * count)                    