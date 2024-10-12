# Hacker News Email Notifier

This is a simple desktop application built using Python,Tkinter library, Beautiful Soup and SMTP Lib. The program allows users to receive the top 10 most popular Hacker News stories from the past 24 hours directly to their email inbox. The application features a graphical user interface (GUI) that prompts the user for an email address and sends the email with the curated content.

# Features

Simple GUI: Users can enter their email address through an easy-to-use graphical interface.

Top Hacker News Stories: Fetches the top 10 most popular stories from Hacker News, including the title, link, vote count, and comment count.

-> Uses Beautiful Soup to Parse through the first 10 pages of the HTML of the website, and get all the Stories's title, votes, number of comments, and link with over 100 votes.

-> Filters them all so it only includes the posts within 24 hours, then sorts it by aggregate (votes plus comments), So we have the top 10 most popular stories.

Email Notification: Sends an email with the top stories formatted in plain text directly to the specified email address.

# Future Plans

I tried using PythonAnywhere so the python script could run 24/7, so it send you an email every single day on the most popular stories, However PythonAnywhere doesnt allow https requests besdies the allowed websites for the free tier.

I also tried deplying the project on heroku, so it could run on a cloud but that also didn't work as I would need to pay for a subscription.

So unfortunately I have to stick to code that you have to run on your computer, and enter your email and it will give you the top stories on hackernews!

![image](https://github.com/user-attachments/assets/62902e64-e6ed-4b07-8065-b3b202839567)

# Instructions

1. Download scrape.py and SendingScrapedDatawithGUI.py

2. Run SendingScrapedDatawithGUI.py on any code editor or console.

3. Enter your email, and you will recieve an email of the top Stories in the past 24 hours!
