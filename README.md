# Snapshot

This code create a simple, separate python app which would monitor your system/server.

## Quick start

1. To install module run `pip install .` or `pip install /path/to/folder_with_setup.py/`
1. To see help run `snapshot -h`
1. By default `snapshot` will output CPU usage, VMemory usage and Memory usage in percent every 30 seconds, and output results into the file test.txt antd in terminal on the plain text.
1. Argument `-i` change time interval and must be integer.
1. Argument `t` can be `json`, that will output results into the file test.json ant in terminal in json format.
1. To clean up and delete module after you're done, run `pip uninstall snapshot`
