import requests
from lxml import html
from StringIO import StringIO
import xlwt


class MEPscraper(object):
	def __init__(self, url, mep_num, ws):
		page = requests.get(url)
		tree = html.fromstring(page.content)
		name = tree.xpath('''//*[@id="mep_name_button"]/text()''') [0]
		europeanparty = tree.xpath('//*[@id="zone_before_content_global"]/div/div[1]/ul/li[2]/text()') [0]
		homeparty = tree.xpath('//*[@id="zone_before_content_global"]/div/div[1]/ul/li[3]/span/text()') [0]
		email = tree.xpath('//*[@id="email-0"]/@href') [0]
		emailREAL = str(email) [::-1]
		emailREAL = emailREAL.replace ("]ta[", '@')
		emailREAL = emailREAL.replace ("]tod[", '.')
		emailREAL = emailREAL.replace (":otliam", ' ')
		name = str(name)
		print name
		print europeanparty
		print homeparty
		print emailREAL
		try:
			website = tree.xpath('//*[@id="content_right"]/div[2]/ul/li[2]/a/@href') [0] #0 to get rid of weird brakets
			#websiteREAL = str(website) [::-1]
			DATA = (name, emailREAL, website, europeanparty, homeparty)
			print website
			print
		except:
			print "no website"
			DATA = (name, emailREAL, "No Website", europeanparty, homeparty)
			print
		

		i=0
		while(i<5):
			ws.write(mep_num, i, DATA[i])
			i+=1
		#ws.col(0).width = 256 * max([len(row[0])for row in DATA])
