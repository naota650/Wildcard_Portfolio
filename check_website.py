from sys import argv
from urllib.request import urlopen
from smtplib import SMTP
import re
import time
import sched
import threading



html = urlopen("http://www.google.com/")
print(html.read())
