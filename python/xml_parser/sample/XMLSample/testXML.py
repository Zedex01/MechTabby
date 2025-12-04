#Matthew Moran 9.4.2024
#This is a sample file for accessing information from an xml file.
'''
XML is useful to store data that needs to be accesed by multiple applications. 
It is a standard widely used and thus is readable by many APIs.
'''
import os
import xml.etree.ElementTree as et

#Get absolute path of this python script
absolutePath = os.path.dirname(__file__)

'''
#Get the reltive path
relativeSamplePath = 'config\country.xml'

#However, my xml file contains the path to the data, let's get it from there.
samplePath = os.path.join(absolutePath,relativeSamplePath)

#Retrive the data path
tree = et.parse(samplePath)

#Get the root of thexml file
root = tree.getroot()

#Get the tag and attributes of the element?
print(root.tag)
print(root.attrib)

#We can then itterate over its children
for child in root:
    print(f"{child.tag}, {child.attrib}")

#children are nested, can access specific children via index
#    element 0 of root, element 1 of child "year"
print(root[0][1].text)
'''

#get relative path to xml
relativeConfigPath = 'config\myFile.xml'

#ok, now lets extract the path from my myFile.xml
xmlPath = os.path.join(absolutePath,relativeConfigPath)

tree = et.parse(xmlPath)
root = tree.getroot()

#Grab the information from the xml file
for child in root:
    if child.tag == 'csvPath':
        xmlFile = child.text

