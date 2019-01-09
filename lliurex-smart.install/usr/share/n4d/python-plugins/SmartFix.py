import os

class SmartFix:
	
	def __init__(self):
		
		self.command="/usr/sbin/lliurex-smart-path-fixer"
		
	#def init
	
	def startup(self,options):
		
		if options["boot"]:
			os.system(self.command)
	
#class SmartFix