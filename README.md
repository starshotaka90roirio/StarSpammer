## StarSpammer
So i wanted to make a trolling tool (still discord related lol), also just trying out argparse and CLI's.

# Table of contents

1. Disclaimer
2. Description (but better)
3. Tutorial
4. Note

# Disclaimer

By using this tool, you acknowledge that YOU are using discord's API, and take the risks for potential bans (due to rate limiting).

# Description

StarSpammer is a trolling tool with a command-line interface used to spam discord webhooks. You can set the limit to how many messages you want, and the message content you want to send.

# Tutorial
## Command

`python main.py -wh WEBHOOK_URL -msgamt AMOUNT_OF_MESSAGES -cont MESSAGE_CONTENT`

## Tutorial

1. Run the command
2. Replace `WEBHOOK_URL` with the url of the webhook
3. Replace `AMOUNT_OF_MESSAGES` with the amount of messages (in integers, for infinite messages just type "inf")
4. Replace `MESSAGE CONTENT` with the content of the message (to use spaces type the message in qoutation marks, python main.py ... -cont "message content")
5. Click enter!
