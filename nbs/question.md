# Polars 100+ノック 問題と解答

## 問題 1.1.1 Polarsのバージョン確認

Polarsのバージョンを、変数`ans`に代入してください。

```python
import polars as pl
```

### 解答 1.1.1

```python
ans = pl.__version__
```

## 問題 1.1.2 辞書からDataFrame

辞書からDataFrameを作成し、`df`に代入してください。

```python
import polars as pl

data = {
    'id': [0, 1, 2],
    'name': ["Alice", "Bob", "Carol"],
    'age': [20, 18, 32],
}
```

### 解答 1.1.2

```python
df = pl.DataFrame(data)
```

## 問題 1.1.3 CSV読込

CSVファイルを読み込んでDataFrameを作成し、`df_titanic`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
```

### 解答 1.1.3

```python
df_titanic = pl.read_csv(file)
```

## 問題 1.1.4 基本情報の確認

`df_titanic`の形状、要素ごとの型、全列名を、それぞれ変数`ans1`、`ans2`、`ans3`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.1.4

```python
ans1 = df_titanic.shape
ans2 = df_titanic.dtypes
ans3 = df_titanic.columns
```

## 問題 1.1.5 要約統計量

`df_titanic`の要約統計量を変数`df`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.1.5

```python
df = df_titanic.describe()
```

## 問題 1.1.6 Parquet形式で出力

`df_titanic`を`out_file`にParquet形式で出力してください。

```python
import polars as pl

in_file = "titanic_train.csv"
df_titanic = pl.read_csv(in_file)

out_file = "titanic.parquet"
```

### 解答 1.1.6

```python
df_titanic.write_parquet(out_file)
```

## 問題 1.1.7 Parquet形式で入力

`out_file`を読み込み、変数`df`に代入してください。

```python
import polars as pl

in_file = "titanic_train.csv"
df_titanic = pl.read_csv(in_file)
out_file = "titanic.parquet"
df_titanic.write_parquet(out_file)
```

### 解答 1.1.7

```python
df = pl.read_parquet(out_file)
```

## 問題 1.1.8 最初の5行

`df_titanic`の最初の5行を変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.1.8

```python
ans = df_titanic.head()
```

## 問題 1.1.9 最後の3行

`df_titanic`の最後の3行を変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.1.9

```python
ans = df_titanic.tail(3)
```

## 問題 1.1.10 ランダムに5行をサンプリング

`df_titanic`からランダムに5行をサンプリングし、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.1.10

```python
ans = df_titanic.sample(n=5)
```

## 問題 1.2.1 特定の列の選択

`df_titanic`の`Name`、`Age`、`Sex`列を選択し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.1

```python
ans = df_titanic.select(["Name", "Age", "Sex"])
```

## 問題 1.2.2 式 (Expression) 

`df_titanic`の`Name`、`Age`、`Sex`列を式 (Expression) を使って選択し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.2

```python
ans = df_titanic.select(pl.col("Name"), pl.col("Age"), pl.col("Sex"))
```

## 問題 1.2.3 データ型で選択

`df_titanic`のすべての数値型（整数と浮動小数点数）の列を選択し、変数`ans`に代入してください。

```python
import polars as pl
import polars.selectors as cs

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.3

```python
ans = df_titanic.select(cs.numeric())
```

## 問題 1.2.4 正規表現で列を選択

`df_titanic`の`P`で始まる列名を持つすべての列を選択し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.4

```python
ans = df_titanic.select(pl.col("^P.*$"))
```

## 問題 1.2.5 フィルタリング

`df_titanic`の30歳より年上の乗客を抽出し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.5

```python
ans = df_titanic.filter(pl.col("Age") > 30)
```

## 問題 1.2.6 ANDでフィルタリング

`df_titanic`の30歳より年上で、かつ女性の乗客を抽出し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.6

```python
ans = df_titanic.filter(
    (pl.col("Age") > 30) & (pl.col("Sex") == "female")
)
```

## 問題 1.2.7 ORでフィルタリング

`df_titanic`の10歳未満の子供、または60歳以上の高齢者を抽出し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.7

```python
ans = df_titanic.filter(
    (pl.col("Age") < 10) | (pl.col("Age") >= 60)
)
```

## 問題 1.2.8 is_inでフィルタリング

`df_titanic`の出港地(`Embarked`)が`C`(Cherbourg)または`Q`(Queenstown)の乗客を抽出し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.8

```python
ans = df_titanic.filter(pl.col("Embarked").is_in({"C", "Q"}))
```

## 問題 1.2.9 1つの列でソート

`df_titanic`を年齢(`Age`)の昇順でソートし、変数`ans`に代入してください。

* 引数`maintain_order=True`をつけること

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.9

```python
ans = df_titanic.sort("Age", maintain_order=True)
```

## 問題 1.2.10 複数列でソート

`df_titanic`を客室クラス(`Pclass`)の昇順、次に年齢(`Age`)の降順でソートし、変数`ans`に代入してください。

* 引数`maintain_order=True`をつけること

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 1.2.10

```python
ans = df_titanic.sort(
    ["Pclass", "Age"],
    descending=[False, True],
    maintain_order=True,
)
```

## 問題 2.1.1 列の追加

`df_titanic`の列`Age`を2倍にした列`Age2`を追加し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.1

```python
ans = df_titanic.with_columns(
    (pl.col("Age") * 2).alias("Age2")
)
```

## 問題 2.1.2 定数値の列を追加

`df_titanic`にすべての値が`Titanic`という文字列である列`Ship`を追加し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.2

```python
ans = df_titanic.with_columns(
    Ship=pl.lit("Titanic")
)
```

## 問題 2.1.3 複数列の追加

`df_titanic`に下記の2列を追加し、変数`ans`に代入してください。

* `FamilySize`: `SibSp + Parch + 1`
* `IsAlone`: `FamilySize == 1`

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.3

```python
ans = df_titanic.with_columns(
    FamilySize=pl.col("SibSp") + pl.col("Parch") + 1
).with_columns(
    IsAlone=pl.col("FamilySize") == 1
)
```

## 問題 2.1.4 列の変更

