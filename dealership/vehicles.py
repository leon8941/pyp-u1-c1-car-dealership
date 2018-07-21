class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
          
    def sale_price(object):
        multiplier = 1.0
        
        if type(object) is Car:
          multiplier = 1.2
        elif type(object) is Truck:
          multiplier = 1.6
        else:
          multiplier = 1.1
        
        return object.base_price * multiplier
      
    def purchase_price(object):
        multiplier = 1.0
        
        if type(object) is Car:
          multiplier = 0.004
        elif type(object) is Truck:
          multiplier = 0.02
        else:
          multiplier = 0.009
        
        return object.sale_price() - (multiplier * object.miles)

class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class Truck(Vehicle):
    pass
