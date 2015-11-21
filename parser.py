#!/usr/bin/env python
import csv
import os
# from enum import Enum

import sys


try:
    import tkinter
    from tkinter.filedialog import askopenfilename
except ImportError:
    try:
        import Tkinter as tkinter
        from tkinter.filedialog import askopenfilename
    except ImportError:
        print("Unable to load TK inter. Only works now with valid argument")
from import_csv import get_offsets
DPX_LOOKUP = "dpx_offsets.csv"


def write_field(data, field_name, file_name):
    with open(file_name, 'r+b') as file:
        start, end = get_offsets(DPX_LOOKUP, field_name)

        # prevents user adding data larger than then will fit
        if len(data) > end - start:
            raise Exception("Data is larger than the allowed space")

        print("Writing into field: {}. \t\"{}\"".format(field_name, data))
        file.seek(start)
        file.write(bytes(data, encoding="ASCII"))


def get_file():
    root = tkinter.Tk()
    root.withdraw()
    file_opt = options = {}
    options['defaultextension'] = '.avi'
    options['filetypes'] = [('CSV', '.csv'),
                            ('All Files', '.*')]
    options['parent'] = root
    options['title'] = 'Select a file'
    f = askopenfilename(**file_opt)
    return f


def main():
    csv_file= None
    files_alterned = 0
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            csv_file = sys.argv[1]
        else:
            sys.stderr.write("Error: Cannot find file \"{}\"\nExiting.".format(sys.argv[1]))
            exit(-1)
    else:
        csv_file = get_file()
    if csv_file:
        print("Starting DPX metadata altering script")
        # f = os.path.normcase(f)
        with open(csv_file) as data_file:
            DPX_records = csv.DictReader(data_file)
            pwd = os.path.dirname(os.path.abspath(csv_file))
            print("Working folder {}.".format(pwd))

            # TODO: make a function that searches for all the files first
            # TODO: change to generator that runs through all the found files

            for record in DPX_records:
                # print(csv_file)

                # pwd = os.path()/

                for f in os.listdir(pwd):
                    if f == os.path.basename(record['RealFileName']):
                        workingFile = os.path.join(pwd, os.path.basename(record['RealFileName']))
                        print("Now Working on: {}".format(workingFile))
                        write_field(data=record['Creator'], field_name='Creator', file_name=workingFile)
                        write_field(data=record['FileName'], field_name='FileName', file_name=workingFile)
                        write_field(data=record['Project'], field_name='Project', file_name=workingFile)
                        files_alterned += 1
                print("")
                pass
            print("{} DPX files changed.".format(files_alterned))
            print("All done.")

if __name__ == '__main__':
    main()