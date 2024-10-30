class BMW():
    def fuel_type(self):
        print("BMW is electric and petrol")
        
    def max_speed(self):
        print("BMW can go upto 300km/h")
        

class Ferrari():
    def fuel_type(self):
        print("Ferrari is only petrol")
        
    def max_speed(self):
        print("Ferrari can go upto 800km/h")
        

obj_BMW = BMW()
obj_Ferrari = Ferrari()

for Vehicle in (obj_BMW, obj_Ferrari):
    Vehicle.fuel_type()
    Vehicle.max_speed()
                            
    