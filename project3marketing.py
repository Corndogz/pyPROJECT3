#author by Hunter Cornay


from urllib.request import urlretrieve
import os
import re
import collections 

#File Setup and Variable Reset
loopCount = 0
redirects = 0
errors = 0
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

#File Checker
if not os.path.isfile(LOCAL_FILE):urlretrieve(URL, LOCAL_FILE)

#Regex Pattern
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'

#Line Reader
lineRead = open(LOCAL_FILE, 'r').readlines()

#Match Finder.
for line in lineRead:
    matchFinder = re.match(pattern, line)
    if not matchFinder:
        continue
        
#Month Breakdown
months_count = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, "Nov": 0, "Dec": 0}
jan_logs = open("janLog.txt", "a+");
feb_logs = open("febLog.txt", "a+");
mar_logs = open("marLog.txt", "a+");
apr_logs = open("aprLog.txt", "a+");
may_logs = open("mayLog.txt", "a+");
jun_logs = open("junLog.txt", "a+");
jul_logs = open("julLog.txt", "a+");
aug_logs = open("augLog.txt", "a+");
sep_logs = open("sepLog.txt", "a+");
oct_logs = open("octLog.txt", "a+");
nov_logs = open("novLog.txt", "a+");
dec_logs = open("decLog.txt", "a+");
