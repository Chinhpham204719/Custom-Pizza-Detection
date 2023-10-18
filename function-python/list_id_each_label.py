import json

# Đường dẫn đến tệp JSON chứa dữ liệu
json_file_path = 'C:\\Users\\chinh\\OneDrive\\Desktop\\MK-Work\\Pizza Detect\\function-python\\pizzacam_fixed.json'

# Đọc tệp JSON
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Danh sách để lưu trữ vị trí của các phần tử có lỗi "Topping - Topping too centered"
error_positions = []

# Duyệt qua các phần tử từ phần tử thứ 750 đến phần tử thứ 4199
for i, item in enumerate(data[749:4200], start=750):
    error_list = item.get('error_list', {})
    topping_errors = error_list.get('Topping - Topping too centered', [])
    
    # Kiểm tra nếu có lỗi "Topping - Topping too centered" và thêm vị trí vào danh sách
    if topping_errors:
        error_positions.append(i)

# In ra danh sách vị trí của các phần tử có lỗi
print(f'Các vị trí của các phần tử có lỗi "Topping - Topping too centered": {error_positions}')
