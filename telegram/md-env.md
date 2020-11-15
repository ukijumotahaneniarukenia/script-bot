telegram

botの各種言語実装へのリンク

- https://core.telegram.org/bots/samples

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

aineボットから私へPhoto送信

- https://core.telegram.org/bots/api#sendphoto

CMD

サイズに比例してラグある

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendPhoto' -F "chat_id=0123456789" -F "photo=@$HOME/script-bot/test.png"|jq
```

OUT

```
{
  "ok": true,
  "result": {
    "message_id": 13,
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
    "date": 1605406025,
    "photo": [
      {
        "file_id": "AgACAgUAAxkDAAMNX7CNSQdMv7c6nH-mlcduyXEgrMoAAiirMRuz4IBVhkx4NXbUX9YcwI5sdAADAQADAgADbQADnSAEAAEeBA",
        "file_unique_id": "AQADHMCObHQAA50gBAAB",
        "file_size": 28018,
        "width": 266,
        "height": 320
      },
      {
        "file_id": "AgACAgUAAxkDAAMNX7CNSQdMv7c6nH-mlcduyXEgrMoAAiirMRuz4IBVhkx4NXbUX9YcwI5sdAADAQADAgADeAADniAEAAEeBA",
        "file_unique_id": "AQADHMCObHQAA54gBAAB",
        "file_size": 68114,
        "width": 457,
        "height": 550
      }
    ]
  }
}
```


aineボットから私へ音声ファイル送信

メタ情報あるので、ファイル名はスペース等含まれていないものに変換してから送信したほうがよい

- https://core.telegram.org/bots/api#sendaudio

CMD

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendAudio' -F "chat_id=0123456789" -F "photo=@$HOME/script-bot/test.mp3"|jq
```

OUT

```
{
  "ok": true,
  "result": {
    "message_id": 14,
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
    "date": 1605406603,
    "audio": {
      "duration": 300,
      "file_name": "test.mp3",
      "mime_type": "audio/mpeg",
      "title": "High Hopes",
      "performer": "Love, Rosie",
      "file_id": "CQACAgUAAxkDAAMOX7CPiwiidp0DaLPo2ovR9lsvfgQAAg0CAAKz4IBVPZP67A9DT48eBA",
      "file_unique_id": "AgADDQIAArPggFU",
      "file_size": 7207334
    }
  }
}
```


aineボットから私へ動画ファイル送信

メタ情報あるので、ファイル名はスペース等含まれていないものに変換してから送信したほうがよい


- https://core.telegram.org/bots/api#sendvideo

CMD

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendVideo' -F "chat_id=0123456789" -F "video=@$HOME/script-bot/test.mp4"|jq
```

OUT

```
{
  "ok": true,
  "result": {
    "message_id": 15,
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
    "date": 1605407038,
    "video": {
      "duration": 39,
      "width": 1910,
      "height": 1006,
      "file_name": "test.mp4",
      "mime_type": "video/mp4",
      "thumb": {
        "file_id": "AAMCBQADGQMAAw9fsJE9df6pWChlBWS_bzrZKCloawACDgIAArPggFVFkFGWJ7pCKrAOUm10AAMBAAdtAAOaOQACHgQ",
        "file_unique_id": "AQADsA5SbXQAA5o5AAI",
        "file_size": 1117,
        "width": 320,
        "height": 169
      },
      "file_id": "BAACAgUAAxkDAAMPX7CRPXX-qVgoZQVkv2862SgpaGsAAg4CAAKz4IBVRZBRlie6QioeBA",
      "file_unique_id": "AgADDgIAArPggFU",
      "file_size": 1511572
    }
  }
}
```


aineボットから私へアニメーションファイル送信

- https://core.telegram.org/bots/api#sendanimation

CMD

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendAnimation' -F "chat_id=0123456789" -F "animation=@$HOME/script-bot/test.gif"|jq
```

OUT

アニメーションでもあり、ドキュメントでもある模様

