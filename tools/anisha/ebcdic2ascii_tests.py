import unittest, os, ebcdic2ascii, subprocess

# test with the file hiearchy in the folder tests/samedir_nonrec
# this means all the files are located in the same directory, and there is no recursive relationship
# between the header files (both header files located in include statements in the .cpp file)
class TestHeadersSameDirNonRec(unittest.TestCase):

	def setUp(self):
		if os.path.isfile('tests/samedir_nonrec/adding_things_after.cpp'):
			os.remove('tests/samedir_nonrec/adding_things_after.cpp')
		if os.path.isfile('tests/samedir_nonrec/add_temp.h'):
			os.remove('tests/samedir_nonrec/add_temp.h')
		if os.path.isfile('tests/samedir_nonrec/subtract_temp.h'):
			os.remove('tests/samedir_nonrec/subtract_temp.h')

	# test with external python use function ebcdic2ascii.openfiles()
	def test_samedir_nonrec_openfiles(self):
		ebcdic2ascii.open_files(['tests/samedir_nonrec/adding_things.cpp', 'tests/samedir_nonrec/adding_things_after.cpp'])
		self.assertTrue(os.path.isfile('tests/samedir_nonrec/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/samedir_nonrec/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/samedir_nonrec/add_temp.h'))

	# test by invoking the file as a shell script
	def test_samedir_nonrec_main(self):
		os.system('python ebcdic2ascii.py tests/samedir_nonrec/adding_things.cpp tests/samedir_nonrec/adding_things_after.cpp')
		self.assertTrue(os.path.isfile('tests/samedir_nonrec/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/samedir_nonrec/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/samedir_nonrec/add_temp.h'))

# test with the file hiearchy in the folder tests/samedir_rec
# this means all of the files are located in the same directory, and there IS a recursive relationship
# between the header files (subtract.h is invoked in add.h)
class TestHeadersSameDirRec(unittest.TestCase):

	def setUp(self):
		if os.path.isfile('tests/samedir_rec/adding_things_after.cpp'):
			os.remove('tests/samedir_rec/adding_things_after.cpp')
		if os.path.isfile('tests/samedir_rec/add_temp.h'):
			os.remove('tests/samedir_rec/add_temp.h')
		if os.path.isfile('tests/samedir_rec/subtract_temp.h'):
			os.remove('tests/samedir_rec/subtract_temp.h')

	def test_samedir_rec_openfiles(self):
		ebcdic2ascii.open_files(['tests/samedir_rec/adding_things.cpp', 'tests/samedir_rec/adding_things_after.cpp'])
		self.assertTrue(os.path.isfile('tests/samedir_rec/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/samedir_rec/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/samedir_rec/add_temp.h'))

	def test_samedir_rec_main(self):
		os.system('python ebcdic2ascii.py tests/samedir_rec/adding_things.cpp tests/samedir_rec/adding_things_after.cpp')
		self.assertTrue(os.path.isfile('tests/samedir_rec/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/samedir_rec/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/samedir_rec/add_temp.h'))

# test with the file hiearchy in the folder tests/nested_nonrec
# this means all of the files are located in different directories, and there it NOT a recursive relationship
# between the header files
class TestHeadersNestedNonRec(unittest.TestCase):

	def setUp(self):
		if os.path.isfile('tests/nested_nonrec/nested1/adding_things_after.cpp'):
			os.remove('tests/nested_nonrec/nested1/adding_things_after.cpp')
		if os.path.isfile('tests/nested_nonrec/nested2/subtract_temp.h'):
			os.remove('tests/nested_nonrec/nested2/subtract_temp.h')
		if os.path.isfile('tests/nested_nonrec/nested2/nested3/add_temp.h'):
			os.remove('tests/nested_nonrec/nested2/nested3/add_temp.h')

	def test_nested_nonrec_openfiles(self):
		ebcdic2ascii.open_files(['tests/nested_nonrec/nested1/adding_things.cpp', 'tests/nested_nonrec/nested1/adding_things_after.cpp'])
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested1/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/nested3/add_temp.h'))

	def test_nested_nonrec_main(self):
		os.system('python ebcdic2ascii.py tests/nested_nonrec/nested1/adding_things.cpp tests/nested_nonrec/nested1/adding_things_after.cpp')
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested1/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/nested3/add_temp.h'))

# test with the file heiarchy in the folder tests/nested_red
# this means all of the files are located in different directories, and there IS a recursive relationship
# between the header files
class TestHeadersNestedRec(unittest.TestCase):

	def setUp(self):
		if os.path.isfile('tests/nested_rec/adding_things_after.cpp'):
			os.remove('tests/nested_rec/adding_things_after.cpp')
		if os.path.isfile('tests/nested_rec/nested1/nested2/subtract_temp.h'):
			os.remove('tests/nested_rec/nested1/nested2/subtract_temp.h')
		if os.path.isfile('tests/nested_rec/nested1/nested3/add_temp.h'):
			os.remove('tests/nested_rec/nested1/nested3/add_temp.h')

	def test_nested_rec_openfiles(self):
		ebcdic2ascii.open_files(['tests/nested_rec/adding_things.cpp', 'tests/nested_rec/adding_things_after.cpp'])
		self.assertTrue(os.path.isfile('tests/nested_rec/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested2/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested3/add_temp.h'))

	def test_nested_rec_main(self):
		os.system('python ebcdic2ascii.py tests/nested_rec/adding_things.cpp tests/nested_rec/adding_things_after.cpp')
		self.assertTrue(os.path.isfile('tests/nested_rec/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested2/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested3/add_temp.h'))

class TestIncludePathsNonRec(unittest.TestCase):

	def setUp(self):
		if os.path.isfile('tests/include_paths_tests/test_nonrecursive/adding_things_after.cpp'):
			os.remove('tests/include_paths_tests/test_nonrecursive/adding_things_after.cpp')
		if os.path.isfile('tests/include_paths_tests/test_nonrecursive/subtract_temp.h'):
			os.remove('tests/include_paths_tests/test_nonrecursive/subtract_temp.h')
		if os.path.isfile('tests/include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'):
			os.remove('tests/include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h')

	def test_include_nonrec_openfiles(self):
		ebcdic2ascii.open_files(['tests/include_paths_tests/test_nonrecursive/adding_things.cpp', 'tests/include_paths_tests/test_nonrecursive/adding_things_after.cpp'], False, False, ['tests/include_paths_tests/', 'tests/include_paths_tests/test_nonrecursive/different_path/'])
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'))

	def test_include_nonrec_main(self):
		os.system('python ebcdic2ascii.py tests/include_paths_tests/test_nonrecursive/adding_things.cpp tests/include_paths_tests/test_nonrecursive/adding_things_after.cpp -I tests/include_paths_tests -I tests/include_paths_tests/test_nonrecursive/different_path/s')
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/adding_things_after.cpp'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'))

if __name__ == '__main__':
	unittest.main()
