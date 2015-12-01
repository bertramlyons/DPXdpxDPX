# DPXdpxDPX - Tools for editing DPX metadata

## How to Use

### Exporting DPX header information to CSV

A user can export all available DPX header information from a DPX image stack into a comma-separated values (CSV) file with `dpx2csv' using the following command:
 
 `./dpx2csv {directory of DPX image stack}`
 
Example: `./dpx2csv /Users/me/myDPXstack`

The resulting CSV file (dpx_data.csv) can be adjusted with the desired field information.

### Writing metadata fields back to DPX

Run `parser.py` and select the adjusted CSV file (dpx_data.csv):

`python3 parser.py`

When executed, the command line will produce the following reportage:

`Now Working on: /Users/me/myDPXstack/000001.dpx`

`Writing into field: Creator. 	"My name"`
`Writing into field: FileName.    "V:\\dpximagestack\000001.dpx"`
`Writing into field: Project. 	  "My project"

`X DPX files changed.`
`All done.`

Note that `parser.py` looks for DPX image stacks in the same folder as the associated CSVs (dpx_data.csv)

### Available ASCII DPX metadata fields

DPX files contain four sections of metadata (Metadata Types):

- Generic file information, image information, data format, and image origination information

- Image data

- Motion-picture and television industry-specific information

- User-defined information. The format of this section is not defined by the standard. 

DPXdpxDPX's `parser.py` script currently works with ASCII text-based fields only. Here are the available ASCII text-based fields within a DPX header:

**Metadata Type**|**Field**|**Data Type**
:-----:|:-----:|:-----:|:-----:
File information|Version number of header format (V1.0)|ASCII
File information|Image filename|ASCII
File information|Creation date/time: YYYY:MM:DD:HH:MM:SS:LTZ |ASCII 
File information|Creator|ASCII
File information|Project name|ASCII
File information|Right to use or copyright statement|ASCII
Image information|Description of image element 1|ASCII
Image orientation information|Source image filename|ASCII
Image orientation information|Source image date/time: YYYY:MM:DD:HH:MM:SS:LTZ |ASCII
Image orientation information|Input device name|ASCII
Image orientation information|Input device serial number|ASCII
Motion-picture film information|Film mfg. ID code (2 digits from film edge code)|ASCII
Motion-picture film information|Film type (2 digits from film edge code)|ASCII
Motion-picture film information|Offset in perfs (2 digits from film edge code)|ASCII
Motion-picture film information|Prefix (6 digits from film edge code)|ASCII
Motion-picture film information|Count (4 digits from film edge code)|ASCII
Motion-picture film information|Format -- e.g. Academy|ASCII
Motion-picture film information|Frame identification -- e.g. keyframe|ASCII
Motion-picture film information|Slate information|ASCII
User-defined data|User identification|ASCII

## Dependencies

MediaConch and XMLStarlet are dependencies for dpx2csv shell script.
Python 2.7+ for csv2dpx.

## To Do

Needs all the binary type values for each field. If you know these, please add them to the dpx_offsets.csv file. Use the following format listed the Python manual [link](https://docs.python.org/2/library/struct.html#format-characters)



