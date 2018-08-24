#!/usr/bin/env python
#coding:utf-8
#Author:

import smtplib
from email.mime.text import MIMEText
import subprocess
body=""
fales="false"
obj=subprocess.Popen("curl -sXGET http://127.0.0.1:9200/_cluster/health?pretty=true"),shell=True,
stdout=subprocess.PIPE()
data=opb.stdout.read()
data1=eval(data)
status=data1.get("status")

if status == "green":
	print 50
else:
	print 100
