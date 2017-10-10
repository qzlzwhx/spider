import scrapy


class CijiluSpider(scrapy.spider):
	name = 'cijilu'
	start_urls = [
		'http://www.yemalu.in/'
	]
	
