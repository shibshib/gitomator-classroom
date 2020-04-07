#!/bin/bash

# Logging function
function log() {
    python3 -c "from loguru import logger; logger.add(\"autograder_logs.out\"); logger.debug(\"$1\")"
}

function run_unit_tests() {
	log "Command: $COMMAND"
	eval $COMMAND 
	LISTENERPID=$!
	log ""
}

function convert_xml_to_json() {
	log "Command: $COMMAND"
	eval $COMMAND 
	LISTENERPID=$!
	log""
}

REPO=$1
log "=== Starting A2 Autograder ==="

log "=== Running unit tests for $REPO ==="
cd $REPO
COMMAND="python3 -m pytest --cov-report xml:./autograder_coverage.xml --cov=. ./tests/unit_tests.py"
run_unit_tests

cd ../../
log "=== Retrieving Coverage file for $REPO ==="
COMMAND="python3 coverage_grader.py --xml_file=$REPO/autograder_coverage.xml --json_file=$REPO/autograder_coverage.json"
convert_xml_to_json

