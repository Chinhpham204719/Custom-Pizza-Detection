import re

# Đọc nội dung từ tệp gốc
with open("pizzacam.json", "r") as file:
    content = file.read()

# Tìm các đối tượng JSON trong nội dung
pattern = r"}\s*{"
replaced_content = re.sub(pattern, "},\n{", content)

# Ghi nội dung đã được sửa vào tệp
with open("pizzacam_fixed.json", "w") as file:
    file.write(replaced_content)