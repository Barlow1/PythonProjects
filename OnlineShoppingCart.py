class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    def print_item_cost(self):
        self.total_cost = (self.item_price * self.item_quantity)
        print("{} {} @ ${} = ${}".format(self.item_name, int(self.item_quantity), int(self.item_price), int(self.total_cost)))
    def print_item_description(self):
        print("{}: {}.".format(self.item_name, self.item_description))
    
class ShoppingCart:
    def __init__(self, customer_name ="none", current_date = "January 1, 2016", cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    def add_item(self,ItemToPurchase):
        '''    add_name = input("Enter the item name:\n")
        add_description = input("Enter the item description:\n")
        add_price = float(input("Enter the item price:\n"))
        add_quantity = int(input("Enter the item quantity:\n"))
        add_item = ItemToPurchase(add_name, add_price, add_quantity, add_description)'''
        self.cart_items.append(add_item)
    def remove_item(self, remove_item):
            for i, o in enumerate(self.cart_items):
                if o.item_name == remove_item:
                    del self.cart_items[i]
                    break
                else:
                    print("Item not found in cart. Nothing removed.")
            
    def modify_item(self, ItemToPurchase):
        for i, o in enumerate(self.cart_items):
            if o.item_name == ItemToPurchase.item_name:
                o.item_quantity = ItemToPurchase.item_quantity
                break
            else:
                print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    def get_cost_of_cart(self):
        for item in self.cart_items:
            item.total_cost = (item.item_price * item.item_quantity)
            cart_total += item.total_cost
        return cart_total
    def print_total(self):
        cart_total = 0
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("OUTPUT SHOPPING CART")
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            num_of_items = len(self.cart_items)
            print("Number of Items: {}".format(num_of_items))
            print("")
            for item in self.cart_items:
                item.total_cost = (item.item_price * item.item_quantity)
                print("{} {} @ ${} = ${}".format(item.item_name, int(item.item_quantity), int(item.item_price), int(item.total_cost)))
                cart_total += item.total_cost
            print("")
            print("Total: ${}".format(int(cart_total)))
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("")
        print("Item Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name,item.item_description))
    def print_menu(self):
        print('''
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit''')
        
                  
                      
                  
                              
              
if __name__ == "__main__":
    input_name = input("Enter customer's name:\n")
    input_date = input("Enter today's date:\n")
    customer_cart = ShoppingCart(input_name, input_date)
    print("Customer Name:", input_name)
    print("Today's date:", input_date)
    while True:
        customer_cart.print_menu()
        user_option = input("Choose an option:\n")
        if user_option.lower() == 'q':
            break
        elif user_option.lower() == 'a':
            print("ADD ITEM TO CART")
            add_name = input("Enter the item name:\n")
            add_description = input("Enter the item description:\n")
            add_price = float(input("Enter the item price:\n"))
            add_quantity = int(input("Enter the item quantity:\n"))
            add_item = ItemToPurchase(add_name, add_price, add_quantity, add_description)
            customer_cart.add_item(add_item)
        elif user_option.lower() == 'r':
            print("REMOVE ITEM FROM CART")
            remove_item = input("Enter name of item to remove:\n")
            customer_cart.remove_item(remove_item)
        elif user_option.lower() == 'c':
            print("CHANGE ITEM QUANTITY")
            modify_name = input("Enter the item name:\n")
            modify_quantity = int(input("Enter the new quantity:\n"))
            modify_item = ItemToPurchase(item_name = modify_name, item_quantity = modify_quantity)
            customer_cart.modify_item(modify_item)
        elif user_option.lower() == 'i':
            customer_cart.print_descriptions()
        elif user_option.lower() == 'o':
            customer_cart.print_total()