`df_titanic`を下記のように修正し、変数`ans`に代入してください。

* 列`Fare`の値をポンドから円に換算し、列名を`FareJPY`に変更する（1ポンド=150円と仮定）。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.4

```python
ans = df_titanic.with_columns(
    FareJPY=pl.col("Fare") * 150
).drop("Fare")
```

## 問題 2.1.5 型の変換

`df_titanic`の列`Pclass`を整数型から文字列型に変換し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.5

```python
ans = df_titanic.with_columns(
    pl.col("Pclass").cast(pl.String)
)
```

## 問題 2.1.6 欠損値

`df_titanic`の列Ageの欠損値を全体の平均年齢で埋めて、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.6

```python
ans = df_titanic.with_columns(
    pl.col("Age").fill_null(pl.col("Age").mean())
)
```

## 問題 2.1.7 行方向の計算

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列名を`MaxFamilyMember`とし、行ごとに「列`SibSp`と列`Parch`の最大値」の列を追加

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.7

```python
ans = df_titanic.with_columns(
    MaxFamilyMember=pl.max_horizontal(pl.col("SibSp"), pl.col("Parch"))
)
```

## 問題 2.1.8 列名の変更

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`PassengerId`の名前を`ID`に変更する
* 列`Pclass`の名前を`Class`に変更する

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.8

```python
ans = df_titanic.rename({"PassengerId": "ID", "Pclass": "Class"})
```

## 問題 2.1.9 全数値列の変更

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* すべての浮動小数点数型の列の値を小数点以下第一位で丸める

```python
import polars as pl
import polars.selectors as cs

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.1.9

```python
ans = df_titanic.with_columns(
    cs.float().round(1)
)
```

## 問題 2.1.10 列の並べ替え

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Survived`、列`Pclass`、列`Name`、列`Sex`、列`Age`の順に列を並べ替え、残りの列をその後ろに配置する

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)

cols = "Survived", "Pclass", "Name", "Sex", "Age"
```

### 解答 2.1.10

```python
ans = df_titanic.select(*cols, pl.exclude(cols))
```

## 問題 2.2.1 条件で列の追加

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Age`に基づいて、18歳未満なら`Child`、18歳以上なら`Adult`とする
  * 列名を`AgeGroup`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.2.1

```python
ans = df_titanic.with_columns(
    AgeGroup=pl.when(pl.col("Age") < 18)
    .then(pl.lit("Child"))
    .otherwise(pl.lit("Adult"))
)
```

## 問題 2.2.2 複数条件の連鎖

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Age`に基づいて、12歳未満なら`Child`、12歳以上60歳未満は`Adult`、60歳以上は`Senior`とする
  * 列名を`AgeCategory`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.2.2

```python
ans = df_titanic.with_columns(
    AgeCategory=pl.when(pl.col("Age") < 12)
    .then(pl.lit("Child"))
    .when(pl.col("Age") < 60)
    .then(pl.lit("Adult"))
    .otherwise(pl.lit("Senior"))
)
```

## 問題 2.2.3 then/otherwiseに式

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Sex`が"female"なら列`Fare`そのままの値、"male"なら列`Fare`の10%増しの値とする
  * 列名を`AdjustedFare`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.2.3

```python
ans = df_titanic.with_columns(
    AdjustedFare=pl.when(pl.col("Sex") == "female")
    .then(pl.col("Fare"))
    .otherwise(pl.col("Fare") * 1.1)
)
```

## 問題 2.2.4 条件に合わない値をnull

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Fare`が50以上の乗客の年齢を値とする（それ以外をnull）
  * 列名を`HighFareAge`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.2.4

```python
ans = df_titanic.with_columns(
    HighFareAge=pl.when(pl.col("Fare") >= 50).then("Age")
)
```

## 問題 2.2.5 複数列の条件の組み合わせ

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Pclass`が1で、かつ列`Embarked`が"S"の乗客に"Elite"という称号を与え、それ以外を"Common"とする
  * 列名を`Status`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.2.5

```python
ans = df_titanic.with_columns(
    Status=pl.when((pl.col("Pclass") == 1) & (pl.col("Embarked") == "S"))
    .then(pl.lit("Elite"))
    .otherwise(pl.lit("Common"))
)
```

## 問題 2.3.1 文字列の長さ(.str)

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Name`の乗客の名前の長さ
  * 列名を`NameLength`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.3.1

```python
ans = df_titanic.with_columns(
    NameLength=pl.col("Name").str.len_chars()
)
```

## 問題 2.3.2 文字列の分割

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Name`をカンマで分割し、最初の要素（姓）を取得
  * 列名を`LastName`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.3.2

```python
ans = df_titanic.with_columns(
    LastName=pl.col("Name").str.split(",").list.first()
)
```

## 問題 2.3.3 文字列を含むか判定

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Name`に`Mr.`が含まれているかどうかを取得する
  * 列名を`IsMr`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.3.3

```python
ans = df_titanic.with_columns(
    IsMr=pl.col("Name").str.contains("Mr.")
)
```

## 問題 2.3.4 正規表現で抽出

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Name`から敬称（例: Mr., Mrs., Miss.）を正規表現で抽出する（ピリオドを除く）
  * 列名を`Title`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.3.4

```python
ans = df_titanic.with_columns(
    Title=pl.col("Name").str.extract(r"(Mr|Mrs|Miss)\."),
)
```

## 問題 2.3.5 日付のパース

