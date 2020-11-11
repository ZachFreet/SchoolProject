"""
    Searches deep inside a directory structure, looking for duplicate file.
    Duplicates aka copies have the same content, but not necessarily the same name.
"""
__author__ = ""
__email__ = ""
__version__ = "1.0"

# noinspection PyUnresolvedReferences
from os.path import getsize, join
from time import time

# noinspection PyUnresolvedReferences
from p1utils import all_files, compare



def search(file_list):
    img = all_files("images")  #Put all image files into list img
    lol = []
    while 0 < len(img):
        dups = [x for x in img if compare(img[0], x)]
        if 1 < len(dups):
            lol.append(dups)
        img = [x for x in img if not compare(img[0], x)]
    return lol




def faster_search(file_list):   # Faster searh function
    lol = []
    file_size = list(map(getsize, file_list))
    filtered = filter(lambda x: 1 < file_size.count(getsize(x)), file_list)
    fl = list(filtered)
    while 0 < len(fl):
        dup = [x for x in fl if compare(fl[0], x)]
        if 1 < len(dup):
            lol.append(dup)
        fl = [x for x in fl if not compare(fl[0], x)]
    return lol


def report(lol):
    print("== == Duplicate File Finder Report == ==")
    item = max(lol, key=len)
    print(f"This file: {item[0]} has the most duplicate files: {len(item) - 1}")
    print("Here are its 7 copies : ")
    for i in range(1, len(item)):
        print(item[i])

    print("")
    item = max(lol, key=lambda x: len(x) * getsize(x[0]))
    print(f"This file: {item[0]} takes up the most disk space : {getsize(item[0]) * (len(item) - 1)}")
    print("Here are its 2 copies")
    for i in range(1, len(item)):
        print(item[i])


if __name__ == '__main__':
    path = join(".", "images")

    # measure how long the search and reporting takes:
    t0 = time()
    report(search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")

    print("\n\n .. and now w/ a faster search implementation:")

    # measure how long the search and reporting takes:
    t0 = time()
    report(faster_search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")
