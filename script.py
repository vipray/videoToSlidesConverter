'''
	Author : Vipray Jain

	Description:
	- It takes video as input and extract different sildes(Images) from the video.
	- Then It convert images into PDF.
	- It Use structural_similarity to check similarity between two frames.
	- Two varaibles can be varied as per your specific case:
		- var "threshold" (depends on amount of change between two frames) can be 
			- decreased if getting False Positives.
			- increased if missing True Positives.
		- var "skipBy" (depends on speed of slides) can be
			- decreased if missing True Positives.
			- increased if getting False Positives.

'''


# imports
import cv2
import sys
import img2pdf
import glob
import os

from skimage.metrics import structural_similarity as ssim

#taking video name as a CLI argument.
videoName = sys.argv[1]

# Start Capturing Video
vidcap = cv2.VideoCapture(videoName)

# Read a frame from the video
success,image = vidcap.read()

# Counter For skipping Frames and Naming the saved Image
count = 0

# Threshold for considering two images different
threshold = 0.98

# To skip frames
skipBy = 30

# To hold last Gray Image
oldGrayImage = None

# "success" is true if vidcap.read() captured an Image
if(success):
	# Open below line to Write Image into the folder
	cv2.imwrite("frame%d.jpg" % count, image)
	
	# Convert colored image into Gray image
	oldGrayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Check frames till the end of the video
while success:

  # Read a frame from the video
  success,image = vidcap.read()

  # "success" is true if vidcap.read() captured an Image
  if(success):
	  # Convert colored image into Gray image
	  currentGrayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	  # Check similarity between the last frame captured (oldGrayImage) and current frame (oldGrayImage)
	  simlarityIndex = ssim(currentGrayImage, oldGrayImage)
	  
	  # If Similarity is less than threshold, consider the two frame as differnet
	  if(simlarityIndex < threshold):
		
		# Write Image into the folder
	  	cv2.imwrite("frame%d.jpg" % count, image)
	  	
	  
	  # Just To See 
	  print('Read a new frame: ', success," ",simlarityIndex)
	  
	  # Store current Gray Image as old Gray Image
	  oldGrayImage = currentGrayImage

	  # Increase Counter to skip some frames
	  count += skipBy

	  # Skip skipBy frames
	  # Checking all the frames doesn't help much, it just increase the Time Complexity.
	  vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)	  



					
''' Images to PDF conversion '''


# List of all Images(name starts with 'frame')
imageList = glob.glob("frame*.jpg")

# Sort with respect to the Image number, so the PDF pages are in proper sequence
sortedImageList = sorted(imageList, key = lambda x: (int(x.split("frame")[1].split(".jpg")[0]), x))

# make a pdf from images using 'img2pdf' library
with open(videoName.split(".")[0]+".pdf","wb") as f:
	f.write(img2pdf.convert(sortedImageList))

# delete all the images once the pdf is ready	
for img in sortedImageList:
	os.remove(img)
