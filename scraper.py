#############################
# Scraper to parse registration calendars. 
# This scraper SHOULD be able to scrape any oakland 
# ice registration (including drop in).
#
# The data for the registration times and
# spots open is nested in html as-a-string
# inside a div.  its insane
#############################

from lxml import html
from datetime import datetime


with open('test_reg.html', 'r') as f:
    txt = f.read()
tree = html.fromstring(txt)

# Spot to start iterating.
# children are 5 rows (weeks) of <tr>
base_table = tree.find_class('rsContentTable')[0]
for week in base_table.getchildren():
    # week (obviously) has 7 (days) of <td>
    for day in week.getchildren():

        # day has 4 <div> children. first get the date.  EX:
        # {href="#2020-01-03" title="1/3/2020" class="rsDateHeader"}
        date_header = day.find_class('rsDateHeader')[0].attrib
        # strip/parse date string and cast datetime > date
        parsed_date = datetime.fromisoformat(
            date_header['href'].replace('#', '')
        ).date

        # holy shit the text is nested 9 tags deep and theres nested html
        # day.getchildren()[1].getchildren()[0].attrib['title'] has the html
        # if the tag with the time range has an image,  that is one of the key words
        # that image is not in the nested.
        # day.getchildren()[1].getchildren()[0]
        


# tree.find_class('rsContent rsMonthView')
# base_cal = tree.find_class('rsContent rsMonthView')[0]
# base_cal.getchildren()
# base_table = base_cal.getchildren()[0]
# base_table.getchildren()
# cal_data = base_table.getchildren()[1]
# cal_data.getchildren()

# def scrape_registration_calendar(html):
