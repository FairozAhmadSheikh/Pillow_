from PIL import Image
import numpy as np

# #create a new image 
image1=Image.new("RGB",(400,500),(255,0,0))
image2=Image.new("RGB",(400,500),(0,255,0))
image3=Image.new("RGB",(400,500),(0,0,255))

# Combine the images horizontally using a single step
image4 = Image.fromarray(
    np.hstack([np.array(image1), np.array(image2), np.array(image3)])
)

# Show the combined image
image4.show()


# Convert the image to a NumPy array
image_array = np.array(image1)

# Print the shape of the array (height, width, channels)
print("Array shape:", image_array.shape)

# Display the array data
print(image_array)

# Convert the NumPy array back to an image
restored_image = Image.fromarray(image_array)

# Show the restored image
restored_image.show()


