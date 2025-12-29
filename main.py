import smtplib,random
my_email = "your email e.g. asdf@xyz.com"
password = "your password"
receiver_email = "reciever email e.g. abc@xyz.com"
with open("quotes.txt") as quotes:
    quotes = quotes.readlines()
    random_quote = random.choice(quotes)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs=receiver_email,msg=f"subject:Morning Motivation\n\n{random_quote}")
