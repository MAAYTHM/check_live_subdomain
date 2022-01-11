#!/usr/bin/python3

import os
from multiprocessing import Pool,cpu_count
from socket import gethostbyname
import requests as rq
import sys


def live_phase_2(domain):
	try:
		code = rq.head('https://' + domain + '/', timeout=2).status_code # checking if domain is reachable
		return [1,code]
	except Exception as e:
		return [0,'']


def live_phase_1(list_):
	length = 0
	while length != (len(l) - 1): # (len(l) - 1)
		try:
			res = gethostbyname(l[length]) # checking if domain is exist
		except Exception as e:
			length += 1
			continue

		code = live_phase_2(l[length])
		if code[0] == 1:
			print(f'{length}) ', l[length], ' -> ', res, '& code - ', code[1]) # printing result

			# writing to file :-
			with open('live.txt', 'a') as f:
				f.write(l[length] + ',' + str(code[1]) + '\n')
				f.close()

		length += 1


pool = Pool(cpu_count())
l = []

with open("subdomain.txt", 'r') as f:
	l = f.read().split('\n')[::-1]
	l = l[1:]
	f.close()

l = sorted(l)
try:
	pool.map(live_phase_1(l))
except Exception as e:
	print('\n',e)
	print('Finished...')
