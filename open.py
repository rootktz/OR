import requests
from platform import system
import os
from colorama import Fore,Style
from multiprocessing.dummy import Pool as ThreadPool

os.system('clear')

print('''\t********************************************\n''')
print('''\t* OpenRedriect Scanner By SoukChawGyi X-Ray*\n''')
print('''\t********************************************''')

a=input("\nEnter target:::> ")
file=input("Enter payload list:::> ")
opened=open(file)
x=[]
x.append(a)
def main(i):
	for i in opened:
		i=i.strip()
		r=requests.get(a+i)
		if r.history:
			print(Fore.GREEN+"vuln==>",Style.RESET_ALL+a+i,'\n')
			print('\t','_'*40,'\n')
			print('\t\tDone!.I am Souk Chaw Gyi')
			print('\t','_'*40)
			exit()
		else:
			print(Fore.RED+'notvuln==>',Style.RESET_ALL+a+i,'\n')
if __name__ == "__main__":
   pool = ThreadPool(100)  
   results = pool.map(main, x)
   pool.close() 
   pool.join()
