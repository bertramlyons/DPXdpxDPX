import csv
import os
# from enum import Enum

import sys


try:
    import tkinter
    from tkinter.filedialog import askopenfilename
except ImportError:
    import Tkinter as tkinter
    from tkinter.filedialog import askopenfilename
from import_csv import get_offsets
DPX_LOOKUP = "dpx_offsets.csv"

def write_field(data, field_name, file_name):
    with open(file_name, 'r+b') as file:
        start, end = get_offsets(DPX_LOOKUP, field_name)
        print("Writing \"{}\" to \"{}\" field.".format(data, field_name))
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
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            csv_file = sys.argv[1]
        else:
            sys.stderr.write("Error: Cannot find file \"{}\"\nExiting.".format(sys.argv[1]))
            exit(-1)
    else:
        csv_file = get_file()
    if csv_file:
        print("starting DPX metadata project")
        # f = os.path.normcase(f)
        with open(csv_file) as data_file:
            reader = csv.DictReader(data_file)
            for record in reader:
                # print(csv_file)
                pwd = os.path.dirname(csv_file)
                # pwd = os.path()/
                # print(pwd)
                for f in pwd:
                    workingFile = os.path.basename(record['RealFileName'])
                    if f == workingFile:
                        print("Now Working on: {}".format(workingFile))
                        write_field(data=record['Creator'], field_name='Creator', file_name=workingFile)
                        write_field(record['FileName'], 'FileName', workingFile)
                        write_field(record['Project'], 'Project', workingFile)
                pass


if __name__ == '__main__':
    main()