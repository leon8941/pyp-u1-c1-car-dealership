from dealership.vehicles import Car, Truck, Motorcycle
from dealership.customers import Customer, Employee

class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super().__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def total_value(self):
        total_value = self.vehicle.sale_price() + (self.vehicle.INTEREST_RATE * self.monthly_payments * self.vehicle.sale_price()/100) 
        total_value = total_value - (total_value * self.customer.DISCOUNT if self.customer.is_employee() else 0)
        
        return total_value
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
    
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super().__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def total_value(self):  
        total_value = self.vehicle.sale_price() + ( self.vehicle.sale_price() * self.vehicle.LEASE_RATE / self.length_in_months )
        total_value = total_value - (total_value * self.customer.DISCOUNT if self.customer.is_employee() else 0)
        
        return total_value
        
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        
        
