from math import floor
from random import shuffle
from shutil import copyfile, rmtree

import csv
import glob
import os
import random
import numpy as np

BASE_FOLDER='~/Downloads'
TARGET_FOLDER=''
OUTPUT_FOLDER='/Volumes/Spaceship/projects/gist-generation/shinji_imagesets/5/buckets/4'
MIN_LENGTH_WORDS=2
ITEMS_PER_GROUP=350

word_list = []
with open('/Users/Zhao/Downloads/unique_word_stemmed.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if len(row) >= 2 and not "-" in row[1] and not "," in row[1] and len(row[1]) >= MIN_LENGTH_WORDS:
            word_list.append(row[1])

with open('/Users/Zhao/Downloads/unique_word_not_stemmed.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if len(row) >= 2 and "-" in row[1] and len(row[1]) >= MIN_LENGTH_WORDS:
            word_list.append(row[1])


random.shuffle(word_list)
print("Total unique words: %d" % len(np.unique(word_list)))

number_of_groups = len(np.unique(word_list))//ITEMS_PER_GROUP + 1
print("Dividing into %d groups with %d words in each group (except the last group)." % (number_of_groups, ITEMS_PER_GROUP))

item_list_code = ""
for i in range(1, number_of_groups):
    start_index = (i-1)*ITEMS_PER_GROUP
    end_index = i*ITEMS_PER_GROUP-1

    subset_words = word_list[start_index:end_index]

    item_list_code = item_list_code + ("<item word_list_%d>\n" % (i))
    for j in range(1, len(subset_words)+1):
        item_list_code = item_list_code + ("/%d = \"%s\"\n" % (j, subset_words[j-1]))
    item_list_code = item_list_code + "</item>\n\n"

item_list_code = item_list_code + ("<item word_list_%d>\n" % (number_of_groups))
last_group = word_list[(number_of_groups-1)*ITEMS_PER_GROUP:]

for j in range(1, len(last_group)+1):
    item_list_code = item_list_code + ("/%d = \"%s\"\n" % (j, last_group[j-1]))
item_list_code = item_list_code + "</item>\n\n"

variable_group_code = "<variables>\n"
for i in range(1, number_of_groups+1):
    variable_group_code = variable_group_code + ("/ group = (%d of %d) (words = word_list_%d)\n" % (i, number_of_groups, i))

variable_group_code = variable_group_code + "/ groupassignment = groupnumber\n</variables>"

with open("./james-word-group-assignments.txt", "w") as text_file:
    print(variable_group_code + "\n\n\n" + item_list_code, file = text_file)
