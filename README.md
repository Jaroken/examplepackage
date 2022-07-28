# examplepackage for python

This is a silly simple package for me to simply document very basic packaging structure and functionality.

The functions included are mainly included to simply prove the package has been installed and the functions are usable.

### How to install this package
requirements: pip and git
##### How to install from jupyter notebook
```python
!pip install git+https://github.com/Jaroken/examplepackage
```
##### How to install from terminal or command line
```python
pip install git+https://github.com/Jaroken/examplepackage
```

##### How to install with conda (just use pip and git in conda)
```python
conda install git
conda install pip
pip install git+https://github.com/Jaroken/examplepackage
```
### How to run package once installed 
#### the package can be used with any python3.5 interpreter or greater like so
importing package and functionality is the same in any environment
```python 
Python 3.9.12 (main, Apr  5 2022, 06:56:58) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from examplepackage import random_dataframe
>>> dz = random_dataframe.random_dataframe()
>>> dz.add_random_columns(2)
>>> dz.df
   monkey_run_pasta_1  topic_punch_netflix_3
0                   2                      8
1                   1                     10
2                   8                      6
3                   5                      2
4                   1                      4
5                   8                      5
6                   5                      7
7                   9                      3
8                   8                      6
9                   5                      7

```

#### Alternatively there is a main.py script that can be run from console as a simple script with arguements
first arg provided is 2 for number of rows
second arg provided is 3 for number of columns
```commandline
 python main.py 2 3
   monkey_break_youtube_1  topic_stretch_netflix_5  topic_kick_youtube_1
0                       8                       10                     8
1                       5                        8                     9

```