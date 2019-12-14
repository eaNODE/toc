
#!/usr/bin/python

# ==================================================================================
import sys
import random
import string
import os
import time
from random import randint
from GCF import comp, remla, remup, chomsky, remuv, greinbach, getG
# ==================================================================================
try:
	answer = input("\t[+] Welcome To The ERKH SCFG Machine; Type *yes* To Continue ? ")
	if answer == 'Yes' or 'yes' or 'y' or 'Y':
		os.system('clear')
		while True:
			antosimp = int(input("\t\t[?] Lambda Production -> 1\n\t\t[?] Unit Production -> 2\n\t\t[?] Useless Production -> 3\n\t\t[?] Chomsky Normal Form(No | Allowed)-> 4\n\t\t[?] Greinbach Normal Form(No | Allowed) -> 5\n\t\t[?] Grammer Complexity -> 6\n"))
			if antosimp == 1:
				os.system('clear')
				result = getG()
				x = 0
				i = 0
				has_landa = False
				while x < len(result):
					if result[x][1].find("^")!=-1:
						has_landa = True
						break
					x = x + 1
				if has_landa:
					compres = remla(result)
					print("\t[+] Your Final Grammer:")
					while i < len(compres):
						print("\t\t", compres[i][1])
						i = i + 1
					# print("\t\t[*] The Complexity Of This Grammer Is: ", comp(compres))
				else:
					os.system('clear')
					print("\t[!] No Lambda Production Found In Your Grammer!")
				print("\t=-=-=-=-=-=-=-=")
			#================================================
			if antosimp == 2:
				os.system('clear')
				result = getG()
				compres = remup(result)
				# print("\t\t[*] The Complexity Of This Grammer After Simplification Process Is: ", comp(compres))
				print("\t=-=-=-=-=-=-=-=")
			#================================================
			if antosimp == 3:
				os.system('clear')
				result = getG()
				i = 0
				j = 0
				atp = []
				while i < len(result):
					r = result[i][1].split("->")
					tp = [c for c in r[1] if r[1].islower() or r[1]=="^"]
					atp.append(tp)
					i = i + 1
				if atp:
					compres = remuv(result)
					print("\t[+] Your Final Grammer:")
					while j < len(compres):
						print("\t\t", compres[j][1])
						j = j + 1
					print("\t\t[*] The Complexity Of This Grammer After Simplification Process Is: ", comp(compres))
				else:
					os.system('clear')
					print("\t[!] No Useless Variables Found In Your Grammer!")
				print("\t=-=-=-=-=-=-=-=")
			#================================================
			if antosimp == 4:
				os.system('clear')
				result = getG()
				i = 0
				z = 0
				dntc = []
				ntc = []
				while i < len(result):
					r = result[i][1].split("->")
					if len(r[1])==2 and r[1][1:].isupper():
						dntc.append(r[0]+"->"+r[1])
					elif len(r[1])==1 and not r[1].isupper():
						dntc.append(r[0]+"->"+r[1])
					elif len(r[1])==1:
						if r[1].islower() or r[1].isupper():
							os.system("clear")
							print("\t[!] Can't Convert!")
							if ntc:
								del ntc[:]
							break
					else:
						ntc.append(r[0]+"->"+r[1])
					i = i + 1
				if ntc:
					compres = chomsky(result)
					print("\t[+] Your Final Grammer:")
					while z < len(compres):
						print("\t\t", compres[z][1])
						z = z + 1
					print("\t\t[*] The Complexity Of This Grammer After Simplification Process Is: ", comp(compres))
				else:
					time.sleep(2)
					os.system("clear")
					print("\t[!] No Need Chomsky Normal Form!")
					print("\t=-=-=-=-=-=-=-=")
			#================================================
			if antosimp == 5:
				os.system('clear')
				result = getG()
				i = 0
				z = 0 
				flag = False
				while i < len(result):
					r = result[i][1].split("->")
					if len(r[1])==1:
						if r[1].isupper():
							os.system("clear")
							print("\t[!] Can't Convert!")
							flag = True
							break
					elif len(r[1])>1 or len(r[1])==2:
						if r[1][:1].isupper():
							os.system("clear")
							print("\t[!] Can't Convert!")
							flag = True
							break
					i = i + 1
				if not flag:
					compres = greinbach(result)
					print("\t[+] Your Final Grammer:")
					while z < len(compres):
						print("\t\t", compres[z][1])
						z = z + 1
					print("\t\t[*] The Complexity Of This Grammer After Simplification Process Is: ", comp(compres))
				else:
					time.sleep(2)
					os.system("clear")
					print("\t[!] No Need Greinbach Normal Form!")
					print("\t=-=-=-=-=-=-=-=")
			#================================================
			if antosimp == 6:
				os.system('clear')
				result = getG()
			#================================================
		if KeyboardInterrupt:
			sys.exit(1)
	else:
		sys.exit(1)
except KeyboardInterrupt:
	print("\n[*] Ctrl + C pressed")
	sys.exit(1)



	
