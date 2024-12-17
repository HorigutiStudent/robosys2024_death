# robosys2024

# get_menue コマンド
![test](https://github.com/HorigutiStudent/robosys2024/actions/workflows/test.yml/badge.svg)

 今週の学食メニュー表を入手するコマンド.
## テスト済み環境
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
apt installl python3-pil python3-pil.imagetk

#pipでインストール(テスト済みでないため非推奨)
pip install PIL
```
テストを実行したい場合は加えてダウンロード
```sh
apt install xvfb
```

## Usage
コマンドは次のように使用する.
```
cd 
echo "場所" | ./get_menues
```
場所には次の候補のうちいずれかを入力.
- sで始まり1で終わる -> 新習志野校舎1階のメニュー
- sで始まり2で終わる -> 新習志野校舎2階のメニュー
- tで始まる         -> 津田沼公社のメニュー
#### Examples
```sh
#新習志野校舎1階のメニューを手に入れる
echo s1 | ./get_menues
#新習志野校舎2階のメニューを手に入れる
echo s2 | ./get_menues
#津田沼校舎のメニューを手に入れる
echo t | ./get_menues
```
  
## LICENSE
- このソフトウェアパッケージは，MITライセンスの下，再頒布および使用が許可されます．
- © 2024 Horiguti Masahumi
