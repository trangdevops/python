#module_python : https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# Tất cả các module trong Python đều có mục đích riêng và cung cấp các tính năng và chức năng khác nhau. Module random trong Python là một trong những module được sử dụng phổ biến để làm việc với các số ngẫu nhiên. Dưới đây là một số module con quan trọng trong module random và giải thích về chúng:

random.random()  #Hàm này trả về một số ngẫu nhiên từ khoảng [0.0, 1.0). Nó sử dụng một phương pháp ngẫu nhiên để tạo ra các số float trong khoảng đã chỉ định.

random.randint(a, b) # Hàm này trả về một số nguyên ngẫu nhiên trong khoảng từ a đến b, bao gồm cả a và b.

random.choice(seq) # Hàm này trả về một phần tử ngẫu nhiên từ một chuỗi hoặc danh sách seq.

random.shuffle(lst) # Hàm này xáo trộn ngẫu nhiên các phần tử trong một danh sách lst. Điều này thay đổi thứ tự của các phần tử trong danh sách ban đầu.

random.sample(population, k) # Hàm này trả về một danh sách con ngẫu nhiên với k phần tử từ một tập hợp population mà không có sự trùng lặp.

random.uniform(a, b) # Hàm này trả về một số ngẫu nhiên trong khoảng từ a đến b, bao gồm cả a và b. Khác với random.randint(), hàm này trả về một số float thay vì số nguyên.

random.seed(a=None, version=2) # Hàm này thiết lập giá trị khởi tạo cho generator số ngẫu nhiên. Nếu không có giá trị a được cung cấp, hàm sẽ sử dụng giá trị hệ thống hiện tại.

#Các module con khác trong module random cũng cung cấp các chức năng và phương thức hữu ích để làm việc với số ngẫu nhiên.