# Polars100本ノック

## はじめに

これはPolars 1.32.0の知識を網羅的に確認するための100問の演習です。

https://docs.pola.rs/

## 準備

`uv`をインストールしてください。

https://docs.astral.sh/uv/

リポジトリ一式をダウンロードして解凍してください。

```
curl -L -o study-polars2.zip https://github.com/SaitoTsutomu/study-polars2/archive/refs/heads/master.zip
unzip study-polars2.zip
cd study-polars2-master
```

## 演習開始

演習用のオリジナルファイルは、`nbs/study_polars2.ipynb`です。
次のコマンドを実行すると、このファイルを`work/study_polars2.ipynb`にコピーし、`work`ディレクトリでJupyterが起動します。

```
uv run study-polars2
```

※ `work/study_polars2.ipynb`が存在する場合はコピーしません。2回目以降は続きから学習できます。もし、新規に始めたい場合は、`uv run study-polars2 --new`としてください。

`study_polars2.ipynb`を開いて学習を始めてください。

### 手順

* 青いセルの説明を読む
* 白いセルに問題の解答を書く
* 黄色いセルを実行して確認する

セル内でしか使わない変数は、`_`で始まります。
