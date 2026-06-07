# =========================
# Question 1 - Bank Account
# =========================

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.account_number}: Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) - Balance: {self.balance}")


accounts_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

accounts = {}

for name, acc_no, balance in accounts_data:
    accounts[acc_no] = BankAccount(name, acc_no, balance)

accounts["A002"].deposit(3000)
accounts["A003"].withdraw(15000)
accounts["A001"].withdraw(2000)


print("\n--- Bank Accounts ---")
for acc in accounts.values():
    acc.get_balance()


# =========================
# Question 2 - Students
# =========================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()
        result = "Pass" if avg >= 40 else "Fail"
        print(f"{self.name} | Avg: {avg:.2f} | Grade: {self.grade()} | {result}")


students_data = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

students = [Student(name, marks) for name, marks in students_data]

print("\n--- Student Results ---")
for s in students:
    s.display()


# =========================
# Question 3 - Delivery App
# =========================

class DeliveryPartner:
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        return 0

    def display(self):
        print(f"{self.name} ({self.partner_id}) - Deliveries: {self.deliveries} - Earning: {self.total_earning()}")


class BikeRider(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    def total_earning(self):
        return (80 * self.deliveries) + (5 * self.km_travelled)


class Walker(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):
        return (60 * self.deliveries) + (50 * self.rainy_deliveries)


class CarDriver(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    def total_earning(self):
        return (120 * self.deliveries) - self.fuel_cost


partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850),
]

print("\n--- Delivery Earnings ---")
for p in partners:
    p.display()

top = max(partners, key=lambda x: x.total_earning())
print("\nTop Earner:", top.name, top.total_earning())


# =========================
# Question 4 - Bus System
# =========================

class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}

    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print(f"Seat {seat_number} already booked")
        elif seat_number < 1 or seat_number > self.total_seats:
            print("Invalid seat number")
        else:
            self.booked[seat_number] = passenger_name

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print("\nPassenger List:")
        for seat in sorted(self.booked):
            print(f"Seat {seat}: {self.booked[seat]}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),
]

for seat, name in bookings:
    bus.book_seat(seat, name)

print("\n--- Bus System ---")
print("Available seats:", bus.available_seats())
bus.passenger_list()