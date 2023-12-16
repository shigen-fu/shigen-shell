### about this project

Some python or shell script shigen used in daily work to make works more efficient

### shell descriptions

#### 1. fake-util.sh

This shell is based on python, depends on `faker` package. You can use it to generate a sequence of data of a specified type with a given quantity. For example:

```shell
python fake-util.py -t phone -c 3
13709337586
18732570297
14519906998
```
More information, just execute the following command:

```shell
python fake-util.py --help
```