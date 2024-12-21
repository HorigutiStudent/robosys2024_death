# robosys2024

# get_menues コマンド
![test](https://github.com/HorigutiStudent/robosys2024/actions/workflows/test.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) \
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat"> \
 今週の学食メニュー表を入手するコマンド.
## テスト済み環境
### Local
- Linux OS
    - Ubuntu 22.04
- Python
    - version:  3.10.12    
### GitHubActions
- Linux OS
    - Ubuntu 22.04
- Python 
    - version: 3.7 ~ 3.10
## Installation
```sh
#コマンドのダウンロード
git clone https://github.com/HorigutiStudent/robosys2024.git

#PIL(Pillow)のインストール
#apt でインストール(推奨)
apt install python3-pil python3-pil.imagetk

#pipでインストール(テスト済みでないため非推奨)
pip install Pillow
```
テストを実行したい場合は加えてインストール
```sh
apt install xvfb
```

## Usage
コマンドは次のように使用する.
```
cd robosys2024
echo "場所" | ./get_menues
```
"場所"には次の候補のうちいずれかを入力.
- sで始まり1で終わる -> 新習志野校舎1階のメニュー
- sで始まり2で終わる -> 新習志野校舎2階のメニュー
- tで始まる         -> 津田沼校舎のメニュー
#### Examples
```sh
#津田沼校舎のメニューを手に入れる
echo t | ./get_menues  #津田沼学食のメニューが表示される
```
![メニュー例](pictures/menue.jpg)
## LICENSE
このソフトウェアパッケージは，MITライセンスの下，再頒布および使用が許可される. \
各ファイルはファイル内に明記されているライセンスに従う. ライセンスが明記されていない場合は、MITライセンスに従う. ライセンスの全文は[LICENSE](https://github.com/HorigutiStudent/robosys2024?tab=MIT-1-ov-file)から確認できる.

## Copyright
© 2024 Horiguti Masahumi 