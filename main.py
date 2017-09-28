from spider import Spider
from urllib.parse import urlparse

BASE_URL = ""

DOMAIN_NAME = urlparse(BASE_URL).hostname

firstSpider = Spider(BASE_URL, DOMAIN_NAME)
