import xmltodict
import json
import argparse

def generate_json_file(xml_file, json_file):
    with open(xml_file) as in_file:
        xml = in_file.read()
        with open(json_file, 'w+') as out_file:
            json_coverage = xmltodict.parse(xml)
            json.dump(xmltodict.parse(xml), out_file)
        return json_coverage
    
def analyze_tests_coverage(coverage):
    coverage = coverage['coverage']
    if coverage:
        lines_covered = coverage.get("lines_covered")
        
        packages = coverage['packages']
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--xml_file',
        default='./coverage.xml',
        type=str,
        help='Path to coverage XML file.'
    )

    parser.add_argument(
        '--json_file',
        default='./coverage.json',
        type=str,
        help='Path to target JSON file.'
    )
    
    args = parser.parse_args()

    json_coverage = generate_json_file(args.xml_file, args.json_file)

