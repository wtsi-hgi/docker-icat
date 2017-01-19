#!/usr/bin/env bash

RESPONSES_FILE=$1

export DB_NAME=`tail -n 4 ${RESPONSES_FILE} | head -n 1`
export DB_USER=`tail -n 3 ${RESPONSES_FILE} | head -n 1`
export DB_PASS=`tail -n 2 ${RESPONSES_FILE} | head -n 1`