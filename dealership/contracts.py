from dealership.vehicles import Car, Truck, Motorcycle
from dealership.customers import Customer, Employee

class Contract(object):
  pass

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        interest_rate = 1
        
        if type(self.vehicle) is Car:
            interest_rate = 1.07
        elif type(self.vehicle) is Motorcycle:
            interest_rate = 1.03
        elif type(self.vehicle) is Truck:
            interest_rate = 1.11
        else:
            interest_rate = 1
        
        total_value = self.vehicle.sale_price() + (interest_rate * self.monthly_payments * self.vehicle.sale_price()/100) 
        total_value = total_value - (total_value * 0.1 if self.customer.is_employee() else 0)
        
        return total_value
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
    
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        least_rate = 1
        
        if type(self.vehicle) is Car:
            least_rate = 1.2
        elif type(self.vehicle) is Motorcycle:
            least_rate = 1
        elif type(self.vehicle) is Truck:
            least_rate = 1.7
        else:
            least_rate = 1
        
        total_value = self.vehicle.sale_price() + ( self.vehicle.sale_price() * least_rate / self.length_in_months )
        total_value = total_value - (total_value * 0.1 if self.customer.is_employee() else 0)
        
        return total_value
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        
        
