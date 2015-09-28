import csv

#Keep file in the same folder with data
csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleanedme.csv', 'w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

#Same field names, holla
writer.writeheader()

for row in reader:

    #Capitalize everything.
    row['first_name'] = row['first_name'].upper()

    row['contrib_code'] = row['contrib_code'].upper()

    row['mid_init'] = row['mid_init'].upper()

    row['last_name'] = row['last_name'].upper()

    row['addr'] = row['addr'].upper()

    row['city'] = row['city'].upper()

    row['state'] = row['state'].upper()
    
 #Adding zeroes to the front of zip codes
    row['zip'] = row['zip'].zfill(5)

#Taking out non-breaking spaces
    row['city'] = row['city'].replace('&NBSP;', ' ')

#Taking out paltry contributions
    if int(row['amount']) >= 1000:
        writer.writerow(row)


