import sys
import os
import datetime
import time 
import socket


status = 'down'
previous_status = 'down'
file = 'path_to_log'
while True:
	conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conn_socket.settimeout(2)
	ldap = ('IP_ADDRESS', PORT)
	response = conn_socket.connect_ex(ldap)
	if response == 0:
		today = datetime.datetime.now()
		now = today.strftime('%m%d%Y, %H:%M')
		print('Connection up')
		value = 'Connection up ' + now + ' \n'
		status = 'up'
		if previous_status != status:
			log_file = open(file, 'a+')
			log_file.write(value.lower())
			log_file.close()
			previous_status = status
		else:
			previous_status = status
	else:
		today = datetime.datetime.now()
		now = today.strftime('%m%d%Y, %H:%M')
		print('Connection down')
		value = 'Connection down ' + now + ' \n'
		status = 'down'
		if previous_status != status:
			log_file = open(file, 'a+')
			log_file.write(value.lower())
			log_file.close()
			previous_status = status
		else:
			previous_status = status

	time.sleep(15)



