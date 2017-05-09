import ebcdic2ascii, sys, re

blacklist = []

# checks if the given header is in the global blacklist, meant for external use
def header_exists(header):
	return header in blacklist

# resets the blacklist to initial empty list, meant for external use
def reset_blacklist():
	blacklist = []

def main(args):

	# args contains the target path which is the path to the header that needs to be
	# translated and the source path which is the path to the original source file
	expr1 = re.compile("(.*)/.*")
	source = expr1.match(args[1]).group(1)

	expr2 = re.compile("(.*)\.(.*)")
	part1 = expr2.match(args[0]).group(1)
	part2 = expr2.match(args[0]).group(2)

	# source header_path is the path to be translated
	# target header_path is the path where the translation is stored
	# currently, that is the same directory as the source header path with the same
	# name and a _temp after that name before the extension
	source_header_path = source + "/" + args[0]
	target_header_path = source + "/" + part1 + "_temp." + part2

	# add the source header path to the blacklist to ensure the same headers aren't being
	# translated again
	if not header_exists(source_header_path):
		blacklist.append(source_header_path)
		ebcdic2ascii.open_files([source_header_path, target_header_path], False, False)
		
	# return the location to the target header path so that it can be written into the
	# translated source file
	return part1 + "_temp." + part2

if __name__ == "__main__":
	main(sys.argv[1:])

