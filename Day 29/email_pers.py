import smtplib
import random

EMAIL = "reaperfs144@gmail.com"
PSSWORD = "7Pz4j56bGYWhsu"

try:
    file = open("quotes.txt", "r")
    quotes = file.readlines()
    msg = random.choice(quotes)
    print(msg)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PSSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="fsaiyad990@gmail.com",
            msg=msg,
            )

except TypeError as e:
    print(e)
