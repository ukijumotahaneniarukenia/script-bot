- https://chatbots.studio/blog/how-to-make-a-reddit-bot-with-python/

アプリ作成
- https://ssl.reddit.com/prefs/apps/

マニュアル

- https://github.com/reddit-archive/reddit/wiki/API



```
feedlyと同じ要領

WEB資産をサーブするアプリが起動しておく。nginxなど。

名前：test-reddit-api

「スクリプト」ラジオボタンを選択

説明：テストダヨーン

リダイレクトURI：http://localhost:80/

「アプリを作成」ボタンを押下

開発したアプリ欄に追加したアプリが表示されていることを確認

クライアントID：QYQxdfHoG3zHaQ

シークレット： 6QQNN8P_aPYdIDLN7WPzB3atkxQwWQ


- https://github.com/reddit-archive/reddit/wiki/OAuth2


- https://github.com/reddit-archive/reddit/wiki/OAuth2#authorization

以下のURLを作成

RANDOM_STRINGにはunko

ブラウザのアドレスバーないしはcurlでリクエスト

https://www.reddit.com/api/v1/authorize?client_id=QYQxdfHoG3zHaQ&response_type=code&state=unko&redirect_uri=http://localhost:80/&duration=permanent&scope=identity+edit+flair+history+modconfig+modflair+modlog+modposts+modwiki+mysubreddits+privatemessages+read+report+save+submit+subscribe+vote+wikiedit+wikiread


レスポンス

codeを控える

http://localhost/?state=unko&code=w381epPkWDKs04ALPLbwqhS6Rtj7eQ


https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example

アクセストークン取得
$ curl -X POST -d 'grant_type=password&username=LOGIN_USER_NAME&password=LOGIN_PASSWORD' --user 'QYQxdfHoG3zHaQ:6QQNN8P_aPYdIDLN7WPzB3atkxQwWQ' https://www.reddit.com/api/v1/access_token
{"access_token": "ACCESS_TOKEN", "token_type": "bearer", "expires_in": 3600, "scope": "*"}


APIリクエスト
$ curl -s -H "Authorization: bearer ACCESS_TOKEN" -A "ChangeMeClient/0.1 by LOGIN_USER_NAME" https://oauth.reddit.com/api/v1/me


```

