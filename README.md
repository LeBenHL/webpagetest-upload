webpagetest-upload
==================

TO USE

1/ Throw URL's into a text file. Where each url is delimited by a new line.  
2/ Run python wpt_batch.py -s [SERVER URL] -i [URLFILE] -f [OUTPUTDIR] -r 1 -t True  
3/ Results will be thrown in OUTPUTDIR/imageComparision.csv  
4/ Image Comparision values for similarity are calculated using Opensift's match binary. This script assumes that you have the binary located at /usr/bin/opensift/bin/match
If the binary is located elsewhere you decide to use a different binary to calculate for similarity values, change line 236 in wpt_batch.py to use the appropriate bash command.

All URL's will be crawled by three different agents: Android, Desktop Chrome, and Desktop Chrome in Mobile mode.

Currently, the columns collected in the CSV file are the screenshot urls for the 3 different agents, the tcpdump urls, the xml urls, Image comparision values for each agent against another agent, and the testing id's.
