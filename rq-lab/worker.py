#!/usr/bin/env python
import sys
from rq import Connection, Worker

# Preload libraries
# import library_that_you_want_preloaded

# Provide queue names to listen to as arguments to this script,
# similar to rq worker
with Connection():
    qs = sys.argv[1:] or ['default']
    print(qs)

    w = Worker(qs)
    w.work()
