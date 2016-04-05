#!/bin/sh

# run ps command, sort by highest cpu, list top 5, and print CPU% and process command


ps aux | sort -rk 3,3 | head -n 6  |  awk '{print $3 "\t" $11}'