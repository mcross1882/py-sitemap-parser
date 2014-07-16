"""
parse.py
Matthew Cross <blacklightgfx@gmail.com>
Apache V2 License
"""
import xml.etree.ElementTree as ET
import csv
import sys

def nodes_to_list(nodes):
    """
    converts a set of XML nodes to a flat array by taking the text values
    of each node and appending them to the resulting array
    """
    result = []
    for child_node in nodes:
        result.append(child_node.text)
    return result

"""
Here we are simply checking to see if the user has supplied
a input file and output file when running this script
"""
if (len(sys.argv) < 2):
    print "Requires a input file and output file"
    exit()

# This statement takes a xml file and loads it into memory for us
parsed_file = ET.parse(sys.argv[1])

"""
Here we take the root node in the XML file this element is usually located after
<?xml?> tag at the top of your file
"""
document_root = parsed_file.getroot()

# This line opens up our csv file with write permissions
with open(sys.argv[2], 'wb') as csvfile:
    # Here we create the writer and set up some basic options when formatting the csv file
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # Next we write the headers to the file. Notice that we're passing in an array of strings
    csv_writer.writerow(['loc', 'lastmod', 'changefreq'])
    
    """
    Now we loop through each node and write their contents in csv format. 
    If the node does not contain any values its simply skipped
    """
    for url_element in document_root:
        row_values = nodes_to_list(url_element)
        if (len(row_values) > 0):
            csv_writer.writerow(row_values);
