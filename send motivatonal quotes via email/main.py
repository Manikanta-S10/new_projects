import random
import datetime as dt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = 'your_EMAIL_ID'
my_password = 'PASSWORD'
To_EMAIL_ID = 'TO_ADDR_EMAIL_ID'

now = dt.datetime.now()
if now.weekday() == 0:  # Check if today is Monday (0 represents Monday)
    # Open the quotes.txt file with UTF-8 encoding
        with open('quotes.txt', encoding='utf-8') as file:
            all_quotes = file.readlines()
            current_quote = random.choice(all_quotes)
        
        print(current_quote)  # Print the selected quote for debugging purposes

        # Create the email with proper UTF-8 encoding using MIMEText
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = To_EMAIL_ID
        msg['Subject'] = 'Motivational Quotes'

        # Attach the quote as the body of the email with UTF-8 encoding
        body = f"Motivational Quote:\n\n{current_quote}"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Send the email using SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()  # Start TLS encryption
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=To_EMAIL_ID,
                msg=msg.as_string()  # Convert MIME message to string format for sending
            )

        print("Email sent successfully!")

        








