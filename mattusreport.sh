#!/bin/sh
nmap -n -sn 192.168.3.0/24 -oG - | awk '/Up$/{print $2}' > new.txt
python3 mattusreport.py
cp diff.txt index.html
mv -f index.html /var/www/html
chmod -R 775 /var/www
