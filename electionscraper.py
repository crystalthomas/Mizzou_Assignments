import csv
import mechanize
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

output = open('electionresults.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

formcount =0
for frm in br.forms():
    if str(frm.attrs["id"])=="Form1":
        break
    formcount=formcount+1
br.select_form(nr=formcount)

control = br.form.find_control(id='MainContent_cboRaces')
control.value = ["460006719"]
br[control.name] = ["460006719"]
br.submit(nr=1)

# Submit the form
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")
main_table = soup.find('table',
    {'id' : "MainContent_dgrdCountyRaceResults"}
)

#other table = class="electtable" cellspacing="0" rules="all" border="1" id="MainContent_dgrdCountyRaceResults" style="border-collapse:collapse;"
for row in main_table.find_all('tr'):
    data_1 = [cell.text for cell in row.find_all('th')]
    writer.writerow(data_1)
    break

for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(data)