# -*- coding: UTF-8 -*-
import pycurl
import StringIO
import zlib

def getWebDataViaCurl(url, referer = None):
	c = pycurl.Curl()
	c.setopt( pycurl.URL , url.encode('utf-8') )
	c.setopt( pycurl.FOLLOWLOCATION , True )

	c.setopt( pycurl.HTTPHEADER , [
		'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0'
		'Host: blog.changyy.org',
		'Connection: keep-alive',
		'Cache-Control: max-age=0',
		'Referer: '+str(referer),
		'Accept-Language: zh-tw,zh;q=0.8,en-us;q=0.5,en;q=0.3',
		'Accept-Encoding: gzip, deflate',
		'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	] )
	outp = open('/tmp/pycurl','wb')
	outp.close() 
	c.setopt( pycurl.COOKIEFILE , '/tmp/pycurl' )
	c.setopt( pycurl.COOKIEJAR , '/tmp/pycurl' )
	
	b = StringIO.StringIO()
	h = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.HEADERFUNCTION, h.write)

	c.perform()

	response = b.getvalue()
	b.close()
	
	header = h.getvalue()
	h.close()
	
	return {'header':header, 'body':response}

#data = zlib.decompress(getWebDataViaCurl(target)['body'], 16+zlib.MAX_WBITS)
