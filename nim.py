import random


players=["p1","p2"]
print('''Rules of the game. you are only allowed to take 1-3 stones. anything greater than 3, is impossible''')
print('Good luck players')
turns= True
player = turns
player_1 =str(input(f"player1 Enter Name: "))
player_2 = str(input(f"player2 Enter Name: "))
while True:
   stone = random.randint(10, 20)
   print(f"The stones are",stone)
   
   remove=int(input("player_1 Enter how many stones you want to remove:  "))

   if remove <= 3:
      remove < stone
      stone = stone - remove
      
      stone_remaining = stone
      
   print(f'''you removed {remove} stones, you have,{stone_remaining}''')
   
   remove=(int(input("player_2 Enter how many stone you want to remove: ")))
  
   if remove  > 3:
      print('Not possible')

   if stone == 0:
         print("player" , player, "wins")
         play_again=input('''Do you want to play again? y/n: ''')
         if play_again.lower()!= 'y':
            print('play on')
        
         else:
      
          print('Thnak you for playing')

         print(f'''you removed {remove}, stones you have,{stone_remaining}''')

         if player ==1:
          player =2
         
  

 

    