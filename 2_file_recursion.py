import os
path = './testdir'
suffix = 'c'


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
    print(os.listdir(path))
    return None

def r_find_files(suffix, path):
    return None


if __name__ == "__main__":
    find_files(suffix, path)
