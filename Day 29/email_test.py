import smtplib
import time
import secrets, string

N = 20
email = "reaperfs144@gmail.com"
password = "7Pz4j56bGYWhsu"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user= email, password=password)

for _ in range(26):
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                                  for i in range(N))
    message = str(res)
    connection.sendmail(from_addr=email, to_addrs="atulpatil.email@gmail.com", msg=res)
    time.sleep(3)

connection.close()