`file`を読み込み、日付の列`DATE`を日付型に変換し、変数`df_weather`に代入してください。

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
```

### 解答 2.3.5

```python
df_weather = pl.read_csv(file).with_columns(
    pl.col("DATE").str.to_date()
)
```

## 問題 2.3.6 年、月、日の抽出(.dt)

`df_weather`の列`DATE`から年、月、日をそれぞれ列`Year`、列`Month`、列`Day`として抽出し、変数`ans`に代入してください。

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 2.3.6

```python
ans = df_weather.with_columns(
    Year=pl.col("DATE").dt.year(),
    Month=pl.col("DATE").dt.month(),
    Day=pl.col("DATE").dt.day(),
)
```

## 問題 2.3.7 日付の差

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 各観測日(`DATE`)がデータセットの最初の日から何日経過しているかを計算する（型はpl.Duration）
  * 列名を`DaysPassed`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 2.3.7

```python
ans = df_weather.with_columns(
    DaysPassed=pl.col("DATE") - pl.col("DATE").min()
)
```

## 問題 2.3.8 曜日

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 列`DATE`から曜日（月曜=1,..., 日曜=7）を取得する
  * 列名を`Weekday`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 2.3.8

```python
ans = df_weather.with_columns(
    Weekday=pl.col("DATE").dt.weekday(),
)
```

## 問題 2.3.9 カテゴリ型(.cat)

`df_titanic`の列`Embarked`をカテゴリカル型に変換し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.3.9

```python
ans = df_titanic.with_columns(
    pl.col("Embarked").cast(pl.Categorical),
)
```

## 問題 2.3.10 カテゴリカル型へ変更

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 列`Pclass`を`1st`、`2nd`、`3rd`という値のカテゴリカル型に変換にする

最初の3行が下記のようになること。

| PassengerId | Survived | Pclass | ...  |
| ----------: | -------: | :----- | :--- |
|           1 |        0 | "3rd"  | ...  |
|           2 |        1 | "1st"  | ...  |
|           3 |        1 | "3rd"  | ...  |

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 2.3.10

```python
ans = df_titanic.with_columns(
    pl.col("Pclass").replace_strict(
        {1: "1st", 2: "2nd", 3: "3rd"}
    ).cast(pl.Categorical)
)
```

## 問題 3.1.1 グループ化して集計

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) ごとに乗客の平均年齢を計算する
  * 列名を`AverageAge`とする
  * `maintain_order=True`をつける
* PclassとAverageAgeの2列とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.1

```python
ans = df_titanic.group_by(
    "Pclass", maintain_order=True
).agg(AverageAge=pl.col("Age").mean())
```

## 問題 3.1.2 複数キーのグループ化

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) と性別 (Sex) の組み合わせごとに、生存率を計算する
  * 列名を`SurvivalRate`とする
* 列`SurvivalRate`で昇順にソートする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.2

```python
ans = (
    df_titanic.group_by(["Pclass", "Sex"])
    .agg(SurvivalRate=pl.col("Survived").mean())
    .sort("SurvivalRate")
)
```

## 問題 3.1.3 複数の集計

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) ごとに、乗客数、平均年齢、最高運賃を計算する
  * 列名をそれぞれ`PassengerCount`、`AgeAverage`、`FareMax`とする
* 列`Pclass`で昇順にソートする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.3

```python
ans = (
    df_titanic.group_by("Pclass")
    .agg(
        PassengerCount=pl.len(),
        AgeAverage=pl.col("Age").mean(),
        FareMax=pl.col("Fare").max(),
    )
    .sort("Pclass")
)
```

## 問題 3.1.4 数値列の集計

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 性別 (Sex) ごとに、すべての数値列の平均値を計算する
  * 列名のサフィックスに`Mean`をつける
* 列`Sex`で昇順にソートする

```python
import polars as pl
import polars.selectors as cs

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.4

```python
ans = (
    df_titanic.group_by("Sex")
    .agg(cs.numeric().mean().name.suffix("Mean"))
    .sort("Sex")
)
```

## 問題 3.1.5 全列の集計

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) ごとに、すべての列の最初の値を取得する
  * `maintain_order=True`をつける

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.5

```python
ans = df_titanic.group_by(
    "Pclass", maintain_order=True
).agg(pl.all().first())
```

## 問題 3.1.6 ユニーク数

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 各出港地 (Embarked) から乗船した乗客の客室クラス (Pclass) の種類の数を数える
  * 列名を`UniquePclassCount`とする
* 列`Embarked`で昇順にソートする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.6

```python
ans = (
    df_titanic.group_by("Embarked")
    .agg(UniquePclassCount=pl.col("Pclass").n_unique())
    .sort("Embarked")
)
```

## 問題 3.1.7 条件を満たす行数

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) ごとに、30歳以上の乗客の数を数える
  * 列名を`CountOver30`とする
* 列`Pclass`で昇順にソートする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.7

```python
ans = (
    df_titanic.group_by("Pclass")
    .agg(CountOver30=pl.col("Age").filter(pl.col("Age") >= 30).len())
    .sort("Pclass")
)
```

## 問題 3.1.8 グループ化の結果のフィルタリング(having句相当)

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) ごとに乗客数を計算
  * 乗客数が200人以上のみ残す
  * 列名を`PassengerCount`とする
* 列`Pclass`で昇順にソートする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.8

```python
ans = (
    df_titanic.group_by("Pclass")
    .agg(PassengerCount=pl.len())
    .filter(pl.col("PassengerCount") > 200)
    .sort("Pclass")
)
```

## 問題 3.1.9 グループ内の各要素

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) ごとに、乗客の名前をリストとして集計する
  * 列名を`PassengerNames`とする
  * `maintain_order=True`をつける

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.9

```python
ans = df_titanic.group_by("Pclass", maintain_order=True).agg(
    PassengerNames="Name"
)
```

## 問題 3.1.10 全体の集計

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 全体の平均年齢と最高運賃を計算する
  * 列名を`TotalAverageAge`と`TotalMaxFare`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 3.1.10

```python
ans = df_titanic.select(
    TotalAverageAge=pl.col("Age").mean(),
    TotalMaxFare=pl.col("Fare").max(),
)
```

## 問題 3.2.1 月ごとに集計

列`DATE`で昇順にソートされた`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 月ごとにグループ化し、各月の最高気温 (`TMAX`) の平均を計算する
  * 列名を`AvgTMAX`とする

最初の3行が下記のようになること。

| DATE       |   AvgTMAX |
| :--------- | --------: |
| 1869-01-01 | 39.516129 |
| 1869-02-01 | 39.714286 |
| 1869-03-01 |  41.83871 |

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(
    pl.col("DATE").str.to_date()
)
```

### 解答 3.2.1

```python
ans = df_weather.group_by_dynamic(
    index_column="DATE", every="1mo"
).agg(AvgTMAX=pl.col("TMAX").mean())
```

