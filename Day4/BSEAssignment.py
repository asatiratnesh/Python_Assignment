import xlwt
import requests
import logging
import sys
import json
import sqlite3
import SendMailModule

# import SendMailModule

authKey = 'jT9zkHRZvtsMHScikddQ'
lastDayValue = []
lossOrProfit = 0
baseFilteredData = []
data = []

workBookObj = xlwt.Workbook()
sheet = workBookObj.add_sheet('Sheet 1')
style = xlwt.XFStyle()
font = xlwt.Font()
font.bold = True
style.font = font

style2 = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['light_green']
style2.pattern = pattern

style3 = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
style3.pattern = pattern

sheet.write(0, 0, "Symbols", style=style)
sheet.write(0, 1, "Company Name", style=style)
sheet.write(0, 2, "Last Day close value", style=style)
sheet.write(0, 3, "Second Last Day Close value", style=style)
sheet.write(0, 4, "Profit/Loss", style=style)

count = 1
for csymoble in (open("Csymbole.csv", 'r')).readline().split(","):
    share_name = csymoble

    url = "https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}".format(share_name, authKey)

    response = requests.get(url)

    if response.status_code != 200:
        logging.error('Error: response type {}'.format(response))
        sys.exit(1)

    content = json.loads(response.content)

    for x in (content['dataset']['data'])[:2]:
        lastDayValue.append(x[4])

    lossOrProfit = lastDayValue[1] - lastDayValue[0]
    print lossOrProfit
    sheet.write(count, 0, csymoble)
    sheet.write(count, 1, content['dataset']['name'])
    sheet.write(count, 2, lastDayValue[0])
    sheet.write(count, 3, lastDayValue[1])
    if lossOrProfit > 0:
        sheet.write(count, 4, lossOrProfit, style=style2)
    else:
        sheet.write(count, 4, lossOrProfit, style=style3)

    count += 1

    dataTuple = (csymoble, content['dataset']['name'], lastDayValue[0], lastDayValue[1], lossOrProfit)

    data.append(dataTuple)
    del dataTuple
    del lastDayValue[:]

workBookObj.save('Sample.xls')

# inset data into database

with sqlite3.connect('BSEData') as db:
    cursor = db.cursor()
    try:
        cursor.execute('''CREATE TABLE BSEData (ID INT, NAME TEXT, closeVal1 real, closeVal2 real, profit_loss real)''')
    except Exception as E:
        print "Error: ", E

    cursor.executemany("INSERT INTO BSEData VALUES (?, ?, ?, ?, ?)", data)

    for row in cursor.execute("SELECT * FROM BSEData"):
        print row
# calling send module

# SendMailModule.sendMail()

