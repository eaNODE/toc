

#--------------------------------------------------------------------------------------------
# it will take a context free grammer and calculate its PDA step by step as the time goes by
#--------------------------------------------------------------------------------------------

import sys, os, time
# grammer class
class Grammer:

	def __init__(self, grammer):
		self._grammer = grammer
		self._stack = [] # instance variable unique to each instance; our pda stack

	# printing the context free grammer
	def show(self):
		if self.cf():
			print("[+] Context Free Detected: {}".format(self._grammer))
		else:
			print("[!] Not A Context Free!")
			sys.exit(1)

	# checking context free procedure
	def cf(self):
		i = 0
		while i < len(self._grammer):
			if len(self._grammer[i][1].split("->")[0])>1:
				return False
				break
			i = i + 1
		return True

	# checking string derivation procedure
	# we know that every variable is reachable from S in the grammer; we assume its a normal grammer!
	# so if we derivate S till we found a match between our str and the derivation itself we can produce our considered string, cause there is a variables
	# which will end up to the lambda or a terminal.
	def strdev(self, st):
		# checking if the string is a derivation from our grammer or not
		# it'll return True if there was any match or false for none
		# we derivate S till we find a match between our str and the derivation itself
		i = j = k = 0
		# cause every varible is reachable from S so we store the first rule which is S in our pdev stack to derivate it till the end of our string
		#pdev = [self._grammer[0][1]]
		terminal_or_lambda_rule = []
		if st[-1:]!=self._grammer[0][1].split('->')[1][-1:]:
			print("[-] Can't Derivate, Last Character '{}' of Input String Detected!".format(st[-1:]))
			return False
		# finding varibles which end up to terminal or lambda in every rule
		for i in range(len(self._grammer)):
			if len(self._grammer[i][1].split("->")[1])==1 and self._grammer[i][1].split("->")[1].islower():
				terminal_or_lambda_rule.append(self._grammer[i][1])
			if len(self._grammer[i][1].split("->")[1])==1 and self._grammer[i][1].split("->")[1]=="^":
				terminal_or_lambda_rule.append(self._grammer[i][1])
			if len(self._grammer[i][1].split("->")[1])==2:
				terminal_or_lambda_rule.append(self._grammer[i][1])
		#print(terminal_or_lambda_rule)
		# every variable is reachable from S so we'll find those variables which is in terminal_or_lambda_rule stack in S and replace them with lambda or their terminals
		# and we'll do this till we find a match between our input string and S produced derivation 
		# ISSUE: it can't derivate the grammer n times, kind of AI required to detect the number of derivations from our input string; doesn't accept "aababab"!!!!
		''' FIXED: we should derivate our devstr as the length as of our input string; 
				 for example if len(st) is equal to 7 then the length of our devstr must be 7
				 (number of lambdas won't calculate, cause they will increase the length of our devstr) '''
		devstr = self._grammer[0][1].split('->')[1]
		input_string_length = len(st)
		devstr_length = len(devstr)
		# we derivate the devstr till we find a match between the length of our input string and the length of devstr itself
		while devstr_length!=input_string_length:
			for k in range(len(terminal_or_lambda_rule)):
				if terminal_or_lambda_rule[k].split("->")[0] in devstr and '^' not in terminal_or_lambda_rule[k].split("->")[1]:
					if terminal_or_lambda_rule[k].split("->")[0]=='S':
						devstr = devstr.replace(terminal_or_lambda_rule[k].split("->")[0], devstr)
					else:
						devstr = devstr.replace(terminal_or_lambda_rule[k].split("->")[0], terminal_or_lambda_rule[k].split("->")[1])
			devstr_length = len(devstr)
		# we found the desired derivation for our input string, then we need to produce our string from our S derivation 
		print(devstr) # debug purposes
		# so we replace varibles in S with their terminals or lambdas		
		for k in range(len(terminal_or_lambda_rule)):
			if terminal_or_lambda_rule[k].split("->")[0] in devstr:
				devstr += "*->"+devstr.replace(terminal_or_lambda_rule[k].split("->")[0], terminal_or_lambda_rule[k].split("->")[1])
		print("[+] Processing Derivation...")
		time.sleep(1)
		print(devstr) # debug purposes
		# removing lambdas from our derivation string 
		print("[+] Removing Lambdas...")
		if "^" in devstr:
			devstr = devstr.replace("^", '')
		time.sleep(1)
		print(devstr) # debug purposes
		if st in devstr:
			print("[+] Derivation Found!")
			return True
		else:
			print("[-] Unable To Find Derivation!")
			return False


	# computing pda for our input string right after we derivated it from our grammer
	def pda(self, st):
		pass
















try:
	# getting & storing the rules
	n = int(input("[+] Number Of Rules: "))
	i = j = 0
	gr = []
	while i < n:
		gr.append(input("[+] Enter Grammer: "))
		i += 1
	# removing | from grammer
	# for j in range(len(gr)):
	# 	if '|' in gr[j].split("->")[1]:
	# 		gr.append(gr[j].split("->")[0]+"->"+gr[j].split("->")[1].split("|")[0])
	# 		gr.append(gr[j].split("->")[0]+"->"+gr[j].split("->")[1].split("|")[1])
	# 		del gr[j]
	# 	else:
	# 		pass
	gr = list(enumerate(gr))
	# initializing grammer instance
	g = Grammer(gr)
	# printing the considered rules
	g.show()
	# getting string from user
	st = input("[+] Input String: ")
	# string derivation process
	g.strdev(st)
	# if g.strdev(st):
	# 	# if we found our string in some derivation of S the there is a pda that accept this string/input
	# 	g.pda(st) 


# user input to stop the script like ctrl+C
except KeyboardInterrupt:
	print("\n[*] Ctrl + C pressed")
	sys.exit(1)