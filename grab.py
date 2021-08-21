# -*- coding: utf-8 -*-
from itertools import cycle
import warnings,random,socket
import requests, re, sys, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from time import time as timer  
import time
year = time.strftime("%y")
month = time.strftime("%m")
day = time.strftime("%d")
live = 0
proxy = ""

Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

def runit(ip):
    untile = 'https://api.hackertarget.com/reverseiplookup/?q='+ip
    print untile
    global live
    total = 0
    global proxy_cycle
    global proxy
    try:
      cepu = requests.get(untile, timeout=10, headers=Headers, proxies=proxy).text
      if 'error check your search parameter' in cepu:
        print '[!] '+ip + ' ====> Wrong List'
        open('broken_result.txt', 'a').write(ip + '\n')
      elif 'API count exceeded' in cepu:
        print '[!] '+ip + ' ====> Tryng Bypass With Proxy'
        soc = next(proxy_cycle)
        proxy = {"http":str(soc),"https":str(soc)}
        runit(ip)
      elif "Can't connect to api.hackertarget.com:443" in cepu:
        time.sleep(5)
        soc = next(proxy_cycle)
        proxy = {"http":str(soc),"https":str(soc)}
        runit(ip)
      elif "No DNS A records found" in cepu:
        print '[!] '+ip + ' ====> 0 Domain'
      else:
        resp = cepu.split('\n')
        for x in resp:
          open('_rev_result.txt', 'a').write(x + '\n')

        print '[-] '+ip + ' ====> Get Grab site Available'
    except Exception as e:
      soc = next(proxy_cycle)
      proxy = {"http":str(soc),"https":str(soc)}
      runit(ip)

def prepare(sites):
    try:
      site = sites.strip()
      url = site.replace('http://', '').replace('https://', '').replace('/', '')
      ips = socket.gethostbyname(url)
      ip = ips + '\n'
      open('listip.txt', 'a')
      if ip not in open('listip.txt', 'r'):
        open('listip.txt', 'a').write(ips + '\n')
        runit(ips)
      else:
        print '[-] '+ip + ' ====> Same Ip'
    except Exception as e:
        print str(e)


Targetssa = sys.argv[1] #for date
aburame = open(sys.argv[2]).read()
hyuga = aburame.splitlines()
proxy_cycle = cycle(hyuga)
def logo():
    clear = "\x1b[0m"
    colors = [32]

    x = """

       _                                                        
      | |                                                       
  __ _| |__   __ _ ______ _ ___  ___ __ _ _ __  _ __   ___ _ __ 
 / _` | '_ \ / _` |_  / _` / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| (_| | | | | (_| |/ / (_| \__ \ (_| (_| | | | | | | |  __/ |   
 \__, |_| |_|\__,_/___\__,_|___/\___\__,_|_| |_|_| |_|\___|_|   
  __/ |\033[0;37;41m[WVS v 0.1 Special ReverseIp]\033[0;40m
 |___/                                                          

    \033[0;37;41m[ Coded by M4L1KL8590X ]
    \033[0;37;41m[ICQ:https://icq.im/greatzcode]
    \033[0;37;41m[Not responsible for any illegal usage of this tool.]
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()

ip_list = open(Targetssa, 'r').read().split('\n')
for sites in ip_list:
  prepare(sites)

