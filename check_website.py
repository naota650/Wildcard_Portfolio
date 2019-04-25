from sys import argv
import sys
import requests
from urllib.request import urlopen
from smtplib import SMTP
import re
import time
import sched
import threading
from urllib.parse import urlparse


html = urlopen("http://www.google.com/")
#print(html.read())

# Checks that correct arguments are present and shows
# correct usage if error occurs
def check_argvs():
    if len(sys.argv) > 1:
        site_url = argv[1]
    else:
        print("first argv must be website url")
        exit
    
    if len(sys.argv) > 2:
        check_interval = int(argv[2])
    else:
        print("second argv must be time interval")
        exit

# Checks that user has connection, checks google and yahoo
# because its not likely that both are down lol
def check_connection():
    g = confirm_status('http://google.com')
    y = confirm_status('http://yahoo.com')

    if g and y:
        #print ("internet is connected")
        return True
    if not g and not y:
        print ("internet down")
        return False
# Opens user url and checks response status code to see if avail
def confirm_status(url):
    url = check_http(url)
 #   check = is_url(url)
 #   if is_url(url):
 #       url_file = urlopen(url)
 #   else:
 #       print("url is not valid")
 #       exit()
    url_file = urlopen(url)
    response = url_file.code
    #print(response)
    if response in (200, 302):
        return True
    else:
        return False

#def is_url(url):
#    try:
#        result = urlparse(url)
#        if result:
#            print ("is an urlparse")
#        return all([result.scheme, result.netlock, result.path])
#    except:
#        return False

# Adds http:// to url if doesn't already have it
def check_http(url):
    if not re.match('^http[s]?://', url):
        url = "http://" + url
    return url

# Checks website connection of user's choice
def check_url(url):
    if check_connection():
        url_check = confirm_status(url)
        if url_check:
            print (url + " is online!!")
        else:
            print ("%s is down!!" % url)
    else:
        print ("internet connection is down")

def main():
    check_argvs()
    site_url = argv[1]
    check_url(site_url)
    #print(html)
    #print(html.read())

if __name__ == '__main__':
    main()