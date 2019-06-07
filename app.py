# -*- coding: utf-8 -*-

import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from me import Me

app = Flask(__name__)
hanhsuan = Me()

# Channel Access Token
line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
# Channel Secret
handler = WebhookHandler('CHANNEL_SECRET')


# 測試用首頁(GET)
@app.route('/', methods=['GET'])
def homepage():
    return 'Chat Bot Server Deployed!'


# 經歷
@app.route('/experience', methods=['GET'])
def experience_page():
    global hanhsuan
    return hanhsuan.map_keywords('經歷')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    signature = request.headers['X-Line-Signature']

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理加入好友
@handler.add(FollowEvent)
def follow_handler(event):
    try:
        profile = line_bot_api.get_profile(event.source.user_id)
    except LineBotApiError as e:
        print(str(e))
        return
    username = profile.display_name
    print('{} 加入好友'.format(username))
    text1 = username + '！歡迎使用林瀚軒的官方帳號，你可以點選下方的圖片選單來跟我互動喔'
    text2 = '之後如果有問題想問我，只要輸入「問問題」就可以開啟問題選單囉！'
    question_buttons_message = hanhsuan.render_ques_sheet(direct_call=True)
    line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=text1), question_buttons_message, TextSendMessage(text=text2)])


# 處理文字訊息
@handler.add(MessageEvent, message=TextMessage)
def message_handler(event):
    global hanhsuan
    in_message = event.message.text
    try:
        profile = line_bot_api.get_profile(event.source.user_id)
    except LineBotApiError as e:
        print(str(e))
        return
    print('{}: {}'.format(profile.display_name, in_message))
    if in_message in hanhsuan.keywords:
        render = hanhsuan.map_keywords(in_message)
    else:
        render = 'Oops！我聽不太懂' + event.message.text + '是什麼意思，你可以點選下方的圖片選單來跟我互動，或是輸入「問問題」來開啟問題選單喔！'
    if isinstance(render, FlexSendMessage) or isinstance(render, TemplateSendMessage):
        line_bot_api.reply_message(event.reply_token, render)
    else:
        if in_message == '你好':
            render = profile.display_name + render
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=render))


# 處理貼圖訊息
@handler.add(MessageEvent, message=StickerMessage)
def sticker_handler(event):
    message = TextSendMessage(text='這貼圖好可愛！我也傳一個，送給你')
    sticker_message = StickerSendMessage(
        package_id='11537',
        sticker_id='52002745'
        )
    line_bot_api.reply_message(event.reply_token, [message, sticker_message])


# 處理其他訊息
@handler.default()
def default_handler(event):
    if isinstance(event, UnfollowEvent):
        return
    message = TextSendMessage(text='Oops！我看不太懂這個，你可以點選下方的圖片選單來跟我互動，或是輸入「問問題」來開啟問題選單喔！')
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)