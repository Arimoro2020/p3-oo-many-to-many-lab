from datetime import datetime, date


class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
        
   
    def books(self):
        return [contract.book for contract in self.contracts()]
    

    def sign_contract(self, book, date, royalties):
        return Contract(self, book,date, royalties)
    
    def total_royalties(self):
        total_amount = [contract.royalties for contract in self.contracts()]
        sum= 0
        for royalty in total_amount:
            sum += royalty
        return sum
       

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        try:
            if type(value) == str and len(value) > 0:
                self._name = value
        except TypeError:
            raise ValueError("invalid value")
        



class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        try:
            if type(value) == str and len(value) > 0:
                self._title = value
        except TypeError:
            raise ValueError("invalid value")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    def __init__(self, author,book,date=datetime.now().date().strftime("%m/%d/%Y"), royalties=None):
        self.book = book
        self.author = author
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted([contract for contract in cls.all], key=lambda x: x.date)
   
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Exception")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise ValueError("Exception")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,value):
        if type(value) == str:
            self._date = value
        else:
            raise ValueError("Exception")

    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if type(value) == int:
            self._royalties = value
    
        else:
            raise ValueError("invalid value")
