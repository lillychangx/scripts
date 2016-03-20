#!/usr/bin/env python
import os, sys, time, socket, time, datetime, subprocess, re, commands



def install_package():
   output = os.system("sudo apt-get update 2>&1 > /tmp/tt")
#  output = os.system("apt-get install openssl -y 2>&1 > /tmp/tt")
   
   curl_output = open("/tmp/tt", "r")
   for line in curl_output:
      if re.match("(.*)Reading(.*)package(.*)lists(.*)Done(.*)", line):
         print line
         #total_time = line.split(":")
   return 0


install_package()


