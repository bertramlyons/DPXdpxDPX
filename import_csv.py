import csv

#csvfile = 'dpx_offsets.csv'
def get_offsets(csvfile, field):

	with open(csvfile) as datafile:
		reader = csv.DictReader(datafile)
		#return reader
		for entry in reader:
			if entry[title] == field:
				start_byte = entry['startByte']
				end_byte = entry['endByte']
				return(start_byte, end_byte)
		raise Exception("BAD BAD BAD")
		# start_byte = reader
		
