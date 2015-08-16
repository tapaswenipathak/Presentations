from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from RecursiveScraper.items import RecursivescraperItem
import re

class RecursiveScrapperSpider (CrawlSpider) :
  handle_httpstatus_list = [302]
  name = "rs" #Name of your spider
  allowed_domains = ["cse.iitd.ernet.in"] #Add allowed domains, leave it blank to allow everything
  start_urls = ['http://www.cse.iitd.ernet.in/~naveen/'] #Has the start URL

  #allow add some regex or links to allow those
  #callback function for a url when allowed by the rul
  

  rules = (
      Rule(SgmlLinkExtractor(allow=("cse\.iitd\.ernet\.in/\~naveen/.*", ), restrict_xpaths=("/html/body/table/tbody/tr/td/a")), callback='parse_item', follow= True),
  )
  def parse_item(self, response) :
    sel = Selector (response)
    item = RecursivescraperItem ()
    item['URL'] = response.request.url
    print response.request.url
    item['content'] = sel.xpath ('/html/body/table/tbody/tr[3]/td[1]/text()[1]').extract()
    return item