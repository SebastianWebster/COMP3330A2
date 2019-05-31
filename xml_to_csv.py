#This will convert the xml file that image labeller generates into an CSV file that we can easily read into our AI
#https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py
#Shout outs datitran
import os
import glob #Globbing utility finds files with pattern matching
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'): #Find all files with the suffix xml and returns them as a list opf strings
        tree = ET.parse(xml_file) #Take the files from the globbing and parse them as xml objects
        root = tree.getroot()
        for member in root.findall('object'): #for each 'object' in this case each label read the relevent data into an a csv struct
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value) #append the csv struct to a list
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'] #Mark the columns
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = os.path.join(os.getcwd(), 'Test') #change file here
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('TestLabels.csv', index=None) #Change file output name here
    print('Successfully converted xml to csv.')


main()