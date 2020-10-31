#Python Compare Two Images
# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()

# load the images -- 
jp_gates1 = cv2.imread("Jp_gate/jp_gates_original.png")
jp_gates2 = cv2.imread("Jp_gate/jp_gates_contrast.png")
jp_gates3 = cv2.imread("Jp_gate/jp_gates_photoshopped.png")
lion1 = cv2.imread("Lion/Lion1.jpg")
lion2 = cv2.imread("Lion/Lion2.jpg")
lion3 = cv2.imread("Lion/Lion3.jpg")
# convert the images to grayscale
jp_gates1 = cv2.cvtColor(jp_gates1, cv2.COLOR_BGR2GRAY)
jp_gates2 = cv2.cvtColor(jp_gates2, cv2.COLOR_BGR2GRAY)
jp_gates3 = cv2.cvtColor(jp_gates3, cv2.COLOR_BGR2GRAY)
lion1 = cv2.cvtColor(lion1, cv2.COLOR_BGR2GRAY)
lion2 = cv2.cvtColor(lion2, cv2.COLOR_BGR2GRAY)
lion3 = cv2.cvtColor(lion3, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Original", jp_gates2), ("Contrast", jp_gates1), ("Photoshopped", jp_gates3), ("Brownish_lion", lion1), ("Southafrica_lion", lion2), ("Blacklion", lion3)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 6, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
compare_images(jp_gates2, jp_gates2, "Original vs. Original")
compare_images(jp_gates2, jp_gates1, "Original vs. Contrast")
compare_images(jp_gates2, jp_gates3, "Original vs. Photoshopped")
compare_images(lion1, lion1, "Brownish_lion vs. Brownish_lion")
compare_images(lion1, lion2, "Brownish_lion vs. Southafrica_lion")
compare_images(lion1, lion3, "Brownish_lion vs. Blacklion")