from DeutscherPreisOnlineMarketing2018.items import Deutscherpreisonlinemarketing2018Item
import scrapy

class DPOM_spider(scrapy.Spider):
	name = 'DPOM_spider'
	allowed_urls = ["https://www.onlinekommunikationspreis.de"]
	start_urls = ["https://www.onlinekommunikationspreis.de/best-of-2018/"]

	def parse(self, response):
		Organisation = response.xpath('//div[@class="organisation"]/text()').extract()
		Projekt = response.xpath('//div[@class="project"]/text()').extract()
		try:
			Agentur = response.xpath('//div[@class="agency"]/text()').extract()
		except:
			Agentur = ""
		# print(url_list)
		# print("-"*50)

		item = Deutscherpreisonlinemarketing2018Item()

		
		item["Organisation"] = Organisation
		item["Projekt"] = Projekt
		item["Agentur"] = Agentur

		yield item

	def errback(self, failure):
		self.logger.error(repr(failure))
		if failure.check(HttpError):
			response = failure.value.response
			self.logger.error('HttpError on %s', response.t_url)
		elif failure.check(DNSLookupError):
			request = failure.request
			self.logger.error('DNSLookupError on %s', request.t_url)
		elif failure.check(TimeoutError, TCPTimedOutError):
			request = failure.request
			self.logger.error('TimeoutError on %s', request.t_url)


