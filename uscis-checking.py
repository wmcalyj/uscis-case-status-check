#!/usr/bin/env python
import urllib
import urllib2
import datetime
import time
import os
from bs4 import BeautifulSoup


def readReceiptNumbers(filename):
    time = datetime.datetime.now()
    timeStr = time.strftime('%Y-%b-%d %H:%M:%S')
    f = open(filename, 'r')
    noNumber = True
    for line in f:
        if not line.strip():
            continue
        number = line.strip()[:13]
        if number[0] != '#':
            noNumber = False
            try:
                status = getStatus(number)
                
                print timeStr + ' -- receipt number: [' + number + '], case status: [' + status + ']'
            except AttributeError:
                print 'Invalid receipt number: [' + number + '], please check your receipt number and try again'
    if noNumber:
        print 'No receipt number is found in ' + filename + ', please put your receipt number there.'

def getStatus(receiptNumber):
    url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
    # changeLocale=&appReceiptNum=YSC1790007419&initCaseSearch=CHECK+STATUS
    values = {'changeLocale' : '',
              'appReceiptNum' : receiptNumber,
              'initCaseSearch' : 'CHECK STATUS' }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page, 'html.parser')
    statusTag = soup.find('div', {'class':'current-status-sec'})
    contents = statusTag.text.split("\n")
    content = contents[2].strip()
    return content

def runScript(filename):
  filepath = os.path.dirname(os.path.realpath(__file__))
  file = os.path.join(filepath, filename)
  readReceiptNumbers(file)

runScript('number.txt')
