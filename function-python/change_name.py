import os

input_folder = r"C:\Users\chinh\OneDrive\Desktop\DATN\Facial Recognition App\data\positive"
output_folder = r"C:\Users\chinh\OneDrive\Desktop\DATN\Facial Recognition App\data\positive"

# Lấy danh sách tệp ảnh trong thư mục đầu vào
image_files = [file for file in os.listdir(input_folder) if file.lower().endswith((".png", ".jpg", ".jpeg"))]

# Đảm bảo thư mục đầu ra tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Đặt biến để đếm số thứ tự
counter = 1

for image_file in image_files:
    old_path = os.path.join(input_folder, image_file)
    file_extension = image_file.split('.')[-1]
    new_filename = f"{counter}.{file_extension}"
    new_path = os.path.join(output_folder, new_filename)  # Sửa đường dẫn thành thư mục đầu ra

    # Thay đổi tên tệp
    os.rename(old_path, new_path)

    counter += 1

print("Đã đổi tên tệp ảnh thành số thứ tự.")
