#Fiverr Keyword Beast Generator
import time
print("This program is create by Lawal Ridwan.")

time.sleep(2)   # Delays for 2 seconds.

user_name = input("What is your name:")

print("Hello ", user_name  + " Welcome To Fiverr Keyword Generation.")

time.sleep(2)   # Delays for 2 seconds.
print(""".
  .
  .
  .""")

print(user_name + " You Will Need passcode for access")
pwd = input("Input passcode: ")

print(""".
  .
  .
  .""")

if pwd == "1234":
  print(user_name, "Welcome")
  print(""".
  .
  .
  .""")
  time.sleep(2)   # Delays for 2 seconds.
  print("Please input your niche in next prompt")
  print(""".
  .
  .
  .""")
  time.sleep(2)   # Delays for 2 seconds.
  my_list = ["1. Ebook","2. Website design","3. Graphics Design", "4. Youtube", "5. Facebook"] 
  print('\n'.join(my_list))


  
else:
  print("Go and get the passcode now")
  exit()





