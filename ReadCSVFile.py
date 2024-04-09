import csv #
with open('OSS.csv', 'r') as csv_file:#open the file
   f=csv.reader(csv_file) #read the file
   for fi in f: #print the file
        print(fi) #print each rows