## 問題 3.2.2 四半期ごとの集計

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 四半期 (3ヶ月) ごとにグループ化し、各四半期の降水量 (PRCP) の合計を計算する
  * 列名を`TotalPRCP`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 3.2.2

```python
ans = df_weather.group_by_dynamic(
    index_column="DATE",
    every="3mo",
    period="3mo",  # ウィンドウの期間(省略可)
    closed="left",  # ウィンドウの開始点を含む(省略可)
).agg(TotalPRCP=pl.col("PRCP").sum())
```

## 問題 3.2.3 年ごとの集計(開始点変更)

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 毎年7月を開始点として年間の降雪量(SNOW)の合計を計算する(例：2020/7/1 - 2021/6/30)
  * 列名を`TotalSnow`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 3.2.3

```python
ans = df_weather.group_by_dynamic(
    index_column="DATE",
    every="1y",
    offset="6mo",  # 7月を開始点にするため、6ヶ月オフセット
).agg(TotalSnow=pl.col("SNOW").sum())
```

## 問題 3.2.4 カテゴリカルキーと時間でグループ化

`df`を次の条件で修正し、変数`ans`に代入してください。

* 地点(Station)ごと、かつ10年ごとに平均最高気温（TMAXの平均）を計算する
  * 列名を`AvgTMAX/decade`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())

# ダミーの観測地点列を追加
df = df_weather.with_columns(
    Station=pl.when(pl.col("DATE").dt.year() < 1950)
    .then(pl.lit("StationA"))
    .otherwise(pl.lit("StationB"))
)
```

### 解答 3.2.4

```python
ans = df.group_by_dynamic(
    index_column="DATE",
    every="10y",  # 10年ごとに集計
    group_by="Station",  # カテゴリカルキーを指定
).agg(pl.col("TMAX").mean().alias("AvgTMAX/decade"))
```

## 問題 3.2.5 ローリング集計

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 7日間の移動平均最高気温を計算する
  * 列名を`AvgTMAX/7d`とする
* `DATE`と`AvgTMAX/7d`の2列とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 3.2.5

```python
ans = df_weather.select(
    pl.col("DATE"),
    pl.col("TMAX").rolling_mean(window_size=7).alias("AvgTMAX/7d"),
)
```

## 問題 3.3.1 アップサンプリング

`df_weather`をダウンサンプリングした`df`を次の条件で修正し、変数`ans`に代入してください。

  * 日次データとしてアップサンプリングする
  * 間のデータは線形補間する
  * 下記のようになること

| DATE       | AvgTMAX |
| :--------- | ------: |
| 1868-12-31 |    29.0 |
| 1869-01-01 |    30.0 |
| 1869-01-02 |    31.0 |
| 1869-01-03 |    35.5 |
| 1869-01-04 |    40.0 |

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())

df = df_weather.group_by_dynamic(
    index_column="DATE", every="2d"
).agg(AvgTMAX=pl.col("TMAX").mean())[:3]
```

### 解答 3.3.1

```python
ans = df.upsample("DATE", every="1d").interpolate()
```

## 問題 3.4.1 内部結合

`df_a`と`df_b`を次の条件で修正し、変数`ans`に代入してください。

* 共通のキーで内部結合する
  * `maintain_order="left"`をつける

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)
df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.1

```python
ans = df_a.join(
    df_b,
    on="key",
    how="inner",
    maintain_order="left",
)
```

## 問題 3.4.2 左外部結合

`df_a`と`df_b`を次の条件で修正し、変数`ans`に代入してください。

* `df_a`を左側として左外部結合を行う

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)

df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.2

```python
ans = df_a.join(df_b, on="key", how="left")
```

## 問題 3.4.3 完全外部結合

`df_a`と`df_b`を次の条件で修正し、変数`ans`に代入してください。

* 完全外部結合する

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)

df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.3

```python
ans = df_a.join(df_b, on="key", how="full")
```

## 問題 3.4.4 クロス結合

`df_a`と`df_b`を次の条件で修正し、変数`ans`に代入してください。

* df_aとdf_bのデカルト積(総当たり)を計算する

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)

df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.4

```python
ans = df_a.join(df_b, how="cross")
```

## 問題 3.4.5 複数キーで結合

`df_c`と`df_d`を次の条件で修正し、変数`ans`に代入してください。

* 共通のキーで内部結合する

```python
import polars as pl

df_c = pl.DataFrame(
    {
        "key1": [1, 1, 2],
        "key2": [0, 1, 0],
        "value_a": ["a10", "a11", "a20"],
    }
)
df_d = pl.DataFrame(
    {
        "key1": [1, 2, 2],
        "key2": [0, 0, 1],
        "value_b": ["b10", "b20", "b21"],
    }
)
```

### 解答 3.4.5

```python
ans = df_c.join(df_d, on=["key1", "key2"], how="inner")
```

## 問題 3.4.6 セミ結合

`df_a`と`df_b`を次の条件で修正し、変数`ans`に代入してください。

* df_aのキーがdf_bにも存在する行のみを、df_aの列だけで抽出する

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)

df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.6

```python
ans = df_a.join(df_b, on="key", how="semi")
```

## 問題 3.4.7 アンチ結合

`df_a`と`df_b`を次の条件で修正し、変数`ans`に代入してください。

* df_aのキーがdf_bに存在しない行のみを、df_aの列だけで抽出する

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)

df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.7

```python
ans = df_a.join(df_b, on="key", how="anti")
```

## 問題 3.4.8 Asof結合

時系列データで、各注文日に最も近い過去の市場価格を結合し、変数`ans`に代入してください。

```python
from datetime import date
import polars as pl

market_prices = pl.DataFrame({
    'time': pl.date_range(pl.date(2023, 1, 2), pl.date(2023, 1, 8), '2d', eager=True),
    'price': range(2, 9, 2),
})
orders = pl.DataFrame({
    'order_time': [date(2023, 1, 1), date(2023, 1, 5), date(2023, 1, 9)],
    'volume': [100, 120, 180],
})
```

### 解答 3.4.8

