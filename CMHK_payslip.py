import os
import pandas as pd
import re
import tika
from tika import parser
from os import listdir
from os.path import isfile, join
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# set working directory
path = 'C:/Users/user/Jupyter Notebook/payslip'

try:
    os.chdir(path)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(path))

    
# get list of files
folderpath = r"C:\Users\user\Jupyter Notebook\payslip"
files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]

# change into array
import numpy as np
my_list = files
my_array = np.array(my_list)

# printing my_array to check
for i in my_array:
    new = i.partition('.')
    fname = new[0]
    print(fname)
    
# define method for decryption
def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

# create array for decrypted files
de_array = []

# create decrypted file for each pdf
for i in my_array:
    new = i.partition('.')
    fname = new[0]
    if __name__ == '__main__':
        filename = fname + '.pdf'
        de_fname = 'de_' + fname + '.pdf'
        decrypt_pdf(filename, de_fname, 'password')
        de_array.append(de_fname)

#initiate tika server
tika.initVM()

for f in de_array:
    raw = parser.from_file(f)
    raw_text = raw['content']
    # convert it to utf-8 
    raw_text = raw_text.encode('utf-8', errors='ignore').decode()    

    #get MPF Employer Mandatory Contribution
    result = re.search('\n(.*)MPF Employer Mandatory Contribution', raw_text) #Regex
    employerMPF = result.group(1)
    
    #get MPF Relevant Income
    result1 = re.search('\n(.*)MPF Relevant Income', raw_text) #Regex
    relevantIncome = result1.group(1)

    #get Total Amount of Received Salary
    result2 = re.search('Total Amount: (.*)\n', raw_text) #Regex
    totalAmt = result2.group(1)
    
    #get Month of Received Salary
    result3 = re.search('-(\w+)-202', raw_text) #Regex
    month = result3.group(1)
    
    #get Year of Received Salary
    result4 = re.search('-(\w+)\n', raw_text) #Regex
    year = result4.group(1)
    
    #create dataframe 
    tax = pd.DataFrame([[year, month, relevantIncome, employerMPF, totalAmt]], columns=['Year', 'Month', 'MPF Relevant Income', 'MPF Employer Mandatory Contribution', 'Total Amount Received'])
    
    # if file does not exist write header 
    if not os.path.isfile('tax.csv'):
        tax.to_csv('tax.csv', header='column_names', index=False)
    else: # else it exists so append without writing the header
        tax.to_csv('tax.csv', mode='a', header=False, index=False)
