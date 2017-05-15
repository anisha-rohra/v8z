import unittest, os, ebcdic2ascii

class TestShellScript(unittest.TestCase):

	def setUp(self):
		os.system('. cleanup.sh tests/nested_nonrec')
        os.system('. cleanup.sh tests/nested_rec')
		os.system('. cleanup.sh tests/include_paths_tests')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u')

	def test_nested_nonrec_main(self):
		os.system('njsc -E -qmakedep tests/nested_nonrec/nested1/test.c > tests/nested_nonrec/nested1/test_temp.c')
		self.assertTrue(os.path.isfile('test.u'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested1/test_temp.c'))
		os.system('python ebcdic2ascii.py -H test.u tests/nested_nonrec/nested1/test.c tests/nested_nonrec/nested1/test_after.c')
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested1/test_after.c'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/nested3/add_temp.h'))

	def test_nested_rec_main(self):
		os.system('njsc -E -qmakedep tests/nested_rec/test.c > tests/nested_rec/test_temp.c')
		self.assertTrue(os.path.isfile('test.u'))
		self.assertTrue(os.path.isfile('tests/nested_rec/test_temp.c'))
		os.system('python ebcdic2ascii.py -H test.u tests/nested_rec/test.c tests/nested_rec/test_after.c')
		self.assertTrue(os.path.isfile('tests/nested_rec/test_after.c'))
		self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested2/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested3/add_temp.h'))

	def test_include_rec_main(self):
		os.system('njsc -E -qmakedep -I tests/include_paths_tests -I tests/include_paths_tests/test_recursive/included_path tests/include_paths_tests/test_recursive/actual_code/test.c > tests/include_paths_tests/test_recursive/actual_code/test_temp.c')
		self.assertTrue(os.path.isfile('test.u'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/actual_code/test_temp.c'))
		os.system('python ebcdic2ascii.py -H test.u include_paths_tests/test_recursive/actual_code/test.c include_paths_tests/test_recursive/actual_code/test_after.c')
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/actual_code/test_after.c'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/actual_code/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/included_path/add_temp.h'))

	def test_include_nonrec_main(self):
		os.system('njsc -E -qmakedep -I tests/include_paths_tests/test_nonrecursive/different_path tests/include_paths_tests/test_nonrecursive/test.c > tests/include_paths_tests/test_nonrecursive/test_temp.c')
		self.assertTrue(os.path.isfile('test.u'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/test_temp.c'))
		os.system('python ebcdic2ascii.py -H test.u tests/include_paths_tests/test_nonrecursive/test.c tests/include_paths_tests/test_nonrecursive/test_after.c')
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/test_after.c'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/subtract_temp.h'))
		self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'))

if __name__ == '__main__':
	unittest.main()
