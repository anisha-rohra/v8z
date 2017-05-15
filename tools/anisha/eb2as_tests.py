import unittest, os

class TestNestedShellScript(unittest.TestCase):

    def setUp(self):
        os.system('. cleanup.sh tests/nested_nonrec')
        os.system('. cleanup.sh tests/nested_rec')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u b.out')

    def test_nonrecursive(self):
        os.system('. eb2as.sh tests/nested_nonrec/nested1/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('garbage.c'))
        self.assertTrue(os.path.isfile('tests/nested_nonrec/nested1/test_temp.c'))
        self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/subtract_temp.h'))
        self.assertTrue(os.path.isfile('tests/nested_nonrec/nested2/nested3/add_temp.h'))
        os.system('./a.out | iconv -f iso8859-1 -t ibm-1047 > b.out')
        compiled_file = open('b.out', 'rt')
        for line in compiled_file:
            self.assertEquals(line, 'helo word\n')

    def test_recursive(self):
        os.system('. eb2as.sh tests/nested_rec/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('tests/nested_rec/test_temp.c'))
        self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested2/subtract_temp.h'))
        self.assertTrue(os.path.isfile('tests/nested_rec/nested1/nested3/add_temp.h'))
        os.system('./a.out | iconv -f iso8859-1 -t ibm-1047 > b.out')
        compiled_file = open('b.out', 'rt')
        for line in compiled_file:
            self.assertEquals(line, 'helo word\n')

class TestSameDirShellScript(unittest.TestCase):

    def setUp(self):
        os.system('. cleanup.sh tests/samedir_nonrec')
        os.system('. cleanup.sh tests/samedir_rec')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u b.out')

    def test_nonrecursive(self):
        os.system('. eb2as.sh tests/samedir_nonrec/test.c -I .')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('tests/samedir_nonrec/test_temp.c'))
        self.assertTrue(os.path.isfile('tests/samedir_nonrec/subtract_temp.h'))
        self.assertTrue(os.path.isfile('tests/samedir_nonrec/add_temp.h'))
        os.system('./a.out | iconv -f iso8859-1 -t ibm-1047 > b.out')
        compiled_file = open('b.out', 'rt')
        for line in compiled_file:
            self.assertEquals(line, 'helo word\n')

    def test_recursive(self):
        os.system('. eb2as.sh tests/samedir_rec/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('tests/samedir_rec/test_temp.c'))
        self.assertTrue(os.path.isfile('tests/samedir_rec/subtract_temp.h'))
        self.assertTrue(os.path.isfile('tests/samedir_rec/add_temp.h'))
        os.system('./a.out | iconv -f iso8859-1 -t ibm-1047 > b.out')
        compiled_file = open('b.out', 'rt')
        for line in compiled_file:
            self.assertEquals(line, 'helo word\n')

class TestIncludesShellScript(unittest.TestCase):

    def setUp(self):
        os.system('. cleanup.sh tests/include_paths_tests')
        if os.path.isfile('test.u'):
            os.system('rm garbage.c test.u')

    def test_include_nonrec(self):
        os.system('. eb2as.sh tests/include_paths_tests/test_nonrecursive/test.c -I tests/include_paths_tests/test_nonrecursive/different_path/')
        self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/test_temp.c'))
        self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/subtract_temp.h'))
        self.assertTrue(os.path.isfile('tests/include_paths_tests/test_nonrecursive/different_path/dir1/add_temp.h'))

    def test_include_rec(self):
        os.system('. eb2as.sh -I tests/include_paths_tests/test_recursive/included_path tests/include_paths_tests/test_recursive/actual_code/test.c')
        self.assertTrue(os.path.isfile('test.u'))
        self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/actual_code/test_temp.c'))
        self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/actual_code/subtract_temp.h'))
        self.assertTrue(os.path.isfile('tests/include_paths_tests/test_recursive/included_path/add_temp.h'))

if __name__ == '__main__':
    unittest.main()
