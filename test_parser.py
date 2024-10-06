import unittest
from parser import parse_json, parse_xml, parse_yaml

class TestParsers(unittest.TestCase):
    def test_parse_json(self):
        data = '{"name": "Alice", "age": 25}'
        parsed_data = parse_json(data)
        self.assertEqual(parsed_data['name'], 'Alice')
        self.assertEqual(parsed_data['age'], 25)

    def test_parse_xml(self):
        data = '<person><name>Alice</name><age>25</age></person>'
        parsed_data = parse_xml(data)
        self.assertEqual(parsed_data['name'], 'Alice')
        self.assertEqual(parsed_data['age'], '25')

    def test_parse_yaml(self):
        data = 'name: Alice\nage: 25'
        parsed_data = parse_yaml(data)
        self.assertEqual(parsed_data['name'], 'Alice')
        self.assertEqual(parsed_data['age'], 25)

if __name__ == '__main__':
    unittest.main()