```python
ans = orders.join_asof(
    market_prices,
    left_on="order_time",
    right_on="time",
    strategy="nearest",
)
```

## 問題 3.4.9 非等価結合

各イベントがどの時間枠に含まれるかを判定して結合し、event_timeでソートして、変数`ans`に代入してください。

```python
import polars as pl

events = pl.DataFrame(
    {
        "event_time": [1.5, 2.8, 3.5, 5.1],
        "event_type": ["a", "b", "c", "d"],
    }
)
windows = pl.DataFrame(
    {
        "window_id": ["x", "y", "z"],
        "start_time": [1.0, 3.0, 5.0],
        "end_time": [2.0, 4.0, 6.0],
    }
)
```

### 解答 3.4.9

```python
ans = events.join_where(
    windows,
    (pl.col("event_time") >= pl.col("start_time"))
    & (pl.col("event_time") < pl.col("end_time")),
).sort("event_time")
```

## 問題 3.4.10 縦に結合

`df_a`と`df_b`を縦に結合し、変数`ans`に代入してください。

* `df_b`の列名は`df_a`に揃える

```python
import polars as pl

df_a = pl.DataFrame(
    {
        "key": [1, 2, 3],
        "value_a": ["a1", "a2", "a3"],
    }
)

df_b = pl.DataFrame(
    {
        "key": [3, 4, 1],
        "value_b": ["b3", "b4", "b1"],
    }
)
```

### 解答 3.4.10

```python
ans = pl.concat([df_a, df_b.rename({"value_b": "value_a"})])
```

## 問題 3.5.1 縦持ち変換 (unpivot)

`df_wide`は、生徒ごとの各科目の点数を横持ちで保持しています。このDataFrameを「生徒(`Student`)」「科目(`Subject`)」「点数(`Score`)」を列に持つ縦長の形式に変換し、変数`ans`に代入してください。

```python
import polars as pl

df_wide = pl.DataFrame({
    "Student": ["Alice", "Bob", "Carol"],
    "Math": [90, 88, 92],
    "Science": [85, 91, 89],
})
```

### 解答 3.5.1

```python
ans = df_wide.unpivot(
    on=["Math", "Science"],
    index="Student",
    variable_name="Subject",
    value_name="Score"
)
```

## 問題 3.5.2 横持ち変換 (pivot)

問題 縦長のDataFrame`df_long`を、再び生徒ごとに行を持ち、各科目が列となる横長の形式に変換し、変数`ans`に代入してください。

```python
import polars as pl

df_long = pl.DataFrame({
    "Student": ["Alice", "Bob", "Carol", "Alice", "Bob", "Carol"],
    "Subject": ["Math", "Math", "Math", "Science", "Science", "Science"],
    "Score": [90, 88, 92, 85, 91, 89],
})
```

### 解答 3.5.2

```python
ans = df_long.pivot(
    on="Subject",
    index="Student",
    values="Score",
)
```

## 問題 4.1.1 グループ内でのランキング

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 各客室クラス (Pclass) 内での運賃 (Fare) の降順ランキングを計算する
  * 列名を`FareRankInClass`とする
  * `method="dense"`をつけること
* FareRankInClass、Pclass、PassengerIdでソートする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.1.1

```python
ans = df_titanic.with_columns(
    FareRankInClass=pl.col("Fare").rank(
        method="dense", descending=True
    ).over("Pclass")
).sort("FareRankInClass", "Pclass", "PassengerId")
```

## 問題 4.1.2 グループ内累積和

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 年ごとに日々の降水量(PRCP)の累積和を計算する
  * 列名を`CumulativePRCP`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(
    pl.col("DATE").str.to_date()
)
```

### 解答 4.1.2

```python
ans = df_weather.with_columns(
    CumulativePRCP=pl.col("PRCP").cum_sum().over(pl.col("DATE").dt.year()),
)
```

## 問題 4.1.3 グループ合計に対する割合

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 運賃 (Fare) が、その乗客が属する客室クラス (Pclass) 内での運賃合計の何パーセントを占めるかを計算する
  * 列名を`FarePercentageOfClass`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.1.3

```python
ans = df_titanic.with_columns(
    FarePercentageOfClass=(
        pl.col("Fare") / pl.col("Fare").sum().over("Pclass") * 100
    )
)
```

## 問題 4.1.4 グループ内差分

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 年ごとに、各日の最高気温 (TMAX) と前日の最高気温との差を計算する
  * 列名を`DiffTMAX`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 4.1.4

```python
ans = df_weather.with_columns(
    DiffTMAX=(pl.col("TMAX") - pl.col("TMAX").shift(1)).over(pl.col("DATE").dt.year())
)
```

## 問題 4.1.5 グループ内移動平均

`df_weather`を次の条件で修正し、変数`ans`に代入してください。

* 年ごとに、最高気温 (TMAX) の7日間移動平均を計算する
  * 列名を`AvgTMAX/7d`とする

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df_weather = pl.read_csv(file).with_columns(pl.col("DATE").str.to_date())
```

### 解答 4.1.5

```python
ans = df_weather.with_columns(
    pl.col("TMAX").rolling_mean(window_size=7)
    .over(pl.col("DATE").dt.year())
    .alias("AvgTMAX/7d")
)
```

## 問題 4.1.6 複数列のウィンドウ

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 客室クラス (Pclass) と性別 (Sex) の両方でグループ化し、その中での年齢 (Age) のランキングを計算する
  * 列名を`AgeRankInClassSex`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.1.6

```python
ans = df_titanic.with_columns(
    AgeRankInClassSex=pl.col("Age")
    .rank()
    .over("Pclass", "Sex")
)
```

## 問題 4.1.7 自身を除くグループ内計算

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 各乗客について、その乗客を除く同じ客室クラスの他の乗客の平均運賃を計算する
  * 列名を`AvgFareOfOthersInClass`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.1.7

```python
ans = df_titanic.with_columns(
    AvgFareOfOthersInClass=(
        (pl.col("Fare").sum().over("Pclass") - pl.col("Fare"))
        / (pl.len().over("Pclass") - 1)
    )
)
```

## 問題 4.1.8 条件付きウィンドウ

