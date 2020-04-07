import xmltodict
import json
import argparse
from loguru import logger
import os

COV_GRADE_FILE = "coverage_grade.txt"

def evaluate_line_rate(line_rate):
    logger.info("Evaluating line rate of {}".format(line_rate))
    grade = 0
    if line_rate > 90:
        grade = 35
    elif line_rate > 80 and line_rate < 90:
        grade = 30
    elif line_rate > 70 and line_rate < 80:
        grade = 25
    elif line_rate > 60 and line_rate < 70:
        grade = 20
    
    return grade

def extract_folderpath(filepath):
    return os.path.dirname(os.path.abspath(filepath))

def generate_json_file(xml_file, json_file):
    with open(xml_file) as in_file:
        xml = in_file.read()
        with open(json_file, 'w+') as out_file:
            json_coverage = xmltodict.parse(xml)
            json.dump(xmltodict.parse(xml), out_file)
        return json_coverage
    
def analyze_tests_coverage(coverage_grade_file_location, coverage):
    grade_file = "{}/{}".format(coverage_grade_file_location, COV_GRADE_FILE)
    coverage = coverage['coverage']
    if coverage:
        line_rate = coverage.get("@line-rate")
        grade = evaluate_line_rate(float(line_rate)*100)
        with open(grade_file, 'w+') as grade_file:
            grade_file.write("Coverage grade: {}".format(grade))
        
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--xml_file',
        default='./autograder_coverage.xml',
        type=str,
        help='Path to coverage XML file.'
    )

    parser.add_argument(
        '--json_file',
        default='./autograder_coverage.json',
        type=str,
        help='Path to target JSON file.'
    )
    
    args = parser.parse_args()

    json_coverage = generate_json_file(args.xml_file, args.json_file)
    coverage_grade_file_location = extract_folderpath(args.json_file)
    analyze_tests_coverage(coverage_grade_file_location, json_coverage)
