#!/bin/python
import yaml
import argparse
import subprocess
import os
from pathlib import Path

# JSON files to be evaluated
get_json_file = "script_get_data.json"
post_json_file = "script_post_data.json"

def process_args():
    # Grabs all cmd line arguments and returns them. 
    parser = argparse.ArgumentParser(description="autograder self tutorial")
    parser.add_argument('assignment_config', metavar='A', type=str, help='path to the assignment config yaml')

    args = parser.parse_args()
    return args

def process_assignment_config(assignment_config):
    # Processes the assignment config yaml file 
    # and returns a dictionary of the contents
    with open(assignment_config, 'r') as file:
        assignment_config = yaml.full_load(file)

    return assignment_config


def autograde_assignment(assignment_dir):
    # goes into the newly created assignment directory 
    # and checks files, then creates a CSV file inside
    # the assignment marking directory
    os.chdir(assignment_dir)
    cur_dir = os.getcwd()
    for filename in Path(cur_dir).rglob('*'):
        print(filename)


if __name__ == "__main__":

    args = process_args()
    
    assignment_config = process_assignment_config(args.assignment_config)
    repos = assignment_config.get('repos')
    env = assignment_config.get('env')
    autograder_script = assignment_config.get('automarker_script')
    assignment_dir = assignment_config.get('assignment_directory')
    
    assignment_deadline = env.get('ASSIGNMENT_DEADLINE', '')

    if assignment_config.get('repos'):
        for repo in repos:
            try:
                assignment_directory = "{}/{}".format(assignment_dir, repo)
                #print("Cloning git repository into {}...".format(assignment_directory))
                #result = subprocess.check_output([autograder_script, repo, assignment_deadline, assignment_directory], stderr = subprocess.STDOUT)

                # cloned repo, now let's get into it and start grading.
                autograde_assignment(assignment_directory)
            except subprocess.CalledProcessError as e:
                print ("Error: {}".format(e.output))
            
            #autograde_assignment(local_dir)


