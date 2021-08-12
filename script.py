import cv2
from skimage.metrics import structural_similarity as ssim

vidcap = cv2.VideoCapture('OS.mp4')
success,image = vidcap.read()
imageOld = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
count = 0
#cv2.imwrite("frame%d.jpg" % count, image)

while success:
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  #cv2.imshow("frame",image)
  success,image = vidcap.read()
  if(success):
	  imageO = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	  simlarityIndex = ssim(imageO, imageOld)
	  imageOld = imageO
	  count += 30
	  vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)	  
	  if(simlarityIndex<0.98):
	  	cv2.imwrite("frame%d.jpg" % count, image)
	  print('Read a new frame: ', success," ",simlarityIndex)

