# mypkg
ros2用のリポジトリ

## インストール方法
* GitHubが利用できる環境で下記のコマンドを入力してください。

```
$ git clone git@github.com:takuto0523/mypkg.git
``` 

## 実行方法
* ubuntuを二つ立ち上げ、ros2_wsディレクトリに移動して以下のコマンドを入力してください。
```
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
```

## 実行結果
```
[INFO] [1704292442.305173496] [listener]: Listen: 3
[INFO] [1704292442.781006851] [listener]: Listen: 4
[INFO] [1704292443.281017780] [listener]: Listen: 5
[INFO] [1704292443.781585161] [listener]: Listen: 6
[INFO] [1704292444.281131184] [listener]: Listen: 7
[INFO] [1704292444.782535929] [listener]: Listen: 8
```

## 必要なソフトウェア
* Python
  * テスト済み: 3.7～3.10

## テスト環境
* Ubuntu 22.04.2 LST

## 著作権・ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードは、下の記スライド (CC-BY-SA 4.0 by Ryuichi Ueda) のものを、本人の許可を得て自身の著作としたものです。一部コードを改変しました。
  * [ryuichiueda/my_slides/robosys2022/](https://github.com/ryuichiueda/my_slides/tree/e62cce75befe2433a96c1e813bcc0eaa2941305b/robosys_2022)
* © 2023 Takuto Suzukawa
