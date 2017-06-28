'''Read csv and output xml'''
import csv

csvFile = 'alerts.csv'
# csvFile = 'test.csv'
def csv2xml(csvFile):
    name = csvFile.split('.')[0]
    xmlFile = name + '.xml'

    csvData = csv.reader(open(csvFile))
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    # there must be only one top-level tag
    xmlData.write("<" + name + ">" + "\n")

    rowNum = 0
    for row in csvData:
        # header -> tags
        if rowNum == 0:
            tags = row
            # replace spaces with underscores in tag names
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
        else: 
            xmlData.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlData.write('    ' + '<' + tags[i] + '>' \
                              + row[i] + '</' + tags[i] + '>' + "\n")
            xmlData.write('</row>' + "\n")

        rowNum +=1

    xmlData.write("</" + name + ">" + "\n")
    xmlData.close()
    print "XML file generated."
csv2xml(csvFile)
