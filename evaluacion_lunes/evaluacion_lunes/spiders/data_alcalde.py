# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "cantones"

    def start_requests(self):
      
        archivo = open("data/url.csv", "r")
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       


        filename = ("data/data_canton.csv")
        with codecs.open(filename, 'a', encoding='utf-8') as f:
        	f.write("Canton;Candidato; Partido \n")
        	lista=response.xpath('//table[@class="wikitable"]')
        	va = lista.xpath('tbody/tr')
        	for v in va:
        		td=v.xpath('td')
        		if len(td)>0:
        			canton=td[0].xpath('text()')
        			if len(canton)>0:
        				canton = td[0].xpath('text()').extract()[0]
        			else:
        				canton= td[0].xpath('a/text()').extract()[0]
        			nombre=td[1].xpath('text()')
        			if len(nombre)>0:
        				nombre = td[1].xpath('text()').extract()[0]
        			else:
        				nombre= td[1].xpath('a/text()').extract()[0]
        			partido=td[2].xpath('a/text()')
        			if len(partido)>0:
        				partido = td[2].xpath('a/text()').extract()[0]
        			else:
        				partido= td[2].xpath('text()').extract()[0]   	
		        	f.write(u"%s;%s;%s\n" % (canton,nombre,partido))
        self.log('Saved file %s' % filename)