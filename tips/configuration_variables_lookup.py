import os, argparse, time
from collections import ChainMap

defaults = {'date': time.time(), 'user': 'guest', 'password': None}

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--date')
parser.add_argument('-u', '--user')
parser.add_argument('-p', '--password')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

# Don't do this
combined = defaults.copy()
combined.update(os.environ)
combined.update(command_line_args)

# Do this instead
combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['date'])
print(combined['user'])
