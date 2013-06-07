webpagetest-upload
==================

TO USE

1/ First, make sure that the Blaze Agents on the Android devices are up and polling for URL's  
2/ Also make sure that the Windows VM have the WPTDriver program running and polling. When logging out from the Windows VM, please just restart the VM instead of closing the rdesktop connection.
Closing the connection will prevent WPTDriver from taking screenshots during the crawls (Will just be Black Screen).  
3/ Throw URL's into a text file. Where each url is delimited by a new line.  
4/ Run python wpt_batch.py -s [SERVER URL] -i [URLFILE] -f [OUTPUTDIR] -r 1 -t True  
5/ The bash command will take a very long time to run so I would either use nohup or use screen to keep the command running even after you shut down your machine.  
6/ Results will be thrown in OUTPUTDIR/imageComparision.csv  
7/ Image Comparision values for similarity are calculated using Opensift's match binary. This script assumes that you have the binary located at /usr/bin/opensift/bin/match
If the binary is located elsewhere you decide to use a different binary to calculate for similarity values, change line 236 in wpt_batch.py to use the appropriate bash command.

All URL's will be crawled by three different agents: Android, Desktop Chrome, and Desktop Chrome in Mobile mode.

Currently, the columns collected in the CSV file are the screenshot urls for the 3 different agents, the tcpdump urls, the xml urls, Image comparision values for each agent against another agent, and the testing id's.
