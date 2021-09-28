# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# sample output:9
import datetime
from datetime import date

date_1 = date(2014, 7, 2)
date_2 = date(2014, 7, 11)

diff_date = date_2 - date_1
print(diff_date.days)
