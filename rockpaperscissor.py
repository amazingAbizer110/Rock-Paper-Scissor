from time import sleep
from getpass import getpass
from random import choice,randint
print("__"*75)
print("\n\n")
print("Welcome to rock paper scissor".center(130))
print("\n\n")
print("__"*75)
name1=input("Enter Player 1 :  ".rjust(75)).upper()
name2=input("Enter Player 2 :  ".rjust(75)).upper()
p1=getpass(f"{name1} Enter Choice  Rock or Paper or Scissor : ".center(130)).strip().lower()
p2=getpass(f"{name2} Enter Choice  Rock or Paper or Scissor : ".center(130)).strip().lower()
n1,n2=0,0
while(p1!="exit"):
	choices=['rock','paper','scissor']
	if p1 not in choices or p2 not in choices:
		print('\n\n')
		print("Error !! Mind your input only (Rock,Paper,Scissor) is allowed".center(130))
		print('\n\n')
		break
	print(f"{name1} Choice : {p1.upper()}".center(130))
	print(f"{name2} Choice : {p2.upper()}".center(130))
	print("Processing...",end='')
	for i in range(randint(1,4)):
		print('.',end='',flush=True)
		sleep(1)
	print()
	p1_win=[('rock','scissor'),('paper','rock'),('scissor','paper')]
	if(p1==p2):
		print('Match Tie !!!'.center(130))
	elif((p1,p2)in p1_win):
		print(f'{name1} Won'.center(130))
		n1+=1
	else:
		print(f'{name2} Won'.center(130))
		n2+=1
	print("Did you want to exit ".center(130))
	e=input(" ".center(63)).lower()
	if(e in ('y','yes','true','yo')):break
	p1=getpass(f"{name1}  Enter Choice  Rock or Paper or Scissor".center(130)).strip().lower()
	p2=getpass(f"{name2}  Enter Choice  Rock or Paper or Scissor".center(130)).strip().lower()
print(f"{name1} score :- {n1}".center(130))
print(f"{name2} score :- {n2}".center(130))
if(n1>n2):
	print(f"{name1} Won".center(130))
elif(n2>n1):
	print(f"{name2} Won".center(130))
else:
	print("Draw".center(130))


