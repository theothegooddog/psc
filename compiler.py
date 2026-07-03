from sys import argv

file = open(argv[1],"r").read().replace("\n","").split(';')

libraries = []
variables = {}

def parsecmd(line):
	def value(x):
		if x in variables:
			return variables[x]
		try:
			return int(x)
		except ValueError:
			return x
	cmd = line.split(" ")[0]
	args = line.split(" ")[1:]
	if cmd == "set":
		variables[args[0]] = value(args[1])
	
	elif cmd == "add":
		variables[args[0]] += value(args[1])
	
	elif cmd == "sub":
		variables[args[0]] -= value(args[1])
	
	elif cmd == "mul":
		variables[args[0]] *= value(args[1])
	
	elif cmd == "div":
		variables[args[0]] /= value(args[1])
	
	elif cmd == "pow":
		variables[args[0]] **= value(args[1])
	
	elif "math" in libraries:
		if cmd == "floor":
			variables[args[0]]=math.floor(int(variables[args[0]]))
		elif cmd == "sin":
			variables[args[0]]=math.sin(int(variables[args[0]]))
		elif cmd == "cos":
			variables[args[0]]=math.cos(int(variables[args[0]]))
	elif cmd == "\n" or cmd == ";":
		print("seperator as cmd; passing")

for line in file:
	if line.startswith("#import "):
		for library in line[7:].split(' ')[1:]:
			if library == "graphics.psl":
				libraries.append("graphics")
			elif library == "math.psl":
				libraries.append("math")
				import math
	else:
		parsecmd(line)

