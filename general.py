import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

PROJECT_NAME = ''
QUEUE_FILE = "queue.txt"
CRAWLED_FILE = "crawled.txt"


# Each website you crawl is a different folder
def create_project(domain_name):
    assert len(domain_name) > 0

    global PROJECT_NAME

    PROJECT_NAME = domain_name.replace(".", "_")
    if not os.path.isdir(os.path.join(os.getcwd(), PROJECT_NAME)):
        print("Creating project " + PROJECT_NAME)
        os.mkdir(PROJECT_NAME)


# Create Queue and crawled files (if not created)
def create_data_files(base_url):
    assert os.path.exists(PROJECT_NAME)

    if not os.path.exists(QUEUE_FILE):
        write_file(QUEUE_FILE, base_url, append=False)
    if not os.path.exists(CRAWLED_FILE):
        write_file(CRAWLED_FILE, "", append=False)


# Method to create file and add data to it.
def write_file(path, data="", append=True, delete=False):
    path = os.path.join(os.getcwd(), PROJECT_NAME, path)
    if delete:
        with open(path, 'w'):
            return
    with open(path, 'a' if append else 'w') as f:
        f.write(data + "\n")


# Read a file and convert it to a set.
def file_to_set(file_name):
    results = set()
    file_name = os.path.join(os.getcwd(), PROJECT_NAME, file_name)
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.strip())
    return results


def set_to_file(links, file_name):
    """Method to convert set into files."""

    write_file(file_name, delete=True)
    for link in sorted(links):
        write_file(file_name, link)


def get_links_from_page(url):
    """Returns a list of all the <a> tags from an html page"""

    handle = urlopen(url)
    html = handle.read()
    handle.close()
    a_tags = BeautifulSoup(html, "html.parser").findAll('a')
    result = []
    for tag in a_tags:
        result.append(tag.get('href'))
    return result
