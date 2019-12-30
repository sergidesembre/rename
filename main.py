#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
## Rename and copy of files from defined path
##################################################
## python software foundation license
##################################################
## Author: Sergi Desembre Garcia <sergi.desembre@gmail.com>
## Copyright: Copyright 2019 All rights reserved, Rename
## License: GNU General Public License v3.0
## Version: 0.0.1
## Status: dev
##################################################

# Generic/Built-in
import shutil, os, glob
from typing import Dict

# Other Libs
import plac, colored

# Owned
from classes.rename_files_to_updated_at import RenameFilesToUpdatedAt
from classes.rename_files_to_numeric import RenameFilesToNumeric
from classes.rename_files import RenameFiles
from classes.file import File

@plac.annotations(
    origin_path='define file path',
    rename_path='define path where copy renamed files',
    filter=('you can filter selected files to rename by type extensions, if is empty select all elements from path (ex: jpg,png,gif). By default select all files from path', 'option', 'f'),
    rename_type=('chose type renaming files (default|numeric|updated_at). The default type is without renaming files, maintaining same filename than the original', 'option', 'rt', str, 'default|numeric|updated_at')
)

def main(origin_path: str, rename_path: str, filter: str, rename_type: str = 'default') -> None:
    files = get_files(origin_path, rename_type, filter)

    files.rename()
    files.change_rename_path(rename_path)

    original = files.original_files().items()
    modified = files.modified.items()
    max_length_path = files.max_length_path()

    print("%sPreview files to rename: %s" % (colored.fore.GREEN, colored.style.RESET))

    for key, file in original:
        print("- %s -> %s" % (str(file).ljust(max_length_path), str(files.modified.get(key))))

    print("%sTotal files to rename: %s%s" % (colored.fore.GREEN, len(modified), colored.style.RESET))

    response = ask_confirm_rename()

    if response:
        print("%sRenaming files and copy into rename path...%s" % (colored.fore.GREEN, colored.style.RESET))
        action_rename_files(original, files.modified)
        print("%sRenaming task completed%s" % (colored.fore.GREEN, colored.style.RESET))

def get_files(path: str, type: str, filter: str) -> RenameFiles:
    switcher = {
        'numeric': RenameFilesToNumeric,
        'updated_at': RenameFilesToUpdatedAt,
        'default': RenameFiles
    }
    filtered_files = switcher[type]([])

    if filter:
        splitted_filters = filter.split(',')

        for filter in splitted_filters:
            file_result = glob.iglob(path + '/*.' + filter)
            for file in file_result:
                if os.path.isfile(file):
                    filtered_files.add_file(File(file))
    else:
        file_result = glob.iglob(path + '/*')
        for file in file_result:
            if os.path.isfile(file):
                filtered_files.add_file(File(file))

    return filtered_files

def ask_confirm_rename() -> bool:
    while True:
        answer = input('Are you sure to rename this files[y/n]: ')
        response = None

        if len(answer) > 0:
            response = answer[0].lower()

        if response not in ['y', 'n']:
            print("%sPlease answer with 'y' or 'n'%s" % (colored.fore.RED, colored.style.RESET))
        else:
            break

    return (False, True)[response == 'y']

def action_rename_files(original_files: dict, files: Dict[str, File]) -> None:
    for identifier, original_file in original_files:
        modified_file = files[identifier]

        if not os.path.exists(modified_file.path):
            os.makedirs(modified_file.path)

        shutil.copy(str(original_file), str(modified_file))

if __name__ == '__main__':
    plac.call(main)