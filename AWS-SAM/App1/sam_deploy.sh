#! /bin/bash
# getopts !!
sam validate && sam build && sam deploy --config-env $1