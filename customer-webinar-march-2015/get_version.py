#!/usr/bin/env python
import os, sys, time, socket, time, datetime, commands, subprocess, re


argument = sys.argv[1]
pattern =  sys.argv[2]

command = "%s 2>&1 > /tmp/tt" % (argument)

output = os.system(command)

command_output = open("/tmp/tt", "r")

for line in command_output:
    if re.match(pattern, line):
        result = line.split(' ', 1)
        print line


