webpagetest-upload
==================

usage: bash wpt_batch.sh [/path/to/urls.txt] [device to test on] [Number of devices to do test on]

This command will split the url.txt file into [Number of devices to do test on] files and invoke the wpt_batch.py script multiple times, sending each subfile of url.txt to a different device to test on.
Results will be put into a new directory created when the script is run.

Device List:
1/ Android-Nexus4
