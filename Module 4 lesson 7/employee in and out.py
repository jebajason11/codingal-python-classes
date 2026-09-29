class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")
def Create_obj():
    print("Making Objects...")
    obj = Employee()
    print("function end...")
    return obj
print ("Calling Create_odj() function...")
obj = Create_obj()
print("Program End...")
        
    