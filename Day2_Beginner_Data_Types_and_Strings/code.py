#Nếu hóa đơn là $150,00, chia cho 5 người, với 12% tiền boa.
#Mỗi người phải trả (150,00/5) * 1,12 = 33,6
#Định dạng kết quả thành 2 chữ số thập phân = 33,60
#Do đó, phần chia của mọi người trong tổng hóa đơn là 30 USD cộng với tiền boa 3,60 USD.

total_bill = float(input("Nhập số tiền hóa đơn: "))
total_member = int(input("Nhập số người: "))
tip_money = float(input("Số tiền khách tip: "))

member_money = round(((total_bill + tip_money) / total_member), 2)

print(f"Số tiền mỗi khách cần thanh toán là: ${member_money}")