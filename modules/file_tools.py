import os
import glob
from pathlib import Path


def file_tree(path):
    ''' Creates a tree of dirs, subdirs and files and writes to file.'''
    for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)

            for f in files:
                print('{}{}'.format(subindent, f))


def recursive_rename(path, old_ref, new_ref):
    ''' Renames all files in given directory that have specified refs. Files to have placeholders i.e. {{PLACE_HOLDER}} '''
    path = Path(path)
    print(path)
    ref = new_ref

    # list files
    for subdir, dirs in os.walk(path):
        for file in glob.glob(old_ref + '*'):
            old_str = file.split(old_ref+' - ')
            print(old_str)
            new_str = ref + ' - ' + old_str[1]
            print(new_str)

            # rename file
            os.rename(file, new_str)


def zip(path):
    pass


def unzip(path):
    pass


if __name__ == '__main__':
    main()
