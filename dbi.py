#!/usr/bin/python2
'''
'''
import httplib2
class dbi:
	def conn(self):
		self.conn = httplib2.Http()
		
	def get(self, key):		
		resp, content = self.conn.request( "http://lindev:1978/files.kch/%s" % key.encode("UTF-8") )
		if content is '':
			content = None
		return content
		
	def set(self, key, value):
		resp, content = self.conn.request( "http://lindev:1978/files.kch/%s" % key.encode("UTF-8"), method="PUT", body = value.encode("UTF-8"), headers={'content-type':'text/plain'} )
		if resp['status'] is not '201':
			return False
		return True
		
