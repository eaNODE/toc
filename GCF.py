# ==================================================================================
import time
import sys
from random import randint
import random
import string
# ==================================================================================
def getG():
	productions = []
	n = int(input("[+] Enter The Number Of Productions! "))
	i = 1
	j = 0
	while i <= n:
		productions.append(input("[+] Enter Production.. "))
		i = i + 1
	result = list(enumerate(productions))
	print("-----------------------------------")

	print("[+] Grammer Analyzing")
	while j < len(result):
		if len(result[j][1].split('->')[0])>1: 
			print('\t[-] Your Grammer IS Not Context-Free! Becuse Of Production Number ', '*',j + 1,'*')
			sys.exit(1)
		print("\t[*] Rule Number", j+1, ":", result[j][1])
		print("\t[*] Variables:", ", ".join(c for c in result[j][1] if c.isupper()))
		print("\t[*] Lambda Production:", " ".join("Yes" for c in result[j][1] if c == '^'))
		print("\t[*] Terminals:", ", ".join(c for c in result[j][1] if c.islower()))
		print("\t=-=-=-=-=-=-=-=")
		j = j + 1
	print("\t[*] The Complexity Of This Grammer Is: ", comp(result))
	print("\t=-=-=-=-=-=-=-=")
	return result
# -----------------------------------------------------------
def comp(result):
	length = 0
	c = 0
	while c < len(result):
		r = result[c][1].split('->')[1] 
		if r.find("|")!=-1:
			r = r.split("|")
			j = 0
			h = 0
			while h < len(r):
				j = j + len(r[h]) + 1
				h = h + 1
			length = j + length
		else:
			j = 0
			j = j + len(r) + 1
			length = j + length
		c = c + 1
	return length
# -----------------------------------------------------------
# BUG: doesn't substitution right
def remla(result):
	print("\t[*] Checking For Nullable Variables...")
	k = 0
	l = 0
	m = 0
	nv = []
	newp = []
	# newp = {}
	newpwl = {}
	oldp = {}
	finalg_l = []
	while k < len(result):
		r = result[k][1].split('->')
		if r[0]!='S':
			sr = ''
			if r[1].find("^")!=-1:
				nv.append(r[0])
				sr += r[0]
				sr += "->^"
				print("\t[*] Rule Number", k+1, "Has Lambda Production Like So:", sr)
				time.sleep(1)
				print("\t[*] Nullable Variable Found!", r[0])
				time.sleep(1)
				print("\t[*] Runing Substitution Process...")
				time.sleep(2)
				if r[1].find("|")!=-1:
					rs = r[1].split("|")
					g = 0
					while g < len(rs):
						if rs[g].find("^")!=-1:
							rs.remove('^')
						g = g + 1
					z = 0
					kr = ''
					if len(rs)>1:
						while z < len(rs):
							kr += rs[z]+'|' 
							z = z + 1
						kr = kr[:-1]
						kr = r[0]+'->'+kr
					else:
						kr += r[0]+'->'+rs[0]
					newpwl[k+1] = kr
				else:
					r.remove("^")
			else:
				print("\t[*] No Lambda Production For Rule Number", k+1, "Found!")
				oldp[k+1] = result[k][1]
				time.sleep(1)
		k = k + 1
	while l < len(result):
		while m < len(nv):
			scwor = ''
			scwor1 = ''
			if result[l][1].split('->')[1].find(nv[m])!=-1:
				scwor = result[l][1].split('->')[1]
				scwor1 += "|"+result[l][1].split('->')[1].replace(nv[m], "^")
				newp.append(result[l][1].split('->')[0]+"->"+scwor+scwor1)
			m = m + 1
		l = l + 1
	for i in range(len(newp)):
		if newp[i].split("->")[1][-2:] == '|^':
			finalg_l.append(newp[i].split("->")[0]+"->"+newp[i].split("->")[1].replace(newp[i].split("->")[1], newp[i].split("->")[1][:-2]))
		else:
			finalg_l.append(newp[i].split("->")[0]+"->"+newp[i].split("->")[1])
	for key, value in newpwl.items():
		finalg_l.append(newpwl[key])
	for key, value in oldp.items():
		finalg_l.append(oldp[key])
	fresult = list(enumerate(finalg_l))
	return fresult
