#!/usr/bin/python
# PYTHON_ARGCOMPLETE_OK

from argparse import ArgumentParser
import argcomplete
import sys

def handle_commit(args):
    print args

class ExampleParsing(object):
    args = None
    def __init__(self):
        parser = ArgumentParser(description="Example Argument Parsing", usage="Add a custom usage")

        parser.add_argument('command', help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])

        command = args.command.replace('-', '_')

        if not hasattr(self, command):
            print "Unrecognized Command"
            parser.print_help()
            exit(1)

        cmd = getattr(self, command)
        cmd()

    def commit(self):
        print "Running commit"
        parser = ArgumentParser()
        parser.set_defaults(func=handle_commit)
        subs = parser.add_subparsers()

        # Subcommands
        get = subs.add_parser("get", help="Get Command")
        get.add_argument("-i", "--id", help="Unique ID")
        put = subs.add_parser("put", help="Put Command")
        put.add_argument("-d", "--id", help="Device")
        delete = subs.add_parser("delete", help="Delete Command")
        delete.add_argument("-e", "--instance", help="Instance")

        argcomplete.autocomplete(parser)
        self.args = parser.parse_args(sys.argv[2:])

    def issue(self):
        print "Running issue"
        pass

    def commit_issue(self):
        print "Running commit_issue"
        pass

    def get_args(self):
        return self.args

parser = ExampleParsing()
args = parser.get_args()
args.func(args)
