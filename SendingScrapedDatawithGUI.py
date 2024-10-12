import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scrape import create_custom_hn
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading

# Set up email parameters
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hackernewsupdates@gmail.com"  # Your address
password = "efroymraqfvkqtma"  # App Password

def send_email(receiver_email, progress):
    progress.start(10)  # Start loading bar

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
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            progress.stop()  # Stop loading bar
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        progress.stop()  # Stop loading bar
        messagebox.showerror("Error", f"Error: {e}")

def start_email_sending():
    receiver_email = email_entry.get()
    if receiver_email:
        progress_bar["value"] = 0
        threading.Thread(target=send_email, args=(receiver_email, progress_bar)).start()
    else:
        messagebox.showerror("Input Error", "Please enter a valid email address.")

# Set up GUI
root = tk.Tk()
root.title("Hacker News Email Notifier")
root.geometry("700x400")  # Set window size

# Set background color to dark forest green
root.configure(bg='#013220')

# Title label in green
title_label = tk.Label(root, text="Hacker News Notifier", font=("Helvetica", 24, "bold"), bg="#013220", fg="#A9DFBF")
title_label.pack(pady=20)

# Create email input field
input_frame = tk.Frame(root, bg="#013220")
input_frame.pack(pady=20)
email_label = tk.Label(input_frame, text="Enter your email address:", font=("Helvetica", 14), bg="#013220", fg="#A9DFBF")
email_label.grid(row=0, column=0, padx=10)
email_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 14))
email_entry.grid(row=0, column=1, padx=10)

# Create send button with green colors
send_button = tk.Button(root, text="Send Email", command=start_email_sending, font=("Helvetica", 14), bg="#145A32", fg="white", activebackground="#196F3D", padx=10, pady=5)
send_button.pack(pady=20)

# Create loading progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
progress_bar.pack(pady=30)

# Customize progress bar colors and height (dark forest green color #228B22)
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' for better theme customization
style.configure("TProgressbar", troughcolor='#0B3D0B', background='#145A32', thickness=40)  # Green shades

# Run the GUI
root.mainloop()
