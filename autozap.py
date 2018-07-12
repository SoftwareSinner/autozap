#!/usr/bin/env python3


import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'http://127.0.0.1' # Replace this with your target URL or IP
# Change to match the API key set in ZAP under tools menu, options, API tab. or use None if the API key is disabled.
apikey = 'Place your API KEY HERE'


class OwaspZap(object):

	def Api_Connect(self):
		zap = ZAPv2(apikey=apikey)
		print('[+]Accessing target {}'.format(target))
		zap.urlopen(target)
		time.sleep(2)

	def Spider_Crawl(self):
		zap = ZAPv2(apikey=apikey)
		print('Spidering target {}'.format(target))
		scanid = zap.spider.scan(target)
		# Give the Spider a chance to start
		time.sleep(2)
		while(int(zap.spider.status(scanid)) < 100):
			#This will loop until the spider has finished
			print('Spider progress %: {}'.format(zap.spider.status(scanid)))
			time.sleep(2)
		print('Spider crawl completed')

	def Passive_Scan(self):
		zap = ZAPv2(apikey=apikey)
		while(int(zap.pscan.records_to_scan) > 0):
			print('Records to passive scan : {}'.format(zap.pscan.records_to_scan))
			time.sleep(2)
		print('Passive Scan completed')

	def Active_Scan(self):
		zap = ZAPv2(apikey=apikey)
		print('Active Scanning target {}'.format(target))
		scanid = zap.ascan.scan(target)
		while(int(zap.ascan.status(scanid)) < 100):
	    		# Loop until the scanner has finished
			print('Scan progress %: {}'.format(zap.ascan.status(scanid)))
			time.sleep(5)
		print('Active Scan completed')

	def Show_Results(self):
		zap = ZAPv2(apikey=apikey)
		# Reports the results
		print('Hosts: {}'.format(', '.join(zap.core.hosts)))
		print('Alerts: ')
		pprint(zap.core.alerts())


zapp = OwaspZap()
zapp.Api_Connect()
zapp.Spider_Crawl()
zapp.Passive_Scan()
zapp.Active_Scan()
zapp.Show_Results()
