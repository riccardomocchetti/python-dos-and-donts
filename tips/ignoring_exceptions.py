import os
from contextlib import suppress

# don't do this
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

# do this instead
with suppress(FileNotFoundError):
    os.remove('somefile.tmp')