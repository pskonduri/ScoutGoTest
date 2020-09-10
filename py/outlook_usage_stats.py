import csv

def getDataFromDate(inputDate):
  tsv_file = open("input/outlook_usage.tsv")
  read_tsv = csv. reader(tsv_file, delimiter="|")
  list_from_csv = []
  for row in read_tsv:
     print (row);
     if (row[2:3] == [inputDate]):
        list_from_csv.append(row)
  tsv_file. close()

  return list_from_csv
  

# getDataFromDate('2020-09-09')
