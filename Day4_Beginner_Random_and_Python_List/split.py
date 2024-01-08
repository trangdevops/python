#Hàm split() trong Python được sử dụng để tách một chuỗi thành một danh sách các phần tử riêng lẻ, dựa trên một ký tự phân tách. Khi áp dụng hàm split() cho một chuỗi, nó sẽ tạo ra một danh sách mới chứa các phần tử được tách ra từ chuỗi gốc.

import random

# Tách chuỗi names_string thành các tên riêng lẻ và đặt chúng vào danh sách tên
names_string = input("Nhập các tên danh sách người sẽ thanh toán bữa này: ")
names = names_string.split(", ")

# Sinh một chỉ số ngẫu nhiên trong khoảng của danh sách names
random_index = random.randint(0, len(names) - 1)

# Chọn tên ngẫu nhiên bằng cách sử dụng chỉ số đã sinh
selected_name = names[random_index]

print(f"Người sẽ thanh toán là: {selected_name}")