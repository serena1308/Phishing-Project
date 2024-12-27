# Phishing project

## Introduction

For this phishing project, the aim is to create a web page resembling an authentic page (like a login form) and use tools like Webhook and Ngrok to retrieve the information sent by the user (username, password).
Bob has a dog (a bull terrier) named “Shimi”. Bob really loves his dog.
Alice has a passion for mechanics. She owns two vintage cars and often likes to parade around with her ancestral objects.
Your mission is to get the password from Alice or Bob.

Here are the steps to complete this project:

### 1. Reproduce the web page

Below you'll find the web page that looks like a typical authentication (example: login form with username and password fields) in HTML and CSS. Here is the page:

### 2. Configuring a web server with a webhook

For this step, we need a local server to process the data submitted to this form. I used Flask (Python Framework) to create this server and receive the information sent via the form. Here's the python code:

### 3. Use Ngrok to expose your local server
Ngrok makes your local server accessible over the Internet. Install Ngrok and run it with the following command after starting your Flask server:

`ngrok http 5000`

Ngrok will provide you with a public URL (e.g. https://xxxxxx.ngrok.io). You can use this URL to test your webhook with your login form.

### 4. Webhook (optionel)

If you want to retrieve information submitted on a third-party service (for example, a webhook on Discord), you can set up a webhook to receive this information. Use a service like Webhook.site to capture data sent via your form.