# !/usr/bin/env python
"""
PREREQUISITE
	Python 3.x - this script has been amended for Python 3.x (tested on 3.7) and only tested on unzipped csv files
SYNOPSIS
    To run script: python SCRIPT_NAME.py
DESCRIPTION
    This Python script can be used to seperate each Emergency Services Gazetteer 
    CSV file into new CSV files based on the record identifiers found 
    within Emergency Services Gazetteer. The script will read both Emergency Services Gazetteer 
    CSV files and zipped CSV files. If you have zipped files it is unneccessary
    to extract the zip file first as the script reads data directly from the zip
    file.
LICENSE
    Crown Copyright (c) 2020 Ordnance Survey
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
    IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
    INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
    BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
    OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
    OF THE POSSIBILITY OF SUCH DAMAGE
VERSION
    0.2
"""


# Imported modules
import zipfile
import csv
import sys
import os
from io import StringIO
import time
from time import strftime

# Header lines for the new CSV files these are used later to when writing the header to the new CSV files
headings10=["RECORD_IDENTIFIER","CUSTODIAN_NAME","LOCAL_CUSTODIAN_NAME","PROCESS_DATE","VOLUME_NUMBER","ENTRY_DATE","TIME_STAMP","VERSION","FILE_TYPE"]
headings21=["RECORD_IDENTIFIER","CHANGE_TYPE","PRO_ORDER","UPRN","LOGICAL_STATUS","BLPU_STATE","BLPU_STATE_DATE","PARENT_UPRN","X_COORDINATE","Y_COORDINATE","LATITUDE","LONGITUDE","RPC","LOCAL_CUSTODIAN_CODE","COUNTRY","START_DATE","END_DATE","LAST_UPDATE_DATE","ENTRY_DATE","ADDRESSBASE_POSTAL","POSTCODE_LOCATOR","MULTI_OCC_COUNT"]
headings24=["RECORD_IDENTIFIER","CHANGE_TYPE","PRO_ORDER","UPRN","LPI_KEY","LANGUAGE","LOGICAL_STATUS","START_DATE","END_DATE","LAST_UPDATE_DATE","ENTRY_DATE","SAO_START_NUMBER","SAO_START_SUFFIX","SAO_END_NUMBER","SAO_END_SUFFIX","SAO_TEXT","PAO_START_NUMBER","PAO_START_SUFFIX","PAO_END_NUMBER","PAO_END_SUFFIX","PAO_TEXT","USRN","USRN_MATCH_INDICATOR","AREA_NAME","LEVEL","OFFICIAL_FLAG"]
headings32=["RECORD_IDENTIFIER","CHANGE_TYPE","PRO_ORDER","UPRN","CLASS_KEY","CLASSIFICATION_CODE","CLASS_SCHEME","SCHEME_VERSION","START_DATE","END_DATE","LAST_UPDATE_DATE","ENTRY_DATE"]
headings99=["RECORD_IDENTIFIER","NEXT_VOLUME_NUMBER","RECORD_COUNT","ENTRY_DATE","TIME_STAMP"]


