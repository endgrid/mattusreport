# mattusreport
![00071-tardigrade](https://github.com/endgrid/mattusreport/assets/104172903/ec709c5f-5dd5-4aad-9c91-5b49343f2284)

Every week, I submit a status report to my boss. What if your network could submit a status report to you?

The mattusreport is a single line of text indicating the IPs that have been added to or have dropped off your network within the last selected time range. It answers the question--what joined the network since the last scan?

## Prerequisites:
Mattusreport runs on linux and requires apache to be configured with your desired URL. It was built on an Ubuntu LXC container. Python and nmap are required.

![image](https://github.com/endgrid/mattusreport/assets/104172903/a9838d0a-7a51-46c3-86c9-0a2262c33f93)
## Step 1: [mattusreport.py](https://github.com/endgrid/mattusreport/blob/main/mattusreport.py)
The python script to compare the most recent two scans uses the libdiff library to compare old.txt and new.txt before replacing the former with the latter. The delta of the two is saved as diff.txt.

## Step 2: [mattusreport.sh](https://github.com/endgrid/mattusreport/blob/main/mattusreport.sh)
The bash script that performs the nmap scans, calls the python script above, and moves the results to the web directory. Note--the IP range will need to be replaced with the range you wish to monitor.

## Step 3: Schedule cron job
`crontab -e`
![image](https://github.com/endgrid/mattusreport/assets/104172903/b8c85116-29f4-4560-9ce0-03d72a28daa7)
The above config runs a scan every 60 minutes.

Assuming you've configured everything above correctly, every 60 minutes or defined time range, a scan will be conducted against the selected IP range. The results will be compared to the last scan performed, and the URL for the server will show changes to the network for that period until the next scan.
![image](https://github.com/endgrid/mattusreport/assets/104172903/89b471a6-f233-448c-a7f3-ca19b770db7c)
A minus symbol indicated a host that is no longer detected, and a plus symbol indicates a host that is newly detected.

Once new IPs have been detected, a savvy analyst could perform reverse lookups, OS detection, port scans, etc. to gather more information on the hosts.
