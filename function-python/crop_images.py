import os
from PIL import Image

# Input image folder
input_image_folder = r"C:\Users\chinh\OneDrive\Desktop\MK-Work\Pizza Detect\coco128\images\train2017"

# Label folder
label_folder = r"C:\Users\chinh\OneDrive\Desktop\MK-Work\Pizza Detect\coco128\labels\train2017"

# Output folder to save cropped images
output_folder = r"C:\Users\chinh\OneDrive\Desktop\MK-Work\Pizza Detect\coco128\crop_images"

# Loop through all label files in the label folder
for label_filename in os.listdir(label_folder):
    if label_filename.endswith(".txt"):
        label_path = os.path.join(label_folder, label_filename)

        # Get the corresponding image filename (replace ".txt" with ".jpg")
        image_filename = label_filename.replace(".txt", ".jpg")
        image_path = os.path.join(input_image_folder, image_filename)

        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"Image file {image_filename} does not exist.")
            continue

        # Read the bounding box coordinates from the label file
        with open(label_path, "r") as label_file:
            line = label_file.readline()
            parts = line.strip().split()
            if len(parts) == 5:  # Make sure there are exactly 5 values
                class_label, x_rel, y_rel, width_rel, height_rel = map(float, parts)
                
                # Calculate absolute pixel coordinates
                image = Image.open(image_path)
                image_width, image_height = image.size
                x_abs = int(x_rel * image_width)
                y_abs = int(y_rel * image_height)
                width_abs = int(width_rel * image_width)
                height_abs = int(height_rel * image_height)

                # Crop the image
                left = x_abs
                top = y_abs
                right = x_abs + width_abs
                bottom = y_abs + height_abs
                cropped_image = image.crop((left, top, right, bottom))

                # Create a path for the cropped image
                output_path = os.path.join(output_folder, image_filename)

                # Save the cropped image
                cropped_image.save(output_path)

                print(f"Successfully cropped image {image_filename}.")

# Completion message
print("Image cropping process completed.")
