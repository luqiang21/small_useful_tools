'''read xml file as dataframe'''
import xml.etree.ElementTree as ET
import pandas as pd

def xml2df(xml_file):
    xml_data = open(xml_file).read()

    root = ET.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    print len(all_records)
    return pd.DataFrame(all_records)

xml_file = 'youXMLFile'
df = xml2df(xml_file)

from lxml import objectify
import pandas as pd

def xml2df_(path):
    xml = objectify.parse(open(path))
    root = xml.getroot()

    columns = []
    for element in root.getchildren()[0].getchildren():
    #     print element.tag
        columns.append(element.tag)

    root.getchildren()[0].getchildren()


    n = len(root.getchildren())
    row_s = []
    for i in range(0,n):
        obj = root.getchildren()[i].getchildren()
        row = {}
        for idx in range(len(columns)):
            column = columns[idx]
            row[column] = obj[idx].text
        row_s.append(row)
        
    df = pd.DataFrame(row_s)
    return df
df2 = xml2df_(xml_file)
df2.head()
