import os
path = 'testdir'
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
    dirs = os.listdir(path)
    for dir in dirs:
        if os.path.isdir(os.path.join(path, dir)):
            print(os.path.join(path, dir), os.listdir(os.path.join(path, dir)))
        else:
            if os.path.isfile(os.path.join(path, dir)):
                print(os.path.join(path, dir),
                      os.path.join(path, dir)[-1] == 'c')
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
    files = []
    ends_with = 'c'
    print(_find_files(os.path.join(os.getcwd(), path), files, ends_with))
