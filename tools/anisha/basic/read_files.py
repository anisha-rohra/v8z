import ebcdic2ascii, sys, re, os

blacklist = []

# checks if the given header is in the global blacklist, meant for external use
def header_exists(header):
	return header in blacklist

# resets the blacklist to initial empty list, meant for external use
def reset_blacklist():
	blacklist = []

def main(args):

	DOT = re.compile('(.*)\.(.*)')
	dot_search = DOT.search(args[0])
	if dot_search is not None:
		target = dot_search.group(1) + "_temp." + dot_search.group(2)
	else:
		target = args[0] + "_temp"

	dot_search2 = DOT.search(args[1])
	if dot_search2 is not None:
		target_to_return = dot_search2.group(1) + "_temp." + dot_search2.group(2)
	else:
		target_to_return = args[1] + "_temp"

	# add the source header path to the blacklist to ensure the same headers aren't being
	# translated again
	if not header_exists(args[0]):
		if not os.path.isfile(args[0]):
			return 1

		blacklist.append(args[0])
		ebcdic2ascii.open_files([args[0], target], False, False, args[2], args[3])

	# return the location to the target header path so that it can be written into the
	# translated source file
	return target_to_return

if __name__ == "__main__":
	main(sys.argv[1:])
