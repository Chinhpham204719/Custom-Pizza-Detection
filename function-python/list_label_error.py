import json

# Đường dẫn đến tệp JSON
json_file_path = "C:/Users/chinh/OneDrive/Desktop/MK-Work/Pizza Detect/function-python/pizzacam_fixed.json"

# Đường dẫn đến tệp TXT để lưu danh sách lỗi topping
txt_file_path = "C:/Users/chinh/OneDrive/Desktop/MK-Work/Pizza Detect/coco128/error_labels/size_error_labels.txt"

# Tạo danh sách lỗi topping
topping_errors = set()

with open(json_file_path, "r") as json_file:
    data = json.load(json_file)
    for item in data:
        error_list = item.get("error_list", {})
        topping_errors.update(error_list.get("Size", []))

# Ghi danh sách lỗi topping vào tệp TXT sử dụng UTF-8
with open(txt_file_path, "w", encoding="utf-8") as txt_file:
    txt_file.write("Size errors:\n")
    for error in topping_errors:
        txt_file.write(f"- {error}\n")

print("Danh sách lỗi  đã được lưu.")
