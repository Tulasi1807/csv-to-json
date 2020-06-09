import csv,json

csvFilePath="drug200.csv"
jsonFilePath="drug200.json"
data={}
with open(csvFilePath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for csvRow in csvReader:
        age=csvRow['Age']
        data[age]=csvRow


with open('jsonFilePath','w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))