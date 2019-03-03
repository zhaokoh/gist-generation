import glob

BASE_FOLDER='/Volumes/Spaceship/Alon_Gist/nishimoto-images'
TARGET_FOLDER='stimulus'
PRACTICE_IMAGES = [3, 9, 14] # These are ignored
NUM_IMAGE_SET = 5

all_images = glob.glob(BASE_FOLDER + "/im*.jpg")

print("<item pictures>")
for img in range(1, len(all_images)):
    filename = all_images[img][all_images[img].rfind("/"):]
    print("/" + str(img) + " = \"" + TARGET_FOLDER + filename + "\"")
print("</item>")
