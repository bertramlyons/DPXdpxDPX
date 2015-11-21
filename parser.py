#!/usr/bin/env python
import csv
import os
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


class DataError(Exception):
    pass


def write_field(data, field_name, file_name):
    with open(file_name, 'r+b') as file:
        start, end = get_offsets(DPX_LOOKUP, field_name)
        max_size = end - start
        try:
            int(data)
            return
        except:
            pass
        # prevents user adding data larger than then will fit
        print("Writing into field: {}. \t\"{}\"".format(field_name, data))

        # fill the rest of the space with blank space
        if len(data) < max_size:
            while len(data) < max_size:
                data += " "
        if len(data) > max_size:
            raise DataError("Data in \"{}\" is larger than the allowed space. "
                            "Tried to add {} bytes of data in a limit of {}.".format(field_name, len(data), max_size))
        file.seek(start)
        file.write(bytes(data, encoding="ascii"))



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
    csv_file = None
    files_altered = 0
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
                        assert(isinstance(record, dict))
                        for key, value in record.items():
                            if key == "Number":
                                continue
                            if key == "RealFileName":
                                continue
                            if key == "Data":
                                continue
                            if value:

                                try:
                                    write_field(data=record[key], field_name=key, file_name=workingFile)
                                    # print(key)
                                except DataError as e:
                                    print("Error with field, {}.\n\"{}\".\n".format(key, e))
                        files_altered += 1
                print("")
                pass
            print("{} DPX files changed.".format(files_altered))
            print("All done.")

if __name__ == '__main__':
    main()