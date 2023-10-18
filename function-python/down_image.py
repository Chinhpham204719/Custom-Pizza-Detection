import requests
import os
import json
import re

# Đường dẫn đến tệp JSON chứa dữ liệu
json_file_path = "C:/Users/chinh/OneDrive/Desktop/MK-Work/Pizza Detect/function-python/pizzacam_fixed.json"

# Thư mục đầu ra để lưu trữ ảnh
output_dir = "C:/Users/chinh/OneDrive/Desktop/MK-Work/Pizza Detect/coco128/list_id_labels/Edge - Too small"

# Đọc dữ liệu từ tệp JSON
with open(json_file_path, "r") as file:
    data = json.load(file)

# Tạo thư mục để lưu trữ ảnh nếu nó không tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Vị trí bắt đầu và kết thúc
start_index = 750  # Vị trí bắt đầu
end_index = 80000  # Vị trí kết thúc

# Biểu thức chính quy cho chuỗi "Edge - Uneven" (không phân biệt chữ hoa chữ thường)
shape_pattern = re.compile(r"Edge - Too small", re.IGNORECASE)

# Lặp qua dữ liệu và tải ảnh từ vị trí start_index đến end_index
for index, item in enumerate(data[start_index:end_index + 1], start=start_index):
    error_list = item.get("error_list", {})
    
    # Kiểm tra xem có chuỗi "Edge - Uneven" trong error_list (không phân biệt chữ hoa chữ thường)
    if any(shape_pattern.search(error.lower()) for error in error_list.get("Shape", [])):
        image_url = item.get("image_url")
        
        # Kiểm tra xem có URL hình ảnh hay không
        if image_url:
            image_name = image_url.split("/")[-1]
            response = requests.get(image_url)
            
            # Kiểm tra xem tải ảnh thành công hay không
            if response.status_code == 200:
                with open(os.path.join(output_dir, image_name), "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {image_name}")
            else:
                print(f"Failed to download {image_name}")
        else:
            print(f"No image URL found for item at index {index}")

print("All images downloaded.")
