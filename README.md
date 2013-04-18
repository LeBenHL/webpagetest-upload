webpagetest-upload
==================

NO NEED TO USE BASH SCRIPT TO SPLIT URL.TEXT TO SEND TO MULTIPLE ANDROID DEVICES. DO NOT USE BASH SCRIPT FOR NOW, JUST SEND URLS TO Android-Nexus4 AND IT WILL AUTOMATICALLY LOAD BALANCE ITSELF.

To use wpt_batch.py, please look read https://sites.google.com/a/webpagetest.org/docs/advanced-features/webpagetest-batch-processing-command-line-tool.

I also added in another option to the python script. Add in flag -b or --mobile to turn on the Chrome mobile emulation.



usage: bash wpt_batch.sh [/path/to/urls.txt] [device to test on] [Number of devices to do test on]

This command will split the url.txt file into [Number of devices to do test on] files and invoke the wpt_batch.py script multiple times, sending each subfile of url.txt to a different device to test on.
Results will be put into a new directory created when the script is run.

Device List:
1/ Android-Nexus4
