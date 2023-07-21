import maskpass
if __name__=="__main__":
  user_name = input('username: ')
  pwd= maskpass.advpass(mask="*")

  print(user_name)
  print(pwd)