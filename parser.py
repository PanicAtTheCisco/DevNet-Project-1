import json
import xml.etree.ElementTree as ET
import yaml

def parse_json(data):
    return json.loads(data)

def parse_xml(data):
    root = ET.fromstring(data)
    parsed_data = {}
    
    # Iterate through the child elements of the root
    for child in root:
        parsed_data[child.tag] = child.text
    
    return parsed_data

def parse_yaml(data):
    return yaml.safe_load(data)


data = '{"name": "Alice", "age": 25}'
print(parse_json(data))
data = '<person><name>Alice</name><age>25</age></person>'
print(parse_xml(data))
data = 'name: Alice\nage: 25'
print(parse_yaml(data))