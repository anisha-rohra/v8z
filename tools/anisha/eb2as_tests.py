import unittest, os

class TestNestedShellScript(unittest.TestCase):

    def setUp(self):
        os.system('../cleanup.sh nested_nonrec')
        os.system('../cleanup.sh nested_rec')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u')

    def test_nonrecursive(self):
        os.system('../eb2as.sh nested_nonrec/nested1/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('garbage.c'))
        self.assertTrue(os.path.isfile('nested_nonrec/nested1/test_temp.c'))
        self.assertTrue(os.path.isfile('nested_nonrec/nested2/subtract_temp.h'))
        self.assertTrue(os.path.isfile('nested_nonrec/nested2/nested3/add_temp.h'))
        self.assertEquals(os.system('./a.out | iconv -f iso8859-1 -t ibm-1047', "hello world\n")

    def adding_nonrecursive(self):
        os.system('../eb2as.sh nested_nonrec/nested1/adding_things.cpp')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('garbage.c'))
        self.assertTrue(os.path.isfile('nested_nonrec/nested1/test_temp.cpp'))
        self.assertTrue(os.path.isfile('nested_nonrec/nested2/subtract_temp.h'))
        self.assertTrue(os.path.isfile('nested_nonrec/nested2/nested3/add_temp.h'))

    def test_recursive(self):
        os.system('../eb2as.sh nested_rec/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('nested_rec/test_temp.c'))
        self.assertTrue(os.path.isfile('nested_rec/nested1/nested2/subtract_temp.h'))
        self.assertTrue(os.path.isfile('nested_rec/nested1/nested3/add_temp.h'))

    def adding_things_recursive(self):
        os.system('../eb2as.sh nested_rec/adding_things.cpp')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('nested_rec/adding_things_temp.cpp'))
        self.assertTrue(os.path.isfile('nested_rec/nested1/nested2/subtract_temp.h'))
        self.assertTrue(os.path.isfile('nested_rec/nested1/nested3/add_temp.h'))

class TestSameDirShellScript(unittest.TestCase):

    def setUp(self):
        os.system('../cleanup.sh samedir_nonrec')
        os.system('../cleanup.sh samedir_rec')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u')

    def test_nonrecursive(self):
        os.system('../eb2as.sh samedir_nonrec/test.c -I .')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('samedir_nonrec/test_temp.c'))
        self.assertTrue(os.path.isfile('samedir_nonrec/subtract_temp.h'))
        self.assertTrue(os.path.isfile('samedir_nonrec/add_temp.h'))

    def adding_things_nonrecursive(self):
        os.system('../eb2as.sh samedir_nonrec/adding_things.cpp')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('samedir_nonrec/adding_things_temp.cpp'))
        self.assertTrue(os.path.isfile('samedir_nonrec/subtract_temp.h'))
        self.assertTrue(os.path.isfile('samedir_nonrec/add_temp.h'))

    def test_recursive(self):
        os.system('../eb2as.sh samedir_rec/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('samedir_rec/test_temp.c'))
        self.assertTrue(os.path.isfile('samedir_rec/subtract_temp.h'))
        self.assertTrue(os.path.isfile('samedir_rec/add_temp.h'))

    def adding_things_recursive(self):
        os.system('../eb2as.sh samedir_rec/adding_things.cpp')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('samedir_rec/adding_things_temp.cpp'))
        self.assertTrue(os.path.isfile('samedir_rec/subtract_temp.h'))
        self.assertTrue(os.path.isfile('samedir_rec/add_temp.h'))

class TestIncludesShellScript(unittest.TestCase):

    def setUp(self):
        os.system('../cleanup.sh includes_path_tests')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u')

    def test_include_nonrec(self):
        os.system('../eb2as.sh include_paths_tests/test_nonrecursive/test.c -I include_paths_tests -I include_paths_tests/test_nonrecursive/different_path/')
        self.assertTrue(os.path.isfile('include_paths_tests/test_nonrecursive/test_temp.c'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_nonrecursive/subtract_temp.h'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'))

    def adding_things_include_nonrec(self):
        os.system('../eb2as.sh include_paths_tests/test_nonrecursive/adding_things.cpp -I include_paths_tests -I include_paths_tests/test_nonrecursive/different_path/')
        self.assertTrue(os.path.isfile('include_paths_tests/test_nonrecursive/adding_things_temp.cpp'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_nonrecursive/subtract_temp.h'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'))

    def test_include_rec(self):
        os.system('../eb2as.sh -I include_paths_tests/test_recursive/included_path include_paths_tests/test_recursive/actual_code/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_recursive/actual_code/test_temp.c'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_recursive/actual_code/subtract_temp.h'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_recursive/included_path/add_temp.h'))

    def adding_things_include_rec(self):
        os.system('../eb2as.sh -I include_paths_tests/test_recursive/included_path include_paths_tests/test_recursive/actual_code/adding_things.cpp')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_recursive/actual_code/adding_things_temp.cpp'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_recursive/actual_code/subtract_temp.h'))
        self.assertTrue(os.path.isfile('include_paths_tests/test_recursive/included_path/add_temp.h'))

if __name__ == '__main__':
    unittest.main()
