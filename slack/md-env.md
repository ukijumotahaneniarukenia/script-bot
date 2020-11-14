slack

web hook url取得
https://slack.com/services/new/incoming-webhook

- 通知対象のチャネル選択で「Incoming Webhookインテグレーションの追加」ボタンを押下する

IN

```
{
  "channel": "#script-sketch-bot",
  "username": "ボットだよーん",
  "text": "<!channel>こんにちは。",
  "icon_emoji": ":shipit:"
}
```

CMD

```
$ curl -s -H 'Content-Type: application/json' -X POST My_Web_Hook_Url -d '@test.json' | awk 4
```

OUT

```
ok
```