# -----------------------------------------------------------
#TODO: make some change on swup list and return final result
def remup(result):
	print("\t[*] Checking For Unit-Productions...")
	time.sleep(1) 
	i = 0
	k = 0
	g = 0
	upr = {}
	swup = []
	while i < len(result):
		r = result[i][1].split("->")
		if r[1].isupper() and len(r[1])==1:
			print("\t[*] Unit Production Found In Rule Number", i+1)
			upr[r[0]]=r[1]
		i = i + 1
	print("\t[*] Runing Substitution Process...")
	time.sleep(1)
	while k < len(result):
		r = result[k][1].split("->")
		scwor = ''
		scwor1 = ''
		for key, val in upr.items():
			if r[1].find(key):
				scwor = r[1]
				scwor1 += "|"+r[1].replace(key, val)
				swup.append(r[0]+"->"+scwor+scwor1)
				print(swup)
		k = k + 1
	if swup:
		print(swup)

# -----------------------------------------------------------
def remuv(result):
	print("\t[*] Removing Useless Variables...")
	time.sleep(2)
	ar = ''
	i = 0
	g = 0
	k = 0
	z = 0
	v = 0
	o = 0
	w = 0
	sp = []
	sp1 = []
	newp = []
	while i < len(result):
		r = result[i][1].split("->")
		tp = [c for c in r[1] if r[1].islower() or r[1]=="^"]
		if tp:
			sp.append(r[0]+"->"+r[1])
		i = i + 1
	while g < len(result):
		r = result[g][1].split("->")
		x = 0
		while x < len(sp):
			if sp[x].split("->")[0] in r[1]:
				sp1.append(r[0]+"->"+r[1])
			x = x + 1
		g = g + 1
	sp2 = sp + sp1
	while w < len(sp2):
		if result[0][1].find(sp2[w].split("->")[0])==-1:
			sp2.remove(sp2[w].split("->")[0]+"->"+sp2[w].split("->")[1])
		w = w + 1
	while o < len(sp2):
		ar+=sp2[o].split("->")[0]
		o = o + 1
	while k < len(result):
		r = result[k][1].split("->")
		while v < len(sp2):
			if r[0] == sp2[v].split("->")[0]:
				if r[1].find("|")!=-1:
					rs = r[1].split("|")
					while z < len(rs):
						if len(rs[z])==1 and ar.find(rs[z]):
							rs.remove(rs[z])
						z = z + 1
					q = 0
					kr = ''
					if len(rs)>1:
						while q < len(rs):
							kr += rs[q]+'|' 
							q = q + 1
						kr = kr[:-1]
					else:
						kr += rs[0]
					newp.append(r[0]+"->"+kr)
					sp2.remove(sp2[v])
			v = v + 1
		k = k + 1
	fresult = list(enumerate(newp+sp2))
	return fresult
