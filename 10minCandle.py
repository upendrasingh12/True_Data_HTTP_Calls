# sample code to connect to TrueData Http Feed
import requests
from time import sleep
import os
from pandas import DataFrame
import pandas as pd
import xlsxwriter


try:
    pubip = open("/Users/upendrasingh/Documents/Projects/TrueData/pubip.txt", "r").read()
except IOError:
    print("pubip.txt file does not exist")    

try:
    userid = open("/Users/upendrasingh/Documents/Projects/TrueData/userid.txt", "r").read()
except IOError:
    print("userid.txt file does not exist")  

try:
    password = open("/Users/upendrasingh/Documents/Projects/TrueData/password.txt", "r").read()
except IOError:
    print("password.txt file does not exist")     


# Logout first
url_logout = 'http://%s/IDAUTH/Logout.aspx' % pubip
login_payload = "UserId=%s&Provider=TRUEDATA&Password=%s" % (userid, password)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    # 'x-authz': key,
    'cache-control': "no-cache",
    }
response = requests.request("POST", url_logout, data=login_payload, headers=headers)


# Login
url_login = "http://%s/IDAUTH/Login.aspx" % pubip
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.request("POST", url_login, data=login_payload, headers=headers)
auth = response.text
key = auth.splitlines()[0]
# or Split the line on newlines and grab the first item from the result:
# key = auth.split('\n', 1)[0]
#print(auth, '\n\n')
#print('key =', key, '\n\n')


# start Current Day History (10min Intraday)
def datafetch():
    url_equity = "http://180.179.151.146/mxds/id1min.aspx?t=1001594&nd=0&p=0"
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-authz': key,
    'cache-control': "no-cache"
    }
    response = requests.request("GET", url_equity, data=login_payload, headers=headers)
    print(response.text)
datafetch()