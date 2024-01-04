# mypkg
ros2用のリポジトリ

## 機能
数字をカウントしてトピック/countupを通じて送信します。
2つのノード間でトピック通信を行います。
メッセージの型は16ビット符号つき整数

* ノード
  * talker
    * 数字をカウントし、その数値をトピックに対して送信します。

  * listener
    * トピックを通じて受信したメッセージを表示します。

* トピック/countup
    * talkerからのメッセージをlistenerに送信します。

## インストール方法
* GitHubが利用できる環境で下記のコマンドを入力してください。

```
$ git clone git@github.com:takuto0523/mypkg.git
``` 

## 実行方法
* talkerとlistenerを別々に立ち上げる方法
  * ubuntuを二つ立ち上げ、ros2_wsディレクトリに移動して以下のコマンドを入力してください。
```
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
```
* launchファイルを使って、talkerとlistenerを同時に立ち上げる方法
  * ros2_wsディレクトリに移動して以下のコマンドを入力してください。
```
$ ros2 launch mypkg talk_listen.launch.py
```

## 実行結果
* talkerとlistenerを別々で実行した場合の結果
```
[INFO] [1704292442.305173496] [listener]: Listen: 3
[INFO] [1704292442.781006851] [listener]: Listen: 4
[INFO] [1704292443.281017780] [listener]: Listen: 5
[INFO] [1704292443.781585161] [listener]: Listen: 6
[INFO] [1704292444.281131184] [listener]: Listen: 7
[INFO] [1704292444.782535929] [listener]: Listen: 8
...
```
* launchファイルを使った場合の結果
```
[listener-2] [INFO] [1704388200.358093534] [listener]: Listen: 0
[listener-2] [INFO] [1704388200.850681227] [listener]: Listen: 1
[listener-2] [INFO] [1704388201.350803707] [listener]: Listen: 2
[listener-2] [INFO] [1704388201.850911960] [listener]: Listen: 3
[listener-2] [INFO] [1704388202.350392181] [listener]: Listen: 4
[listener-2] [INFO] [1704388202.850845868] [listener]: Listen: 5
...
```

## 必要なソフトウェア
* Python
  * テスト済み: 3.7～3.10

## テスト環境
* Ubuntu 22.04.2 LST
* Ros2 Foxy

## 著作権・ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードは、下の記スライド (CC-BY-SA 4.0 by Ryuichi Ueda) のものを、本人の許可を得て自身の著作としたものです。一部コードを改変しました。
  * [ryuichiueda/my_slides/robosys2022/](https://github.com/ryuichiueda/my_slides/tree/e62cce75befe2433a96c1e813bcc0eaa2941305b/robosys_2022)
* © 2023 Takuto Suzukawa
