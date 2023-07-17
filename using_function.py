def greet(name: str)-> None:
   
    print(f'welcome {name}')
    
if __name__=='__main__':
    counter =1
    while True:
        name=input('Enter A Name: ')
        greet(name)
        if counter == 5:
            break
        counter+= 1

