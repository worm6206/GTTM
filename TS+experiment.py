
# coding: utf-8

# In[218]:
import sys
if len(sys.argv) != 2:
    sys.exit("usage: need 1 argument, and 1 only.")

def isLeaf(node): # ts
    if node.find('primary') is not None:
        return False
    else:
        return True

def getNote(node):
    return node.find('head').find('chord').find('note').attrib['id'][3:]
    
def xml2dict(node):
    obj = {}
    if not isLeaf(node):
        obj['children'] = []
        if getNote(node.find('primary').find('ts')) > getNote(node.find('secondary').find('ts')):
            obj['children'].append(xml2dict(node.find('secondary').find('ts')))
            obj['children'].append(xml2dict(node.find('primary').find('ts')))
        else:
            obj['children'].append(xml2dict(node.find('primary').find('ts')))
            obj['children'].append(xml2dict(node.find('secondary').find('ts')))
    else:
        obj['name'] = getNote(node)
    return obj


# In[221]:

# READ TS-XML
import xml.etree.ElementTree as ET
xmldoc = ET.parse(str(sys.argv[1]))
root = xmldoc.getroot()
tree = []
tree.append(xml2dict(root.find('ts')))
print(tree)


# In[ ]:



