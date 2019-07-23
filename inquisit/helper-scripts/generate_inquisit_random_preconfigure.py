from math import floor
from random import shuffle
from shutil import copyfile, rmtree

import glob
import os
import random
import numpy as np

BASE_FOLDER='/Volumes/Spaceship/projects/gist-generation/shinji_imagesets/2/buckets/5'
TARGET_FOLDER=''
OUTPUT_FOLDER='/Volumes/Spaceship/projects/gist-generation/shinji_imagesets/2/buckets/5'
PRACTICE_IMAGES = ['im0000003.jpg', 'im0000009.jpg', 'im0000014.jpg'] # These are ignored
NUM_IMAGES_PER_SET = 21
NUM_SOA_GROUP = 3
NUM_PER_SOA = int(NUM_IMAGES_PER_SET/NUM_SOA_GROUP)
NUM_OF_RESPONSE_PER_SOA = 10
TOTAL_PARTICIPANTS = NUM_SOA_GROUP * NUM_OF_RESPONSE_PER_SOA

def shift(l, n):
    return l[n:] + l[:n]

all_images = glob.glob(BASE_FOLDER + "/im*.jpg")

actual_stimuli_files = []

for img in range(0, len(all_images)):
    filename = all_images[img][all_images[img].rfind("/")+1:]
    
    if (filename not in PRACTICE_IMAGES):
        actual_stimuli_files.append(filename)


actual_stimuli_files = actual_stimuli_files[0:NUM_IMAGES_PER_SET]

# Now we have a list of filenames, e.g. im0000029.jpg in a list.
# We shuffle them and divide into num_of_buckets
shuffle(actual_stimuli_files)

# Generates the matrix for SOA MxN, M=Number of participants, N=The SOA used for each image
soa_matrix = [[0] * TOTAL_PARTICIPANTS for i in range(NUM_IMAGES_PER_SET)]
soa_array = [67] * NUM_OF_RESPONSE_PER_SOA + [133] * NUM_OF_RESPONSE_PER_SOA + [267] * NUM_OF_RESPONSE_PER_SOA

batch_67imgs = actual_stimuli_files[0:NUM_PER_SOA]
batch_133imgs = actual_stimuli_files[NUM_PER_SOA:NUM_PER_SOA*2]
batch_267imgs = actual_stimuli_files[NUM_PER_SOA*2:NUM_PER_SOA*3]

participant_soa_matrix = [[0] * NUM_IMAGES_PER_SET for i in range(TOTAL_PARTICIPANTS)]
participant_image_matrix = [[0] * NUM_IMAGES_PER_SET for i in range(TOTAL_PARTICIPANTS)]

print("Participant Image Matrix: %d x %d" % (np.shape(participant_image_matrix)))
print("Participant SOA Matrix: %d x %d" % (np.shape(participant_soa_matrix)))

for a_participant in range(TOTAL_PARTICIPANTS):
    pointer = 0

    actual_stimuli_files = shift(actual_stimuli_files, 1)

    for an_image_index in range(NUM_IMAGES_PER_SET):
        soa_list = [67, 133, 267]

        participant_soa_matrix[a_participant][an_image_index] = soa_list[an_image_index % NUM_SOA_GROUP]
        participant_image_matrix[a_participant][an_image_index] = actual_stimuli_files[an_image_index]


image_soa_matrix = [[0] * NUM_IMAGES_PER_SET for i in range(NUM_SOA_GROUP)]

# The following are sanity check to ensure all conditions have exactly the same count
image_soa_dict = {}
for i in range(len(participant_image_matrix)):
    for j in range(len(participant_image_matrix[i])):
        if (participant_image_matrix[i][j] in image_soa_dict.keys()):
            value = image_soa_dict[participant_image_matrix[i][j]]
        else:
            value = [0, 0, 0]
            image_soa_dict[participant_image_matrix[i][j]] = value
        
        if (participant_soa_matrix[i][j] == 67):
            value[0] = value[0]+1
        elif (participant_soa_matrix[i][j] == 133):
            value[1] = value[1]+1
        elif (participant_soa_matrix[i][j] == 267):
            value[2] = value[2]+1


print(image_soa_dict)

variable_group_code = "<variables>\n"
picset_code = ""

# Now we are happy - we will shuffle everything and print the Inquisit code
for i in range(len(participant_image_matrix)):

    image_67 = []
    image_133 = []
    image_267 = []

    for j in range(len(participant_image_matrix[i])):
        if (participant_soa_matrix[i][j] == 67):
            image_67.append(participant_image_matrix[i][j])
        elif (participant_soa_matrix[i][j] == 133):
            image_133.append(participant_image_matrix[i][j])
        elif (participant_soa_matrix[i][j] == 267):
            image_267.append(participant_image_matrix[i][j])

    picset_code = picset_code + ("<item picset_67_%d>\n" % (i+1))
    for s in range(len(image_67)):
        picset_code = picset_code + ("/%d = \"%s\"\n" % (s+1, image_67[s]))
    picset_code = picset_code + "</item>\n"

    picset_code = picset_code + ("<item picset_133_%d>\n" % (i+1))
    for s in range(len(image_133)):
        picset_code = picset_code + ("/%d = \"%s\"\n" % (s+1, image_133[s]))
    picset_code = picset_code + "</item>\n"

    picset_code = picset_code + ("<item picset_267_%d>\n" % (i+1))
    for s in range(len(image_133)):
        picset_code = picset_code + ("/%d = \"%s\"\n" % (s+1, image_267[s]))
    picset_code = picset_code + "</item>\n"

    variable_group_code = variable_group_code + ("/ group = (%d of %d) (items_67soa = picset_67_%d, items_133soa = picset_133_%d, items_267soa = picset_267_%d)\n" % (i+1, TOTAL_PARTICIPANTS, i+1, i+1, i+1))

variable_group_code = variable_group_code + "/ groupassignment = groupnumber\n</variables>"

# print(picset_code)
# print(variable_group_code)

with open(OUTPUT_FOLDER + "/" + "groupassignment.txt", "w") as text_file:
    print(variable_group_code + "\n\n\n" + picset_code, file = text_file)
