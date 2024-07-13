import csv
class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def to_dict(self):
        return{
            "Product_id": self.product_id,
            "Name": self.name,
            "Price": self.price,
            "Quantity":self.quantity
        }
    def __str__(self):
        return f"Product_id: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
class Inventory:
    def __init__(self,filepath = "inventory.csv"):
        self.filepath = filepath
        self.inventory = []
        self.read_file()
    def read_file(self):
        with open (self.filepath,'r',newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(row['Product_id'],row['Name'],float(row['Price']),int(row['Quantity']))
                self.inventory.append(product)
    def write_file(self):
        with open (self.filepath,'w',newline='') as csvfile:
            fieldnames = ['Product_id',"Name","Price","Quantity"]
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            for item in self.inventory:
                writer.writerow(item.to_dict())
    def find_product(self,product_id):
        for product in self.inventory:
            if product.product_id == product_id:
                return True
        return False
    def add(self,product_id,name,price,quantity):
        if not self.find_product(product_id):
            product = Product(product_id,name,price,quantity)
            self.inventory.append(product)
            self.write_file()
        else:
            print(f"Product Id :{product_id} already exists")
    def update(self,index,product_id,name,price,quantity):
        if 0 <= index < len(self.inventory):
            self.inventory[index + 1] = Product(product_id,name,price,quantity)
            self.write_file()
        else:
            print("Invalid Index")
    def remove(self,index):
        if 0 <= index < len(self.inventory):
            del self.inventory[index+1]
            self.write_file()
        else:
            print("Invalid Index")


    def view(self):
        for index,item in enumerate(self.inventory):
            print(f"{index+1}-{item}")


item1 = Inventory()
#item1.add(101,"Laptop",700,10)
#item1.add(102,"keyboard",100,18)
#item1.add(103,"printer",300,20)
#item1.add(101,"Laptop",700,10)
item1.remove(2)
item1.view()