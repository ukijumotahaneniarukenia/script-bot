- https://chatbots.studio/blog/how-to-make-a-reddit-bot-with-python/

アプリ作成
- https://ssl.reddit.com/prefs/apps/

マニュアル

- https://github.com/reddit-archive/reddit/wiki/API



```
feedlyと同じ要領

WEB資産をサーブするアプリが起動しておく。nginxなど。

名前：test-reddit-api

ウェブアプリケーション

説明：テストダヨーン

リダイレクトURI：http://localhost:80/

「アプリを作成」ボタンを押下

開発したアプリ欄に追加したアプリが表示されていることを確認

クライアントID：HOGEHOGE

シークレット：TOGETOGE


- https://github.com/reddit-archive/reddit/wiki/OAuth2


- https://github.com/reddit-archive/reddit/wiki/OAuth2#authorization

以下のURLを作成

RANDOM_STRINGにはunko

ブラウザのアドレスバーないしはcurlでリクエスト

https://www.reddit.com/api/v1/authorize?client_id=HOGEHOGE&response_type=code&state=unko&redirect_uri=http://localhost:80/&duration=temporary&scope=identity+edit+flair+history+modconfig+modflair+modlog+modposts+modwiki+mysubreddits+privatemessages+read+report+save+submit+subscribe+vote+wikiedit+wikiread

許可するボタンを押下する

レスポンス

codeを控える

http://localhost/?state=unko&code=MYCODE

```
