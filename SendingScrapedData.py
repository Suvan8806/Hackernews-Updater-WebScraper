import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scrape import create_custom_hn
import schedule
import time

# Set up email parameters
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hackernewsupdates@gmail.com"  # Enter your address
receiver_email = input("Enter your email address: ") 
password = "efroymraqfvkqtma"  # App Password

def send_email():
    # Create the email message
    msg = MIMEMultipart()
    msg['Subject'] = "Top 10 Most Popular Topics in the past 24 hours from Hacker News"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Get the top stories
    top_stories = create_custom_hn()

    # Format the email body
    text = "Here are the top 10 stories:\n\n\n"
    for story in top_stories:
        text += f"{story['title']} \n ({story['link']}) - Votes: {story['votes']}, Comments: {story['comments']}\n\n"

    msg.attach(MIMEText(text, 'plain'))

    # Send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            print("Trying to login...")
            server.login(sender_email, password)
            print("Logged in successfully!")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

send_email()

# # Schedule the email to be sent every 24 hours
# schedule.every(24).hours.do(send_email)

# print("Email scheduler is running...")
# while True:
#     schedule.run_pending()
#     time.sleep(1)  # Sleep for a short period to prevent busy-waiting
