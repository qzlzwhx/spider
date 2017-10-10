import scrapy


class CijiluSpider(scrapy.Spider):
	name = 'cijilu'
	start_urls = [
		'http://www.yemalu.in/'
	]
	def parse(self, response):
		host = self.start_urls[0]
		urls = []
		for link in response.css('div.well-sm a'):	
			url =host + link.css('a::attr(href)').extract_first()
			urls.append(url)
		for video_url in urls:
			video_page = response.urljoin(video_url)
			yield scrapy.Request(video_url, callback=self.parse_video)

	def parse_video(self, response):
		mp4_download_url = response.css('ul.dropdown-menu')[-1]
		video_urls = mp4_download_url.css('a::attr(href)').extract()
		print '---------------------'
		print video_urls
		print '---------------------'
		
