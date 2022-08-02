#!/bin/bash
set -eux

declare HOST=$1
declare STATUS=$2

HOST=$HOST STATUS=$STATUS bash -c \
    'while [[ ${STATUS_RECEIVED} != ${STATUS} ]];\
        do STATUS_RECEIVED=$(curl -X GET -s -o /dev/null -L -w ''%{http_code}'' ${HOST}) && \
        echo "received status: $STATUS_RECEIVED" && \
        sleep 5;\
    done;
    echo success with status: $STATUS_RECEIVED'