#!/usr/bin/python

import socket
import os # provide function to see if files exist
import sys # allow to check number of arguments specified

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] File Does Not Exist'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[-] Access Denied'
			exit(0)
	else:
		print '[-] Usage: ' + str(sys.argv[0]) + " <vuln filename>"
