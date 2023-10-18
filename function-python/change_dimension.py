from PIL import Image
import os

input_folder = r"C:\Users\chinh\OneDrive\Desktop\MK-Work\Pizza Detect\coco128\test_images"
output_folder = r"C:\Users\chinh\OneDrive\Desktop\MK-Work\Pizza Detect\coco128\test_images"

# Đảm bảo thư mục đầu ra tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lấy danh sách tệp ảnh trong thư mục đầu vào
image_files = [file for file in os.listdir(input_folder) if file.lower().endswith((".png", ".jpg", ".jpeg"))]

for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)

    # Mở ảnh bằng Pillow
    image = Image.open(input_path)

    # Thay đổi kích thước ảnh
    resized_image = image.resize((640, 640), Image.LANCZOS)

    # Lưu ảnh đã thay đổi kích thước
    resized_image.save(output_path)

print("Đã thay đổi kích thước ảnh xong.")
