from math import floor
from random import shuffle
from shutil import copyfile, rmtree

import glob
import os

BASE_FOLDER='/Volumes/Spaceship/projects/gist-generation/shinji_imagesets/5'
TARGET_FOLDER=''
OUTPUT_FOLDER='/Volumes/Spaceship/projects/gist-generation/shinji_imagesets/5/buckets'
PRACTICE_IMAGES = ['im0000003.jpg', 'im0000009.jpg', 'im0000014.jpg'] # These are ignored
NUM_IMAGES_PER_SET = 21

all_images = glob.glob(BASE_FOLDER + "/im*.jpg")

actual_stimuli_files = []

for img in range(0, len(all_images)):
    filename = all_images[img][all_images[img].rfind("/")+1:]
    
    if (filename not in PRACTICE_IMAGES):
        actual_stimuli_files.append(filename)

# Now we have a list of filenames, e.g. im0000029.jpg in a list.
# We shuffle them and divide into num_of_buckets

total_files = len(actual_stimuli_files)
print("Shuffling the stimuli files...%d" % (total_files))
shuffle(actual_stimuli_files)

num_of_buckets = floor(total_files/NUM_IMAGES_PER_SET)
print("Total files: %d. Each bucket will contain %d images. Total of %d buckets." % (total_files, NUM_IMAGES_PER_SET, num_of_buckets))

for i in range(0, num_of_buckets):
    image_bucket_files = actual_stimuli_files[i*NUM_IMAGES_PER_SET:(i+1)*NUM_IMAGES_PER_SET]

    if i == num_of_buckets-1: # The last set will include the remaining images (leftovers)
        image_bucket_files = actual_stimuli_files[i*NUM_IMAGES_PER_SET:]

    print("Image bucket %d has %d images." % (i+1, len(image_bucket_files)))
    
    # Now we copy the files over the output folder and generate the corresponding Inquisit syntax
    data_set = i+1
    data_set_dir = OUTPUT_FOLDER + "/" + str(data_set)
    if os.path.exists(data_set_dir):
        rmtree(data_set_dir)

    os.mkdir(data_set_dir)

    inquisit_text = "<item pictures>\n"
    for j in range(0, len(image_bucket_files)):
        subset_file = image_bucket_files[j]
        copyfile(BASE_FOLDER + "/" + subset_file, data_set_dir + "/" + subset_file)
        inquisit_text = inquisit_text + "/" + str(j+1) + " = \"" + TARGET_FOLDER + subset_file + "\"\n"
    inquisit_text = inquisit_text + "</item>\n"

    with open(data_set_dir + "/" + "inquisit.txt", "w") as text_file:
        print(inquisit_text, file = text_file)

