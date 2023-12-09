class employee:
    'this is employee class'
    name = "empty name"
    address ="empty address"

class doctor:
    pass

class computer:
    class hard:
        pass
    


emp = employee()

print(employee.__name__)
print(doctor.__name__)
print(computer.__name__)
print(computer.hard.__name__)
