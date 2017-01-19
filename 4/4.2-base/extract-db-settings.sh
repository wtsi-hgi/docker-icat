#!/usr/bin/env bash

RESPONSES_FILE=$1

export DB_NAME=`sed -n 7p ${RESPONSES_FILE}`
export DB_USER=`sed -n 8p ${RESPONSES_FILE}`
export DB_PASS=`sed -n 10p ${RESPONSES_FILE}`