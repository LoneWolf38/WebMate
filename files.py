import os

# Folder will be made for each website you want to crawl

def create_project_dir(project_name):
    if not os.path.exists(project_name):
        print("Creating Project {}".format(project_name))
        os.makedirs(project_name)

# Files made to keep track of link crawled  or to be crawled


def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name +"/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        f.close


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        file.close

# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")

