import ebcdic2ascii, sys, re

def main(args):
	print(args)

	expr1 = re.compile("(.*)/.*")
	source = expr1.match(args[-1]).group(1)
	print(source)
	
	for file in args[:-1]:	

		expr2 = re.compile("(.*)\.(.*)")
		part1 = expr2.match(file).group(1)
		part2 = expr2.match(file).group(2)

		ebcdic2ascii.main([source + "/" + file, source + "/" + part1 + "_temp." + part2])


if __name__ == "__main__":
	main(sys.argv[1:])

