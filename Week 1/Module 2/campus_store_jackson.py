# Campus Store Checkout System
# Part A - Welcome and Input

print("=" * 40)
print("WELCOME TO THE CAMPUS STORE")
print("=" * 40)

# Show available items
print("Available items:")
print("1. Notebook")
print("2. Pen")
print("3. Pencil")
print("4. Eraser")
print()

# Collect inputs
customer = input("Customer name: ")
item = input("Chosen item: ")
price = float(input("Unit price: "))          # convert to decimal
quantity = int(input("Quantity: "))            # convert to whole number
paid = float(input("Amount paid: "))           # convert to decimal
student = input("Are you a student? (yes/no): ")



# Part B - Calculate the bill

subtotal = price * quantity
discount = subtotal * 0.10
discounted_amount = subtotal - discount
service = discounted_amount * 0.05
final_total = discounted_amount + service
difference = paid - final_total



#Part C - Operator Skills

points = 0
points += quantity

available_items = ["Notebook", "Pen", "Pencil", "Eraser"]
valid_item = item in available_items

payment_sufficient = paid >= final_total

student_eligible = (subtotal >= 1000) and (student == "yes")



#Part D - Display receipt 

print()
print("=" * 40)
print("        CAMPUS STORE RECEIPT")
print("=" * 40)
print("Customer:", customer)
print("Item:", item)
print("Unit price:{:.2f}".format(price))
print("Quantity:", quantity)
print("-" * 40)
print("Subtotal:{:.2f}".format(subtotal))
print("Discount (10%):{:.2f}".format(discount))
print("After discount:{:.2f}".format(discounted_amount))
print("Service charge (5%):{:.2f}".format(service))
print("Final total:{:.2f}".format(final_total))
print("-" * 40)
print("Amount paid:{:.2f}".format(paid))
print("Payment difference:{:.2f}".format(difference))
print("-" * 40)
print("Payment sufficient:", payment_sufficient)
print("Item available:", valid_item)
print("Student eligibility:", student_eligible)
print("Points earned:", points)
print("=" * 40)
print("Final total:", round(final_total, 2))