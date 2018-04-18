from scrapy import cmdline
from jd.spiders.JdSpider import JdSpider

if __name__ =="__main__":
    JdSpider.start_urls =["https://search.jd.com/Search?keyword=显示器&enc="+
                          "utf-8&suggest=3.his.0.0&pvid=3c0df64a9a3544c0aea06d3f5c3a30a8"]
    cmdline.execute("scrapy crawl jd".split())