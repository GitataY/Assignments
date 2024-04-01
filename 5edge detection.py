from skimage import io, filters, feature, color
import matplotlib.pyplot as plt

# Load an image
image_path = r'C:\Users\Yvonne\Downloads\data science\image\tools image.png' 
image = io.imread(image_path)

# Check if the image has 4 channels (RGBA), convert it to RGB
if image.shape[-1] == 4:
    image_rgb = color.rgba2rgb(image)
else:
    image_rgb = image

# Convert the RGB image to grayscale
image_gray = color.rgb2gray(image_rgb)

# Apply a Gaussian filter to the grayscale image
gaussian_filtered_image = filters.gaussian(image_gray, sigma=1)

# Perform edge detection using the Canny edge detector
edges = feature.canny(gaussian_filtered_image)

# Display the original, RGB (if converted), grayscale, Gaussian filtered, and edge-detected images
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(25, 5))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title('Original Image')
ax[0].axis('off')

if image.shape[-1] == 4:
    ax[1].imshow(image_rgb)
    ax[1].set_title('RGB Image')
    ax[1].axis('off')
else:
    ax[1].set_visible(False)

ax[2].imshow(image_gray, cmap=plt.cm.gray)
ax[2].set_title('Grayscale Image')
ax[2].axis('off')

ax[3].imshow(gaussian_filtered_image, cmap=plt.cm.gray)
ax[3].set_title('Gaussian Filtered')
ax[3].axis('off')

ax[4].imshow(edges, cmap=plt.cm.gray)
ax[4].set_title('Canny Edges')
ax[4].axis('off')

plt.tight_layout()
plt.show()
