import csv


# csvfile = 'dpx_offsets.csv'
# start_byte = reader

def get_offsets(csvfile, field):
    start_byte = None
    end_byte = None
    with open(csvfile, encoding="UTF-8") as datafile:
        # assert os.path.exists(csvfile)
        reader = csv.DictReader(datafile)
        foo = []
        try:
            for entry in reader:
                foo.append(entry)
        except:
            pass
            # print(entry)
        # print(csvfile)

        for entry in foo:
            if entry['title'] == field:
                start_byte = int(entry['startByte'])
                end_byte = int(entry['endByte'])
                # print("Found {}".format(field))
                break
    if start_byte is not None and end_byte is not None:
        # print(start_byte, end_byte)
        return int(start_byte), int(end_byte)
    else:
        raise Exception("Missing field \"{}\"".format(field))


# get_offsets("D:/sandbox/projects/python/dpx/DPXdpxDPX/dpx_offsets.csv", "Creator")
