class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
      
    def is_employee(object):
      if type(object) is Customer:
        return False
      else:
        return True
    
class Customer(Person):
    pass

class Employee(Person):
    DISCOUNT = 0.1


