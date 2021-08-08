#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab


from __future__ import unicode_literals, division, absolute_import, print_function

import sys
import os
import datetime
import zipfile
from zipfile import ZipFile


fsencoding = sys.getfilesystemencoding()

# handle paths that might be filesystem encoded
def pathof(s, enc=fsencoding):
    if s is None:
        return None
    if isinstance(s, str):
        return s
    if isinstance(s, bytes):
        try:
            return s.decode(enc)
        except:
            pass
    return s

# properly handle relative paths as well
def relpath(path, start=None):
    return os.path.relpath(pathof(path) , pathof(start))

# generate a list of files in a folder
def walk_folder(top):
    top = pathof(top)
    rv = []
    for base, dnames, names  in os.walk(top):
        base = pathof(base)
        for name in names:
            name = pathof(name)
            rv.append(relpath(os.path.join(base, name), top))
    return rv

_SKIP_LIST = [
    'encryption.xml',
    'rights.xml',
    '.gitignore',
    '.gitattributes'
]

# return True if file should be copied to destination folder
def valid_file_to_copy(rpath):
    segs = rpath.split(os.sep)
    if ".git" in segs:
        return False
    filename = os.path.basename(rpath)
    keep = filename not in _SKIP_LIST
    return keep


def build_epub_from_folder_contents(foldpath, epub_filepath):
    outzip = zipfile.ZipFile(pathof(epub_filepath), mode='w')
    files = walk_folder(foldpath)
    if 'mimetype' in files:
        outzip.write(pathof(os.path.join(foldpath, 'mimetype')), pathof('mimetype'), zipfile.ZIP_STORED)
        print("  loading: ", "mimetype")
    else:
        raise Exception('mimetype file is missing')
    files.remove('mimetype')
    for file in files:
        print("  adding: ", file)
        if valid_file_to_copy(file):
            filepath = os.path.join(foldpath, file)
            outzip.write(pathof(filepath),pathof(file),zipfile.ZIP_DEFLATED)
    outzip.close()


def main(argv=sys.argv):
    tagname = datetime.datetime.now().strftime('%Y.%m.%d')
    if os.getenv('GITHUB_TAGNAME') not in (None, ''):
        print('Tag build: {}'.format(os.getenv('GITHUB_TAGNAME')))
        if os.getenv('GITHUB_TAGNAME') == 'true':
            if os.getenv('GITHUB_TAGNAME') not in (None, ''):
                tagname = os.getenv('GITHUB_TAGNAME')
                print('Tag: {}'.format(tagname))

    foldpath = os.path.join(os.path.dirname(__file__), "..", "..", "src")
    
    # use folder name as name for epub
    epubname = "Sigil_User_Guide_{}.epub".format(tagname)
                
    rv = -1
    data = b''        

    epubpath = os.path.join(os.path.dirname(__file__), "..", "..", epubname)
    try:
        build_epub_from_folder_contents(foldpath, epubpath)
        with open(epubpath,'rb') as fp:
            data = fp.read()
        rv = 0
    except Exception as e:
        print("Guide EPUB build failed")
        print(str(e))
        rv = -1

    if rv == -1:
        return -1
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
