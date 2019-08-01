# link-preview-bot

## What is this
This is a tiny Teleegram bot ([@linkpreviewbot](t.me/linkpreviewbot)) written in python that sends all links back to you that were found in your (think: forwarded) message.
This is useful you want to see the link preview or visit the instant view page but the original sender disabled the preview.
This happens often when subscribing to newsletter bots.

## How do I install it locally
Make sure you have Python 3.7 installed.
(You might want to use a virtual environment.)

`git clone git@github.com:KnorpelSenf/link-preview-bot.git`

`pip install -r requirements.txt`

## How do I deploy it on Google
The code acts as a Google Cloud Function.
1) Make sure you have a bot token from [@BotFather](t.me/botfather).
1) Create a project in the Google Cloud Console and create a Cloud Function for your bot.
1) Upload this source code using any of the four options.
1) Define "webhook" as the main function.
1) Store the bot token in an environment variable called `BOT_TOKEN`.
1) Remember to set the webhook at api.telegram.org to your Cloud Function's URL.

## I don't understand X
Sorry, I hacked this in (more or less) one afternoon.
Contact me on [Telegram](t.me/KnorpelSenf) if you cannot figure it out.
I know that there could be better docs.