`df_titanic`を次の条件で修正し、変数`ans`に代入してください。

* 各客室クラス (Pclass) 内で、運賃が50以上の乗客のみを対象に、運賃の累積和を計算する
  * 運賃が50未満の乗客は運賃を0とみなす
  * 列名を`ConditionalCumulativeFare`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.1.8

```python
ans = df_titanic.with_columns(
    ConditionalCumulativeFare=pl.when(pl.col("Fare") >= 50)
    .then(pl.col("Fare"))
    .otherwise(0)
    .cum_sum()
    .over("Pclass")
)
```

## 問題 4.2.1 EagerクエリからLazyクエリに変換

Parquetファイルを次の条件で読み込み、変数`df_retail`に代入してください。

* `scan_parquet`を使って、LazyFrameとして読み込むこと

```python
import polars as pl

file = "online_retail.parquet"
```

### 解答 4.2.1

```python
df_retail = pl.scan_parquet(file)
```

## 問題 4.2.2 クエリ

`df_retail`で下記のクエリを作成し、変数`query`に代入してください。

* 数量 (Quantity) が10より大きいイギリス (`"United Kingdom"`) の取引をフィルタリングする

```python
import polars as pl

file = "online_retail.parquet"
df_retail = pl.scan_parquet(file)
```

### 解答 4.2.2

```python
query = df_retail.filter(
    (pl.col("Quantity") > 10) & (pl.col("Country") == "United Kingdom")
)
```

## 問題 4.2.3 述語プッシュダウン

最初に`df_retail.explain()`を表示し、df_retailでは述語プッシュダウンが起きていないことを確認してください。

次に、`query`の実行計画を作成し、変数`ans`に代入してください。
`ans`を表示し述語プッシュダウンが起きていることを確認してください。

```python
import polars as pl

file = "online_retail.parquet"
df_retail = pl.scan_parquet(file)
query = df_retail.filter(
    (pl.col("Quantity") > 10) & (pl.col("Country") == "United Kingdom")
)
```

### 解答 4.2.3

```python

ans = query.explain()
```

## 問題 4.2.4 射影プッシュダウン

`query`に次の条件を追加し、変数`selected_query`に代入してください。
`selected_query`の実行計画を表示し、射影プッシュダウンが起きていることを確認してください。

* QuantityとCountryの2列を選択する

```python
import polars as pl

file = "online_retail.parquet"
df_retail = pl.scan_parquet(file)
query = df_retail.filter(
    (pl.col("Quantity") > 10) & (pl.col("Country") == "United Kingdom")
)
```

### 解答 4.2.4

```python
selected_query = query.select("Quantity", "Country")
```

## 問題 4.2.5 遅延クエリの実行

遅延クエリ`selected_query`を実行し、変数`ans`に代入してください。

```python
import polars as pl

file = "online_retail.parquet"
df_retail = pl.scan_parquet(file)
query = df_retail.filter(
    (pl.col("Quantity") > 10) & (pl.col("Country") == "United Kingdom")
)
selected_query = query.select("Quantity", "Country")
```

### 解答 4.2.5

```python
ans = selected_query.collect()
```

## 問題 4.3.1 リスト列

`df_titanic`を次の条件で修正し、変数`df_word`に代入してください。

* 列`Name`を単語に分割してリスト化する
  * 列名を`NameWords`とする
* 列`NameWords`をリストの要素数を求める
  * 列名を`WordCount`とする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.3.1

```python
df_word = df_titanic.with_columns(
    NameWords=pl.col("Name").str.split(" "),
).with_columns(
    WordCount=pl.col("NameWords").list.len(),
)
```

## 問題 4.3.2 リスト列の展開

`df_word`を次の条件で修正し、変数`ans`に代入してください。

* 列`NameWords`を展開し、各単語が個別の行になるようにする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
df_word = df_titanic.with_columns(
    NameWords=pl.col("Name").str.split(" "),
).with_columns(
    WordCount=pl.col("NameWords").list.len(),
)
```

### 解答 4.3.2

```python
ans = df_word.explode("NameWords")
```

## 問題 4.3.3 リスト内要素の変換

`df_word`を次の条件で修正し、変数`ans`に代入してください。

* 列`NameWords`の各単語をすべて大文字に変換する
* 列`NameWords`だけにする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
df_word = df_titanic.with_columns(
    NameWords=pl.col("Name").str.split(" "),
).with_columns(
    WordCount=pl.col("NameWords").list.len(),
)
```

### 解答 4.3.3

```python
ans = df_word.select(
    pl.col("NameWords").list.eval(pl.element().str.to_uppercase())
)
```

## 問題 4.3.4 構造体列

`df_titanic`を次の条件で修正し、変数`df_titanic_struct`に代入してください。

* 列`Age`と列`Fare`からなる構造体列を作成する
  * 列名を`PassengerInfo`とする
* 列`PassengerInfo`だけにする

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 4.3.4

```python
df_titanic_struct = df_titanic.select(
    PassengerInfo=pl.struct(pl.col("Age"), pl.col("Fare")),
)
```

## 問題 4.3.5 構造体列の展開

`df_titanic_struct`を次の条件で修正し、変数`ans`に代入してください。

* 列`PassengerInfo`を元の列`Age`と列`Fare`に展開する

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
df_titanic_struct = df_titanic.select(
    PassengerInfo=pl.struct(pl.col("Age"), pl.col("Fare")),
)
```

### 解答 4.3.5

```python
ans = df_titanic_struct.unnest("PassengerInfo")
```

## 問題 4.3.6 JSONから構造体

`df_json`を次の条件で修正し、変数`df_struct`に代入してください。

* JSON文字列の列`ItemJson`を、構造体に変換する
  * 列名を`ItemStruct`とする
  * 構造体の型として、変数`dtype`の値を用いる

```python
import polars as pl

