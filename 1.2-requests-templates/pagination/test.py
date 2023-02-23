import csv

with open('/Users/antonarambillet/Desktop/Django/Echeverria_Anton_DJ-66/1.2-requests-templates/pagination/data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        new_reader = [row for row in reader]
        #print(new_reader.Name)
        for row in new_reader:
            print(row.Name)