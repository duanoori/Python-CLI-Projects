from random import *
import os
u_pwd = input("Enter Password: ")
m_pwd = ['0','1','2','3','4','5','6','7','8','9']
pwd = ""
while(pwd != u_pwd):
    pwd = ""
    for letter in range(len(u_pwd)):
        guess_pwd = m_pwd[randint(0,9)]
        pwd = str(guess_pwd) + str(pwd)
        print(pwd)
        print("Cracking Password...Please wait")
        os.system("cls")
print("Your Password is : ", pwd)
# Lets Crack...
