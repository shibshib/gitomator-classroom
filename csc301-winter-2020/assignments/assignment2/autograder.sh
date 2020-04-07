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

REPO="a2-starter"
log "=== Starting A2 Autograder ==="

log "=== Running unit tests for $REPO ==="
COMMAND="pytest --cov-report xml --cov=$REPO $REPO/tests/unit_tests.py"

run_unit_tests

log "=== Retrieving Coverage file for $REPO ==="
COMMAND="python3 xml_to_json.py --xml_file=./coverage.xml --json_file=./coverage.json"
convert_xml_to_json

