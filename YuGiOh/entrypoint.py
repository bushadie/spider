from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'YuGiOhMonsterSpider', '-o', 'monster.csv'])
