# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print (add(2,3))
# print(add(2,3,5))
# print(add(2,3,5,7))
# print(add(2,3,5,7,9))

# def display_name(*args):
#     for arg in args:
#         print(arg, end= " ")

# display_name("Ezeh" , " Mmachi" , " lawricia", "III")


def print_address(**kwargs):
    for key, value  in kwargs.keys.items(): 
     print(value)

        
print_address(street="123 no str",  city=" lagos", state = "la", zip ="7789")
