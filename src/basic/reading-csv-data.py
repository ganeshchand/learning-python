# To be able to read csv formated files, we will first have to import the
# csv module.
import csv
import os

csvFilePath = '/Users/ganeshchand/gh/gc/python/learning-python/src/pipeline/sales.csv'

# using csv.reader()
with open(csvFilePath, 'rb') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        print(row)

# using dictionary


with open(csvFilePath, 'rb') as f:
    csvDictReader = csv.DictReader(f, delimiter=',')
    for line in csvDictReader:
        if int(line["age"]) > 20:
            # print(line["id"]),
            # print(line["name"])
            print(line)

# write csv file
print("Writing a CSV File")

# examaples


with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# end of examples


# list of lists

inputData = ["id ,name,age,sex,city,state,zip".split(","),
             "100, John Smith, 32,M, Austin, TX, 78727".split(","),
             "200, Joe Johnson, 13, M, Dallas, TX, 75201".split(","),
             "300, Bob Jones, 14, M, Houston, TX, 77028".split(",")]


def writeCsvUsingCsvWriter(path, data):
    with open(path, 'wb') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        for list in data:
            writer.writerow(list)


def writeCsvUsingCsvDictWriter(path, data):
    my_list = []
    fieldNames = data[0]
    rows = data[1:]

    for row in rows:
        dictionary = dict(zip(fieldNames, row))
        my_list.append(dictionary)

    with open(path, 'wb') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()
        for row in my_list:
            writer.writerow(row)
            print(row)


writeCsvUsingCsvWriter("output/output-sales1.csv", inputData)
writeCsvUsingCsvDictWriter("output/output-sales2.csv", inputData)
