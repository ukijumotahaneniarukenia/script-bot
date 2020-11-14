import requests
import json

web_hook_url = 'https://hooks.slack.com/services/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'
target_channel = '#script-sketch-bot'
notify_user_name = 'ボットだよーん'
icon_emoji = ':shipit:'

message = {
    'channel': target_channel,
    'username': notify_user_name,
    'text': '<!channel>こんにちは。pythonプログラムから実行。',
    'icon_emoji': icon_emoji
}

requests.post(url=web_hook_url,data=json.dumps(message))

# 最近は「slackweb」パッケージがあるらしくハンディになっているぽいなど。
# https://qiita.com/shtnkgm/items/4f0e4dcbb9eb52fdf316
