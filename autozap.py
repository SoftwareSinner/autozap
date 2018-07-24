#!/usr/bin/env python3


import time
from pprint import pprint
from zapv2 import ZAPv2

target = '' # Replace this with your target URL or IP
# Change to match the API key set in ZAP under tools menu, options, API tab. or use None if the API key is disabled.
apiKey = '' # Place your OWASP ZAP API key in the quotes 


class OwaspZap(object):

	def spider_login(self):
		#spider crawling the main login page
		zap = ZAPv2(apikey=apiKey)
		print('[+]Accessing target {}'.format(target))
		zap.urlopen(target)
		time.sleep(2)
		print('Now Spidering target {}'.format(target))
		scanid = zap.spider.scan(target)
		# Give the Spider a chance to start
		time.sleep(2)
		while(int(zap.spider.status(scanid)) < 100):
			#This will loop until the spider has finished
			print('Spider progress %: {}'.format(zap.spider.status(scanid)))
			time.sleep(2)
		print('Spider crawl on login page completed')

	def active_login(self):
    	#Active scanner on login page
		zap = ZAPv2(apikey=apiKey)
		print('Running Active Scan {}'.format(target))
		scanid = zap.ascan.scan(target)
		while(int(zap.ascan.status(scanid)) < 100):
	    		# Loop until the scanner has finished
			print('Scan progress %: {}'.format(zap.ascan.status(scanid)))
			time.sleep(5)
		print('Active Scan completed')
		zap = ZAPv2(apikey=apiKey)
		# Reports the results
		print('Hosts: {}'.format(', '.join(zap.core.hosts)))
		print('Alerts: ')
		pprint(zap.core.alerts())	
	
	def url_auth(self):
		zap = ZAPv2(apikey=apiKey)
		ctx_name = " " Place a context for the url here
		ctx_id = zap.context.new_context(ctx_name)
		print('zap initizalized')
		login_url = " " # Place URL path you would like to scan here after authenticating with ZAP
		print("Now Authenticating..")
		zap.authentication.set_authentication_method(ctx_id, "formBasedAuthentication", "loginUrl=" + login_url)
	
	def spider_dashboard(self):
    		#spider crawling the dashboard after authenticating
		dash = " " # place dashboard page url here after authenticating into web app
		zap = ZAPv2(apikey=apiKey)
		ctx_name = " " # Place context here
		ctx_id = zap.context.new_context(ctx_name)
		print('[+]Accessing  Dashboard {}'.format(dash))
		zap.urlopen(dash)
		time.sleep(2)
		print('Now Spidering target {}'.format(dash))
		scanid = zap.spider.scan(dash,ctx_id)
		# Give the Spider a chance to start
		time.sleep(2)
		while(int(zap.spider.status(scanid)) < 100):
			#This will loop until the spider has finished
			print('Spider progress %: {}'.format(zap.spider.status(scanid)))
			time.sleep(2)
		print('Spider crawl on Dashboard page completed')


	def active_dash(self):
    	#Active scanner on login page
		zap = ZAPv2(apikey=apiKey)
		dash = " " # Place url path here
		print('Running Active Scan {}'.format(dash))
		scanid = zap.ascan.scan(dash)
		while(int(zap.ascan.status(scanid)) < 100):
	    		# Loop until the scanner has finished
			print('Scan progress %: {}'.format(zap.ascan.status(scanid)))
			time.sleep(5)
		print('Active Scan on Dashboard.action completed')
	

	def show_results(self):
		zap = ZAPv2(apikey=apiKey)
		# Reports the results
		print('Hosts: {}'.format(', '.join(zap.core.hosts)))
		print('Alerts: ')
		pprint(zap.core.alerts())


zapp = OwaspZap()
zapp.spider_login()
zapp.active_login()
zapp.url_auth()
zapp.spider_dashboard()
zapp.active_dash()
zapp.show_results()
