import os


# Each website you crawl is a different folder
def create_project(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.mkdir(directory)


# Create Queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    assert os.path.exists(project_name)
    os.chdir(project_name)
    queue = "queue.txt"
    crawled = "crawled.txt"

    if not os.path.exists(queue):
        write_file(queue, base_url, append=False)
    if not os.path.exists(crawled):
        write_file(crawled, "", append=False)


# Method to create file and add data to it.
def write_file(path, data="", append=True, delete=False):
    if delete:
        with open(path, 'w'):
            return
    with open(path, 'a' if append else 'w') as f:
        f.writelines(data)


# Read a file and convert it to a set.
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.strip())
    return results


# Method to convert set into files.
def set_to_file(links, file_name):
    write_file(file_name, delete=True)
    for link in sorted(links):
        write_file(file_name, link)
