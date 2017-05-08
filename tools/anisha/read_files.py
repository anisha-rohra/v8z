import ebcdic2ascii, sys, re

blacklist = []

def header_exists(header):
	return header in blacklist

def reset_blacklist():
	blacklist = []

def main(args):
	print(args)

	expr1 = re.compile("(.*)/.*")
	source = expr1.match(args[1]).group(1)

	expr2 = re.compile("(.*)\.(.*)")
	part1 = expr2.match(args[0]).group(1)
	part2 = expr2.match(args[0]).group(2)
	source_header_path = source + "/" + args[0]
	target_header_path = source + "/" + part1 + "_temp." + part2

	if not header_exists(source_header_path):
		blacklist.append(source_header_path)
		ebcdic2ascii.files([source_header_path, target_header_path])
		
	return part1 + "_temp." + part2

if __name__ == "__main__":
	main(sys.argv[1:])

