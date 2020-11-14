telegram

telegram install

- https://telegram.org/

```
$ cd /usr/local/src

$ tar xvf tsetup.2.4.7.tar.xz

起動
$ /usr/local/src/Telegram/Telegram
```

デスクトップアプリを起動して左上の検索欄に「@BotFather」を入力し、BOT登録を進める
やり取りをやり直したかったら、「Delete Chat」をクリックする

私

```
/start
```

BotFather
```
I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual (https://core.telegram.org/bots).

You can control me by sending these commands:

/newbot - create a new bot
/mybots - edit your bots [beta]

Edit Bots
/setname - change a bot's name
/setdescription - change bot description
/setabouttext - change bot about info
/setuserpic - change bot profile photo
/setcommands - change the list of commands
/deletebot - delete a bot

Bot Settings
/token - generate authorization token
/revoke - revoke bot access token
/setinline - toggle inline mode (https://core.telegram.org/bots/inline)
/setinlinegeo - toggle inline location requests (https://core.telegram.org/bots/inline#location-based-results)
/setinlinefeedback - change inline feedback (https://core.telegram.org/bots/inline#collecting-feedback) settings
/setjoingroups - can your bot be added to groups?
/setprivacy - toggle privacy mode (https://core.telegram.org/bots#privacy-mode) in groups

Games
/mygames - edit your games (https://core.telegram.org/bots/games) [beta]
/newgame - create a new game (https://core.telegram.org/bots/games)
/listgames - get a list of your games
/editgame - edit a game
/deletegame - delete an existing game
```

私
```
/newbot
```

BotFather
```
Alright, a new bot. How are we going to call it? Please choose a name for your bot.
```

私
```
aine
```

BotFather
```
Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.
```

私

ハイフンだめなようだった
```
script-sketch-bot
```

BotFathter

```
Sorry, this username is invalid.
```

私

```
script_sketch_bot
```


BotFathter

BOT_URLとAPI_TOKENを教えてくれるので、控える

```
Done! Congratulations on your new bot.

https://core.telegram.org/bots/api
```

リクエストを作る

- https://core.telegram.org/bots/api#making-requests

```
https://api.telegram.org/bot$API_TOKEN/METHOD_NAME
```


CMD

```
$ curl -s -H 'Content-Type: application/json' -X GET 'https://api.telegram.org/bot$API_TOKEN/getMe' | jq
```

OUT

```
{
  "ok": true,
  "result": {
    "id": 1428447873,
    "is_bot": true,
    "first_name": "aine",
    "username": "script_sketch_bot",
    "can_join_groups": true,
    "can_read_all_group_messages": false,
    "supports_inline_queries": false
  }
}
```

利用可能なメソッド名など

- https://core.telegram.org/bots/api#available-methods

自分のユーザーIDを取得する


デスクトップアプリを起動して左上の検索欄に「@userinfobot」を入力し、ユーザー情報の確認を進める

私
```
/start
```

userinfobot
```
Id: 0123456789
First: うんこ
Last: もりこ
```

aineボットから私へテキストメッセージ送信


IN
```
$ cat postData.json
{
  "chat_id": 0123456789,
  "text": "すもももももももものうち"
}
```

CMD

```
$ curl -s -H 'Content-Type: application/json' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendMessage' -d '@postData.json' | jq
```

OUT
```
{
  "ok": true,
  "result": {
    "message_id": 2,
    "from": {
      "id": 9876543210,
      "is_bot": true,
      "first_name": "aine",
      "username": "script_sketch_bot"
    },
    "chat": {
      "id": 0123456789,
      "first_name": "うんこ",
      "last_name": "もりこ",
      "type": "private"
    },
    "date": 1605335738,
    "text": "すもももももももものうち"
  }
}
```
