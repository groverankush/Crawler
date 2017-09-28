from general import *


class Spider:
    crawled_set = set()
    queued_set = set()

    def __init__(self, url_to_crawl, domain_name):
        self.url = url_to_crawl
        self.domain = domain_name

        self.boot()
        self.crawl()

    def boot(self):
        create_project(self.domain)
        create_data_files(self.url)
        Spider.crawled_set = file_to_set(CRAWLED_FILE)
        Spider.queued_set = file_to_set(QUEUE_FILE)

    def crawl(self):
        if self.url not in Spider.crawled_set:


