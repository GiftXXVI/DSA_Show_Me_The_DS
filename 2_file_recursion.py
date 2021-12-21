import unittest
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is not None:
        if os.path.isdir(path):
            files = []
            return _find_files(path, files, suffix)
    return None


def _find_files(path, files, ends_with):
    if os.path.isfile(path):
        if path[-1] == ends_with:
            files.append(path)
        return None
    else:
        dirs = os.listdir(path)
        if len(dirs) == 0:
            return None
        else:
            for dir in dirs:
                _find_files(os.path.join(path, dir), files, ends_with)
            return files


class Tests(unittest.TestCase):
    def setUp(self):
        self.path = 'testdir'
        self.listing = ['testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c',
                        'testdir/subdir5/a.c', 'testdir/t1.c']
        self.suffix = 'c'
        self.none = None
        self.empty = 'testdir1'

    def test_recursion(self):
        self.assertEqual(
            sorted(find_files(self.suffix, self.path)), sorted(self.listing))

    def test_null(self):
        self.assertEqual(find_files(self.suffix,  self.none), None)

    def test_empty(self):
        self.assertEqual(find_files(self.suffix, self.empty), None)


if __name__ == "__main__":
    unittest.main()