df_json = pl.DataFrame(
    {
        "OrderID": [101, 102, 103],
        "ItemJson": [
            '{"name": "Laptop", "price": 1200}',
            '{"name": "Mouse", "price": 25}',
            '{"name": "Keyboard", "price": 75}',
        ],
    }
)
dtype = pl.Struct([
    pl.Field("name", pl.String),
    pl.Field("price", pl.Int64),
])
```

### 解答 4.3.6

```python
df_struct = df_json.with_columns(
    ItemStruct=pl.col("ItemJson").str.json_decode(dtype),
)
```

## 問題 4.3.7 フィールド抽出

`df_struct`を次の条件で修正し、変数`ans`に代入してください。

* 列`ItemStruct`からnameを独立した列にする

```python
import polars as pl

df_json = pl.DataFrame(
    {
        "OrderID": [101, 102, 103],
        "ItemJson": [
            '{"name": "Laptop", "price": 1200}',
            '{"name": "Mouse", "price": 25}',
            '{"name": "Keyboard", "price": 75}',
        ],
    }
)
dtype = pl.Struct({"name": pl.String, "price": pl.Int64})
df_struct = df_json.with_columns(
    ItemStruct=pl.col("ItemJson").str.json_decode(dtype),
)
```

### 解答 4.3.7

```python
ans = df_struct.with_columns(
    pl.col("ItemStruct").struct.field("name"),
)
```

## 問題 4.4.1 要素ごとに関数を適用 (map_elements)

`df`に下記の条件で列`Desc`を追加し、変数`ans`に代入してください。

* 列`Val`の各要素に対して、`f"value: {要素}"`とする
* 関数`value`を使うこと

```python
import polars as pl

df = pl.DataFrame({"Val": [10, 21, 35]})

def value(v: int)->str:
    return f"value: {v}"
```

### 解答 4.4.1

```python
ans = df.with_columns(
    Desc=pl.col("Val").map_elements(value, return_dtype=pl.String),
)
```

## 問題 4.4.2 行ごとに関数を適用 (map_rows)

`df`を次の条件で修正し、変数`ans`に代入してください。

* 各行に関数`value`を適用した列だけにする
 * 列名を`Val`とする
* 関数`value`を使うこと

```python
import polars as pl

df = pl.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

def value(row: tuple[int, int]) -> int:
    return row[0] + 2 * row[1]
```

### 解答 4.4.2

```python
ans = df.map_rows(value).rename({"map": "Val"})
```

## 問題 4.4.3 バッチごとに関数を適用 (map_batches)

LazyFrame`lf`に関数double_dfを適用し、列`Score`のみのDataFrameにして、変数`ans`に代入してください。

```python
import polars as pl

import numpy as np
lf = pl.LazyFrame({"Name": ["Alice", "Bob", "Carol"], "Score": [40, 32, 48]})

def double_df(df: pl.DataFrame)->pl.DataFrame:
    return 2 * df
```

### 解答 4.4.3

```python
ans = lf.select(pl.col("Score")).map_batches(double_df).collect()
```

## 問題 4.4.4 グループごとに関数を適用 (map_groups)

`df`を列`Group`でグループ化し、グループごとに関数max_rowを適用し、変数ansに代入してください。

```python
import polars as pl

df = pl.DataFrame({
    "Group": ["a", "a", "b", "b", "a"],
    "Val": [1, 3, 2, 5, 4],
})
def max_row(df: pl.DataFrame)->pl.DataFrame:
    return df.max()
```

### 解答 4.4.4

```python
ans = df.group_by("Group", maintain_order=True).map_groups(max_row)
```

## 問題 5.1.1 Pandasに変換

`df_titanic`をPandasのDataFrameに変換し、変数`df_pandas`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 5.1.1

```python
df_pandas = df_titanic.to_pandas()
```

## 問題 5.1.2 PandasからPolars

`df_pandas`をPolarsのDataFrameに変換し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
df_pandas = df_titanic.to_pandas()
```

### 解答 5.1.2

```python
ans = pl.from_pandas(df_pandas)
```

## 問題 5.1.3 Apache Arrow Tableに変換

`df_titanic`をApache Arrow Tableに変換し、変数`df_arrow`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
```

### 解答 5.1.3

```python
df_arrow = df_titanic.to_arrow()
```

## 問題 5.1.4 Apache Arrow TableからPolars

`df_arrow`をPolarsのDataFrameに変換し、変数`ans`に代入してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
df_arrow = df_titanic.to_arrow()
```

### 解答 5.1.4

```python
ans = pl.from_arrow(df_arrow)
```

## 問題 5.2.1 SQLContextにテーブル登録

`df_titanic`のLazyDataFrameをSQLContext(`ctx`)にtitanicという名前で登録してください。

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)

ctx = pl.SQLContext()
```

### 解答 5.2.1

```python
ctx.register("titanic", df_titanic.lazy())
```

## 問題 5.2.2 SQLクエリの実行

`ctx`から次の要件でDataFrameを作成し、変数`ans`に代入してください。

* 登録した'titanic'テーブルから、30歳以上の男性乗客をPclassの昇順で選択するSQLクエリを実行する

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)

ctx = pl.SQLContext()
ctx.register("titanic", df_titanic)

query = """
SELECT Name, Age, Pclass
FROM titanic
WHERE Age >= 30 AND Sex = 'male'
ORDER BY Pclass
"""
```

### 解答 5.2.2

```python
ans = ctx.execute(query).collect()
```

## 問題 5.2.3 DataFrameに直接SQL実行

次の要件でDataFrameを作成し、変数`ans`に代入してください。

* グローバルスコープにあるDataFrameに対して `pl.sql()`を使って直接クエリを実行する

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)

query = "SELECT COUNT(*) as num_passengers FROM df_titanic"
```

### 解答 5.2.3

```python
ans = pl.sql(query).collect()
```

## 問題 5.2.4 SQLでテーブル作成

`ctx`から次の要件でDataFrameを作成し、変数`ans`に代入してください。

* 登録した'titanic'テーブルから、新しいテーブル作成のSQLクエリを実行する

```python
import polars as pl

file = "titanic_train.csv"
df_titanic = pl.read_csv(file)
ctx = pl.SQLContext()
ctx.register("titanic", df_titanic.lazy())

