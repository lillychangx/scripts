#!/bin/sh

#get disk utilization, sort to get largest files/directories, print top 10


du -a | sort -n -r | head -n 10
