# Self introducing Line bot of Han-Hsuan Lin
A Line bot server app deployed on Heroku, including basic replying, button menu, rich menu and self introducing cards.
## Requirements
- python 2.7
- flask 1.0.3
- gunicorn 19.9.0
- line-bot-sdk 1.9.0
## Usage
1. [Create a Line channel](https://developers.line.biz/en/docs/messaging-api/getting-started/)
2. Creating a bot and fill your **Channel Access Token** and **Channel Secret** in app.py just like below:
```
# Channel Access Token
line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
# Channel Secret
handler = WebhookHandler('CHANNEL_SECRET')
``` 
3. [Create a Heroku app](https://www.heroku.com)
4. Clone this repository and push to the Heroku app server
5. In the [Line bot console](https://developers.line.biz/console/register/messaging-api/provider/), enable webhook and fill this address in the blank of webhook url:
`https://{your_heroku_app_name}.herokuapp.com/callback`
6. Happy ever after
## Implementation
Here's my Line bot's QRcode, enjoy.


![Line Bot QRcode](https://i.imgur.com/BzbRjnt.png)
---
2019 Han-Hsuan Lin
National Chengchi University
