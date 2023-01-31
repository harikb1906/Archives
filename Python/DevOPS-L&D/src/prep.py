#! /usr/bin/env python
import os
import sys


def get_cli_arguments():
    return sys.argv


def execute_cli_commands(cmd):
    os.system(cmd)


def get_env_variables(name):
    return os.getenv(name)

if __name__ == '__main__':
    # get_cli_arguments()
    # execute_cli_commands('du -h')
    print(get_env_variables('SHELL'))
