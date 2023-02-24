# ===== Importing libraries ===========
import os.path
from tabulate import tabulate

# ============= Variables ============

# Set the global variables
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


# ======== Define the class ==========
class Shoe:

    # Constructor that initialises the attributes and assigns them values
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method gets the cost of the item
    def get_cost(self):
        return self.cost

    # Method gets the quantity of the item
    def get_quantity(self):
        return self.quantity

    # Method gets the code of the item
    def get_code(self):
        return self.code

    # Method sets a new quantity of the item
    def set_quantity(self, quantity_new):
        self.quantity = quantity_new

    # Method returns the string representation of the full information about the particular item
    def __str__(self):
        output = (f"{self.country},"
                  f"{self.code},"
                  f"{self.product},"
                  f"{self.cost},"
                  f"{self.quantity}")
        return output


# ============= Shoe list ===========

# The list to store a list of objects of shoes
shoe_list = []


# ========== Functions outside the class ==============

# Create the function opens the file 'inventory.txt' and read the data from this file,
# then create a shoes object with this data and append this object into the shoes list
def read_shoes_data():
    # Set local variable
    path = "inventory.txt"

    # Set 'True' value that file 'inventory.txt' exists
    check_file = os.path.isfile(path)

    # Check if the file 'inventory.txt' is not exist
    if not check_file:
        print("The file is not exist.")
    else:
        # Open the file for reading
        shoes_file = open("inventory.txt", "r")
        contents = shoes_file.read()
        shoes_file.close()

        # Convert a string file into the list
        list_contents = contents.split("\n")

        # Clearing the list of objects
        shoe_list.clear()

        # The loops to create the list with the shoes data
        for n in range(1, len(list_contents)):
            list_content = list_contents[n]
            shoe_info = list_content.split(",")

            # Catch for the IndexError
            try:
                # Create the shoes object with the data
                shoe_data = Shoe(shoe_info[0], shoe_info[1], shoe_info[2], shoe_info[3], int(shoe_info[4]))
            except IndexError:
                print(RED + BOLD + "Data in the file is not complete. Please check the data." + END)
                continue

            # Append the object into the shoes list
            shoe_list.append(shoe_data)


# Create the function allows a user to capture data about a shoe
# and use this data to create a shoe object and append this object inside the shoe list
def capture_shoes():
    # Request the user to enter the information about the shoe
    country_input = input("Please enter the country: ")
    code_input = input("Please enter the code: ")
    product_name = input("Please enter the product name: ")
    cost_input = input("Please enter the cost per item: ")
    quantity_input = int(input("Please enter the quantity: "))

    # Create a shoe object
    new_shoe = Shoe(country_input, code_input, product_name, cost_input, quantity_input)

    # Append the object inside the shoe list
    shoe_list.append(new_shoe)


# Create the function which iterates over the shoe list and prints the details of the shoes in a table format
def view_all():
    # Set the local variables
    table = []
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]

    # The loop to create a new list where each element is a list with full information about every shoe
    for n in range(0, len(shoe_list)):
        table.append(str(shoe_list[n]).split(','))

    # Print out the data in a table format
    print(tabulate(table, headers=headers))


# Create the function that finds the shoe object with the lowest quantity, which is the shoes that need to be re-stocked
def re_stock():
    # Set the local variables
    dict_quantity = {}
    shoes_to_restock = []

    # The loop to create a dictionary with the values are equal to quantities of shoes
    for v in range(0, len(shoe_list)):
        dict_quantity[shoe_list[v]] = shoe_list[v].get_quantity()

    # Find the minimum value in the dictionary values (minimum quantity)
    min_value = min(dict_quantity.values())

    # The loop to iterate through the list with the items
    for n in range(0, len(shoe_list)):

        # Check to find the item with the lowest quantity
        if shoe_list[n].get_quantity() == min_value:

            # Add the item to the list for the shoes to re-stock
            shoes_to_restock.append(shoe_list[n])

            # Print out the details of the shoes with the lowest quantity
            print(f"The shoe with the lowest quantity is: {shoe_list[n]}")

    # Request the user to answer if he/she wants to add the quantity of shoes and update the data
    update_value = input("Please choose if you want to add the quantity of shoes and update the data (Yes/No): ").lower()

    # Check if the user answered 'yes' to previous question
    if update_value == "yes":

        # The loop to print out all shoes for re-stoke and update their quantities
        for shoe in shoes_to_restock:
            try:
                shoe.set_quantity(int(input(f"New quantity for ({shoe}): ")))
                print(GREEN + f"The quantity of shoe was successfully updated: {shoe}" + END)

                # The loop to update the quantity for the shoe in the 'inventory.txt'
                with open("inventory.txt", "w") as file1:
                    for i in range(0, len(shoe_list)):
                        file1.write(f"\n{shoe_list[i]}")
            except ValueError:
                print(RED + BOLD + "Invalid value" + END)

    else:
        print(RED + BOLD + "\nThe quantity of shoe wasn't updated." + END)


