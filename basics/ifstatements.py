has_good_credit  = False
amount = 1000000
ten_percent = 0.1
twenty_percent  = 0.2

if has_good_credit:
    down_payment = amount*ten_percent
else:
    down_payment = amount*twenty_percent
print(f"Down payment: ${down_payment}")
