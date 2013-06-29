# -*- coding: UTF-8 -*-
import os, sys
import urllib2
import json
from BeautifulSoup import BeautifulSoup

def help(argv):
	print "Usage> ", argv[0], "blogger_url /path/output"

if __name__ == '__main__':
	if len(sys.argv) < 3:
		help(sys.argv)
		sys.exit(0)
	url = sys.argv[1]
	output = sys.argv[2]

	hash = {}
	hash_check = len(hash)

	target = url
	while True:
		print "Target: " +target.encode('utf-8')
		data = urllib2.urlopen(target)
		soup = BeautifulSoup(data)

		articles = soup.findAll("h3", {'class':'post-title entry-title'}) # blogger
		print "add: ", len(articles), " before_add: ", hash_check
		for article in articles:
			#print article
			link = article.a['href']
			title = article.a.contents[0]
			hash[title] = link
	
		referer = target
		next = soup.findAll("a", {'id':'Blog1_blog-pager-older-link'})
		if len(next) > 0 :
 			target = soup.findAll("a", {'id':'Blog1_blog-pager-older-link'})[0]['href'].strip()
		else:
			target = ""

		if target == "" or len(articles) == 0 or len(hash) == hash_check:
			print "Done"
			break

		hash_check = len(hash)
		sys.stdout.flush()

	out = open(output, "wb")
	out.write( json.dumps(hash) )
	out.close()

