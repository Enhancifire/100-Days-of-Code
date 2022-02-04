import pandas as pd
import datetime as dt, smtplib

EMAIL = "reaperfs144@gmail.com"
PSS = "7Pz4j56bGYWhsu"

bday = pd.read_csv("birthday.csv")

date = dt.datetime.now()
today = (date.date, date.month)
print(today)
