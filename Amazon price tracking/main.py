import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

URL_ENDPOINT = "https://appbrewery.github.io/instant_pot/"
SENDER_EMAIL = os.environ["SENDER_EMAIL_ID"]
SENDER_PASSWORD = os.environ["SENDER_PASSWORD"]
RECIVER_EMAIL = os.environ["RECIVER_EMAIL_ID"]
TARGET = 100

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

response = requests.get(url=URL_ENDPOINT,headers=header)
if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")
    price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
    title_tag  = soup.find(class_="po-break-word").getText().split()
    title = ' '.join(title_tag)
    if price < TARGET:
        subject = "AMAZON PRICE REDUCED"
        body = f"Now price of {title} went down ${price} \n BUY NOW"
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = RECIVER_EMAIL
        message['subject'] = subject
        message.attach(MIMEText(body,"plain"))
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECIVER_EMAIL,
                msg=message.as_string()
            )
            print('Email sent successfully')
else:
    print(f"Unable to fetech the Error {response.status_code}")    


      