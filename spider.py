from general import *
from urllib.parse import urlparse


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
            self.add_urls_to_queue()
            Spider.queued_set.remove(self.url)
            Spider.crawled_set.add(self.url)
            Spider.update_files()

    def add_urls_to_queue(self):
        urls = get_links_from_page(self.url)
        for url in urls:
            if urlparse(url).hostname != self.domain:
                continue
            if url in Spider.queued_set or url in Spider.crawled_set:
                continue
            Spider.queued_set.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.crawled_set, CRAWLED_FILE)
        set_to_file(Spider.queued_set, QUEUE_FILE)