def createCSV():
	print('This program will split OS Emergency Services Gazetteer Zip CSV or extracted CSV files by record identifier into new CSV files')
	starttime = time.time()
	# Rather than using arguments the program asks the user to input the path to the folder of OS Emergency Services Gazetteer files
	# print('Please type in the full path to the directory of OS AddressBase zip files:')
	# directorypath = raw_input('Directory Path: ')
	directorypath = os.getcwd()
	# An emtpy array and counter used to store and count the number of CSV files the program finds
	csvfileList = []
	csvfileCount = 0
	# An emtpy array and counter used to store and count the number of Zip files the program finds
	zipfileList = []
	zipfileCount = 0
	# The following code walks the directory path that the user input earlier and searches for either CSV files or Zip files
	# It will initially see if AddressBasePremium is in the filename if not it will then check the first value of the file against
	# the record types above. Obviously is there is a CSV in the folder that has one of these record types as a first value
	# it will also be included.
	for dirname, dirnames, filenames in os.walk(directorypath):
		for filename in filenames:
			if filename.endswith(".csv"):
				csvfile = os.path.join(directorypath, filename)
				csvfileList.append(csvfile)
				csvfileCount += 1
			elif filename.endswith(".zip"):
				zippath = os.path.join(directorypath, filename)
				zipfileList.append(zippath)
				zipfileCount += 1
			else:
				pass
	# The following section makes sure that it is dealing with the correct files, either CSV or Zip but not both types
	try:
		if csvfileCount > 0 and zipfileCount > 0:
			print("Program has found both OS Emergency Services Gazetteer CSV  and ZIP files.")
			print("Please tidy up the folder of files and try again")
			time.sleep(5)
			sys.exit()
		else:
			pass
		if csvfileCount > 0:
			print("Program has found %s OS Emergency Services Gazetteer CSV Files" % csvfileCount)
		else:
			pass
		if zipfileCount > 0:
			print("Program has found %s OS Emergency Services Gazetteer Zipped CSV Files" % zipfileCount)
		else:
			pass

		if csvfileCount == 0 and zipfileCount == 0:
			print("Program could not find any OS Emergency Services Gazetteer files and will now exit")
			time.sleep(5)
			sys.exit()
	finally:
		pass

	# Create the ID10_Header_Records.csv file, it checks to see if it exists first, if so deletes it, then creates a fresh one
	if os.path.isfile('ID10_Header_Records.csv'):
		os.remove('ID10_Header_Records.csv')
		header_10 = open('ID10_Header_Records.csv', 'a', encoding='utf-8')
		write10 = csv.writer(header_10, delimiter=',', quotechar='"', lineterminator='\n')
		#print(os.path)
		write10.writerow(headings10)
	else:
		header_10 = open('ID10_Header_Records.csv', 'a', encoding='utf-8')
		write10 = csv.writer(header_10, delimiter=',', quotechar='"', lineterminator='\n')
		write10.writerow(headings10)
	
	# Create the ID21_BLPU_Records.csv file, it checks to see if it exists first, if so deletes it, then creates a fresh one
	if os.path.isfile('ID21_BLPU_Records.csv'):
		os.remove('ID21_BLPU_Records.csv')
		blpu_21 = open('ID21_BLPU_Records.csv', 'a', encoding='utf-8')
		write21 = csv.writer(blpu_21, delimiter=',', quotechar='"', lineterminator='\n')
		write21.writerow(headings21)
	else:
		blpu_21 = open('ID21_BLPU_Records.csv', 'a', encoding='utf-8')
		write21 = csv.writer(blpu_21, delimiter=',', quotechar='"', lineterminator='\n')
		write21.writerow(headings21)
	# Create the ID24_LPI_Records.csv file, it checks to see if it exists first, if so deletes it, then creates a fresh one
	if os.path.isfile('ID24_LPI_Records.csv'):
		os.remove('ID24_LPI_Records.csv')
		lpi_24 = open('ID24_LPI_Records.csv', 'a', encoding='utf-8')
		write24 = csv.writer(lpi_24, delimiter=',', quotechar='"', lineterminator='\n')
		write24.writerow(headings24)
	else:
		lpi_24 = open('ID24_LPI_Records.csv', 'a', encoding='utf-8')
		write24 = csv.writer(lpi_24, delimiter=',', quotechar='"', lineterminator='\n')
		write24.writerow(headings24)
	# Create the ID32_Class_Records.csv file, it checks to see if it exists first, if so deletes it, then creates a fresh one
	if os.path.isfile('ID32_Class_Records.csv'):
		os.remove('ID32_Class_Records.csv')
		class_32 = open('ID32_Class_Records.csv', 'a', encoding='utf-8')
		write32 = csv.writer(class_32, delimiter=',', quotechar='"', lineterminator='\n')
		write32.writerow(headings32)
	else:
		class_32 = open('ID32_Class_Records.csv', 'a', encoding='utf-8')
		write32 = csv.writer(class_32, delimiter=',', quotechar='"', lineterminator='\n')
		write32.writerow(headings32)
	# Create the ID99_Trailer_Records.csv file, it checks to see if it exists first, if so deletes it, then creates a fresh one
	if os.path.isfile('ID99_Trailer_Records.csv'):
		os.remove('ID99_Trailer_Records.csv')
		trailer_99 = open('ID99_Trailer_Records.csv', 'a', encoding='utf-8')
		write99 = csv.writer(trailer_99, delimiter=',', quotechar='"', lineterminator='\n')
		write99.writerow(headings99)
	else:
		trailer_99 = open('ID99_Trailer_Records.csv', 'a', encoding='utf-8')
		write99 = csv.writer(trailer_99, delimiter=',', quotechar='"', lineterminator='\n')
		write99.writerow(headings99)
	print('Finished creating empty CSV files with Header line')
	# The following counters are used to keep track of how many records of each Record Identifier type are found
	counter10 = 0
	counter21 = 0
	counter24 = 0
	counter32 = 0
	counter99 = 0

	# Counter to keep track of the number of files processed
	processed = 0
	# There is a different routine for processing CSV files compared to ZIP files
	# This sections processes the CSV files using the Python CSV reader and write modules
	# It used the first value of the row to determine which CSV file that row should be written to.
	if csvfileCount > 0:
		print("Program will now split the OS Emergency Services Gazetteer files")
		for filepath in csvfileList:
			processed += 1
			print("Processing file number " + str(processed) + " out of " + str(csvfileCount))
			with open(filepath, encoding='utf-8') as f:
				csvreader = csv.reader(f, delimiter=',', doublequote=False, lineterminator='\n', quotechar='"', quoting=0, skipinitialspace=True)
				try:
					for row in csvreader:
						abtype = row[0]
						if "10" in abtype:
							write10.writerow(row)
							print(row)
							counter10 += 1
						elif "21" in abtype:
							write21.writerow(row)
							counter21 += 1
						elif "24" in abtype:
							write24.writerow(row)
							counter24 += 1
						elif "32" in abtype:
							write32.writerow(row)
							counter32 += 1
						elif "99" in abtype:
							write99.writerow(row)
							counter99 += 1
						else:
							pass
				except KeyError as e:
					pass
		header_10.close()
		blpu_21.close()
		lpi_24.close()
		class_32.close()
		trailer_99.close()

	else:
		pass
	# The following section processes the Zip files.
	# It uses the Python Zipfile module to read the data directly from the Zip file preventing the user having
	# to extract the files before splitting the data.
	if zipfileCount > 0:
		print("Program will now split the OS Emergency Services Gazetteer files")
		for filepath in zipfileList:
			processed += 1
			print("Processing file number " + str(processed) + " out of " + str(zipfileCount))
			basename = os.path.basename(filepath)
			shortzipfile = os.path.splitext(basename)[0]
			removecsvzip = shortzipfile[0:-4]
			zipcsv = '.'.join([shortzipfile, 'csv'])
			zipcsv2 =  '.'.join([removecsvzip, 'csv'])
			with open(filepath, 'rb') as zname:
				zfile = zipfile.ZipFile(zname)
				try:
					data = StringIO(zfile.read(zipcsv).decode('utf-8'))
					csvreader = csv.reader(data, delimiter=',', doublequote=False, lineterminator= '\n', quotechar= '"', quoting= 0, skipinitialspace=True)
					for row in csvreader:
						abtype = row[0]
						if "10" in abtype:
							write10.writerow(row)
							counter10 += 1
						elif "21" in abtype:
							write21.writerow(row)
							counter21 += 1
						elif "24" in abtype:
							write24.writerow(row)
							counter24 += 1
						elif "32" in abtype:
							write32.writerow(row)
							counter32 += 1
						elif "99" in abtype:
							write99.writerow(row)
							counter99 += 1
						else:
							pass

				except KeyError as e:
					data = StringIO(zfile.read(zipcsv2))
					csvreader = csv.reader(data, delimiter=',', doublequote=False, lineterminator= '\n', quotechar= '"', quoting= 0, skipinitialspace=True)
					for row in csvreader:
						abtype = row[0]
						if "10" in abtype:
							write10.writerow(row)
							counter10 += 1
						elif "21" in abtype:
							write21.writerow(row)
							counter21 += 1
						elif "24" in abtype:
							write24.writerow(row)
							counter24 += 1
						elif "32" in abtype:
							write32.writerow(row)
							counter32 += 1
						elif "99" in abtype:
							write99.writerow(row)
							counter99 += 1
						else:
							pass
				finally:
					pass
		header_10.close()
		blpu_21.close()
		lpi_24.close()
		class_32.close()
		trailer_99.close()

	endtime = time.time()
	elapsed = endtime - starttime
	# Summary statistics showing number of records and time taken
	print("Program has finished splitting the Emergency Services Gazetteer Files")
	print('Finished translating data at ', strftime("%a, %d %b %Y %H:%M:%S"))
	print('Elapsed time: ', round(elapsed/60,1), ' minutes')
	print("Number of Header Records: %s" % str(counter10))
	print("Number of BLPU Records: %s" % str(counter21))
	print("Number of LPI Records: %s" % str(counter24))
	print("Number of Classification Records: %s" % str(counter32))
	print("Number of Trailer Records: %s" % str(counter99))

	print("The program will close in 10 seconds")
	time.sleep(10)
	sys.exit()


def main():
	createCSV()


if __name__ == '__main__':
	main()
