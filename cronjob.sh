#!/bin/bash
dir=$(pwd)
cronjob1="30 17 * * 1-5 cd "
cronjob2=" && ./uscis-checking.py >> "
cronjob3="/cronjob.log 2>&1"
cronjob=$cronjob1$dir$cronjob2$dir$cronjob3
echo "Cronjob is $cronjob"
# Write out current cronjob
# crontab -l > mycron
# Echo new cronjob into mycron
echo "MAILTO=\"\"" > mycron
echo "$cronjob" >> mycron
# Install new cron file
crontab mycron
# rm mycron
