import os
path = 'testdir'
suffix = 'c'
files = []


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
                print(path)
                _find_files(os.path.join(path, dir), files, ends_with)
            return files


if __name__ == "__main__":
    #find_files(suffix, path)
    suffix = 'c'
    print(find_files(suffix, os.path.join(os.getcwd(), path)))