# Create the function that searches for a shoe from the list using the shoe code and print out this item details
def search_shoe():
    # Set local variable
    found = False

    # Request the user to enter the code for searching in the shoes list
    code_input = str(input("Please enter the code to search the shoe: "))

    # The loop to iterate through the shoe list
    for value in shoe_list:

        # Check if the code of any item in the list is equal to entered code by the user
        if value.get_code() == code_input:

            # Change the value of the variable for 'True' if the code was found in the shoe list
            found = True

            # Print out the item details
            print(GREEN + "\nThe item is found. Please see details below:" + END)
            print(f"\n{value}")

    if not found:
        print(RED + BOLD + "\nThe code is not found. Please try again." + END)


# Create the function that calculates the total value for each item
def value_per_item():
    # Set the local variables
    temp = []
    code_list = []
    value_list = []

    # The loop to create the list inside with another list of all information about each shoe
    for i in range(0, len(shoe_list)):
        temp.append((str(shoe_list[i]).split(",")))

    # The loop to calculate the total value for each shoe
    for y in range(0, len(temp)):
        value = int(temp[y][3]) * int(temp[y][4])

        # Add value of each item to the list
        value_list.append(value)

        # Add code of each item to the list
        code_list.append(temp[y][1].strip(" "))

    # Create a dictionary from two lists (codes and values)
    dict_value = dict(zip(code_list, value_list))

    # Print out the dictionary keys and values (codes and values)
    print(GREEN + "\nShoe Code  Value" + END)
    print("——————————————————")
    for key, value in dict_value.items():
        print(f"{key}   {value}")


# Create the function that determines the product with the highest quantity and print this shoe as being for sale
def highest_qty():
    # Set the local variables
    dict_quantity = {}

    # The loop to iterate through the list with the items and create a dictionary
    for m in range(0, len(shoe_list)):
        dict_quantity[shoe_list[m]] = shoe_list[m].get_quantity()

    # Find the maximum value among the values in the dictionary
    max_value = max(dict_quantity.values())

    # The loop to iterate through the shoe list
    for k in range(0, len(shoe_list)):

        # Check if the quantity of the element of the list is equal to max value, then print out this item details
        if shoe_list[k].get_quantity() == max_value:
            print(f"The shoe with the highest quantity and for SALE is: {shoe_list[k]}")


# ========== Main Menu =============

# The loop for the menu list
while True:
    print(BOLD + BLUE + "\n««««««   Welcome to the menu   »»»»»»" + END)

    # Request the user to choose the option from the menu
    menu = input('''\nSelect one of the following options below:
r - Read shoes data
a - Adding a new shoe 
va - View all shoes
vr - View shoes for re-stock 
vs - View shoes for sale
ss - Search Shoe
dv - Display total value for each item
dc - Display cost for each item
e - Exit
: ''').lower()

    # Check for the particular menu option
    if menu == "r":
        print("——————————————————————————————————————————————————")

        # Call the function read shoes data
        read_shoes_data()

    # Check for the particular menu option
    elif menu == "a":
        print("——————————————————————————————————————————————————")

        # Call the function to add a new shoe
        capture_shoes()

        # Append data for a new shoe to the 'inventory.txt'
        with open("inventory.txt", "a") as file:
            file.write(f"\n{str(shoe_list[len(shoe_list)-1])}")

        print("——————————————————————————————————————————————————")

    # Check for the particular menu option
    elif menu == "va":
        print("————————————————————————————————————————————————————————————")

        # Call the function to read the data
        read_shoes_data()

        # Call the function to view the shoes data
        view_all()

        print("————————————————————————————————————————————————————————————")

    # Check for the particular menu option
    elif menu == "vr":
        print("————————————————————————————————————————————————————————————")

        # Call the function to read the data
        read_shoes_data()

        # Call the function to display the item for re-stock and update the inventory data if required
        re_stock()

        print("————————————————————————————————————————————————————————————")

    # Check for the particular menu option
    elif menu == "vs":
        print("————————————————————————————————————————————————————————————")

        # Call the function to read the data
        read_shoes_data()

        # Call the function to display the item with the highest quantity and for sale
        highest_qty()

        print("————————————————————————————————————————————————————————————")

    # Check for the particular menu option
    elif menu == "ss":
        print("————————————————————————————————————————————————————————————")

        # Call the function to read the data
        read_shoes_data()

        # Call the function to search the item in the inventory data
        search_shoe()

        print("————————————————————————————————————————————————————————————")

    # Check for the particular menu option
    elif menu == "dv":
        print("————————————————————————————————————————————————————————————")

        # Call the function to read the data
        read_shoes_data()

        # Call the function to display a value per each item
        value_per_item()

        print("————————————————————————————————————————————————————————————")

    # Check for the particular menu option
    elif menu == "dc":
        print("———————————————————————————")

        # Call the function to read the data
        read_shoes_data()

        # Print out the header of the table
        print(GREEN + "\nShoe Code  Cost" + END)
        print("———————————————————————————")

        # The loop to print out the code and cost of each item in the shoe list
        for j in range(0, len(shoe_list)):
            print(f"{shoe_list[j].get_code()}   {shoe_list[j].get_cost()}")

        print("—————————————————————————————")

    # Check for the particular menu option
    elif menu == "e":
        print(BLUE + BOLD + "\n««««««   Goodbye!   »»»»»»" + END)
        exit()

    else:
        print(RED + BOLD + "\nYou have entered invalid value. Please try again." + END)
