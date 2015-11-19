import csv
import os
from enum import Enum
from import_csv import get_offsets
DPX_LOOKUP = "dpx_offsets.csv"
# def get_offsets(csvfile, field):
#
#     with open(csvfile) as datafile:
#         assert os.path.exists(csvfile)
#         reader = csv.DictReader(datafile)
#
#         # print(csvfile)
#         for entry in reader:
#             if entry['title'] == field:
#
#                 start_byte = entry['startByte']
#                 end_byte = entry['endByte']
#                 # print(start_byte, end_byte)
#
#                 return start_byte, end_byte
#             raise Exception("BAD BAD BAD")

class fields(Enum):
    Magic = 'Magic number'
    Offset = 'Offset to image data'
    Version = 'Version number of header format'
    Total = 'Total image file size'
    Ditto = 'Ditto Key'
    Generic = 'Generic section header length'
    Industry = 'Industry specific header length'
    User= 'User-defined header length'
    FileName= 'FileName'
    Creation = 'Creation Date'
    Creator= 'Creator'
    Project= 'Project'
    Right = 'Right to use or copyright statement'
    Encryption = 'Encryption key'
    Reserved = 'Reserved for future use'
    Image = 'Image orientation'
    Number = 'Number of image elements'
    Pixels = 'Pixels per line'
    Lines = 'Lines per image element'
    Data_sign = 'Data sign'
    Reference_low_data  = 'Reference low data code value'
    Reference_low_quantity = 'Reference low quantity represented'
    Reference_high_data = 'Reference high data code value'
    Reference_high_quantity = 'Reference high quantity represented'
    Descriptor = 'Descriptor'
    Transfer = 'Transfer characteristic'
    Colorimetric = 'Colorimetric specification'
    Bit = 'Bit depth'
    Packing= 'Packing'
    Encoding= 'Encoding'
    Offset2data = 'Offset to data'
    eol_padding= 'End-of-line padding'
    End_of_image_padding = 'End-of-image padding'
    Description = 'Description of image element'
    Padding= 'Padding'
    Reserved4future = 'Reserved for future use'
    X_Offset = 'X Offset'
    Y_Offset = 'Y Offset'
    X_center = 'X center'
    Y_center = 'Y center'
    X_original_size = 'X original size'
    Y_original_size = 'Y original size'
    Source_image_filename = 'Source image filename'
    Source_image_datetime = 'Source image date/time'
    Input_dev_name = 'Input device name'
    Input_dev_serial = 'Input device serial number'
    XL_border = 'XL border'
    XR_border = 'XR border'
    YT_border = 'YT border'
    YB_border = 'YB border'
    Pixel_ratio_hor = 'Pixel ratio : horizontal'
    Pixel_ratio_ver = 'Pixel ratio : vertical'
    X_scanned_size = 'X scanned size'
    Y_scanned_size = 'Y scanned size'

    Film_mfg_ID_code = 'Film mfg. ID code'
    Film_type = 'Film type'
    Offset_pefs = 'Offset in perfs'
    Prefix= 'Prefix'
    Count= 'Count'
    Format = 'Format - e.g. Academy'
    Frame = 'Frame position in sequence'
    Sequence = 'Sequence length (frames)'
    Held = 'Held count (1 = default)'
    Frame_rate_orig = 'Frame rate of original (frames/s)'
    Shutter = 'Shutter angle of camera in degrees'
    Frame_id = 'Frame identification - e.g. keyframe'
    Slate = 'Slate information'
    # Reserved = 'Reserved for future use'
    SMPTE_timecode = 'SMPTE time code'
    SMPTE_userbits = 'SMPTE user bits'
    Interlace= 'Interlace'
    Field = 'Field number'
    Video = 'Video signal standard'
    Zero= 'Zero'
    Horizontal = 'Horizontal sampling rate (Hz)'
    Vertical = 'Vertical sampling rate (Hz)'
    Temporal = 'Temporal sampling rate or frame rate (Hz)'
    Time = 'Time offset from sync to first pixel (ms)'
    Gamma= 'Gamma'
    Black_level_code = 'Black level code value'
    Black_gain = 'Black gain'
    Breakpoint = 'Breakpoint'
    Reference_white_level = 'Reference white level code value'
    Integration_time = 'Integration time (s)'
    # Reserved = 'Reserved for future use'
    Data = 'Data'

def write_field(data, field_name, file_name):
    with open(file_name, 'r+b') as file:
        start, end = get_offsets(DPX_LOOKUP, field_name)
        print(start)
        file.seek(start)
        file.write(bytes(data, encoding="ASCII"))

def main():
    csv_file = "dpx_data.csv"

    with open(csv_file) as data_file:
        reader = csv.DictReader(data_file)
        for record in reader:
            for f in os.listdir("."):
                workingFile = os.path.basename(record['RealFileName'])
                if f == workingFile:
                    write_field(record['Creator'], 'Creator', workingFile)
            pass


if __name__ == '__main__':
    main()