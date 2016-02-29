#!/usr/bin/env python
from argparse import ArgumentParser
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)s:%(asctime)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
def simple():
    app = ArgumentParser()
    app.add_argument('name', nargs='?')
    args = app.parse_args()
    name = (args.name or 'World')
    print("Hello, {}!".format(name))

def advanced():
    app = ArgumentParser()
    app.add_argument('-v', '--verbose', default=False, action='store_true', help='Increase Verbosity') # boolean type
    app.add_argument('-n', '--number', type=int, default=1,help='Number of times to greet NAME')
    app.add_argument('name', type=str, help='The Person to greet')

    args = app.parse_args()

    for i in range(args.number):
        print("Hello, {}!".format(args.name))
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        LOG = logging.getLogger('logtest')
        LOG.debug("Finished Printing name")

#simple()

# To run:
# python argument-parser.py # gives Hello, World!
#  python argument-parser.py Python # gives Hello, Python!
#  python argument-parser.py --help


advanced()