```
{
  "ok": true,
  "result": {
    "message_id": 16,
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
    "date": 1605407440,
    "animation": {
      "file_name": "test.gif.mp4",
      "mime_type": "video/mp4",
      "duration": 5,
      "width": 320,
      "height": 170,
      "thumb": {
        "file_id": "AAMCBQADGQMAAxBfsJKPHEdnX8sUhOo-VyC6puX9wQACmQEAArPgiFW5XGP4nU7Xv36WtW50AAMBAAdtAAOgEgACHgQ",
        "file_unique_id": "AQADfpa1bnQAA6ASAAI",
        "file_size": 8754,
        "width": 320,
        "height": 169
      },
      "file_id": "CgACAgUAAxkDAAMQX7CSjxxHZ1_LFITqPlcguqbl_cEAApkBAAKz4IhVuVxj-J1O178eBA",
      "file_unique_id": "AgADmQEAArPgiFU",
      "file_size": 57019
    },
    "document": {
      "file_name": "test.gif.mp4",
      "mime_type": "video/mp4",
      "thumb": {
        "file_id": "AAMCBQADGQMAAxBfsJKPHEdnX8sUhOo-VyC6puX9wQACmQEAArPgiFW5XGP4nU7Xv36WtW50AAMBAAdtAAOgEgACHgQ",
        "file_unique_id": "AQADfpa1bnQAA6ASAAI",
        "file_size": 8754,
        "width": 320,
        "height": 169
      },
      "file_id": "CgACAgUAAxkDAAMQX7CSjxxHZ1_LFITqPlcguqbl_cEAApkBAAKz4IhVuVxj-J1O178eBA",
      "file_unique_id": "AgADmQEAArPgiFU",
      "file_size": 57019
    }
  }
}
```



aineボットから私へドキュメントファイル送信

- https://core.telegram.org/bots/api#senddocument

CMD

PDFファイルを送信してみる

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendDocument' -F "chat_id=0123456789" -F "document=@$HOME/script-bot/test.pdf"|jq
```

OUT

```
{
  "ok": true,
  "result": {
    "message_id": 17,
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
    "date": 1605407874,
    "document": {
      "file_name": "test.pdf",
      "mime_type": "application/pdf",
      "thumb": {
        "file_id": "AAMCBQADGQMAAxFfsJSCApDNJPk9fEIIM7L_i1DxgwACmgEAArPgiFW2h2cY1zJSqqFNTG50AAMBAAdtAAPXEAACHgQ",
        "file_unique_id": "AQADoU1MbnQAA9cQAAI",
        "file_size": 1371,
        "width": 226,
        "height": 320
      },
      "file_id": "BQACAgUAAxkDAAMRX7CUggKQzST5PXxCCDOy_4tQ8YMAApoBAAKz4IhVtodnGNcyUqoeBA",
      "file_unique_id": "AgADmgEAArPgiFU",
      "file_size": 10757
    }
  }
}
```

XLSXファイルを送信してみる

CMD

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendDocument' -F "chat_id=0123456789" -F "document=@$HOME/script-bot/test.xlsx"|jq
```

OUT

```
{
  "ok": true,
  "result": {
    "message_id": 19,
    "from": {
      "id": 1428447873,
      "is_bot": true,
      "first_name": "aine",
      "username": "script_sketch_bot"
    },
    "chat": {
      "id": 1190634294,
      "first_name": "Kota",
      "last_name": "Higashi",
      "type": "private"
    },
    "date": 1605408647,
    "document": {
      "file_name": "test.xlsx",
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "file_id": "BQACAgUAAxkDAAMTX7CXh-yC3HFuHu6eF0vW3aUs6HUAAqMBAAKz4IhVlEX7FMkx490eBA",
      "file_unique_id": "AgADowEAArPgiFU",
      "file_size": 23814
    }
  }
}
```



aineボットから私へ音声ファイル送信

oggファイルを送信してみる
音質いい

- https://core.telegram.org/bots/api#sendvoice

CMD

```
$ time curl -s -H 'Content-Type: multipart/form-data' -X POST 'https://api.telegram.org/bot$API_TOKEN/sendVoice' -F "chat_id=0123456789" -F "photo=@$HOME/script-bot/test.ogg"|jq
```

OUT

```
{
  "ok": true,
  "result": {
    "message_id": 18,
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
    "date": 1605408544,
    "voice": {
      "duration": 0,
      "mime_type": "audio/ogg",
      "file_id": "AwACAgUAAxkDAAMSX7CXH1HpF7Q_64WHOLFspfuvjHIAAqEBAAKz4IhV9WGKwfW_R3UeBA",
      "file_unique_id": "AgADoQEAArPgiFU",
      "file_size": 3627218
    }
  }
}
```
