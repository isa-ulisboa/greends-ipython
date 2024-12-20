# Introduction to Python 2024/2025

Masters in Data Science applied to agricultural and food sciences, environment, and forestry engineering.

Instructor: Manuel Campagnolo (mlc@isa.ulisboa.pt)

Teaching assistant: Dominic Welsh (djwelsh@edu.ulisboa.pt)

<details markdown="block">
<summary> 
 
# Online resources for the course

</summary>
 
* **Required:** [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022): lectures (videos and notes), problems sets, shorts; The platform allows you to test your code at the [CS50 codespace](https://cs50.dev/) for the proposed problems (you need to have your own GitHub account to access the codespace).
* Python Programming course at [PP.fi](https://programming-23.mooc.fi/): same features as CS50 but to test your solutions to problems you are required to pass previous tests 
* [Learn Python](https://v2.scrimba.com/learn-python-c03): lectures (videos) and interactive examples and exercises 
* [Introduction to Python (VScode)](https://vscodeedu.com/courses/intro-to-python): interactive lectures and exercises 
* Basic concepts and features of the Python language and system: [The Python Tutorial at python.org](https://docs.python.org/3/tutorial/index.html).
* Fenix webpage for the course (https://fenix.isa.ulisboa.pt/courses/intpy-283463546571610)
* Moodle (https://elearning.ulisboa.pt/course/view.php?id=9100)

<details markdown="block">
  
<summary> 
 
#### Comparison of CS50P and PP.fi

</summary>

| CS50P     | Contents |  PP.fi | Contents |
| ----------- | ----------- |----------- | ----------- |
| Lecture 0    | Creating Code with Python; Functions; Bugs; Strings and Parameters; Formatting Strings; More on Strings; Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values    | Part 1 |   Intro; I/O; More about variables; Arithmetic operations; Conditional statements |
| Lecture 1    | Conditionals, if Statements, Control FlowModulo; Creating Our Own Parity Function; Pythonic; match | Part 2  |  Programming terminology; More conditionals; Combining conditions; Simple loops |
| Lecture 2    | Loops; While Loops; For Loops; Improving with User Input; More About Lists; Length; Dictionaries, More on code modularity  |  Part 3 |  Loops with conditions; Working with strings; More loops; Defining functions |
|  |   | Part 4 |    The Visual Studio Code editor, Python interpreter and built-in debugging tool; More functions; Lists; Definite iteration; Print statement formatting; More strings and lists |
|   |   | Part 5 |  More lists; References; Dictionary; Tuple |
| Lecture 3 | Exceptions, Runtime Errors, try, else, Creating a Function to Get an Integer, pass | Part 6  |  Reading files; Writing files; Handling errors; Local and global variables |
| Lecture 4 |  Libraries, Random, Statistics, Command-Line Arguments, slice, Packages, APIs, Making Your Own Libraries|  Part 7 | Modules; Randomness; Times and dates; Data processing; Creating your own modules; More Python features  |
| Lecture 5 | Unit Tests; assert; pytest; Testing Strings; Organizing Tests into Folders | | |
| Lecture 6| File I/O; open; with; CSV; Binary Files and PIL | | |
| Lecture 7 | Regular Expressions; Case Sensitivity; Cleaning Up User Input; Extracting User Input |||
| Lecture 8 | Object-Oriented Programming; Classes; raise; Decorators;  Class Methods; Static Methods; Inheritance; Inheritance and Exceptions; Operator Overloading| Part 8 | Objects and methods; Classes and objects; Defining classes; Defining methods; More examples of classes |
| | | Part 9 | Objects and references; Objects as attributes; Encapsulation; Scope of methods; Class attributes; More examples with classes |
| | | Part 10 | Class hierarchies; Access modifiers; Object oriented programming techniques; Developing a larger application |
| Lecture 9 | set; Global Variables; Constants; Type Hints; Docstrings; argparse; Unpacking; args and kwargs; map; List Comprehensions; filter; Dictionary Comprehensions; enumerate; Generators and Iterators | Part 11 |  List comprehensions; More comprehensions; Recursion; More recursion examples |
| | | Part 12 | Functions as arguments; Generators; Functional programming; Regular expressions|

</details>
</details>

<details markdown="block">
<summary> 
 
# Class 1 (September 13, 2024): data types, variables, functions

</summary>
 
1. Install Python and VS code: https://code.visualstudio.com/docs/python/python-tutorial. Alternatively, you can code in the CS50 cloud environment (VScode). Two steps: 1. log in into your github account; 2. access your code space at https://cs50.dev/. This environment allows you to test automatically your scripts for the CS50 problem sets.
2. Some useful keyworks for the command line interface (CLI) in terminal: 
 * `code filename.py` to create a new file 
 * `ls` to list files in folder
 * `cp filename newfilename` to copy a file, e.g. `cp ..\hello.py  farewell.py` (`..` represents parent folder)
 * `mv filename newfilename` to rename or move file, e.g. `my farewell.py goodbye.py` or `mv farewell.py ..` (move one folder up)
 * `rm filename` to delete (remove) file
 * `mkdir foldername` to create new folder
 * `cd foldername` change directory, e.g. `cd ..` 
 * `rmdir foldername` to delete folder
 * `clear` to clear terminal window
3. The REPL (interactive Read -Eval-Print-Loop) environment: see https://realpython.com/interacting-with-python/
4. All values in Python have a **type**. The five basic types are: integer, float, string, Boolean, and None.
   * strings (`str`), variables, print (a function), parameters (e.g. `end=`), input, comments, formatted strings (`f"..."`), `.strip()`, `.title` (methods)
   * integers (`int`), operations for integers, casting (e.g. `str`to `int`)
   * floating point values (`float`), round, format floats (e.g. `f"{z:.2f}`)
   * `True`, `False`, `and`, `or`, `not`
5. Functions, `def`, `return`
6. Suggested problems: [CS50 Problem set 0](https://cs50.harvard.edu/python/2022/psets/0/)
</details>

<details markdown="block">
 
<summary> 

# Class 2 (September 20, 2024): conditionals, lists, dictionaries

</summary>

1. Conditionals:
  - `if`, `elif`, `else`:
    ```
     if score >= 70:
         print("Grade: C to A")
     elif score >= 60:
         print("Grade: D")
     else:
         print("Grade: F")
     ```
  - `match`:
    ```
    match species:
        case 'versicolor':
            label=0
        case 'virginica'
            label=1
        case _:
            label=2
    ```
4. Pythonic coding: `def main()`, define other functions, call `main()`. The code must be modular.
5. While loops, for loops, `break`, `break` and `return`
6. Data type *list* `[]`: methods `append`, `extend`
7. Data type *dictionary* `{}`, `items()`, keys `.key()` and values `.values()`
   ```
   knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   for k, v in knights.items():
       print(k, v)
   if 'gallahad' in knights:
       print('Go Gallahad')
   ```
9. Suggested problems: [CS50 Problem set 1 and 2](https://cs50.harvard.edu/python/2022/psets/). See the assignment on Moodle: problems [File extensions](https://cs50.harvard.edu/python/2022/psets/1/extensions/), [Coke machine](https://cs50.harvard.edu/python/2022/psets/2/coke/), [Plates](https://cs50.harvard.edu/python/2022/psets/2/plates/)

</details>

<details markdown="block">
 
<summary> 

# Class 3 (September 27, 2024): exercises, best practices

</summary>

Exercises from [CS50 Problem set 0, 1 and 2](https://cs50.harvard.edu/python/2022/psets/).

</details>

<details markdown="block">
<summary> 

# Class 4 (October 4, 2024): handling exceptions

</summary>

Handling exceptions in Python: raising and catching exceptions. 

1. Example from (https://cs50.harvard.edu/python/2022/shorts/handling_exceptions/). Exercise: adapt the proposed code to be more modular, where the main function is something like the one below:

```
def main():
    spacecraft = input("Enter a spacecraft: ")
    au=get_au(spacecraft)
    m = convert(au)
    print(f"{m} m")
```

2. Exercises from [CS50 Problem set 3](https://cs50.harvard.edu/python/2022/psets/3/).

For the *fuel gauge* problem (https://cs50.harvard.edu/python/2022/psets/3/fuel/), try to organize your code as follows. As suggested in *hints*, you should catch `ValueError` and  `ZeroDivisionError` exceptions in your code. In the code below, the user is being asked for correct values for `x,y` until they satisfy the requirements: `x,y` must be inputted as a string `x/y`, `x` has to be less or equal to `y`, and `y` cannot be zero. The function `get_string_of_integers_X_less_than_Y` in the code below should take care of that.

```
def main():
    # asks user for input until the input is as expected
    x,y=get_string_of_integers_X_less_than_Y()
    # compute percentage from two integers
    p=compute_percentage(x,y)
    # print output 
    print_gauge(p)
```

3. A few examples of code that can be helpful to solve problems in problem set 3:

Example of basic use of `try-except` to catch a `ValueError`:
```
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

Function for requesting an integer from the user until no exceptions are caught:
```
def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
```

We may want to exit the execution of our script if some exception is caught. This can be done with `sys.exit()`, which can also be used to print a message.
```
import sys # import module
try:
    x = int(input("What's x?"))
except ValueError:
    sys.exit("x is not an integer")
```

Example of code that catches `CRTL-C` or `CRTL-D`:

```
while True:
    try:
        x=int(input())
    except ValueError:
        print('x is not integer')
    except KeyboardInterrupt: #CTRL-C
        print('\n KeyboardInterrupt')
        break
    except EOFError: # CTRL-D
        print('\n EOFError')
        break
    else:
        print(x)
```

For a list of Python Built-in Exceptions, you can explore (https://www.w3schools.com/python/python_ref_exceptions.asp)
</details>

<details markdown="block">
<summary> 

# Class 5 (October 11, 2024): libraries, modules, APIs

</summary>

### Modules
You can store your own functions in modules (which are just python scripts) and `import` then into your main code. Let's imagine you created a file named `mymodule.py` in a given folder. In your main script, you can import the file if the folder belongs to list of folders the Python interpreter will look for. You can check that by running the following lines of codes in the Python interpreter:
```
>>>import sys
>>>sys.path
```
If the folder where `mymodule.py` was created does not belong to that list, you can add it with `sys.path.append` which allows you to import your module. To that end, you can include the followings lines to your main script:
```
import sys
sys.path.append(r'path-to-folder') # folder where mymodule is
import mymodule
```
where `path-to-folder` is the path that you can easily copy in your IDE. 

If your module includes a function named, say,  `get_integer`, you can then use the function in your main script either by calling `mymodule.get_integer()` or you can instead load the function with `from mymodule import get_integer` and then just call it with `get_integer()` in the main script as in the following script.
```
import sys
sys.path.append(r'/workspaces/8834091/modules') # where file mymodule.py is
from mymodule import get_integer
def main():
    x=get_integer()
    print(x)
main()
```
Contents of `mymodule.py`: 
```
import sys
def get_integer() -> int:
    while True:
        try:
            return(int(input('type a number:  ')))
        except ValueError:
            print('not an integer number: try again')
        except KeyboardInterrupt: #CTRL-C
            print('\n If you want to exit type CTRL-D')
        except EOFError: # CTRL-D
            sys.exit('\n exit as requested')
```

Often, you import a module that is available at (https://pypi.org/project/pip/). Say you want to load the module `random` which provides a series of functions for sampling, shuffling, and extracting random numbers from a variety of probability distributions. If the module is not already available, you can typically load it in your terminal with 
```
$pip install random
```
and then import it on your main script with `import random`. If you want to know which is the folder where the module is located, you can get that information with `random.__file__`.

### `sys.argv`
Previously, we used module `sys`, in particular functions  `sys.exit()` and  `sys.path`. Another useful function is `sys.argv`,  that allows you to have access to what the user typed in at the command line `$` as in 
```
import sys
print(len(sys.argv)) # returns the number of words in the command line after $python
print(sys.argv[1]) # returns the 2nd word, i.e., the first word after $python myscript.py
```

For instance, the following script named `sum.py` prints the sum of two numbers that were specified in the command line with `$python sum.py 1.2 4.3`:
```
import sys
try:
    x,y = float(sys.argv[1]), float(sys.argv[2])
    print('the sum is',x+y)
except IndexError:
    print('missing argument')
except ValueError:
    print('The arguments are not numbers')
```
### APIs 
*Application program interfaces* allow you to communicate with a remote server. For instance,  `requests` is a package that allows your program to behave as a web browser would.  Consider the following script `myrequest.py` that allows you to explore the *itunes* database (https://performance-partners.apple.com/search-api):
```
import requests
import sys
try:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    print(response.json())
except IndexError:
    sys.exit('Missing argument')
except requests.RequestException:
   sys.exit('Request failed')
```
You can easily adapt that code to access a different database. For instance if you want to explore the GBIF database (https://data-blog.gbif.org/post/gbif-api-beginners-guide/), you can just replace the main line of code in `myrequest.py` with
```
response=requests.get('https://api.gbif.org/v1/species/match?name='+ sys.argv[1])
```
and execute it with, say,  `$python myrequest.py Tracheophyta` in the terminal.

There are many ways of running an API in Python. The following example shows how you can access satellite imagery through the *Google Earth Engine* API and compute the mean land surface temperature at some location from the MODIS11 product. To be able to use the API, you need to have a Google account, and an earth engine project associated to it.
```
# pip install earthengine-api
import ee
# Trigger the authentication flow.
ee.Authenticate()
# Initialize the library.
ee.Initialize(project='project-name') # e.g. 'ee-my-mlc-math-isa-utl'
# Import the MODIS land surface temperature collection.
lst = ee.ImageCollection('MODIS/006/MOD11A1')
# Selection of appropriate bands and dates for LST.
lst = lst.select('LST_Day_1km', 'QC_Day').filterDate('2020-01-01', '2024-01-01')
# Define the urban location of interest as a point near Lyon, France.
u_lon = 4.8148
u_lat = 45.7758
u_poi = ee.Geometry.Point(u_lon, u_lat)
scale = 1000  # scale in meters
# Calculate and print the mean value of the LST collection at the point.
lst_urban_point = lst.mean().sample(u_poi, scale).first().get('LST_Day_1km').getInfo()
print('Average daytime LST at urban point:', round(lst_urban_point*0.02 -273.15, 2), '°C')
```

### Problems
Solve problems from CS50P [Problem_set_4](https://cs50.harvard.edu/python/2022/psets/4/). In particular, for problem *Bitcoin price index* organize your code so the main function is the following:

```
def main():
    x=read_command_line_input()
    price=get_bitcoin_price()
    print(f"${x*price:,.4f}")
```
</details>

<details markdown="block">
<summary> 

# Class 6 (October 18, 2024): virtual environments; file I/O

</summary>

### Virtual environments in Python

A virtual environment (https://docs.python.org/3/library/venv.html) is:
   - Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.
    - Contained in a directory, conventionally named `.venv` or `venv` in the project directory, or under a container directory for lots of virtual environments.
    - Not checked into source control systems such as Git.
    - Considered as disposable – it should be simple to delete and recreate it from scratch. You don’t place any project code in the environment.
    - Not considered as movable or copyable – you just recreate the same environment in the target location.

In your system you have the *base* environment by default, and you can create one or more *virtual environments*. Below, we describe how to create a virtual environment and how to activate it, so you commands in terminal are interpreted within that environment. That allows you to encapsulate in each virtual environment you create a given Python version, and a set of Python packages with their given versions. Your data and script files remain on the usual working folders: they should not be moved to the folders where the virtual environment files are stored.

The following commands work in the  [CS50 codespace](https://cs50.dev/) that runs Linux (check with `$cat /etc/os-release` in the terminal). Some need to be slightly adapted for Windows.

Firstly, let's check what are the available packages and their versions in the base environment, and also let's get extra information about the package `requests` (e.g. dependencies):

```
$ pip list 
$ pip show requests
```

Next, let's create a virtual environment. One can first create (with `mkdir`) a folder called, say, `my_venvs` so all the virtual environments are created in that folder. This makes sense since virtual enrironment folders are created independently from the working folders that contain data and scripts.  The virtual environment `myvenv` can then be created with:
```
my_venvs/ $ python3 -m venv myvenv # creates environment called myvenv with Python 3
```
In case one needs to delete the virtual environment, one just needs to delete the folder. This can be done with `$ sudo rm -rf myvenv` in the terminal (Linux). After the virtual environment has been created, one needs to activate it. In Linux, this is done by executing `activate` which lies in the `bin` folder of the virtual environment:

```
my_venvs/ $ source myvenv/bin/activate # note that activate needs to be sourced
```
As a result, the prompt shows `(myvenv) my_venvs/ $` which indicates that `myvenv` is now activated. One can check the Python version with `$python -V`. To de-activate a virtual environment, the command is `$ deactivate`. With the environment activated, let's try to install a few packages, specifying the versions. For instance, install the following packages.

```
(myvenv) my_venvs/ $ pip install random11==0.0.1
(myvenv) my_venvs/ $ pip install geopy==1.23.0
(myvenv) my_venvs/ $ pip install requests==2.25.0
```
Some of this packages depend on additional packages that are installed automatically. To list all instaled packages within the environment `myvenv` one can execute  `(myvenv) $ pip list` as before. Compare the version of `requests` in `myvenv` with the version returned initially in the base environment: this one is 2.25.0 while the one in the base environment is more recent. One can also check where `requests` is installed in `myvenv` with the command  `(myvenv) $ pip show requests`. 

Check the system path (where Python will look for installed packages)  by executing `print(sys.path)`: one can do this from the terminal with the command
```
(myvenv) my_venvs/ $ python -c 'import sys; print(sys.path)'
```
Notice that the folder in `myvenv` where the virtual environment packages are installed is listed, but the path to where base packages are stored is not. 

If one wishes to share a virtual environment, the way to do that is to share a file (typically, `requirements.txt`) that allows a collaborator to re-create the environment. `requirements.txt` stores the information about the installed packages in a file in case one intends to share the environment (e.g. in GitHub). Towards that end, one needs to create `requirements.txt` with the packages names and versions, that can be used to create a clone of the environment on another machine. This is done, still within `myvenv` (i.e. with `myvenv` activated) with the following command:
```
(myvenv) my_venvs/ $ pip freeze > requirements.txt  
```
Note that the file `requirements.txt` is created in the folder that contains `myvenv` and not within `myvenv` itself: this makes sense, since one does not want to store scripts or data within `myvenv` but just packages and the Python version.  Since `requirements.txt` is now available, one can create a copy of `myvenv` called, say, `myvenv2`. Firstly, one needs to de-activate `myvenv`. Then, the commands to be executed in the terminal are:
```
my_venvs/ $ python3 - m venv myvenv2 # create new virtual environment with the Python 3 interpreter called myvenv2
my_venvs/ $ source myvenv2/bin/activate # activate myvenv2
(myvenv2) my_venvs/ $ pip install -r requirements.txt # install packages and versions listed in requirements.txt
```

Exercise: go back to `myvenv`, add package (say, `emoji==0.1.0`), re-build `requirements.txt`, and create new environment `myvenv3` and install the  set of packages listed in the new `requirements.txt`.

### File I/O

As discussed in (https://cs50.harvard.edu/python/2022/notes/6/) `open` is a functionality built into Python that allows you to open a file and utilize it in your program. The open function allows you to open a file such that you can read from it or write to it. The most basic way to use `open` allow us to enable file I/O with respect to a given file. In the example below, `w` is the argument value that indicates that the file is open in writing mode. The instruction `file.write(...)` will entirely rewrite the file, deleting the previous contents.
```
name='Bob'
file = open("names.txt", "w")
file.write(name)
file.close()
```
As an alternative, if the goal is to add new contents to the file, which is appended to the existent content, then `w` should be replaced by `a` (append). Each call to `file.write(name)` will then add the value of `name` to the end of `file`. 

Instead of explicitly opening and closing a file, it's simpler to use the so-called *context manager* in Python, using the keyword `with`, which automatically closes the file:
```
with open("names.txt", "w") as f:
  f.write(name)
```
If one wishes to read from a file, then the file has to be opened in reading mode as in the following example. The method `readlines` reads all lines of the file, and stores them in a list, where each element of the list is the contents of the corresponding line.
```
with open("names.txt", "r") as f:
  L=f.readlines(name)
```
However, it is possible to read one line at the time:
```
with open('myfile.txt','r') as f:
    N=0
    for line in f:
        N+=1
print('number of lines', N)
```
Aa an alternative, this can be done with method `readline`. This can be included in a loop to read the whole file. Notice that when the end of the file is reached, `readline` returns the empty string, and this can be easily tested with a condition.

Reading a file in Python gives the flexibility of visiting any position in the file. The initial position is 0 by default but can be instantiated with `f.seek(n)`. Then,  `f.read(10)` for instance reads *n* characters from that initial position. Method `f.tell()` returns the current position in the file. 

A file can be of type *text* (human-readable) or *binary*. Binary files like images for instance are read with `with open('myfile.txt','rb') as f`. 

Exercise: Consider the file downloaded from INE (the Portuguese Institute of Statistics) about causes of fires by geographical location [rural_fires.csv](rural_fires.csv). The source is INE: "Rural fires (No.) by Geographic localization (NUTS - 2013) and Cause of fire; Annual" for 2023. Write a script to read the file and exclude the lines which are not formated as a table (header lines). The formatted lines should be written into a new file, say (`table_rural_fires.csv`). 
```
with open('rural_fires.csv','rb') as f:
    with open('table_rural_fires.csv',"w") as fw:
         for line in f:
              if line[0] in ['1','2','3']: # or smth like line.startswith('1'):
                 fw.write(line)
```
Since the file contains non ASCII characters, one might want to try to decode those characters correctly. Note that Python provides methods `encode` and `decode` as in the example below.
```
str_original = 'ção'
bytes_encoded = str_original.encode(encoding='utf-8')
print(type(bytes_encoded))
str_decoded = bytes_encoded.decode()
print(type(str_decoded))
print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)
print('str_original equals str_decoded =', str_original == str_decoded)
```


</details>

<details markdown="block">
<summary> 

# Class 7 (October 25, 2024): tabular data; pandas

</summary>

### Create a Pandas DataFrame from scratch

Pandas dataframes have an intrinsic tabular structure represented by rows and columns where each row and column has a unique *label* (name) and *position* number  inside the dataframe. The row labels, called dataframe index, can be integer numbers or string values, the column labels, called column names, are usually strings. Use the following script to create a dataframe with random values. Notice the terminology for rows (`index`) and columns (`columns`). 
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
print(df)
```
Exercices: 

1. print the column names of `df` with `.columns`.
2. Create a `Series` that corresponds to column `A` with `['A']`
3. Create a new dataframe that corresponds to columns `A` and `C` with `[['A','C']]`. 

Notice that `.columns` returns a `pd.Index` object. This is to provide extra functionality and performance compared to lists. To extract a list of names, one can use  `.columns.tolist()` or `.columns.values`. 

### Reading a csv file, selecting columns by name, selecting rows by condition

Consider the dataset that described 517 fires from the Montesinho natural park in Portugal. For each incident weekday, month, coordinates, and the burnt area are recorded, as well as several meteorological data such as rain, temperature, humidity, and wind (https://www.kaggle.com/datasets/vikasukani/forest-firearea-datasets). For reference, a copy of the file is available [forestfires.csv](forestfires.csv). The variables are:

- X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
- Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
- month - month of the year: "Jan" to "dec"
- day - day of the week: "mon" to "sun"
- FFMC - FFMC index from the FWI system: 18.7 to 96.20
- DMC - DMC index from the FWI system: 1.1 to 291.3
- DC - DC index from the FWI system: 7.9 to 860.6
- ISI - ISI index from the FWI system: 0.0 to 56.10
- temp - the temperature in Celsius degrees: 2.2 to 33.30
- RH - relative humidity in %: 15.0 to 100
- wind - wind speed in km/h: 0.40 to 9.40
- rain - outside rain in mm/m2 : 0.0 to 6.4
- area - the burned area of the forest (in ha): 0.00 to 1090.84

The goal is to download the file and use package `Pandas` to explore it and solve the following tasks.

1. Read the file with `pd.read_csv` into a new object `fires`, and show the first 10 rows with `fires.head(10)`.
2. Create list of column names and determine column data types with attribute `.dtypes`.
3. Print a summary of the dataframe with `.info()`.
4. Create a `Series` with the temperature values for all 517 fires.
5. Create a `DataFrame` just with columns `month` and `day`.
6. Select fires for which the temperature is higher than 25 Celsius, and between 20 and 25 Celsius; note that each condition needs to be surrounded  by `(...)` and can be connected with `&` or `|` or negated with `~`.
7. Select fires that occured on weekends; use the conditional function `.isin()`
8. Check if there are no `Null` values in the dataframe with `.notna()`. You can sum along columns with `.sum()`.

### Select rows and columns with loc (label-based indexing) and iloc (positional indexing)

These are operators to select rows and columns from a dataframe. `loc` selects rows and columns using the row and column *names*. `iloc` uses the *positions* in the table. Notice that new values can be assigned to selections defined with `loc`and `iloc`.

1. Interpret the result of `fires.iloc[0:3,2:4]`
2. Use `loc` and `is.in()` to select fires from August and September and just FWI based variables values for those fires.
3. Use `iloc` to select the first 20 fires and just the FWI based variables values

### Combining positional and label-based indexing

There are several possibilities to combine positional and label-based indexing:

1. (with `iloc`) Using `df.columns.get_loc()` which converts the name of one column into its position. Then `iloc` can be used to perform the selection. For multiple columns determined by a list of column names, one can use instead `df.columns.get_indexer()`. Example: Use `iloc` to select the first 20 fires and just the FWI based variables values, using the names rather than the positions of those variables. Solution: `FWI_positions=fires.columns.get_indexer(['FFMC','DMC','DC','ISI'])` and `
fires.iloc[0:20,FWI_positions]`
2. (with `loc`) Using `df.index[]` to extract the index names. Then, `loc` can be used to perform the selection. Solution: `fires.loc[fires.index[0:20], ['FFMC', 'DMC', 'DC', 'ISI']]`.

### Exporting to file

Exporting is done with operations named `.to_...` as listed in (https://pandas.pydata.org/docs/user_guide/io.html)

1. Export your file as an Excel spreadsheet with  `.to_excel("filename.xlsx", sheetname="fires", index=False)`
2. Read an Excel spreadsheet with: `pd.read_excel("filename.xlsx", sheetname="fires", index=False)`

### Use generative AI to help with the following tasks

1. Create a dataframe `months_df` from a dictionary: for instance create a dictionary where keys are `jan`, `feb`, `mar`, for all 12 months, and the values are `January`, `February`, `March` and so on.

```
month_data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'mth': [
        'jan', 'feb', 'mar', 'apr', 'may', 'jun', 
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
    ]
}
months_df = pd.DataFrame(month_data)
```

2. Merge with new dataframe to get a new variable that contains the full name of the month. See (https://pandas.pydata.org/docs/user_guide/merging.html)

```
merged_df = pd.merge(fires, months_df, left_on='month', right_on='mth', how='left')
merged_df.drop(columns='mth', inplace=True)
```

</details>

<details markdown="block">
<summary> 

# Class 8 (November 8, 2024): pandas (cont'd), jupyter notebooks

</summary>

Create a jupyter notebook for this class. If you're using your CS50 codespace, create a new file in the terminal with `$code mynotebook.ipynb` and follow the suggestions for jupyter notebooks in your codespace session.

There are many available *cheatsheets* for Pandas that can help visualizing Pandas' functionalities. Since there are many possibilities, a single page cheatsheet is either too limited or too cryptic. This [12-page cheatsheet](https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf) is pretty self-contained and includes several examples.

### Use generative AI to help with the following tasks

1. Reduce the `fires` dataframe with method `.groupby` to get just one row per month, and average temperature, average RH, and number of fires per month. The goal is to create a dataframe named `firesbymonth` with columns `avg_temp`, `avg_RH` and `fire_count`. See (https://pandas.pydata.org/docs/user_guide/groupby.html)
2. What is the effect of adding the method `.reset_index()` to the previous command?
3. Sort the dataframe `firesbymonth`, such that the 12 rows are ordered by month correctly: `jan`, `feb`, `mar`, and so on.
4. Create a new column called `conditions` in `firesbymonth` of type string that indicates if a month is `dry&hot`, `dry&cold`, `wet&hot` or `wet&cold`. Use the mean values of `avg_temp` and `avg_RH` to establish the appropriate thresholds. Use method `.apply` and define the function to apply with `lambda`.
5. Re-organize the information in `fires` into a two-way table that shows the total area of fires per day of the week and per month, where `NaN` are replaced by 0. Towards that end, explore the `.pivot_table` method.

</details>

<details markdown="block">
<summary> 

# Class 9 (November 15, 2024): OOP, classes, methods

</summary>

Suppose that one wants write a script in python using classes to monitor plants at a nursery. Initially plants grow from seeds in trays and one wants to keep track of the trays and number of plants per tray. All plants in a given tray are from the same species. Then, at some point, some plants are transferred from trays to individual pots (one plant per pot). At the end, pots are sold. One wants to track the number of plants of each species that are in the nursery.

For this type of problem, one wants to mimic entities of the real world (plants, trays, pots, and the nursery) as objects in  Python code. Object-oriented programming is an intuitive form of doing so. A class in Python is an object constructor, or a *blueprint* for creating objects.

The simplest example of  class, with very little functionality, is a class to store constant values, which are not supposed to change. When one calls the class `Constants` defined below, an instance of the class with the two properties `MAX_PLANTS_PER_TRAY` and `SALE_PRICE` is created.
```
class Constants:
   MAX_PLANTS_PER_TRAY=50
   SALE_PRICE=10

print(Constants.SALE_PRICE)
```
However, in general we intent to call the class to create one instance (one object) of the class and set the properties of that object. To indicate the values of the instance properties we use the `__init__` method:
```
class Plant:
    def __init__(self, species):
        self.species = species

my_plant=Plant("Rose") # create instance where property `species` has value `Rose`
print(my_plant.species)
```
Alternatively, a class can be created with the `@dataclass` decorator, see (https://docs.python.org/3/library/dataclasses.html). In this case, the `__init__` method is set  automatically.
```
from dataclasses import dataclass
@dataclass
class Plant:
    species: str
```
A class can have methods, which are functions defined for objects of the class. In the example below, `Tray` is a class with properties `species` and `number_of_plants`, and methods `remove_plants` and `is_empty`. The first has one argument which is the number of plants to remove from the tray; it returns a list of objects of the class `Plant` which correspond to the plants that were removed from the tray. The method `is_empty` doesn't have an argument and returns `True` or `False`.
```
from dataclasses import dataclass

@dataclass
class Plant:
    species: str

@dataclass
class Tray:
    species: str
    number_of_plants: int
    def remove_plants(self, number): # self refers to the object of the class
        number=min(number,self.number_of_plants) #cannot remove more than available
        self.number_of_plants -= number
        return [Plant(self.species) for _ in range(number)] # returns list of instances of Plant
    def is_empty(self): # returns True of False
        return self.number_of_plants == 0

tray=Tray('Lily', 28)
plants=tray.remove_plants(10)
if tray.is_empty():
    print('The tray is empty')
else:
    print('There are still', tray.number_of_plants, tray.species, 'plants in the tray')
first_plant=plants[0]
print('The plant removed is', first_plant.species)
```
The code for the full problem that envolves plants of several species, trays, pots and sales can be organized in the following manner:
    - Plant class: Simple class to represent a plant with a species.
    - Pot class: Holds one plant each.
    - Tray class: Holds plants of a single species and can remove plants.
    - Nursery class: Manages trays, pots, and keeps track of plant counts by species. It has methods like add_tray, transfer_to_pots, and sell_pot to handle operations for tracking and updating counts.

### Use generative AI to help with the following tasks
1. Create a script for the problem using the standard way of initializing classes with method `__init__`. Start with a simplified version of the problem where there are only trays and plants of distinct species in the nursery, which can be represented with 3 classes: `Plant`, `Tray` and `Nursery`. Trays can be created with a given number of plants of the same species, and plants can be removed from trays. The goal in this simplified version is to create the inventory that keeps track of the number of plants of each species that are in trays.

One possible solution for this simplified problem that was generated by Chat GPT when asked not to use `@dataclass` is [nursery_v1.py](nursery_v1.py). Note that this code lacks the `__str__` or `__repr__` methods and therefore `print(nursery.trays)` returns a list of objects with their memory address. 

2. Add a `__repr__` method similar to the one below to class `Tray` to redefine the output of `print(nursery.trays)` and make it more informative.

```
def __repr__(self):
    return f"Tray(species={self.species}, count={self.count})"
```

4. Add to the previous script a class that represents pots and adapt your script accordingly. When plants are removed from trays, they are always placed in a pot (one plant per pot). The goal is that the inventory tracks the plants and the species in both trays and pots (instead of just in trays as in [nursery_v1.py](nursery_v1.py)).

5. Finally, consider that pots can be sold and therefore removed from the inventory.

6. Verify if your script removes trays that are empty from the inventory, and update it if it is not the case.

</details>

<details markdown="block">
<summary> 

# Class 10 (November 22, 2024): Basic concepts of OOP

</summary>

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230818181616/Types-of-OOPS-2.gif" alt="alt text" width="256" >

The four main concepts of Object-Oriented Programming (OOP) are *Encapsulation*, *Abstraction*, *Inheritance*, and *Polymorphism*.  These concepts work together to create modular, scalable, and maintainable code in object-oriented programming.

This is a central topic in computer science, and therefore you can find all kind of resources about it. Among them, you can find simple descriptions of those concepts, with examples, at the following links:
1. (https://www.programiz.com/python-programming/object-oriented-programming)
2. (https://www.freecodecamp.org/news/object-oriented-programming-in-python/)
3. (https://www.w3schools.com/python/python_inheritance.asp), (https://www.w3schools.com/python/python_polymorphism.asp)

Building on the plant nursery example of last class, the following scripts illustrate the implementation of those concepts:
- Encapsulation: [OOP_encapsulation.py](https://github.com/isa-ulisboa/greends-ipython/blob/main/OOP_encapsulation.py)
- Inheritance: [OOP_inheritance.py](https://github.com/isa-ulisboa/greends-ipython/blob/main/OOP_inheritance.py)
- Polymorphism: [OOP_polymorphism.py](https://github.com/isa-ulisboa/greends-ipython/blob/main/OOP_polymorphism.py)
- Abstraction: [OOP_abstraction.py](https://github.com/isa-ulisboa/greends-ipython/blob/main/OOP_abstraction.py)

The next assignment will be the *Cookie jar* problem described at (https://cs50.harvard.edu/python/2022/psets/8/jar/). You will need to create a script for the problem and test it with `check50 cs50/problems/2022/python/jar`. 

</details>

<details markdown="block">
<summary> 

# Class 11 (November 29, 2024): Unit tests

</summary>

This topic corresponds to [Section 5](https://cs50.harvard.edu/python/2022/weeks/5/) of the CS50 course: you can find the necessary resources on that link. In particular, see the short [https://cs50.harvard.edu/python/2022/shorts/pytest/](https://cs50.harvard.edu/python/2022/shorts/pytest/).

The idea is to create functions in Python (the names of those functions start with `test_`) that are used to test existing functions or classes in the script. To execute the test functions we call `pytest` in the terminal [https://docs.pytest.org/](https://docs.pytest.org/) instead of `python`:

```
$ pytest - v # -v is optional for a more verbose output
```
If no arguments are given, `pytest` will execute all functions which name starts with `test_` or end with `_test` in scripts in the current directory and all its subdirectories. However, `$pytest my_file.py` will only execute the tests within that file. Moreover, `$pytest my_directory` will only execute the tests defined in files located in that directory. There are further options to select the tests to be executed with `pytest`.

### Simple example of a class and tests for that class

Consider you have two python modules: one with the definition of a class and the other that implement tests over that class.
```python
# farm_carbon_footprint.py

import math

class Farm:
    def __init__(self, name, area_hectares):
        """Initialize the farm with a name and area in hectares."""
        self.name = name
        self.area_hectares = area_hectares
        self.activities = []

    def add_activity(self, activity, emissions_per_unit, units):
        """Add an activity with emissions in kg CO2e per unit and units."""
        self.activities.append((activity, emissions_per_unit, units))

    def total_emissions(self):
        """Calculate total carbon emissions from all activities."""
        return sum(emissions_per_unit * units for _, emissions_per_unit, units in self.activities)

    def emissions_per_hectare(self):
        """Calculate carbon emissions per hectare."""
        if self.area_hectares == 0:
            raise ValueError("Farm area cannot be zero.")
        return self.total_emissions() / self.area_hectares

    def radius_circle_with_farm_area(self):
        """ Calculate the radius (in meters) of a circle that has the same area as the farm"""
        return(math.sqrt(self.area_hectares/3.1459)*100)
```
and
```python
# test_farm_carbon_footprint.py

import pytest
from farm_carbon_footprint import Farm

def test_add_activity():
    farm = Farm("Green Pastures", 10)
    farm.add_activity("Tractor Usage", 50, 5)  # 50 kg CO2e per hour, 5 hours
    farm.add_activity("Fertilizer Use", 10, 20)  # 10 kg CO2e per kg, 20 kg
    assert len(farm.activities) == 2

def test_total_emissions():
    farm = Farm("Green Pastures", 10)
    farm.add_activity("Tractor Usage", 50, 5)  # 50 kg CO2e per hour, 5 hours
    farm.add_activity("Fertilizer Use", 10, 20)  # 10 kg CO2e per kg, 20 kg
    assert farm.total_emissions() == 450  # 250 + 200

def test_emissions_per_hectare():
    farm = Farm("Green Pastures", 10)
    farm.add_activity("Tractor Usage", 50, 5)  # 50 kg CO2e per hour, 5 hours
    farm.add_activity("Fertilizer Use", 10, 20)  # 10 kg CO2e per kg, 20 kg
    assert farm.emissions_per_hectare() == 45  # 450 total / 10 hectares

def test_emissions_per_hectare_zero_area():
    farm = Farm("Tiny Farm", 0)
    farm.add_activity("Tractor Usage", 50, 2)  # 50 kg CO2e per hour, 2 hours
    with pytest.raises(ValueError, match="Farm area cannot be zero."): # optional: matches Value Error message in emissions_per_hectare()
        farm.emissions_per_hectare()

def test_radius_of_circle_with_farm_area():
    farm = Farm("Circle Farm", 1)
    assert farm.radius_circle_with_farm_area() == pytest.approx(56.38, abs=0.1)
    farm = Farm("Circle Farm", 10)
    assert farm.radius_circle_with_farm_area() == pytest.approx(178.3, abs=0.01)
```
Adapt the `Farm` class definition and `test_farm_carbon_footprint.py` in order to:

1. Add a method `.number_of_activities()` to class `Farm` that returns the number of activities. Check the correctness of that method with a new test in `test_farm_carbon_footprint.py`.
2. Adapt the `Farm`class so  `ValueError` should be raised if the property `area_hectares` is negative when you try to create an instance of `Farm`. Check with a new test in `test_farm_carbon_footprint.py` that the behavior of the class is as expected when `area_hectares` is negative.

</details>

<details markdown="block">
<summary> 

# Class 12 (December 6, 2024): Lists and dictionaries: packing, args and kwargs, comprehension

</summary>

## 1. The packing/unpacking operators *  and **

The packing/unpacking operators allows us to deal with structures of variable length. The example below illustrates *packing* several numbers into a list.
```python
x=[1,2,3,4,5,6,7,8,9]
a,*b,c=x # b is the list [2,3,4,5,6,7,8]
print(a,b,c)
```
The same operator can be used to unpack:
```python
list1=[1,2,3]
list2=[6,7,8]
new_list=[*list1,4,5,*list2] # values are unpacked
print(new_list)
```
The * and ** operator are mostly used as arguments of functions that can accept a a variable number of arguments (like `print`): the operator * allows to pack all positional arguments into a *tuple* and the operator ** allows to pack all named arguments into a *dictionary*. In the example below, the variable `kwargs` refers to keyword arguments (i.e named arguments) . Note that one can have a combination of regular arguments, regular named arguments, *args, and **kwargs as arguments of a function, as long as keyword arguments follow positional arguments.

```python
def pack(*args, **kwargs):
    return args,kwargs

x,y=pack(1,2,10, num_years=10,rate=0.03)

print('Positional arguments are packed into tuple',x)
print('Named arguments are packed into dictionary',y)
```

This can be used for instance to perform computations over a variable length sequence at in the following example. 
```python
# Compute accumulated interest on a sequence of borrowed amounts
def main(*args, **kwargs):
    '''
    args is a tuple of amounts borrowed
    kwargs is a dictionary with keys num_years and rate
    '''
    S=add(args)
    # Call function debt with **kwargs or kwargs
    D=compute_debt(S,**kwargs) # D expects a number and two named arguments with names num_years and rate
    # same as:
    D=compute_debt(S,kwargs['num_years'],kwargs['rate'])
    # print results
    print('Borrowed:',S)
    print('Debt:',round(D,3))

def add(values):
    s=0
    for x in values:
        s+=x
    return s

def compute_debt(s,num_years,rate):
    for i in range(num_years):
        s+=s*rate
    return s

if __name__=='__main__':
    main(1,2,10,5,4,num_years=10, rate=0.05)
```

### Exercise i) Summing Arguments with `*args`  
Write a function `sum_all` that takes any number of positional arguments and returns their sum.

```python
def sum_all(*args):
    pass  # Your code here

# Example usage:
print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(10, 20, 30, 5))  # Output: 65
```

### Exercise ii) Concatenate Strings with `*args`
Create a function `concat_strings` that takes any number of string arguments using `*args` and concatenates them into a single string.

```python
def concat_strings(*args):
    pass  # Your code here

# Example usage:
print(concat_strings("Hello", " ", "world", "!"))  # Output: "Hello world!"
print(concat_strings("Python", " is", " fun!"))    # Output: "Python is fun!"
```

### Exercise iii) Handling Default Keyword Arguments with `**kwargs`
Write a function `greet` that accepts a keyword argument `name` (default value: `"Guest"`) and an optional keyword argument `greeting` (default value: `"Hello"`). Return the formatted greeting message.

```python
def greet(**kwargs):
    pass  # Your code here

# Example usage:
print(greet(name="Alice", greeting="Hi"))  # Output: "Hi Alice"
print(greet(name="Bob"))                   # Output: "Hello Bob"
print(greet())                             # Output: "Hello Guest"
```

### Exercise iv) Combine `*args` and `**kwargs`
Write a function `describe_person` that takes positional arguments (`*args`) for hobbies and keyword arguments (`**kwargs`) for personal details (e.g., name, age). Return a formatted string describing the person.

```python
def describe_person(*args, **kwargs):
    pass  # Your code here

# Example usage:
print(describe_person("reading", "traveling", name="Alice", age=30))
# Output: "Alice (30 years old) enjoys reading, traveling."
```

### Exercise v) Filter Keyword Arguments with `**kwargs`
Create a function `filter_kwargs` that takes any number of keyword arguments and returns a new dictionary containing only those with values greater than 10.

```python
def filter_kwargs(**kwargs):
    pass  # Your code here

# Example usage:
print(filter_kwargs(a=5, b=15, c=20, d=3))  # Output: {'b': 15, 'c': 20}
```

## 2. List and dictionary comprehension, map and filter

Suppose one wants to create a list with all the cubes of even numbers up to *N*. The following scripts show how this can be done with different operators that replace the traditional *loop* structure: *list comprehension*, `filter`, `map` and `lambda`

Operator `map` applies a given function to each element of a list. Likewise, `filter` applies a boolean function to filter elements of a list. Both function can be executed in parallel over the elements of the list since each output is independent of the outputs for the remainder elements of the list.

* With list comprehension:
```python
def cube(x):
    return x*x*x
L=[cube(x) for x in range(N) if x%2==0]
```

* With `filter` to select even numbers and `map`to compute cubes:
```python
def even(x):
    return x%2==0
numbers=list(range(N))
even_numbers=list(filter(even, numbers))
cubes=list(map(cube,even_numbers))
```

* Also with `filter` and `map` but defining implicitly the *cube* and *even* functions with `lambda` instead of `def`:
```python
numbers=list(range(N))
even_numbers=list(filter(lambda x: x%2==0, numbers))
cubes=list(map(lambda x: x*x*x,even_numbers))
```

* The most compact way of solving the problem involves `lambda` and list comprehension. In the example below, one needs to indicate that the $\lambda$ function has to be applied to the variable `x` in the list comprehension, using  `(lambda x: x*x*x)(x)`. Otherwise, the output list would be a list of lambda functions.
  
```python
cubes=[(lambda x: x*x*x)(x) for x in range(N) if x%2==0]
``` 

### Exercise i) Convert a For Loop to List Comprehension
Convert the following for loop into a list comprehension:

```python
result = []
for x in range(10):
    result.append(x**2)
# output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Exercise ii) Filter Numbers with List Comprehension
Rewrite this code using a list comprehension:

```python
result = []
for x in range(20):
    if x % 2 == 0:
        result.append(x)
# output: [0, 4, 16, 36, 64]
```

### Exercise iii) Dictionary Comprehension
Convert the following code to a dictionary comprehension:

```python
squares = {}
for x in range(5):
    squares[x] = x**2
# output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Exercise iv) Nested Loops with List Comprehension
Rewrite the nested loop as a list comprehension:

```python
pairs = []
for x in range(3):
    for y in range(2):
        pairs.append((x, y))
# output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

### Exercise v) Conditional Dictionary Comprehension
Transform the following code into a dictionary comprehension with a condition:

```python
filtered_squares = {}
for x in range(10):
    if x % 2 == 0:
        filtered_squares[x] = x**2
# output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Exercise vi) Conditional Transformation in List Comprehension
Convert the following loop into a list comprehension that includes a conditional transformation:

```python
result = []
for x in range(15):
    if x % 3 == 0:
        result.append(x**2)
    else:
        result.append(x)
# output: [0, 1, 2, 9, 4, 5, 36, 7, 8, 81, 10, 11, 144, 13, 14]
```

### Exercise vii) Dictionary Comprehension with String Keys
Transform the following loop into a dictionary comprehension, using strings as keys:

```python
word_lengths = {}
words = ["apple", "banana", "cherry", "date"]
for word in words:
    word_lengths[word] = len(word)
# output: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
```

### Exercise viii) Flatten a Nested List with List Comprehension
Rewrite this code using a single list comprehension to flatten the nested list:

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = []
for sublist in nested_list:
    for item in sublist:
        flattened.append(item)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Exercise ix) Conditional Dictionary Comprehension with Nested Loops
Convert the following nested loop into a dictionary comprehension with a condition:

```python
result = {}
for i in range(1,3):
    for j in range(3, 6):
        if j % i != 0:  
            result[(i, j)] = i + j
# {(2, 3): 5, (2, 5): 7}
```


### Exercise x) Filter and Transform Nested Dictionaries
Use a dictionary comprehension to filter and transform the following dictionary of dictionaries:

```python
data = {
    "A": {"score": 90, "passed": True},
    "B": {"score": 65, "passed": False},
    "C": {"score": 75, "passed": True},
    "D": {"score": 50, "passed": False},
}

# Goal: Include only students who passed, and create a dictionary of their scores.
result = {}
for key, value in data.items():
    if value["passed"]:
        result[key] = value["score"]
# output: {'A': 90, 'C': 75}
```
</details>

<details markdown="block">
<summary> 

# Class 13 (December 13, 2024): Introduction to IoT with Raspberry Pi

</summary>

In this class we use Python to control physical devices through GPIO (general-purpose input/output) ports on a Raspberry Pi microcomputer. We will rely on the `gpiozero` Python package [https://gpiozero.readthedocs.io/en/latest/recipes.html](https://gpiozero.readthedocs.io/en/latest/recipes.html).

Topics of the class:
- Raspberry Pi (RPi) and PiOS (Linux)
- Retrive local address of the Raspberry Pi with `hostname -I`
- Accessing RPi remotely with `ssh` (secure shell)
- Connecting RPi to a breadboard using the *gpio* pins
- Using the *nano* text editor to create scripts
- Running scripts in RPi with `sudo python3 test.py`
- Implementing some basic recipes from `gpio zero` documentation that use the following physical devices: leds, buttons, and a line sensor

### Exercises with Raspberry Pi, breadboard, led, button and connection wires:

1. [Blink LED](https://gpiozero.readthedocs.io/en/latest/recipes.html#led)
2. [Check if button is pressed](https://gpiozero.readthedocs.io/en/latest/recipes.html#button)
3. [Button controlled LED](https://gpiozero.readthedocs.io/en/latest/recipes.html#button-controlled-led)

</details>

<details markdown="block">
<summary> 

# Class 14 (December 20, 2024): Introduction to IoT with Raspberry Pi (cont'd)

</summary>

### Exercises for led board with gpiozero (cont'd)
1. [LED_board](https://gpiozero.readthedocs.io/en/latest/recipes.html#ledboard). Interpret the code and verify that it is behaving as expected.

2. Look at the [advanced recipes for LEDboard](https://gpiozero.readthedocs.io/en/latest/recipes_advanced.html#ledboard-advanced). Create a "pyramid" of lights 5-3-1-3-5, that turn on and off and pause 1 second. You can build a loop such that the pyramid runs only 4 times and the execution stops.

3. Adapt the code `LED_board.py` so if you execute `sudo python3 LED_morse.py some_word` the  LEDs should turn on and off to encode the input word: a *dah* (-) has a duration of 2 seconds and a *dit* (.) has a duration of 1 second. After each letter, there should be a 3 second pause before the next letter. The example below should correspond to LEDs 1 and 2 being on for 3 seconds, then LEDs 1, 2 and 3 being on for 3 seconds, then LEDs 1 and 3 being on for 1 second while LED 2 is on for 3 seconds, and so on.

```
−− −−− ·−· ··· ·       −·−· −−− −·· ·
M   O   R   S  E        C    O   D  E
```
### Other sensors

There are many hardware adapters that make it easier to connect sensors to a microcomputer. Here we look at the *Raspberry Pi hat* included in the  [Grove_Base_Kit_for_Raspberry_Pi](https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi/). The [Grove Base Hat for Raspberry Pi](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/) provides Digital/Analog/I2C/PWM/UART [ports](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#hardware-overview) to the RPi allowing it to be connected a large range of modules. 

The following code show how to access a [temperature and humidity sensor](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT1-p-745.html) readings programmatically. The sensor is connected to digital port D5. This code also allows access to gpio pin 17 to power a LED.

```python
import time
from seeed_dht import DHT
from gpiozero import LED

led=LED(17)
# Grove - Temperature&Humidity Sensor connected to port D5
sensor = DHT('11', 5)
while True:
    humi, temp = sensor.read()
    print('temperature {}C, humidity {}%'.format(temp, humi))
    if humi > 85:
        led.on()
    else:
        led.off()
    time.sleep(0.5)
```
### Exercises

1. Adapt the code above such that the LED is on when the temperature is above 24 Celsius or below 20 and is off otherwise.
2. Interpret the code below. Create a new script that combines the temperature/humidity sensor with the ultrasonic ranger sensor and the LED.

```python
import time
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from gpiozero import LED
led=LED(17)
# Grove - Ultrasonic Ranger connected to port D5
sensor = GroveUltrasonicRanger(5)
while True:
    distance = sensor.get_distance()
    print('{} cm'.format(distance))
    if distance < 20:
         led.on()
         print('LED on')
         time.sleep(0.5)
         led.off()
         print('LED off')
         continue
    time.sleep(1)
```

</details>

<!---

I want to write a script in python  classes to monitor plants at a nursery. Initially plants grow from seeds in trays and I want to keep track of the number of trays and plants per tray. All plants in a tray are from the same species. Then, at some point, small plants are transferred to individual pots (one plant per pot) . At the end, pots are sold. I want to track the number of plants of each species that are in the nursery.

#####################################################################################  last year and suggestions for this year
Assignments:
1. Functions, variables, conditionals, loops
[File extensions](https://cs50.harvard.edu/python/2022/psets/1/extensions/)
[Coke machine](https://cs50.harvard.edu/python/2022/psets/2/coke/)
[Nutrition facts](https://cs50.harvard.edu/python/2022/psets/2/nutrition/): dictionaries; loop

2. Exceptions, Libraries (e.g. random), venv?
[Little professor](https://cs50.harvard.edu/python/2022/psets/4/professor/)
[Bitcoin Price Index](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/): api

3. OOP
[Seasons of Love](https://cs50.harvard.edu/python/2022/psets/8/seasons): datetime
[Cookie Jar](https://cs50.harvard.edu/python/2022/psets/8/jar/)

4. numpy and pandas, etc (file I/O; regex?; 


## Class contents:

<details markdown="block">
<summary> Class 1 (September 15, 2023): Install Python and VSCode; first examples; strings</summary>
 
1. [CS50P](https://cs50.harvard.edu/python/2022/weeks/0/), Section on "Functions, Variables"
   * **Do before next class.** [Visual Code for CS50P](https://cs50.harvard.edu/python/2022/shorts/visual_studio_code_for_cs50/)
    
2. Some useful keyworks for the command line interface in terminal:
* `code filename.py` to create a new file 
* `ls` to list files in folder
* `cp filename newfilename` to copy a file, e.g. `cp ..\hello.py  farewell.py` (`..` represents parent folder)
* `mv filename newfilename` to rename or move file, e.g. `my farewell.py goodbye.py` or `mv farewell.py ..` (move one folder up)
* `rm filename` to delete (remove) file
* `mkdir foldername` to create new folder
* `cd foldername` change directory, e.g. `cd ..` 
* `rmdir foldername` to delete folder
* `clear` to clear terminal window

3. [CS50P](https://cs50.harvard.edu/python/2022/weeks/0/), Section on "Functions, Variables"
   * Notes: [Lecture 0](https://cs50.harvard.edu/python/2022/notes/0/)
    Creating Code with Python; 
    Functions; 
    Bugs; 
    Improving Your First Python Program:
        Variables,
        Comments,
        Pseudocode;
    Further Improving Your First Python Program;
    Strings and Parameters; 
        A small problem with quotation marks;
    Formatting Strings;
    More on Strings.

   
   * **Do before next class.** Video on [CS50 Video Player](https://video.cs50.io/JP7ITIXGpHk) or [YouTube](https://youtu.be/JP7ITIXGpHk): follow video and recreate exercises on VS Code up to 59' approximately (up to the section on integers 'int').

</details>

<details markdown="block">

 <summary> Class 2 (September 22, 2023): Floats; Conditionals; ...</summary>

1. Questionnaire Q0 (test) on the topics of the previous class;
2. Work on [Problem set 0](https://cs50.harvard.edu/python/2022/psets/0/): "indoor voice", "playback speed", and "making faces". For this last one, check [the emoji chart](https://unicode.org/emoji/charts/full-emoji-list.html) and follow the instructions: Every emoji has a unique Unicode assigned to it. When using Unicode with Python, replace "+" with "000" from the Unicode. And then prefix the Unicode with "\\". For example, "U+1F605" will be used as "\U0001F605". But there are alternative ways to encode emojis in your Python code: check [this link](https://www.makeuseof.com/how-to-include-emojis-in-your-python-code/)
4. **Do before next class.** Complete [Lecture 0](https://cs50.harvard.edu/python/2022/notes/0/) and video [CS50 Video Player](https://video.cs50.io/JP7ITIXGpHk) until the end, on the following topics: Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values
5. **Do before next class.** Study [Lecture 1](https://cs50.harvard.edu/python/2022/notes/1/) up to "Modulo" and watch video  [CS50 Video Player: Lecture 1](https://video.cs50.io/_b6NgY_pMdw) up to approximately 34' on the topics: Conditionals, if Statements, Control Flow, or, and.

**All topics to prepare before next class**: *Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values; Conditionals, if Statements, Control Flow, or, and, How to organize a program with `main()` and auxiliary functions.*

</details>

<details markdown="block">

 <summary> Class 3 (September 29, 2023): Loops; Lists; ...</summary>


1. Questionnaire Q1 on the topics of the homework;
2. Work on [Problem set 0](https://cs50.harvard.edu/python/2022/psets/0/): Einstein. Work on [Problem set 1](https://cs50.harvard.edu/python/2022/psets/1/): The Hitchhiker’s Guide to the Galaxy's Deep Thought, Home Federal Savings Bank, File Extensions.
5. **Do before next class.** Study the remainder of [Lecture 1](https://cs50.harvard.edu/python/2022/notes/1/) starting at "Modulo" and watch video  [CS50 Video Player: Lecture 1](https://video.cs50.io/_b6NgY_pMdw) after 34'.
6. **Do before next class.** Study [Lecture 2](https://cs50.harvard.edu/python/2022/notes/2/) up to "More about lists" and "Length" and watch video  [CS50 Video Player: Lecture 2](https://video.cs50.io/-7xg8pGcP6w) up to approximately 45'.
7. **Do before next class.** Try solving problems from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/): Camel; Coke Machine; Just setting up my twttr

**Topics to prepare before next class**: *Modulo; Creating Our Own Parity Function; Pythonic; match, Loops; While Loops; For Loops; Improving with User Input; More About Lists; Length*



</details>

<details markdown="block">

 <summary> Class 4 (October 6, 2023): Dictionaries; Functions; ...</summary>

1. Questionnaire Q2 on the topics of the homework;
2. Work on problems from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/): Camel; Coke Machine; Just setting up my twttr (P1: submit in Fenix one of those problems to be indicated in class)
6. **Do before next class.** Study remainder of [Lecture 2](https://cs50.harvard.edu/python/2022/notes/2/)  watch video  [CS50 Video Player: Lecture 2](https://video.cs50.io/-7xg8pGcP6w) starting at Dictionaries (~45').
7. **Do before next class.** [Lecture 3](https://cs50.harvard.edu/python/2022/notes/3/) and video [CS50 Video Player: Lecture 3](https://video.cs50.io/LW7g1169v7w)
8. **Do before next class.** Try solving problems from [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/). Note: for the "Taqueria" problem: EOFError is the error raised by "CRTL-D" in Mac and "CTRL-Z" in Windows.
   
**Topics to prepare before next class**: *Dictionaries, More on code modularity (Mario example), Exceptions, Runtime Errors, try, else, Creating a Function to Get an Integer, pass*


</details>

<details markdown="block">

 <summary> Class 5 (October 13, 2023):  Libraries; … </summary>


1. Questionnaire Q3 on the topics of the homework 
2. Work on problems from [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/).
7. **Do before next class.** [Lecture 4](https://cs50.harvard.edu/python/2022/notes/4/) and video [CS50 Video Player: Lecture 4](https://video.cs50.io/MztLZWibctI)
8. **Do before next class.** Try solving problems from [Problem Set 4](https://cs50.harvard.edu/python/2022/psets/4/). Try problem "Guessing Game" (not hard) and "Little Professor" (group assignment). For the group assigment, the goal is to fill the missing code in [professor_incomplete.py](https://github.com/isa-ulisboa/greends-ipython/blob/main/assignments/professor_incomplete.py). The completed code should pass the correctness test in [https://cs50.dev/](https://cs50.dev/).
   
**Topics to prepare before next class**: *Libraries, Random, Statistics, Command-Line Arguments, slice, Packages, APIs, Making Your Own Libraries*



</details>

<details markdown="block">

 <summary>Class 6 (October 20, 2023): Organizing and testing code; Unit tests</summary>


1. Questionnaire Q4 on the topics of the homework 
2. Evaluated group assignment ("Little Professor") in class
3. Discussed references in Python with examples from Part 5 of [PP.fi](https://programming-23.mooc.fi/) and made experiments with PythonTutor: [Visualize code](https://pythontutor.com/visualize.html#mode=edit).
4. **Do before next class.** Some groups still have to improve the previous assignment. All groups should solve Problem P3 (also a group assigment):
   - [P3_distances description and file](https://github.com/isa-ulisboa/greends-ipython/tree/main/assignments/P3_distances)
   - Groups members should try to collaborate by syncronizing their work through VSCode and GitHub using the Source Control menu in VSCode:
    * [Working with GitHub in VS Code (VSCode documentation)](https://code.visualstudio.com/docs/sourcecontrol/github)
    * Notes on [how to clone GitHub repository and syncronize it with local folder](https://github.com/isa-ulisboa/greends-ipython/blob/main/github_vscode/Clone_GitHub_repository_and_syncronize_with_local_folder.pdf)
    * Notes on [how to publish a local folder to GitHub](https://github.com/isa-ulisboa/greends-ipython/blob/main/github_vscode/VSCode_local_folder_to_GitHub.pdf)

</details>

<details markdown="block">

 <summary>  Class 7 (October 27, 2023):  File I/O</summary>


1. Questionnaire Q5 on recent topics 
2. Evaluate group assignment P3 ("Distances") in class
3. Unit tests with `pytest`: examples 
4. **Do before next class (November, 11).**
   * [Lecture 5 on Unit tests](https://cs50.harvard.edu/python/2022/notes/5/) and video [CS50 Video Player: Lecture 5](https://video.cs50.io/tIrcxwLqzjQ)
   * Group assignment, which is mostly about creating unit tests for code. Groups members should collaborate through VSCode and GitHub using Source Control menu in VSCode or git command lines. The problem description and the necessary files are available at [P4_haversine](https://github.com/isa-ulisboa/greends-ipython/tree/main/assignments/P4_haversine).
   * [Lecture 6 on File I/O](https://cs50.harvard.edu/python/2022/notes/6/) and video [CS50 Video Player: Lecture 6](https://video.cs50.io/KD-Yoel6EVQ)

</details>

<details markdown="block">

<summary> Class 8 (November 10, 2023): Pandas </summary>

1. Questionnaire Q6 on recent topics. 
2. Evaluate group assignment on Unit Tests in class (P4 "Haversine").
3. Pandas: series and dataframes; I/O; first examples.
4. **Do before next class (November 17).**
   * [Pandas documentation/getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) up to section "How to combine data from multiple tables".
   * Optional: Check videos on Pandas on [Python Tutorials by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU): from [Python Pandas Tutorial (Part 2): DataFrame and Series Basics - Selecting Rows and Columns](https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=129) to [Python Pandas Tutorial (Part 6): Add/Remove Rows and Columns From DataFrames](https://www.youtube.com/watch?v=HQ6XO9eT-fc).

</details>

<details markdown="block">

<summary> Class 9 (November 17, 2023): Regular expressions </summary>

1. Questions about Pandas.
2. Questionnaire Q7 on recent topics. 
3. Finish to evaluate group assignment P4 on Unit Tests ("Haverside") in class (remaining groups)
4. Regular expressions (regex)
5. **Do before next class (November 24).**
 * [Lecture 7](https://cs50.harvard.edu/python/2022/notes/7/) and video [CS50 Video Player: Lecture 7](https://video.cs50.io/hy3sd9MOAcc)
 * Solve problems from [Problem Set 7](https://cs50.harvard.edu/python/2022/psets/7/). In particular, you should solve problems "NUMB3RS" and "Regular, um, Expressions", following the instructions (i.e. solve and test your solution).
 * Try [https://regex101.com/](https://regex101.com/) to do experiments and understand better how "regex" works.


</details>

<details markdown="block">

<summary> Class 10 (November 24, 2023): Object-oriented programming </summary>

1. Questions about regular expressions and problems  "NUMB3RS" and "Regular, um, Expressions". Indication on how to submit the assignment.
2. Questionnaire Q8 on recent topics. 
3. Presentation of the **semester project**.
4. Object-oriented programming: see script [mage_v1.py](https://github.com/isa-ulisboa/greends-ipython/blob/main/OOP/mage_v1.py)
5. **Do before next class (December 15).**
 * [Lecture 8](https://cs50.harvard.edu/python/2022/notes/8/) on OOP
 * Video [CS50 Video Player: Lecture 8](https://video.cs50.io/e4fwY9ZsxPw)

</details>

<details markdown="block">

<summary> Class 11 (December 15, 2023): Object-oriented programming; sets, global, unpacking, args and kwargs </summary>

1. Solve [Cookie jar problem ](https://cs50.harvard.edu/python/2022/psets/8/jar/) and submit code in Fenix (P6)
2. Questionnaire Q9 on object-oriented programming; 
4. Presentation of some [additional Python topics](https://cs50.harvard.edu/python/2022/weeks/9/) with examples
5. **Do before next class (December 22).**
 * [Lecture 9](https://cs50.harvard.edu/python/2022/notes/9/); in particular, explore the following topics: sets, global variables, constants, unpacking, args (*) and kwargs (**), map, list comprehensions, filter, dictionary comprehensions.
 * Video [CS50 Video Player: Lecture 9](https://video.cs50.io/6pgodt1mezg)
 * Sugestion: Video [Python Tutorial: Comprehensions - How they work and why you should be using them](https://www.youtube.com/watch?v=3dt4OGnU5sM)
6. Example of use of `*args`and `**kwargs`. Check examples scripts in the [ETC folder](https://github.com/isa-ulisboa/greends-ipython/tree/main/ETC).
   

</details>


<details markdown="block">

<summary> Class 12 (December 22, 2023): Args and kwargs, list comprehension, dictionary comprehension, lambda, map, filter </summary>
 
1. Discussion of assigments P5 (*numb3rs* and *um*)
2. Discussion of guidelines for final project
3. Presentation of some topics from [Lecture 9](https://cs50.harvard.edu/python/2022/notes/9/):  args (*) and kwargs (**), list comprehensions, lambda functions, map, filter, dictionary comprehensions. Check examples scripts in the [ETC folder](https://github.com/isa-ulisboa/greends-ipython/tree/main/ETC).

   Example: distinct possible ways of creating a list with all the cubes of even numbers up to *N*. In the last cases, `map` applies a given function to each element of a list. Likewise, `filter` applies a boolean function to filter elements of a list. Both function can be executed in parallel over the elements of the list since each output is independent of the outputs for the remainder elements of the list.
   * With list comprehension:
     ```
     def cube(x):
         return x*x*x
     L=[cube(x) for x in range(N) if x%2==0]
     ```
   * With `filter` to select even numbers and `map`to compute cubes:
     ```
     def even(x):
         return x%2==0
     numbers=list(range(N))
     even_numbers=list(filter(even, numbers))
     cubes=list(map(cube,even_numbers))
     ```
   * Also with `filter` and `map` but defining implicitly the *cube* and *even* functions with `lambda` instead of `def`: 
     ```
     numbers=list(range(N))
     even_numbers=list(filter(lambda x: x%2==0, numbers))
     cubes=list(map(lambda x: x*x*x,even_numbers))
     ```
   * The most compact way of solving the problem involves `lambda` and list comprehension. In the example below, if one would just write `lambda x: x*x*x` instead pf `(lambda x: x*x*x)(x)` the output list would be a list of lambda functions. 
     ```
     L=[(lambda x: x*x*x)(x) for x in range(N) if x%2==0]
     ``` 
5. Observations about using vectorization to speed-up computations.

   A conditional can be replaced by arithmetic and logical operations. For example, let `L=[x/5 for x in range(-10,10)]` be a list of equally spaced numbers between -2 and 2, and say we want to apply the stepwise linear sigmoid function to the elements of the list. One could define *sigma* as below and then apply it to `L` with `map`.
   ```
   def sigma(x):
       if x>1:
           return 1
       elif x<-1:
           return -1
       else:
           return x
   list(map(sigma,L))
   ```
   However, instead of using the conditional `if` once can define *sigma* in a simpler way with logical and arithmetic operations. 
   ```
   def sigma(x):
       return (x>=1)*1+(-1<x<1)*x+(x<=-1)*-1
   list(map(sigma,L))
   ```
   Note that we don't need to define explicitly *sigma*: it could be encapsulated in a `lambda` function `lambda x: (x>=1)*1+(-1<x<1)*x+(x<=-1)*-1` as the first argument of `map`. One advantage of using arithmetic and logical operations is that computations can then be easily vectorized, which allows to speed them up, since the processing time for a pair of vectors is similar to the processing time for a pair of numbers.

   Similarly to *list comprehension*, Python provides *dictionary comprehension* which allows to create dictionaries. The example below uses `ord`which is a function that returns the *ascii* index of a character, to create a dictionary of vowels, where the key is the vowel in uppercase and the value is the rank of the letter starting at 0 for *a*.
   ```
   {x.upper(): ord(x.lower())-97 for x in 'aeiou'} # returns {'A': 0, 'E': 4, 'I': 8, 'O': 14, 'U': 20}
   ```

   
</details>


## Install Python 3 and Visual Studio Code (VS Code)

<details markdown="block">
  
<summary> Steps to install Python 3 and Visual Studio Code</summary>

[Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial):
  * Python 3 interpreter; For Windows, download either from python.org or from the Microsoft Store; For macOS install Python using Homebrew; Linux: built-in Python 3 installation
  * VS Code; Download from VS code site
  * VS Code Python extension: A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the language: >=3.7), including features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more!

</details>

## Python documentation and tutorials

### CS50P
The main tutorial for the class is [CS50P](https://cs50.harvard.edu/python/2022/weeks/). The table below compares the contents of that course with another well-known 
free online Python Programming course at [PP.fi](https://programming-23.mooc.fi/). The **CS50P** course problem sets tend to be difficult, while you can find at **PP.fi** a set of problems with a larger range of difficulty, from very easy to advanced. Both online courses provide a platform for coding and testing the corretness of the solutions. Both courses provide recorded lectures: [CS50P](https://cs50.harvard.edu/python/2022/weeks/) and [PP.fi](https://programming-23.mooc.fi/#lectures).

<details markdown="block">
  
<summary> Comparison of CS50P and PP.fi</summary>

| CS50P     | Contents |  PP.fi | Contents |
| ----------- | ----------- |----------- | ----------- |
| Lecture 0    | Creating Code with Python; Functions; Bugs; Strings and Parameters; Formatting Strings; More on Strings; Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values    | Part 1 |   Intro; I/O; More about variables; Arithmetic operations; Conditional statements |
| Lecture 1    | Conditionals, if Statements, Control FlowModulo; Creating Our Own Parity Function; Pythonic; match | Part 2  |  Programming terminology; More conditionals; Combining conditions; Simple loops |
| Lecture 2    | Loops; While Loops; For Loops; Improving with User Input; More About Lists; Length; Dictionaries, More on code modularity  |  Part 3 |  Loops with conditions; Working with strings; More loops; Defining functions |
|  |   | Part 4 |    The Visual Studio Code editor, Python interpreter and built-in debugging tool; More functions; Lists; Definite iteration; Print statement formatting; More strings and lists |
|   |   | Part 5 |  More lists; References; Dictionary; Tuple |
| Lecture 3 | Exceptions, Runtime Errors, try, else, Creating a Function to Get an Integer, pass | Part 6  |  Reading files; Writing files; Handling errors; Local and global variables |
| Lecture 4 |  Libraries, Random, Statistics, Command-Line Arguments, slice, Packages, APIs, Making Your Own Libraries|  Part 7 | Modules; Randomness; Times and dates; Data processing; Creating your own modules; More Python features  |
| Lecture 5 | Unit Tests; assert; pytest; Testing Strings; Organizing Tests into Folders | | |
| Lecture 6| File I/O; open; with; CSV; Binary Files and PIL | | |
| Lecture 7 | Regular Expressions; Case Sensitivity; Cleaning Up User Input; Extracting User Input |||
| Lecture 8 | Object-Oriented Programming; Classes; raise; Decorators;  Class Methods; Static Methods; Inheritance; Inheritance and Exceptions; Operator Overloading| Part 8 | Objects and methods; Classes and objects; Defining classes; Defining methods; More examples of classes |
| | | Part 9 | Objects and references; Objects as attributes; Encapsulation; Scope of methods; Class attributes; More examples with classes |
| | | Part 10 | Class hierarchies; Access modifiers; Object oriented programming techniques; Developing a larger application |
| Lecture 9 | set; Global Variables; Constants; Type Hints; Docstrings; argparse; Unpacking; args and kwargs; map; List Comprehensions; filter; Dictionary Comprehensions; enumerate; Generators and Iterators | Part 11 |  List comprehensions; More comprehensions; Recursion; More recursion examples |
| | | Part 12 | Functions as arguments; Generators; Functional programming; Regular expressions|

</details>


### Documentation
You can find information on basic concepts and features of the Python language and system at  [The Python Tutorial at python.org](https://docs.python.org/3/tutorial/index.html). 

### Other tutorials

<details markdown="block">
<summary> w3schools, etc </summary>

1. A nice interactive site is W3schools' [Python Tutorial](https://www.w3schools.com/python/default.asp) where you can find in particular an easy to use  [Python reference documentation](https://www.w3schools.com/python/python_reference.asp).

2. Another nice and very clear series of videos on Python are available in this Youtube channel: [Python Tutorials by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU). In particular, you might be interested in the following specific topics discussed in class:
* [text](https://docs.python.org/3/tutorial/introduction.html#text) and video [Python Tutorial for Beginners 2: Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2)
* [numbers](https://docs.python.org/3/tutorial/introduction.html#numbers) and video [Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data](https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3)
* [f-strings and other formatting options](https://docs.python.org/3/tutorial/inputoutput.html);
* [Lists](https://docs.python.org/3/tutorial/introduction.html#lists) and video [Python Tutorial for Beginners 4: Lists, Tuples, and Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4&t=1223s)
* [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), see video [Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs](https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5&pp=iAQB)
* I/O and csv files: [File Objects - Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25); [CSV Module - How to Read, Parse, and Write CSV Files](https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=28)
* List and dictionary comprehensions, zip: [Python Tutorial: Comprehensions - How they work and why you should be using them](https://www.youtube.com/watch?v=3dt4OGnU5sM)

</details>

### Problem sets

1. List of both simple and more advanced programming exercises that you can run and test online: [programming-23.mooc.fi](https://programming-23.mooc.fi/all-exercises). Sign-in to have access to code editor and testing.
   
2. Compiled list of [CS50P proposed problems](https://raw.githack.com/isa-ulisboa/greends-ipython/main/problems.html)  (to be completed)

### Other interactive links
1. PythonTutor, that show how Python manages variables in memory: [Visualize code](https://pythontutor.com/visualize.html#mode=edit)
2. Regular expressions: [https://regex101.com/](https://regex101.com/)

### Student projects

<details markdown="block">
<summary> Project repositories </summary>
 
1. [Calculation of the Enteric Fermentation Methane Emission Factor of Cows](https://github.com/PauloCanaveira/project)
 
2. [Scrabble Training](https://github.com/domwelsh/scrabble_training/tree/main)
   
4. [Forecast Hunter: A toolbox for assessing seasonal weather forecast data usability on ETo estimation](https://github.com/dgarcian9/ForecastHunter)
   
6. [Customized and fast downloading of satellite images](https://github.com/Emmanuel461/Final_project)
   
8. [Pest Tracker: simular uma aplicação para a previsão da praga da mosca da azeitona no olival](https://github.com/filipefelisardo/PestTracker)
   
10. [Pokemon_battle_simulator](https://github.com/nachiet/Pokemon_battle_simulator)
    
12. [Forest roads under the influence of heavy rain events](https://github.com/justusnoe/forest_roads)
    
14. [Weather Report](https://github.com/marianadc01/weather-report/tree/main)
    
16. [As suas receitas na palma da mão](https://github.com/marianavalho/python_project)
    
18. [Word Wizardry](https://github.com/Sofs27/Final_Project_Alicia_Sofia)
    
20. [Calculation of Urban Density with QGIS and Python](https://github.com/laurafi97/submission-python-qgis-)
    
22. [Avaliação do risco de tempestades](https://github.com/Damiao97/isa_python_final_rep)
    
24. [Fertilização: auxiliar a fertilização com base em resultados de análises de solo](https://github.com/RubenRomeroTorrado/Fertilizacao/)
</details>

--->
