TODO: Reflect on what you learned this week and what is still unclear.

## 1 - setup

### update course

pull all new contents:

```powershell
cd ..\course
git pull
```

## 2 - create new repo for your project

1. public
2. add a README file
3. Add `.gitignore` - Python
4. MIT License
5. clone it down to your laptop
6. go to the file open it in the VScode

```powershell
git clone https://github.com/zeenaz/data_py.git

cd ../data_py

code . -r
```

1. reveal file in folder
2. copy all files (no folder) form `1161/course/data_introduction` paste it into your data project folder
3. open `basic_pandas.ipyb`

```python
import numpy as np
import pandas as pd
```

what can import do?

it allows you to change the definition in this file

### 2 - Working wit Pandas

1. use `pd.read_csv(filepath)`

```python
if os.path.isfile("penalty_data_set_0.csv"):
    filepath = "penalty_data_set_0.csv"
    print("loading from file")
else:
    filepath = "http://www.osr.nsw.gov.au/sites/default/files/file_manager/penalty_data_set_0.csv"
    print("loading from the internet")

penalty_data = pd.read_csv(filepath)
print("done")
```

1. how to see the dataset in sheet format?

```python
penalty_data.head()
```

1. how to see the titles? columns name?

```python
penalty_data.columns
```

1. how to define a row in your name and related to the datasets?

You can't index a row directly, you need to use the iloc property.

This gives us the row as a _Series_.

first you named it in row_one, linked to a location in your dataset

second you

```python
row_one = penalty_data.iloc[1]
row_one

\\\\\\\\\\\\\\\\\\\\\\\
row_one["OFFENCE_DESC"]
\\\\\\\\\\OR\\\\\\\\\\
row_one.OFFENCE_DESC
```

1. how to put all data in label "xxx" in a box?

```python
penalty_data["FACE_VALUE"]

\\\\\\\\\\\ "you can get 246304 data in this dataset" \\\\\\\\\\
"""
Name: FACE_VALUE, Length: 246305, dtype: int64
"""
```

1. how to plot your data into graphics?

```python
penalty_data["FACE_VALUE"].plot()
```

1. how to get make histogram?

```python
penalty_data["FACE_VALUE"].hist()
```

1. select certain range of values and show it in your histogram ?

for example: exclude all the values above $3,000

```python
penalty_data.FACE_VALUE[penalty_data.FACE_VALUE < 3000.hist()
```

1. how to use `boolean indexing` to get the values in ranges?

That's pretty crazy/powerful, so let's see that happen a bit more clearly.

We'll make our own series and call it `some_numbers`

Let's give it the values 0-99

1. less than 8
2. less than 4 or more than 97

```python
some_numbers = pd.Series(range(100))
some_numbers.head()

some_numbers[some_numbers < 8]

"""
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
"""

some_numbers[(some_numbers < 4) | (some_numbers > 97)]
"""
0      0
1      1
2      2
3      3
98    98
99    99
"""

```
