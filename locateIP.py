#!/usr/bin/python3.5
import urllib.parse
import urllib.request
import webbrowser
import re

try:
    # Grab your current IP from httpbin.org/ip and stores it in a variable
    fp = urllib.request.urlopen('http://httpbin.org/ip')
    mybytes = fp.read()
    page_responce = mybytes.decode('utf8')
    fp.close()
    list_of_ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', page_responce )
except urllib.error.URLError as e:
    # Check for error on the HTTP requests, and if found with gracefully exit the program
    print(e.reason)



# Open a browser and send to the following query to Google: “ip locator <your ip>” (replace <your ip> with the IP variable from the previous step)

url = 'https://www.google.com/search?&q=ip+locator+' + str(list_of_ip[0])

#firefox on linux path
firefox_path = '/usr/bin/firefox %s'

webbrowser.get(firefox_path).open(url)