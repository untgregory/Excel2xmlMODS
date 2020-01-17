# Split XML containing many <mods> elements into invidual files
# Modified from script found here: http://stackoverflow.com/questions/36155049/splitting-xml-file-into-multiple-at-given-tags
# and from a script by Bill Levay for California Historical Society
# New usage for local NOVA repositories and updating for Python 3 by Gregory Pierce

import os, lxml.etree as ET

# output and source xml path shown are for server paths and should be changed
output_path = 'S:\\Digitization\\Metadata\\tools\\XMLcreator\\SplitMODS_XML\\'

# parse source.xml with lxml
tree = ET.parse('S:\\Digitization\\Metadata\\tools\\XMLcreator\\MODSsource.xml')

# start cleanup
# remove any element tails
for element in tree.iter():
    element.tail = None

# remove any line breaks or tabs in element text
    if element.text:
        if '\n' in element.text:
            element.text = element.text.replace('\n', '') 
        if '\t' in element.text:
            element.text = element.text.replace('\t', '')

# remove any remaining whitespace
parser = ET.XMLParser(remove_blank_text=True, remove_comments=True, recover=True)
treestring = ET.tostring(tree)
clean = ET.XML(treestring, parser)

# remove recursively empty nodes
# found here: https://stackoverflow.com/questions/12694091/python-lxml-how-to-remove-empty-repeated-tags
def recursively_empty(e):
   if e.text:
       return False
   return all((recursively_empty(c) for c in e.iterchildren()))

context = ET.iterwalk(clean)
for action, elem in context:
    parent = elem.getparent()
    if recursively_empty(elem):
        parent.remove(elem)

# remove nodes with blank attribute
# for element in clean.xpath(".//*[@*='']"):
#    element.getparent().remove(element)

# remove nodes with attribute "null"
for element in clean.xpath(".//*[@*='null']"):
    element.getparent().remove(element)

# finished cleanup
# write out to intermediate file
with open('clean.xml', 'wb') as f:
    f.write(ET.tostring(clean))
print("XML is now clean")

# parse the clean xml
cleanxml = ET.iterparse('clean.xml', events=('end', ))

# find the <mods> nodes
for event, elem in cleanxml:
    if elem.tag == '{http://www.loc.gov/mods/v3}mods':

        # the filenames of the resulting xml files will be based on the <identifier> element
        # edit the specific element or attribute if necessary
        identifier = elem.find('{http://www.loc.gov/mods/v3}identifier[@type="local"]').text
        filename = format(identifier + "_MODS.xml")

        # write out to new file
        with open(output_path+filename, 'wb') as f:
            f.write("<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n".encode("UTF-8"))
            f.write(ET.tostring(elem, pretty_print = True))
        print("Writing", filename)

# remove the intermediate file
os.remove('clean.xml')
print("All done!")
