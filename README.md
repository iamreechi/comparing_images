# comparing_images
 Image Classification using SSIM and MSE 
 
 This is an image classifier that can tell how similar two images using SSIM (Structural Similarity Index) and MSE (Mean Square Error)
 MSE calculate the mean square error between each pixels for the two images we are comparing. Whereas SSIM will do the opposite and look for similarities within pixels; i.e. if the pixels in the two images line up and or have similar pixel density values.
 While generally the higher the MSE the least similar they are SSIM on the other hand puts everything in a scale of -1 to 1. A score of 1 meant they are very similar and a score of -1 meant they are very different