query = "CREATE TABLE survivors AS SELECT * FROM titanic WHERE Survived = 1"
```

### 解答 5.2.4

```python
ans = ctx.execute(query).collect()
```

## 問題 5.3.1 折れ線グラフ

`df`を使って次の要件で折れ線グラフを作成し、変数`ans`に代入してください。

* X軸は列`Name`
* Y軸は列`Score`
* Y軸のラベルは`得点`
* 列`Subject`ごとに線を引くこと

```python
import polars as pl

import altair as alt

df = pl.DataFrame({
    "Name": ["A", "A", "B", "B", "C", "C"],
    "Subject": ["Math", "Music", "Math", "Music", "Math", "Music"],
    "Score": [85, 90, 94, 88, 80, 93],
})
```

### 解答 5.3.1

```python
ans = df.plot.line(
    x="Name",
    y=alt.Y("Score", title="得点"),
    color="Subject",
)
```

## 問題 5.3.2 散布図

`df`を使って次の要件で散布図を作成し、変数`ans`に代入してください。

* X軸は列`Math`
* Y軸は列`Music`
* タイトルは`2教科の関係`

```python
import polars as pl

import altair as alt

df = pl.DataFrame({
    "Math": [33, 21, 42],
    "Music": [23, 34, 26],
})
```

### 解答 5.3.2

```python
ans = df.plot.scatter(
    x="Math",
    y="Music",
).properties(
    title="2教科の関係",
)
```

## 問題 5.4.1 時系列異常検知

この演習では、NYC Weatherデータセットを使い、これまでに学んだ複数のスキルを組み合わせて、気温の異常値を検出します。

`df`を元に、下記の処理の最終結果を、変数`ans`に代入してください。

1. 列`DATE`をdate型に変更する
2. 月ごとに、日次の最高気温(TMAX)の平均(MonthlyAvgTMAX)と標準偏差(MonthlyStdTMAX)を計算する
3. 最高気温が、その月の平均から標準偏差の2倍以上離れている日を「異常日(IsAnomaly)」とする
4. 異常日だけ抽出し日付順にソートする

最初の3行が下記のようになること。

| DATE       | PRCP | SNOW | SNWD | TMIN | TMAX | MonthlyAvgTMAX | MonthlyStdTMAX | IsAnomaly |
| :--------- | ---: | ---: | :--- | ---: | ---: | -------------: | -------------: | :-------- |
| 1869-02-13 |  0.0 |  0.0 | null |   40 |   61 |      39.674638 |      10.025825 | true      |
| 1869-03-01 |  0.0 |  0.0 | null |    4 |   26 |      47.824675 |       10.51861 | true      |
| 1869-03-07 |  0.0 |  0.0 | null |   20 |   26 |      47.824675 |       10.51861 | true      |

```python
import polars as pl

file = "NYC_Central_Park_weather_1869-2022.csv"
df = pl.scan_csv(file)
```

### 解答 5.4.1

```python
# 1. 列`DATE`をdate型に変更
tmp = df.with_columns(pl.col("DATE").str.to_date())

# 2. 月ごとの最高気温(TMAX)の平均と標準偏差の計算
tmp = tmp.with_columns(
    MonthlyAvgTMAX=pl.col("TMAX").mean().over(pl.col("DATE").dt.month()),
    MonthlyStdTMAX=pl.col("TMAX").std().over(pl.col("DATE").dt.month()),
)

# 3. 最高気温が月平均から標準偏差の2倍以上を異常日
tmp = tmp.with_columns(
    IsAnomaly=(pl.col("TMAX") - pl.col("MonthlyAvgTMAX")).abs() > 2 * pl.col("MonthlyStdTMAX"),
)

# 4. 異常日のを抽出してソート
ans = tmp.filter(pl.col("IsAnomaly")).sort("DATE").collect()
```

## 問題 5.4.2 顧客のRFM分析

この最終演習では、Online Retailデータセットを用いて、顧客セグメンテーションの一般的な手法であるRFM（Recency, Frequency, Monetary）分析を行います。これは、データクリーニング、時系列処理、複雑な集計など、多くのスキルを統合する実践的な課題です。

`df`を元に、各顧客についてRFM指標を計算し、最終結果を変数`ans`に代入してください。

**手順**

1. データクリーニング
  * InvoiceDateをdatetime型に変換(`format="%m/%d/%y %H:%M"`)
  * Quantity > 0、UnitPrice > 0、CustomerIDが欠損以外でフィルタリング

2. RFM指標を計算
  * CustomerIDでグループ化し以下を修正
    * 列`Recency`として、「グループ化前のInvoiceDateの最大値」からInvoiceDateの最大値を引いた日数+1
    * 列`Frequency`として、InvoiceNoのユニーク数
    * 列`Monetary`として、(Quantity * UnitPrice)の合計

3. 列`Monetary`で降順に、列`CustomerID`で昇順にソート

最初の3行が下記のようになること。

| CustomerID | Recency | Frequency |  Monetary |
| ---------: | ------: | --------: | --------: |
|      14646 |       7 |        29 | 121973.65 |
|      18102 |      12 |        20 | 106601.55 |
|      12346 |     160 |         1 |   77183.6 |

```python
import polars as pl

file = "online_retail.parquet"
df = pl.scan_parquet(file)
```

### 解答 5.4.2

```python
# 1. データクリーニング
tmp = df.with_columns(
    pl.col("InvoiceDate").str.to_datetime(format="%m/%d/%y %H:%M"),
).filter(
    pl.col("Quantity") > 0,
    pl.col("UnitPrice") > 0,
    pl.col("CustomerID").is_not_null(),
)

# 2. RFM指標を計算
tmp = (
    tmp.with_columns(
        Recency=(
            pl.col("InvoiceDate").max() - pl.col("InvoiceDate").max().over("CustomerID")
        ).dt.total_days() + 1,
    )
    .group_by("CustomerID")
    .agg(
        pl.col("Recency").first(),
        Frequency=pl.col("InvoiceNo").n_unique(),
        Monetary=(pl.col("Quantity") * pl.col("UnitPrice")).sum(),
    )
)

# 3. 列`Monetary`で降順に、列`CustomerID`で昇順にソート
ans = tmp.sort(["Monetary", "CustomerID"], descending=[True, False]).collect()
```
