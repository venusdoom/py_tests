# counting test
print("This application is used for simple counting.")
print("User should enter start number, end number and interval for counting.")

# initialising variables for counting
start = int(input("\nEnter start number: "))
end = int(input("Enter end number: "))
interval = int(input("Enter interval number: "))

# counting
print("\nCounting:")
for i in range(start, end, interval):
    print(i)

input("\nPress Enter to exit.")
