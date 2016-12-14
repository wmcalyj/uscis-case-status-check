# uscis-case-status-check
This project is for quick uscis case status check.

### BEFORE: Make sure you have BeautifulSoup installed
To run the script, please make sure BeautifulSoup is installed. If it's not, there is a tarball for BeautifulSoup4-4.5.1, you can download it and install beautiful following here: https://www.crummy.com/software/BeautifulSoup/ or you can unzip the the tarball and run "python setup.py install" in that folder.

Once you have BeautifulSoup installed, following the steps below:

For the first two steps, you only need to do them once.

1. Enter your receipt number in number.txt
2. run "chmod +x uscis-chcking.py" in your terminal
3. run "./uscis-checking.py" in your terminal and you can see your case status

You can put multiple numbers in number.txt, just make sure it's one number a line.

### Cronjob installation

To create a cronjob for this script, run cronjob.sh.
This script will create a cronjob for the python script and all the output will be appeneded to cronjob.log.

## WARNING

Running cronjob.sh will erase all existing cronjobs in crontab and only create one cronjob for the python script.
If you want to keep your eisting cronjobs, modify the cronjob.sh however you like
