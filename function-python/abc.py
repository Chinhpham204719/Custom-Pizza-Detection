import json
import os
import requests

# Đường dẫn đến tệp JSON chứa dữ liệu
json_file_path = "C:/Users/chinh/OneDrive/Desktop/MK-Work/Pizza Detect/function-python/pizzacam_fixed.json"

# Thư mục đầu ra để lưu trữ ảnh
output_dir = "C:/Users/chinh/OneDrive/Desktop/MK-Work/Pizza Detect/coco128/test_images"

# Đảm bảo thư mục đầu ra tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Đọc dữ liệu từ tệp JSON
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

 
# Lặp qua các mục từ vị trí 1 đến 300 và tải ảnh
for i in range(201, 10000):
    item = data[i - 1]  # Do chỉ mục trong Python bắt đầu từ 0
    image_url = item['image_url']
    image_id = item['_id']['$oid']
    
    # Tạo đường dẫn cho ảnh đầu ra
    output_path = os.path.join(output_dir, f'{image_id}.jpg')
    
    # Tải ảnh từ URL và lưu vào thư mục đầu ra
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as image_file:
            image_file.write(response.content)
        print(f"Tải xuống ảnh {image_id} thành công.")
    else:
        print(f"Tải xuống ảnh {image_id} thất bại.")

print("Hoàn thành tải xuống ảnh.")
