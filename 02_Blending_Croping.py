from PIL import Image
import numpy as np

# Paths to the images
image1_path = "c1.jpg"
image2_path = "c2.jpg"

# Open the images
img1 = Image.open(image1_path).convert("RGBA")
img2 = Image.open(image2_path).convert("RGBA")

# Resize the second image to match the size of the first image
img2 = img2.resize(img1.size)

# Convert images to NumPy arrays
arr1 = np.array(img1)
arr2 = np.array(img2)

# Blend the images (50% each)
blended_arr = ((arr1 * 0.5) + (arr2 * 0.5)).astype(np.uint8)
blended_img = Image.fromarray(blended_arr, "RGBA")

# Save and display the blended image
blended_img.show()
blended_img.save("blended_image.png")

# Crop the blended image
crop_box = (50, 50, 300, 300)  # (left, top, right, bottom)
cropped_img = blended_img.crop(crop_box)

# Save and display the cropped image
cropped_img.show()
cropped_img.save("cropped_image.png")
