from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,
import os

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["Dymq73CEX4d2R4WVF3F5OC5gizR0hPwg1Xmhf8HJhgZB01RL7Be+ohvSiVmLZfCsp19nko2676ifgyx2uGdiUk2AZUyf1orLtak7zA4gM4WIkJx9CaUMyBax/A1fDDJM84UeSZiOu0zx7iZAvpTZ5wdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["2b624aef7b38470f6d4e5e8eb432eff3"]
line_bot_api = LineBotApi(Dymq73CEX4d2R4WVF3F5OC5gizR0hPwg1Xmhf8HJhgZB01RL7Be+ohvSiVmLZfCsp19nko2676ifgyx2uGdiUk2AZUyf1orLtak7zA4gM4WIkJx9CaUMyBax/A1fDDJM84UeSZiOu0zx7iZAvpTZ5wdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler(2b624aef7b38470f6d4e5e8eb432eff3)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)