class library:
    def __init__(self,title,stock):
        self.title = title
        self.stock = stock
    def borrow(self,s):
        if self.stock >0:
            self.stock-=s
            return f"{self.stock}stocks remining..."
        else:
            print("haven't stock left.")

    def return_book(self,n):
        self.stock+=n
        
        return f"you're stock added successfully.. now {self.stock} are remining.. "
    def check_stock(self):
        print(self.stock)

book1 = library("goat life",5)
print(book1.borrow(1))
print(book1.return_book(5))
book1.check_stock()
