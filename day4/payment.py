class Payment:
    def pay(self, amt):
        print(f"Paid Rs.{amt}")

class CashPay(Payment):
    def pay(self, amt):
        print(f"Paid Rs.{amt} in cash")

class CardPay(Payment):
    def pay(self, amt):
        print(f"Paid Rs.{amt} using card")

class UPIPay(Payment):
    def pay(self, amt):
        print(f"Paid Rs.{amt} using UPI")

l = [CashPay(), CardPay(), UPIPay()]
amt = int(input("Enter amount: "))
for i in l:
    i.pay(amt)

#With encapsulation
# class Payment:
#     def __init__(self, amt):
#         self._amt = amt  # protected variable

#     def pay(self):
#         print(f"Paid Rs.{self._amt}")

# class CashPay(Payment):
#     def pay(self):
#         print(f"Paid Rs.{self._amt} in cash")

# class CardPay(Payment):
#     def pay(self):
#         print(f"Paid Rs.{self._amt} using card")

# class UPIPay(Payment):
#     def pay(self):
#         print(f"Paid Rs.{self._amt} using UPI")

# payments = [CashPay(1000), CardPay(1000), UPIPay(1000)]
# for p in payments:
#     p.pay()