# -----------------------------------------------------------
def chomsky(result):
	print("\t[*] Converting To Chomsky Normal Form...")
	time.sleep(1)
	i = 0
	j = 0
	dntc = []
	ntc = []
	chp = []
	chnf = []
	while i < len(result):
		r = result[i][1].split("->")
		if len(r[1])==2 and r[1][1:].isupper():
			dntc.append(r[0]+"->"+r[1])
		elif len(r[1])==1 and not r[1].isupper():
			dntc.append(r[0]+"->"+r[1])
		else:
			ntc.append(r[0]+"->"+r[1])
		i = i + 1
	# print(dntc)
	# print(ntc)
	while j < len(ntc):
		lowercase_letters = [c for c in ntc[j].split("->")[1] if c.islower()]
		if len(ntc[j].split("->")[1])>2:
			# pass ntc[j] to CR function
			chnfr = CR(ntc[j])
			for i in range(len(chnfr)):
				chnf.append(chnfr[i])
			# x = random.choice(string.ascii_uppercase)
			# chp.append(x+"->"+ntc[j].split("->")[1][:2])
			# chp.append(ntc[j].split("->")[0]+"->"+x+ntc[j].split("->")[1][2:]) 
		elif len(lowercase_letters)==2:
			x = random.choice(string.ascii_uppercase)
			y = random.choice(string.ascii_uppercase)
			chp.append(x+"->"+ntc[j].split("->")[1][:1])
			chp.append(y+"->"+ntc[j].split("->")[1][1:])
			chp.append(ntc[j].split("->")[0]+"->"+x+y)
		elif len(ntc[j].split("->")[1])==2:
			x = random.choice(string.ascii_uppercase)
			lowlet = [c for c in ntc[j].split("->")[1] if c.islower()]
			chp.append(x+"->"+lowlet[0])
			if ntc[j].split("->")[1][:1] == lowlet[0]:
				chp.append(ntc[j].split("->")[0]+"->"+x+ntc[j].split("->")[1][1:])
			else:
				chp.append(ntc[j].split("->")[0]+"->"+ntc[j].split("->")[1][:1]+x)
		j = j + 1
	
	# print(chp+dntc+chnf)
	fresult = list(enumerate(chp+dntc+chnf))
	return fresult
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def CR(r):
	rt = []
	var = r.split("->")[0]
	rhs = r.split("->")[1]
	lrhs = len(rhs)
	nr = ''
	while lrhs!=2:
		x = random.choice(string.ascii_uppercase)
		nrhs = x+"->"+rhs[:2]
		rt.append(nrhs)
		nr = var+"->"+x+rhs[2:]
		rhs = nr.split("->")[1]
		lrhs = len(rhs)
	rt.append(nr)
	return rt
#------------------------------------------------------------
def greinbach(result):
	print("\t[*] Converting To Greinbach Normal Form...")
	time.sleep(1)
	i = 0
	j = 0
	dntc = []
	ntc = [] 
	chp = []
	kr = []
	while i < len(result):
		r = result[i][1].split("->")
		if len(r[1])==1:
			dntc.append(r[0]+"->"+r[1])
		elif len(r[1])==2:
			if r[1][-1].isupper():
				dntc.append(r[0]+"->"+r[1])
			elif r[1][-1].islower():
				ntc.append(r[0]+"->"+r[1])
		elif len(r[1])>1:
			if r[1][1:].isupper():
				dntc.append(r[0]+"->"+r[1])
			else:
				ntc.append(r[0]+"->"+r[1])
		i = i + 1
	while j < len(ntc):
		if ntc[j].split("->")[1][:1].islower():
			v = 1
			while v < len(ntc[j].split("->")[1]):
				if ntc[j].split("->")[1][v].islower():
					x = random.choice(string.ascii_uppercase)
					if chp:
						z = 0
						while z<len(chp):
							if ntc[j].split("->")[1][v]!=chp[z].split("->")[1]:
								chp.append(x+"->"+ntc[j].split("->")[1][v])
							z = z + 1
					else:
						#x = random.choice(string.ascii_uppercase)
						chp.append(x+"->"+ntc[j].split("->")[1][v])
					if ntc[j].split("->")[1].find(ntc[j].split("->")[1][v])!=-1:
						kr.append(ntc[j].split("->")[0]+"->"+ntc[j].split("->")[1][:1]+ntc[j].split("->")[1][1:].replace(ntc[j].split("->")[1][v], x))
				v = v + 1
		j = j + 1
	kr = list(set(kr))
	fresult = list(enumerate(chp+kr+dntc))
	return fresult