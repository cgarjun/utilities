#!/usr/bin/env python
import sys
import os

def main(startpath):
    for root, dirs, files in os.walk(startpath):
        if "." in root:
            pass
        else:
            print root
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

if __name__ == '__main__':
    main(sys.argv[1])
