

from datetime import datetime
import pandas
import random
import smtplib, ssl

MY_EMAIL = "bonny.ross1122@gmail.com"
MY_PASSWORD = "I)f8*XBN5RQ$#O"
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

today = datetime.now()
today_tuple = (today.month, today.day) # this tuple checks if its the birth date of a loved one

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#print(birthdays_dict)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    context = ssl.create_default_context()
    message = f"Subject:Happy Birthday!\n\n{contents}"
    receiver_email = birthday_person["email"]

    print(receiver_email)


    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(MY_EMAIL, MY_PASSWORD)
        server.sendmail(MY_EMAIL, receiver_email, message)

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=birthday_person["email"],
    #         msg=f"Subject:Happy Birthday!\n\n{contents}"

    #  )
