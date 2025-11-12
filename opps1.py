# initiate a class
class employee:
    #special method/magic method - constructor
    def __init__(self):
        print("Employee has joined the company on 1998 ")
        self.id =123
        self.salary = 12000 
        self.designation = "Majdoor"
        print("attributes are created")
    
    def travel(self, destination):
        print(f" Employee is travelling to {destination} ")

# create an object/instance of the class
sam = employee()

# print(sam.id)
# print(sam.salary)
# sam.travel("Delhi")
print(type(sam))