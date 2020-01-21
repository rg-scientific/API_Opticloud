import requests
from xml.etree import ElementTree
from xml.etree import cElementTree as xmlTree

def read_authentication(fileName):
    auth = [line.rstrip('\n') for line in open(fileName)]
    return auth[0], auth[1]

login, pw = read_authentication('opti_authentication')

req = requests.get('https://ice1erdschluss.opticloud.de/API/Devices/list', auth=(login, pw))
print(req)

'''
#print(req.headers['content-type'])

#response = requests.get(url)
print(req.content)
tree = ElementTree.fromstring(req.content)
print(type(tree))
#print(tree.attrib)

for child in tree:
    print(child.tag, child.attrib)

#for dev in tree.iter('ID'):
#    print(dev.attrib)
'''