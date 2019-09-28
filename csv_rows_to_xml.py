import csv
import lxml.etree as ET

# Reading csv file and build tree

f = open('/Users/YourName/Desktop/example_source.csv', encoding='windows-1251')
csvreader = csv.reader(f, delimiter=';')
headers = next(csvreader)

for count, row in enumerate(csvreader):

    # Initializing XML
    # Call, Data, audio and ets - your custom fields (if need)
    root = ET.Element('Call', nsmap={'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}, attrib={'{xsi}noNamespaceSchemaLocation': 'GenericAdapterScheme.xsd'})
    data = ET.SubElement(root, "Data")
    custom = ET.SubElement(root, "Custom_Data")
    audio = ET.SubElement(data, "audio")
    group = ET.SubElement(audio, "audio_segment")

    for column_index, value in enumerate(row):
        column_name = headers[column_index]

        if column_index < 6: # Your condition (if need)
            ET.SubElement(group, column_name).text = value
        else:
            ET.SubElement(data, column_name).text = value

        # Dumping XML tree to string
        tree_out = (ET.tostring(root,
                                pretty_print=True,
                                xml_declaration=True,
                                encoding="UTF-8"))

        # Writing xml to file
        with open('/Users/YourName/Desktop/example'+str(count)+'.xml', 'wb') as f:
              f.write(tree_out)