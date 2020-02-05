#!/bin/bash

REPO_BASE="git@github.com:csc301-winter-2020"

echo "Clone a temp copy of student's assignment..."

git clone ${REPO_BASE}/${1} ${3}

# make sure we're at the tip of the master branch
cd ${3}
git checkout master

if [ -z "$3" ]
then
	echo "Missing ASSIGNMENT_DEADLINE env (UTC time in 'YYYY-MM-DD HH:MM' format)"
	exit 255
else
	echo "Check out latest commit before deadline"
	echo "checkout commit `git log -1 --before=$3" --format=%h`"
	git checkout `git log -1 --before="$3" --format=%h`
fi






