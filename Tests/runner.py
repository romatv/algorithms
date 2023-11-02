import unittest

test_suite = unittest.defaultTestLoader.discover(start_dir='.', pattern='test_*.py')

test_runner = unittest.TextTestRunner(verbosity=1)


if __name__ == '__main__':
    result = test_runner.run(test_suite)
    if result.wasSuccessful():
        print('All tests passed!')
    else:
        print('Some tests failed.')