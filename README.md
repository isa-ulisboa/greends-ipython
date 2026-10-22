# Introduction to Python 2026/2027

Masters in Data Science applied to agricultural and food sciences, environment, and forestry engineering.

Instructor: Manuel Campagnolo (mlc@isa.ulisboa.pt)

Teaching assistant: Hannah Nathanson (hnathanson@edu.ulisboa.pt)

---

**Revised class schedule**: class (Friday, room 48) will start at 11:45 and end at 14:45, with a ~45 minute break for lunch.

<!-- Please fill the course diagnostic form at <https://forms.gle/VMK681TQ3LMXZqWU8> --->


---

<details markdown="block">
<summary><h2>  Online resources for the course </h2></summary>
<blockquote>

  * You need to self-register for the course in Moodle at <https://elearning.ulisboa.pt/user/index.php?id=12863>. The Moodle site allows you to access assignments; submissions; detailed grades and comments
  * If you don't have one already, create a GitHub account at <https://github.com/signup>
  * [CS50P: CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python). Lectures (videos and notes), problems sets, shorts;
  * [CS50 codespace](https://cs50.dev/). VScode codespace that allows you to use a customized AI bot (CS50's duck debugger, or DDB for short) and test your solutions for CS50P proposed problems (you can access the codespace with your GitHub user).
  * [Python tutor](https://pythontutor.com/). Python Tutor is a online tool that lets you write code in a web browser and see what happens step-by-step as the computer runs it.
  * [Fenix webpage for the course](https://fenix.isa.ulisboa.pt/courses/intpy-564938523285845): administrative information and final grades
  * [Help me](https://1drv.ms/o/c/0bedfe7ffa5a0eb8/IgA-CgpLN8IVTJsDg9FJ9m67AQrx95SYxoXvGRBOMDVRwjI): general help, assignements


<details markdown="block">
  <summary>  Advanced exercises, alternative tutorials and reference materials </summary>
  
  * [Codewars](https://www.codewars.com/)  is an online educational platform used to practice, improve, and master programming skills through gamified coding challenges in Python and many other programming languages. You can log in with your GitHub account and choose your proficiency level. Codewars will propose exercises for your level. 
  * [Learn Python with Scrimba, Olof Paulson](https://v2.scrimba.com/learn-python-c03): interactive lectures (videos), examples and exercises 
  * [Introduction to Python (VScode)](https://vscodeedu.com/courses/intro-to-python): interactive step by step lectures and exercises, real-time quizzes.
  * Basic concepts and features of the Python language and system: [The Python Tutorial at python.org](https://docs.python.org/3/tutorial/index.html).
  * Python Programming course at [PP.fi](https://programming-25.mooc.fi/): same features as CS50 but to test your solutions to problems you are required to pass previous tests 
  * If you curious about the story of Python, check out [this video](https://www.youtube.com/watch?v=GfH4QL4VqJ0). In this video, you'll learn about the output of `>>> import this` and many other anecdotes about Python.
  
  </blockquote>
</details>
</details>

---

<details markdown="block">
<summary><h2>  Class 1 (September 11, 2026): data types, variables, lists, functions </h2></summary>
<blockquote>

1.  The recommendation for this class is to code using the CS50 codespace. Two steps: 1. log in into your GitHub account; 2. access your code space at <https://cs50.dev/>. This environment allows you to test automatically your scripts for the CS50 problem sets and gives access to a customized AI bot (DDB) 
2. Some useful keyworks for the command line interface (CLI): 
 * `code filename.py` to create a new file 
 * `ls` to list files in folder
 * `cp filename newfilename` to copy a file, e.g. `cp ..\hello.py  farewell.py` (`..` represents parent folder)
 * `mv filename newfilename` to rename or move file, e.g. `my farewell.py goodbye.py` or `mv farewell.py ..` (move one folder up)
 * `rm filename` to delete (remove) file
 * `mkdir foldername` to create new folder
 * `cd foldername` change directory, e.g. `cd ..` 
 * `rmdir foldername` to delete folder
 * `clear` to clear terminal window
3. Typing `python` gives you access to a REPL (interactive Read-Eval-Print-Loop) environment (<https://realpython.com/interacting-with-python/>).
4. All values in Python have a **type**. The **primitive data types** are: integer, float, string, Boolean, and None (see <https://www.geeksforgeeks.org/python/primitive-data-types-vs-non-primitive-data-types-in-python/>). There are also **Non-Primitive Data Types** like `list`, `tuple`, `set` and `dictionary`. 
   * strings (`str`), variables, print (a function), parameters (e.g. `end=`), input, comments, formatted strings (`f"..."`), `.strip()`, `.title` (methods)
   * integers (`int`), operations for integers, casting (e.g. `str` to `int`)
   * floating point values (`float`), round, format floats (e.g. `f"{z:.2f}`)
   * Boolean: `True`, `False`, that can be combined with operators `and`, `or`, `not`
5. Functions, `def`, `return`. Example:
  ```
  def square(x):
      return x*x
  ```
6. View the step-by-step execution of this code on [Python Tutor](https://pythontutor.com/visualize.html#code=def%20main%28%29%3A%0A%20%20%20%20x%3D4%0A%20%20%20%20y%3Dsquare%28x%29%0A%20%20%20%20print%28f%22%7Bx%7D%20squared%20is%20%7By%7D%22%29%0A%0Adef%20square%28n%29%3A%0A%20%20%20%20s%3Dn*n%0A%20%20%20%20return%28s%29%0A%0Amain%28%29&curInstr=12&mode=display&origin=opt-frontend.js&py=311). Identify the scope of the variables. Try to add `print(s)` in line 4 after calling function `square` inside the `main` function: why do you get a `NameError`?

7. Suggested problems: [CS50 Problem set 0](https://cs50.harvard.edu/python/psets/0/). Find a solution to the problems at your CS50 codespace, and dialog with the AI bot (DDB) for help. The bot won't produce code but will help you by answering your to questions: very precise prompts originate more details in the answers. Resist the temptation of looking for a solution on the web or using a generic AI bot. 

</blockquote>
</details>


---

<details markdown="block">
<summary><h2> Class 2 (September 18, 2026): conditionals, lists, dictionaries </h2></summary>
<blockquote>

1. See:
   - [notes on CS50P lecture 1](https://cs50.harvard.edu/python/notes/1/): conditionals `if`, `match`, boolean expressions, etc
   - [notes on CS50P lecture 2](https://cs50.harvard.edu/python/weeks/2/): `for` and `while` loops, etc

3. Conditionals:
   - `if`, `elif`, `else`:
     ```Python
     if score >= 70:
         print("Grade: C to A")
     elif score >= 60:
         print("Grade: D")
     else:
         print("Grade: F")
     ```
   - `match`:
     ```Python
     match species:
         case 'versicolor':
             label=0
         case 'virginica':
             label=1
         case _:
             label=2
     ```
3. Pythonic coding: `def main()`, define other functions, call `main()`. The code must be modular.
4. While loops, for loops, `break`, `break` and `return`
   ```
   s='intro to python'
   for i in range(15):
       print(s[i])
   ```
   
   ```
   # require user to provide a positive number
   while True:
      n = int(input("What's n? "))
      if n > 0:
          break
   ```
6. Data type *list* `[]`: methods `append`, `extend`
7. Data type *dictionary* `{}`, `items()`, keys `.key()` and values `.values()`
   ```Python
   knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   for k, v in knights.items():
       print(k, v)
   if 'gallahad' in knights:
       print('Go Gallahad')
   ```
8. Suggested problems: [CS50 Problem set 1](https://cs50.harvard.edu/python/2022/psets/): Deep Thought, Home Federal Savings Bank, Math Interpreter, Meal Time
    
9. Assignment #1 available on Moodle: problems [File extensions (set 1)](https://cs50.harvard.edu/python/2022/psets/1/extensions/), [Coke machine (set 2)](https://cs50.harvard.edu/python/2022/psets/2/coke/), [Plates (set 2)](https://cs50.harvard.edu/python/2022/psets/2/plates/)

</blockquote>
</details>

---

<details markdown="block">
<summary><h2>  Class 3 (September 25, 2026): list and dictionary comprehensions, collaborative exercise </h2></summary>
<blockquote>

1. See lecture on [List and dictionary comprehensions](https://cs50.harvard.edu/python/shorts/list_dictionary_comprehensions/)

2. [Exercises on list comprehension (with some solutions)](docs/exercises_list_comprehension.md)
 

2. [Exercises on dictionary comprehension (with some solutions)](docs/exercises_dict_comprehension.md)

 
3. Collaborative project: each student or small group of students should define each necessary function to complete the script below. The side effect of `main()` is a simple histogram printed in the terminal.
   
 ```Python
from read_values import read_values
from determine_min_max import determine_min_max
from number_of_classes_sturges import number_of_classes_sturges
from amplitude import amplitude
from determine_frequency import determine_frequency
from print_frequency import print_frequency

def main():
   # read values
   x=read_values() # x is a list of numbers, either integers or floats
   n=len(x) # integer; number of values
   # determine min value and max value 
   xmin,xmax=determine_min_max(x) # integers or floats
   # determine number of classes
   m=number_of_classes_sturges(n) # m is a positive integer such that 2**(m-1) <= n <= 2**m
   # determine class amplitude
   delta=amplitude(xmin,xmax,m) # positive float, the range of values divided by the number of classes
   # Compute frequency for each class and plot histogram row by row
   for i in range(m):
      left=xmin+i*delta
      if i < m-1:
         right=left+delta
      else:
         right=left+delta+1 # either 1 or any positive value
      freq=determine_frequency(x,left,right) # integer;  note that each value must belong to one and only one class
      print_frequency(freq) # the output must be '****' where each * represents one observation
 # execute main
 main()
 ```
---
 
To share code, students should submit a  *pull request* on GitHub.

Test how to perform a pull request with a trivial `run()` function for each team:
```text
1. Fork the course repository `https://github.com/isa-ulisboa/greends-ipython` on your GitHub account
2. In your fork, go to `collaborative_proj/submissions/`.
3. Create a file called `team_name.py` with your own team name, say `team_01.py`
4. Add a `run()` function to the file with contents like `print('team 1')`
5. Commit the file.
6. Click Contribute → Open pull request.
7. Make sure it goes from your fork to the teacher’s original repository `https://github.com/isa-ulisboa/greends-ipython`
8. Click `Create pull request`.
```

If the teacher's original repository changes after you forked it (for instance, the README is updated or other teams' pull requests are merged), your fork does not update automatically. Before working on a new submission, bring your fork up to date:
```text
1. Open your fork on GitHub (https://github.com/<your_username>/greends-ipython).
2. If it says "This branch is X commits behind isa-ulisboa/greends-ipython:main", click Sync fork → Update branch.
3. If you also have a local clone of your fork, run `git pull` in it to get the updates.
```
Alternatively, from a local clone of your fork, using the command line:
```bash
git remote add upstream https://github.com/isa-ulisboa/greends-ipython.git   # only the first time
git fetch upstream
git merge upstream/main
git push origin main
```

</blockquote>
</details>

---


<details markdown="block">
<summary><h2>  Class 4 (October 2, 2026): handling exceptions in Python: catching and raising exceptions </h2></summary>  

0. See [CS50P lecture 3](https://cs50.harvard.edu/python/weeks/3), in particular the [short on handling exceptions](https://cs50.harvard.edu/python/shorts/handling_exceptions/): `try`, `except`, `ValueError`, `KeyError`.

1. A few examples of code that can be helpful to solve problems in [CS50 Problem set 3](https://cs50.harvard.edu/python/2022/psets/3/).

<blockquote>

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
For a list of Python Built-in Exceptions, besides `ValueError`, you can check https://www.w3schools.com/python/python_ref_exceptions.asp

</blockquote>

2. The *fuel gauge* problem (https://cs50.harvard.edu/python/2022/psets/3/fuel/)

<blockquote>

To solve this problem, try to organize your code as follows. As suggested in *hints*, you should catch `ValueError` and  `ZeroDivisionError` exceptions in your code. In the code below, the user is being asked for correct values for `x,y` until they satisfy the requirements: `x,y` must be inputted as a string `x/y`, `x` has to be less or equal to `y`, and `y` cannot be zero. The function `get_string_of_integers_X_less_than_Y` in the code below should take care of that.

```
def main():
    # asks user for input until the input is as expected
    x,y=get_string_of_integers_X_less_than_Y()
    # compute percentage from two integers
    p=compute_percentage(x,y)
    # print output 
    print_gauge(p)
```

</blockquote>

3. Example from <https://cs50.harvard.edu/python/2022/shorts/handling_exceptions/>

<blockquote>

Exercise: adapt the code proposed in the short to be more modular, where the main function is something like the one below:

```
def main():
    spacecraft = input("Enter a spacecraft: ")
    au=get_au(spacecraft)
    m = convert(au)
    print(f"{m} m")
```
</blockquote>

4. Other useful applications of try-except

<blockquote>
   
- We may want to exit the execution of our script if some exception is caught. This can be done with `sys.exit()`, which can also be used to print a message.
```
import sys # import module
try:
    x = int(input("What's x?"))
except ValueError:
    sys.exit("x is not an integer")
```

- Example of code that catches `CRTL-C` or `CRTL-D`:

```
while True:
    try:
        x=int(input())
    except ValueError:
        print('x is not integer')
    except KeyboardInterrupt: #CTRL-C (in Linux, interrupt execution)
        print('\n KeyboardInterrupt')
        break
    except EOFError: #CTRL-D (in Linux, log out terminal/end-of-file)
        print('\n EOFError')
        break
    else:
        print(x)
```
</blockquote>

5. Exercise (Asking for an haphazard list of numbers): Create a program that asks the user to provide haphazardly a series of numbers that you want to store in a list. The user is asked for a number at the time. Only inputs that are numbers are stored in  the list. When the user wants to stop, it should type CTRL-D. Then, the program should print the list of numbers.

</details>

---

<details markdown="block">
<summary><h2>  Class 5 (October 9, 2026): modules, packages, APIs </h2></summary>

1. See lecture <https://cs50.harvard.edu/python/weeks/4/>

2. Modules and packages
<blockquote>


Suggestion: watch <https://cs50.harvard.edu/python/shorts/creating_modules_packages/>
 
Modules are just python scripts (files like `module_name.py`) which can be imported into your main code and that can be shared between multiple applications. You can import everything that belongs to the module, or just some given function(s) or other objects.

<details markdown="block">
<summary> Create and import your own module </summary>

Exercise: Create file named `utils.py` and file `main.py` in http://cs50.dev. Organize the files in the following folders:
```
|--- class_5 # or whatever folder name you wish
     |--- common # General reusable code used across the project
          |--- __init__.py # optional: marks the folder as a package
          |--- utils.py
     |--- main.py
```

The contents of `utils.py` are typically functions or constants that you can re-use in different contexts. Let's suppose that `utils.py` has the following contents.

<details markdown="block">
<summary> utils.py </summary>
 
```Python
import sys

Constants={
    'e'   : 2.718281828459045, # Euler's constant
    'pi'  : 3.141592653589793, # Archimedes' constant
    'phi' : 1.618033988749895  # Golden ratio
}

def get_integer() -> int:
    #get integer from user
    while True:
        try:
            return(int(input('Type a number:  ')))
        except ValueError:
            print('Not an integer number: try again')
        except KeyboardInterrupt: #CTRL-C
            print('\n If you want to exit type CTRL-D')
        except EOFError: # CTRL-D
            sys.exit('\n Exit as requested')
```
</details>

and `main.py` is the following file:

<details markdown="block">
<summary> main.py (1st version) </summary>
 
```Python
import common.utils

def main():
    x=common.utils.get_integer()
    print(x)

main()
```
</details>

Run `main.py` from inside the `class_5` folder (`cd class_5`, then `python main.py`), so that Python can find the `common` folder.

If you prefer, you can explicitly import some given functions from the module as in the following example.

<details markdown="block">
<summary> main.py (2nd version) </summary>
 
```Python
from  common.utils import get_integer

def main():
    x=get_integer()
    print(x)

main()

```
</details>

You can also import everything from the module with `from common.utils import *` instead of the more specific (and recommended) `from common.utils import get_integer`.

The examples above follow the directory tree that was suggested. If you change the module's location, you need to adapt the code accordingly. In alternative, you can add the path to the directories where your modules lies to `sys.path` as in the following example.

```Python
import sys
sys.path.append(r'path-to-folder') # folder that contains utils.py (e.g. `/workspaces/8834091/class_5/common`)
import utils
```
</details>

As explained on the recommended video, a python **package** is just a folder with modules and a special file named `__init__.py`


<details markdown="block">
<summary> Pip install</summary>

Some modules, like `sys`, `math` or `random`, are part of the Python *standard library*: they come with Python and can be imported without installing anything. For instance, `random` provides a series of functions for sampling, shuffling, and extracting random numbers from a variety of probability distributions.

Many other packages are available at the Python Package Index, https://pypi.org/. They need to be installed before they can be imported, which is done in the terminal with `pip`. For instance, the package `requests` (used below to access APIs) is installed with

```
$ pip install requests
```
and then imported in your script with `import requests`. If you want to know the folder where a module is located, you can get that information with the attribute `__file__`, as in the following script. Compare the two folders: the standard library and the installed packages (`site-packages`) are in different places.

```Python
import random
import requests
print(random.__file__)
print(requests.__file__)
```

Suggestion: write a script to  estimate the value of $\pi$ with a Monte Carlo algorithm that makes calls to `random.uniform(-1, 1)`. One possible solution: https://www.geeksforgeeks.org/dsa/estimating-value-pi-using-monte-carlo/

</details>


</blockquote>

3. `sys.argv`
<blockquote>

Previously, we used module `sys`, in particular functions  `sys.exit()` and  `sys.path`. Another useful function is `sys.argv`,  that allows you to have access to what the user typed in at the command line `$` as in the following script.

```Python
import sys
print(len(sys.argv)) # returns the number of words in the command line after $python
print(sys.argv[1]) # returns the 2nd word, i.e., the first word after $python myscript.py
```

For instance, the following script named `sum.py` prints the sum of two numbers that were specified in the command line.

<details markdown="block">
<summary> sum.py </summary>

```Python
# sum.py
import sys
try:
    x,y = float(sys.argv[1]), float(sys.argv[2])
    print('the sum is',x+y)
except IndexError:
    print('missing argument')
except ValueError:
    print('The arguments are not numbers')
```
</details>

To run it, you can for instance execute the command `$python sum.py 1.2 4.3` in the terminal.

</blockquote>


4. APIs
<blockquote>

Suggestion: watch https://cs50.harvard.edu/python/shorts/api_calls/ (13')

*Application program interfaces* allow you to communicate with a remote server. For instance,  `requests` is a package that allows your program to behave as a web browser would.  Consider the following script `myrequest.py` that allows you to explore the *itunes* database (https://performance-partners.apple.com/search-api):

<details markdown="block">
<summary> Example: iTunes </summary>

```Python
import requests
import sys
try:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])
    print(response.json())
except IndexError:
    sys.exit('Missing argument')
except requests.RequestException:
   sys.exit('Request failed')
```
You can then call the API from your terminal with `$python myrequest.py 'name of my favorite band'`. What you see printed on the terminal is a dictionary. How can you edit your script such that the output is just a list of track names (key `trackName`)? Notice that `&limit=2` in the search sets the number of songs that are returned by the API.

</details>

<details markdown="block">
<summary> Example: GBIF </summary>

You can easily adapt that code to access a different database. For instance if you want to explore the GBIF database <https://data-blog.gbif.org/post/gbif-api-beginners-guide/>, you can just replace the main line of code in `myrequest.py` with
```
response=requests.get('https://api.gbif.org/v1/species/match?name='+ sys.argv[1])
```
and execute it with, say,  `$python myrequest.py Tracheophyta` in the terminal.

</details>

<details markdown="block">
<summary> Example: open-meteo </summary>

Another example of a useful API for weather data is https://open-meteo.com/en/docs#api_documentation. You can find a customized `requests` package for **open-meteo**  at https://pypi.org/project/openmeteo-requests/.

```Python
import openmeteo_requests

openmeteo = openmeteo_requests.Client()

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": [38.74,41.15], # Lisbon, Porto
	"longitude": [-9.14,-8.6] ,
	"current": ["temperature_2m", "relative_humidity_2m","wind_speed_10m"],
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
for i in range(len(responses)):
    response = responses[i]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m")

    # Process current data. The order of variables needs to be the same as requested.
    current = response.Current()
    print(f"Current temperature_2m: {current.Variables(0).Value()}")
    print(f"Current relative_humidity_2m: {current.Variables(1).Value()}")
    print(f"Current wind_spreed_10m: {current.Variables(2).Value()}")
    print()
```
</details>

</blockquote>

5. Suggested problem
<blockquote>

Solve problem *Bitcoin price index* from CS50P [Problem_set_4](https://cs50.harvard.edu/python/2022/psets/4/). In particular, organize your code so the main function is the following:

```
def main():
    x=read_command_line_input()
    price=get_bitcoin_price()
    print(f"${x*price:,.4f}")
```
</blockquote>

</details>



---
<details markdown="block">
<summary><h2>  Class 6 (October 16, 2026): virtual environments; file I/O with images </h2></summary>

- For virtual environments, watch [How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=APOPm01BVrk) (17') and see the official documentation <https://docs.python.org/3/library/venv.html>
- For file I/O and images with Pillow, see lecture <https://cs50.harvard.edu/python/weeks/6/> (sections on `open`, `with` and *Binary Files and PIL*). CSV files will be discussed later with Pandas.

In this class we build a small project, `image_project`, that downloads and processes images of leaves. First we prepare a virtual environment with the packages the project needs (`requests` and `Pillow`), then we use it to read and write text and image files. At the end of the class, the project folder should look like this:

```
image_project/            <- all commands are run from here
|--- .venv/               <- the virtual environment (created by python -m venv .venv; not shared)
|--- .gitignore           <- tells Git to ignore .venv/
|--- requirements.txt     <- list of packages and versions (shared)
|--- images/              <- input images
|--- output/              <- files created by our scripts
|--- notes.py
|--- download_image.py
|--- explore_image.py
|--- process_images.py
```

<ul>
<details markdown="block">
<summary> 1. Why virtual environments? </summary>

Suppose your script was written and tested with version 12.0.0 of Pillow, but a colleague has an older version installed that behaves differently, or another project of yours needs a different version. Installing every package in the same place (the *base* environment) quickly leads to conflicts. A *virtual environment* solves this problem. It is:

- A folder that contains a Python interpreter and a set of packages, with given versions, for **one** project. It is isolated from other virtual environments and from the packages installed in the base environment.
- Conventionally named `.venv` and placed at the root of the project folder. Tools such as VS Code detect it automatically.
- Disposable: it should be simple to delete and re-create it from scratch. **You never place your scripts or data inside `.venv`.**
- Not shared (e.g. not checked into Git) and not copied to another computer. Instead, one shares the list of packages (`requirements.txt`) and each person re-creates the environment.

Let's first look at the base environment. The following commands list the installed packages and show information about the package `requests` (version, location, dependencies):

```
$ pip list
$ pip show requests
```

The commands below work in the [CS50 codespace](https://cs50.dev/), which runs Linux. When a command is different in Windows, the Windows version is given in a comment.

</details>

<details markdown="block">
<summary> 2. Create and activate a virtual environment </summary>

1. Create the project folder and move into it. From now on, all commands are executed from `image_project`:
```
$ mkdir image_project
$ cd image_project
```

2. Create the virtual environment. This creates the folder `.venv` inside `image_project`:
```
image_project/ $ python -m venv .venv
```
Since the name starts with a dot, `.venv` is a hidden folder: use `ls -a` to see it.

3. Activate the environment:
```
image_project/ $ source .venv/bin/activate      # Windows: .venv\Scripts\activate
```
The prompt now starts with `(.venv)`, which shows that the environment is active: the commands `python` and `pip` now refer to the Python and packages in `.venv`. To de-activate it, the command is `deactivate`.

4. Check which Python is running and which packages are installed. A new environment has (almost) no packages:
```
(.venv) image_project/ $ python -c "import sys; print(sys.prefix)"
(.venv) image_project/ $ pip list
```
`sys.prefix` is the folder of the Python installation in use: it should be the `.venv` folder of your project.

</details>

<details markdown="block">
<summary> 3. Install packages and create requirements.txt </summary>

1. With the environment active, install the packages for the project, specifying the versions:
```
(.venv) image_project/ $ pip install pillow==12.0.0 requests==2.32.5
```
Packages that these depend on (e.g. `urllib3` for `requests`) are installed automatically. Compare the result of `pip list` and `pip show requests` with what you got in the base environment: the version and the location are different.

2. Check where Python looks for packages:
```
(.venv) image_project/ $ python -c "import sys; print(sys.path)"
```
The `site-packages` folder inside `.venv` is listed, but the folder where the base environment packages are stored is not.

3. Save the list of installed packages and versions to `requirements.txt`, at the root of the project:
```
(.venv) image_project/ $ pip freeze > requirements.txt
```
Open `requirements.txt` to see its contents: one line per package, such as `pillow==12.0.0`.

4. Tell Git to ignore the `.venv` folder, by creating a file `.gitignore` with the line `.venv/`:
```
(.venv) image_project/ $ echo ".venv/" > .gitignore
```
If you share the project (e.g. on GitHub), you share the scripts, `requirements.txt` and `.gitignore`, but not `.venv`.

</details>

<details markdown="block">
<summary> 4. Delete and re-create the environment </summary>

Since `.venv` is disposable, we can delete it and re-create it from `requirements.txt`. This is also what a colleague does after downloading your project.

```
(.venv) image_project/ $ deactivate
image_project/ $ rm -rf .venv                     # Windows (PowerShell): Remove-Item -Recurse -Force .venv
image_project/ $ python -m venv .venv
image_project/ $ source .venv/bin/activate        # Windows: .venv\Scripts\activate
(.venv) image_project/ $ pip install -r requirements.txt
(.venv) image_project/ $ pip list
```

Exercise: install one more package in your environment (say, `emoji`), update `requirements.txt`, and send the file to a colleague. Your colleague should create a new project folder with a `.venv` environment from your `requirements.txt` and check with `pip list` that both environments have the same packages and versions.

</details>

<details markdown="block">
<summary> 5. Reading and writing text files </summary>

First, create the folders for the input and output files:
```
(.venv) image_project/ $ mkdir images output
```

In this step we write a script `notes.py`, in the `image_project` folder, that writes some notes about the leaf to a text file and then reads them back. Add each piece of code below at the end of `notes.py`, and run the script after each addition with
```
(.venv) image_project/ $ python notes.py
```
Then check the contents of `output/notes.txt` (open it in the editor, or use `cat output/notes.txt` in the terminal).

`open` is a function built into Python that allows you to open a file to read from it or to write to it. The second argument is the *mode*: `"w"` (write), `"a"` (append) or `"r"` (read, the default). In the code below, the file is opened in writing mode: if the file already exists, its previous contents are deleted. This is why running `notes.py` several times does not accumulate notes: each run starts with an empty file.
```Python
# notes.py
file = open("output/notes.txt", "w")
file.write("olive leaf, upper surface dark green\n")
file.close()
```
Notice that `write` does not add a new line: we need to include `"\n"` at the end of the string. To add new contents at the end of an existing file, open it in mode `"a"` (append) instead.

Instead of explicitly opening and closing a file, it's simpler and safer to use a *context manager*, with the keyword `with`, which automatically closes the file at the end of the block, even if an error occurs. Add the following lines to `notes.py`, which append a second note to the file:
```Python
with open("output/notes.txt", "a") as f:
    f.write("olive leaf, lower surface silvery\n")
```

To read the file, open it in mode `"r"`. The method `readlines` returns a list where each element is a line of the file (including the `"\n"` at the end). Add these lines to `notes.py`, so the script prints what it wrote:
```Python
with open("output/notes.txt", "r") as f:
    lines = f.readlines()
print(lines)
```
It is also possible to read the file one line at a time, which is better for large files. Add this last block to `notes.py` and compare its output with the previous one:
```Python
with open("output/notes.txt", "r") as f:
    for line in f:
        print(line.rstrip()) # rstrip() removes the "\n" at the end of the line
```

</details>

<details markdown="block">
<summary> 6. Binary files: downloading and inspecting an image </summary>

Files can be *text* files (human-readable, like `notes.txt` or a `.py` script) or *binary* files, like images. Binary files are opened with the modes `"rb"` and `"wb"`, and their contents are `bytes` instead of `str`.

The following script `download_image.py` downloads a photo of an olive leaf (upper and lower surface) from Wikimedia Commons, using the package `requests` (see class 5). The image is in `response.content`, which is a `bytes` object, so the file is opened in mode `"wb"`. Wikimedia Commons rejects requests without a descriptive *User-Agent* (the name of the program that makes the request), so we add one in `headers`.

```Python
# download_image.py
import requests

url = "https://upload.wikimedia.org/wikipedia/commons/b/b2/Olive-tree-leaf-0.jpg"
headers = {"User-Agent": "greends-ipython-course/1.0"}
response = requests.get(url, headers=headers)
response.raise_for_status() # raises an exception if the download failed
print(response.headers["Content-Type"], len(response.content), "bytes")

with open("images/olive_leaf.jpg", "wb") as f:
    f.write(response.content)
```
If the download fails, you can copy the same image from [datasets/olive_leaf.jpg](datasets/olive_leaf.jpg) in this repository. (Photo: Rnbc at en.wikipedia, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Olive-tree-leaf-0.jpg).)

The first bytes of a file usually identify its format. Let's read the first 4 bytes of the image:
```Python
with open("images/olive_leaf.jpg", "rb") as f:
    first_bytes = f.read(4)
print(first_bytes) # b'\xff\xd8\xff\xe0'
```
All JPEG files start with `b'\xff\xd8'`, and all PNG files start with `b'\x89PNG'`. Try to open the image in text mode (`"r"`) and see what happens.

</details>

<details markdown="block">
<summary> 7. Images with Pillow </summary>

Reading the bytes of an image is not enough to work with its pixels: we need to *decode* the file format. The package `Pillow` (imported as `PIL`) does that for many formats. The following script `explore_image.py` opens the image, prints its properties and saves three new images in `output`.

```Python
# explore_image.py
from PIL import Image

with Image.open("images/olive_leaf.jpg") as img:
    print(img.format, img.size, img.mode) # JPEG (1024, 768) RGB

    # each pixel of an RGB image is a tuple (red, green, blue) with values between 0 and 255
    print("upper surface:", img.getpixel((450, 220))) # (x, y) = (column, row), from the top-left corner
    print("lower surface:", img.getpixel((500, 580)))

    gray = img.convert("L") # "L" means grayscale: one value between 0 (black) and 255 (white) per pixel
    gray.save("output/olive_leaf_gray.png") # the format is given by the extension

    thumb = img.copy()
    thumb.thumbnail((256, 256)) # resizes in place, keeping the proportions
    thumb.save("output/olive_leaf_thumb.jpg")

    img.rotate(90, expand=True).save("output/olive_leaf_rotated.jpg")
```

Questions:
- Which surface of the leaf is brighter? Compare the values of `gray.getpixel(...)` at the same two points.
- What is the size of the thumbnail? Why is it not `(256, 256)`?
- Check the first bytes of `output/olive_leaf_gray.png` as in step 6: is it a PNG file?

</details>

<details markdown="block">
<summary> 8. Exercise: process a folder of images </summary>

Write a script `process_images.py` that creates a grayscale thumbnail of each image in a folder, and keeps a log of the processed files. The input and output folders are given in the command line (see `sys.argv` in class 5):
```
(.venv) image_project/ $ python process_images.py images output
```
For each image `name.jpg` (or `.jpeg`, `.png`) in `images`, the script saves `output/name_thumb.png` and appends a line `name.jpg -> output/name_thumb.png` to the file `output/log.txt`. Other files in the folder are ignored. Add a few more leaf images to `images` to test it.

Use the template below. The module `os` (standard library) provides `os.listdir(folder)`, which returns the list of file names in a folder, `os.path.join(folder, name)`, which builds a path, and `os.path.splitext(name)`, which splits a name such as `"olive_leaf.jpg"` into `("olive_leaf", ".jpg")`.

```Python
import os
import sys
from PIL import Image

def main():
    input_folder, output_folder = read_command_line()
    for file_name in os.listdir(input_folder):
        if is_image(file_name):
            input_path = os.path.join(input_folder, file_name)
            output_path = make_thumbnail(input_path, output_folder)
            write_log(output_folder, file_name, output_path)

def read_command_line():
    '''returns the input and output folders; exits with a usage message if they are missing'''
    ...

def is_image(file_name):
    '''returns True if the extension of file_name is .jpg, .jpeg or .png (in lower or upper case)'''
    ...

def make_thumbnail(input_path, output_folder, size=(256, 256)):
    '''saves a grayscale thumbnail of the image as a png file in output_folder and returns its path'''
    name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, name + "_thumb.png")
    ...
    return output_path

def write_log(output_folder, file_name, output_path):
    '''appends the line "file_name -> output_path" to output_folder/log.txt'''
    ...

main()
```

Suggested problem: *CS50 P-Shirt* from CS50P [Problem set 6](https://cs50.harvard.edu/python/psets/6/).

</details>
</ul>

</details>



---

<details markdown="block">
<summary><h2>  Class 7 (October 23, 2026): Jupyter notebooks; tabular data with pandas </h2></summary>

- Getting started with pandas: <https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html>
- Videos: overview by Rob Mulla, [Learning Pandas for Data Analysis? Start Here.](https://www.youtube.com/watch?v=DkjCaAMBGWM) (22'); course by Corey Schafer, [Pandas tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) (11 videos)
- Tidy data: H. Wickham (2014), [Tidy Data](https://doi.org/10.18637/jss.v059.i10), *Journal of Statistical Software* 59(10)

The goal of this class is not to memorise pandas syntax, which is well documented, but to understand **how pandas thinks about data**, because that is what makes it a tool for data science. All the code is in the notebook [class7/class7_pandas.ipynb](class7/class7_pandas.ipynb):

- **Part 1** (expository): typed columns and vectorisation, boolean masks, the index.
- **Part 2** (guided): `groupby`, `merge`, tidy vs wide tables.
- **Part 3** (on your own): cleaning and analysing official statistics on rural fires in Portugal (INE).

<ul>
<details markdown="block">
<summary> 1. Setup: a Jupyter notebook in the CS50 codespace </summary>

A Jupyter notebook (`.ipynb`) mixes text cells (Markdown) and code cells. Code cells are run one at a time with **Shift+Enter**, and their results (tables, numbers, plots) appear right below. Variables stay in memory between cells, which makes notebooks convenient to explore data step by step.

In the terminal of the [CS50 codespace](https://cs50.dev/):

1. Create a folder for the class and move into it:
```
$ mkdir class7
$ cd class7
```
2. (Recommended, see Class 6) Create and activate a virtual environment:
```
$ python -m venv .venv
$ source .venv/bin/activate
```
3. Install `pandas`, and `ipykernel`, which allows VS Code to run notebooks with this environment:
```
$ pip install pandas ipykernel
```
4. Download the notebook and open it:
```
$ wget https://raw.githubusercontent.com/isa-ulisboa/greends-ipython/main/class7/class7_pandas.ipynb
$ code class7_pandas.ipynb
```
5. Click **Select Kernel** (top right of the notebook) → **Python Environments** → choose `.venv`. If VS Code asks to install the *Jupyter* extension, accept.
6. Run the first cell. If it shows the pandas version, you are ready.

The datasets are read directly from the course repository, so there is no need to download them.

If the notebook cannot be set up in the codespace, open it in [Google Colab](https://colab.research.google.com/) (*File → Open notebook → GitHub*, then paste the notebook's URL).

</details>

<details markdown="block">
<summary> 2. The logic of pandas </summary>

1. **A table is a set of typed columns, not a list of rows.** Until now, we stored records as lists of dictionaries, one per observation. A `DataFrame` stores them as columns, and each column (a `Series`) has a single data type (`df.dtypes`). A `DataFrame` can be thought of as a dictionary of columns that share the same row labels.
2. **Vectorisation: describe *what*, not *how*.** Because a column has one type, an operation can be applied to the whole column at once, instead of looping over its elements:
   ```
   # the "Python lists" way
   temp_f = []
   for t in fires['temp']:
       temp_f.append(t * 9 / 5 + 32)
   # the pandas way
   fires['temp_f'] = fires['temp'] * 9 / 5 + 32
   ```
   The second version is shorter, and also much faster on large tables since the loop runs in compiled code.
3. **A boolean column is a question.** `fires['temp'] > 25` is a column of `True`/`False` (a *mask*), and `fires[mask]` keeps the rows where the mask is `True`. Masks are combined with `&` (and), `|` (or), `~` (not), with each condition between parentheses. Since `True` counts as 1, `mask.sum()` counts and `mask.mean()` gives a proportion.
4. **Rows have labels (the index), and pandas matches data by label.** See section 3.
5. **Split–apply–combine.** `fires.groupby('month')['area'].sum()` splits the rows by month, applies `sum` to each group and combines the results in a new table. This replaces the "loop and accumulate in a dictionary" pattern that we used in Classes 2 and 3. Together with `merge` (combine two tables through a common key, like a database join), it answers most descriptive questions about a dataset.

</details>

<details markdown="block">
<summary> 3. The index: labels vs positions </summary>

Every row of a `DataFrame` has a **label** (the *index*, shown on the left) and a **position** (0, 1, 2, ...). Columns also have labels (the column names) and positions. There are two ways to select rows and columns:

| | `.loc[rows, columns]` | `.iloc[rows, columns]` |
|---|---|---|
| selects by | label | position |
| slice `a:b` | includes `b` | excludes `b`, like Python lists |
| slice example | `fires.loc[0:4, 'temp':'wind']`<br>5 rows (labels 0 to 4), columns `temp`, `RH`, `wind` | `fires.iloc[0:4, 8:10]`<br>4 rows (positions 0 to 3), columns `temp`, `RH` (positions 8, 9) |
| typical use | `fires.loc[fires['month'] == 'aug', ['temp', 'RH']]` | `fires.iloc[:20, 4:8]` |

When a CSV file is read, the index is `0, 1, 2, ...`, so labels and positions coincide and `loc` and `iloc` *seem* to do the same thing. The difference appears as soon as rows are filtered, because **the original labels are kept**:
```
hot = fires[fires['temp'] > 25]
hot.iloc[0]      # first row of hot (by position)
hot.loc[0]       # KeyError: there is no longer a row with label 0
```

Labels do not need to be integers. `set_index` turns a column into the index:
```
months = pd.DataFrame({'mth': ['jan', 'feb', 'mar'], 'name': ['January', 'February', 'March']})
months = months.set_index('mth')
months.loc['feb', 'name']    # 'February'
```

**Why does the index exist? Alignment.** When two `Series` are combined, pandas matches their values **by label**, not by position. Labels that exist in only one of them give `NaN` (missing value), instead of a silent mismatch:
```
a = pd.Series([1, 2, 3], index=['jan', 'feb', 'mar'])
b = pd.Series([10, 20, 30], index=['mar', 'jan', 'feb'])
a + b            # jan 21, feb 32, mar 13
```
For instance, `fires.loc[fires['area'] > 10, 'month'].value_counts() / fires['month'].value_counts()` gives the proportion of large fires for each month, although the two counts have months in different orders.

`.reindex(labels)` builds a new `Series` (or `DataFrame`) with exactly the given labels, in the given order: existing labels keep their values, new labels get `NaN`, and labels not in the list are dropped:
```
a.reindex(['mar', 'jan', 'apr'])     # mar 3, jan 1, apr NaN (feb is dropped)
```

**After `groupby`, the group key becomes the index** of the result, sorted alphabetically (`apr`, `aug`, `dec`, ...). Therefore, the rows can be put in calendar order with `.reindex(['jan', 'feb', ...])`, and `.reset_index()` turns the index back into an ordinary column (useful before exporting or merging).

If needed, labels and positions can be converted into each other: `fires.columns.get_indexer(['FFMC', 'DMC'])` gives the positions of the columns, to use with `iloc`; `fires.index[0:20]` gives the labels of the first 20 rows, to use with `loc`.

</details>

<details markdown="block">
<summary> 4. Tidy vs wide data </summary>

A table is **tidy** when (1) each variable is a column, (2) each observation is a row, and (3) each type of observational unit is a table. The forest fires table is tidy: one row per fire, one column per variable.

A **wide** table spreads a variable across several columns. For instance, the total burned area by month and weekday:
```
wide = fires.pivot_table(index='month', columns='day', values='area', aggfunc='sum', fill_value=0)
```
Here, the weekday is a variable, but each weekday became a column. Wide tables are good for **people** (easy to read and compare, common in reports and in official statistics). Tidy tables are good for **computing**: filtering, `groupby`, `merge` and plotting all expect one variable per column. `melt` converts a wide table into a tidy (long) one:
```
long = wide.reset_index().melt(id_vars='month', var_name='day', value_name='area')
```
Rule of thumb: keep data tidy while working, and make it wide at the end, for a report.

</details>

<details markdown="block">
<summary> 5. Exercises with the forest fires dataset </summary>

The dataset [datasets/forestfires.csv](datasets/forestfires.csv) describes 517 fires in the Montesinho natural park, in Portugal ([source](https://archive.ics.uci.edu/dataset/162/forest+fires)). The variables are:

- `X`, `Y`: cell in a 9×9 grid over the park map
- `month`, `day`: month (`jan` to `dec`) and weekday (`mon` to `sun`); note that there is no year
- `FFMC`, `DMC`, `DC`, `ISI`: indices of the Canadian Fire Weather Index (FWI) system
- `temp`: temperature (°C); `RH`: relative humidity (%); `wind`: wind speed (km/h); `rain`: rain (mm/m²)
- `area`: burned area (ha), from 0 to 1090.84

The notebook covers the following exercises:

1. Read the file with `pd.read_csv` into a dataframe `fires`. Explore it with `.head()`, `.shape`, `.dtypes`, `.info()` and `.describe()`.
2. Compare the mean and the median of `area`. What proportion of the fires has `area == 0`? What is the best summary of a "typical" fire?
3. Select the fires with temperature above 25 °C, and with temperature between 20 and 25 °C.
4. How many fires occurred on weekends (use `.isin()`)? Is it more than expected if fires were spread evenly over the week?
5. Use `loc` to select the FWI variables for the fires in August and September. Then use `iloc` to take the first 5 rows of the result. Why does `.loc[0:4]` not give the same result?
6. Create a dataframe `by_month` with one row per month and columns `n_fires`, `avg_temp`, `avg_RH` and `total_area`, using `.groupby('month').agg(...)`. Order its rows from `jan` to `dec` with `.reindex()`. What is the effect of `.reset_index()`?
7. Create a dataframe `months` with the abbreviation, full name and season of each month, and `merge` it with `fires`. Compare the burned area by season.
8. Build a two-way table with the total burned area per month and weekday with `.pivot_table()`, and convert it back to a tidy table with `.melt()`.

</details>

<details markdown="block">
<summary> 6. On your own: rural fires in Portugal (INE) </summary>

The file [datasets/rural_fires.csv](datasets/rural_fires.csv) was exported from [INE](https://www.ine.pt), and contains the number of rural fires in 2023 by geographic unit and cause of fire. As with most official statistics, it was prepared for people and not for computing:

- the first 11 lines contain titles, and there are notes at the end of the file;
- the separator is `;`;
- each number is followed by ` &`, so pandas reads numbers as text;
- the first column combines a code and a name (`1111601: Arcos de Valdevez`);
- the rows mix different units (country, NUTS I, II, III regions, and municipalities);
- the table is wide: the cause of the fire is spread over six columns.

Part 3 of the notebook guides you through the following steps, from basic to challenging:

1. Look at the raw text of the file, and read only the data rows with `pd.read_csv(..., sep=';', skiprows=11, nrows=347, header=None, usecols=range(8), names=[...])`.
2. Convert the numeric columns to integers, using string methods on whole columns (`.str.replace`, `.str.strip`), and `.astype(int)`.
3. Split the first column into `code` and `name` with `.str.split(': ', n=1, expand=True)`, and keep the municipalities (codes with 7 characters).
4. Validate the data: does the sum over municipalities equal the total for Portugal? Is the total of each municipality equal to the sum of the six causes?
5. Compute the percentage of fires due to negligence in each municipality.
6. Convert the table into a tidy table with columns `code`, `name`, `cause`, `n_fires` with `.melt()`.
7. Use the first two characters of the municipality code to obtain its NUTS II region, and `merge` with the NUTS II rows to get the region names.
8. Compute the percentage of each cause in each region, and present the result as a wide table (regions × causes).
9. Export the tidy table with `.to_csv('rural_fires_2023_tidy.csv', index=False)`.

</details>

<details markdown="block">
<summary> 7. Exporting to file </summary>

Exporting is done with methods named `.to_...`, and reading with functions named `pd.read_...`, as listed in <https://pandas.pydata.org/docs/user_guide/io.html>. For instance:

1. Export a dataframe as a CSV file with `df.to_csv('filename.csv', index=False)`. Use `index=False` unless the index contains information (for instance, after `groupby`); otherwise, the labels `0, 1, 2, ...` are written as an extra column.
2. Export as an Excel spreadsheet with `df.to_excel('filename.xlsx', sheet_name='fires', index=False)` (requires `pip install openpyxl`).
3. Read an Excel spreadsheet with `pd.read_excel('filename.xlsx', sheet_name='fires')`.

</details>
</ul>

</details>


<!--

---

<details markdown="block">
<summary>  Class 8 (November 7, 2025): Pandas</summary>

Exercises with Pandas. Continued from last class

</details>

---

<details markdown="block">
<summary> Class 9 (November 15, 2025): OOP, classes, methods, attributes </summary>

Suggestions:
- [CS50P: Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/).
- Self contained [Python Object Oriented Programming (OOP) - For Beginners (53')](https://www.youtube.com/watch?v=JeznW_7DlB0). This beginner-friendly Python tutorial explains object-oriented programming (OOP) concepts. It covers classes and objects, demonstrating how to create custom objects using classes. Learn about methods, attributes, and inheritance.

Suppose that one wants write a script in python using classes to monitor plants at a nursery. Initially plants grow from seeds in trays and one wants to keep track of the trays and number of plants per tray. All plants in a given tray are from the same species. Plants can be removed or added to the tray. One wants to track the plants of each species that are in the nursery.

For this type of problem, one wants to mimic entities of the real world (plants, trays, nursery) as objects in  Python code. Object-oriented programming is an intuitive form of doing so. A class in Python is an object constructor, or a *blueprint* for creating objects.

The simplest example of  class, with very little functionality, is a class to store constant values, which are not supposed to change. When one calls the class `Constants` defined below, an instance of the class with the two properties `MAX_PLANTS_PER_TRAY` and `SALE_PRICE` is created.

```python
class Constants:
   MAX_PLANTS_PER_TRAY=50
   SALE_PRICE=5

print(Constants.SALE_PRICE)
```
However, in general we intent to call the class to create one instance (one object) of the class and set the **attributes** of that object. To indicate the values of the instance attributes we use the `__init__` method:
```python
class Tray:
  def __init__(self,species, number_of_plants=12):
     self.species=species
     self.number_of_plants=number_of_plants

tray=Tray('Pansy')
print(f"the tray has {tray.number_of_plants} {tray.species} plants")
```

A class can have **instance methods**, which are functions defined for objects of the class. In the example, `Tray` is a class with attributes `species` and `number_of_plants`, and we want to create methods `remove_plants` and `add_plants`. We can think of this as an *action* performed on the specific instance of the class.

```python
class Tray:
  def __init__(self,species, number_of_plants=12):
     self.species=species
     self.number_of_plants=number_of_plants
  # method to remove plants from tray
  def remove_plants(self, N):
      # check if N plants can be removed
      if N > self.number_of_plants:
          self.number_of_plants=0
      else:
          self.number_of_plants -= N
  # method to add plants to tray
  def add_plants(self, N):
      # check how many plants can be added
      if self.number_of_plants + N > Constants.MAX_PLANTS_PER_TRAY:
          self.number_of_plants = Constants.MAX_PLANTS_PER_TRAY
      else:
          self.number_of_plants += N
```
To test this try the following instructions, which you can think of as a sequence of actions: create tray, add or remove plants, and so on.

```python
tray1=Tray('Pansy', 26)
tray2=Tray('Petunia', 28)
tray1.add_plants(10)
tray2.remove_plants(5)
print(f"tray1 has {tray1.number_of_plants} {tray1.species} plants")
print(f"tray2 has {tray2.number_of_plants} {tray2.species} plants")
```
Note that we don't have an adequate `print` method for this class. This can be fixed by adding the method `__str__` to the class. You can adapt the following code and include it into the `Tray` class.

```
def __str__(self):
    return f"This tray contains {self.number_of_plants} {self.species} plants"
```

**Exercise**:

If you want to have a better control on all the plants in the nursery, you might want to create a new class called, say, `Inventory`. An instance of that class will represent your nursery, which contains trays (objects from class `Tray` above), with plants from different species. Class `Inventory` could have, for instance, the following attributes and methods:

- `trays`, an attribute which is a dictionary to store trays, with tray names as keys
- `add_tray`, a method that adds a tray object to the inventory, and gives it a name
- `remove_tray`, a method to remove a tray, identified by its name
- `get_tray`, a method to retrieve a tray, identified by its name. This allows to obtain a `tray` object, so you can add or remove plants to it.
-  `list_all_trays`, a method to list the current state of the inventory.

Suggestion of solution:

```python
class Inventory:
  def __init__(self,nursery_name,list_of_trays=[]):
    self.nursery_name=nursery_name
    self.list_of_trays=list_of_trays
  def add_tray(self,tray):
    self.list_of_trays.append(tray)
  def __str__(self):
    return f"This inventory contains {len(self.list_of_trays)} trays" 
  def get_tray(self,index):
    return self.list_of_trays[index]
```

Try:
```python
my_inventory=Inventory("my_nursery")
tray1=Tray('Pansy',25)
tray2=Tray('Pansy',32)
tray3=Tray('Petunia',10)
tray4=Tray('Petunia',25)
my_inventory.add_tray(tray1)
my_inventory.add_tray(tray2)
my_inventory.add_tray(tray3)
my_inventory.add_tray(tray4)
tray=my_inventory.get_tray(2)
tray.add_plants(10)
print(tray)
```

</details>

---

<details markdown="block">
<summary> Class 10 (November 21, 2025): Main concepts of OOP; Unit tests </summary>

<details markdown="block">
<summary> Main concepts of OOP</summary>

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230818181616/Types-of-OOPS-2.gif" alt="alt text" width="256">

The four main concepts of Object-Oriented Programming (OOP) are *Encapsulation*, *Abstraction*, *Inheritance*, and *Polymorphism*.  These concepts work together to create modular, scalable, and maintainable code in object-oriented programming.

This is a central topic in computer science, and therefore you can find all kind of resources about it. Among them, you can find simple descriptions of those concepts, with examples, at the following links:
1. (https://www.programiz.com/python-programming/object-oriented-programming)
2. (https://www.freecodecamp.org/news/object-oriented-programming-in-python/)
3. (https://www.w3schools.com/python/python_inheritance.asp), (https://www.w3schools.com/python/python_polymorphism.asp)


Building on the plant nursery example of last class, the following scripts illustrate the implementation of those concepts:
- [Polymorphism](oop_polymorphism_example_1.ipynb)  
- [Inheritance](oop_inheritance_polymorphism_example_2.ipynb)
- [Encapsulation: basic example](oop_encapsulation_example_3.ipynb)
- [Encapsulation: other example](oop_encapsulation_example_4.py)

Note that it is easy to abuse of classes in Python, which can make your code difficult to manage. Check the following video on [Avoid These BAD Practices in Python OOP](https://www.youtube.com/watch?v=yFLY0SVutgM) about *Learn why you should replace unnecessary classes with functions, use modules instead of classes with only static methods, and flatten deep inheritance hierarchies.*
</details>

<details markdown="block">
<summary> Unit tests</summary>

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
    with pytest.raises(ValueError, match="Farm area cannot be zero."): # match is optional: it matches Value Error message in emissions_per_hectare()
        farm.emissions_per_hectare()

def test_radius_of_circle_with_farm_area():
    farm = Farm("Circle Farm", 1)
    assert farm.radius_circle_with_farm_area() == pytest.approx(56.38, abs=0.1)
    farm = Farm("Circle Farm", 10)
    assert farm.radius_circle_with_farm_area() == pytest.approx(178.3, abs=0.01)
```

Exercise: Adapt the `Farm` class definition and `test_farm_carbon_footprint.py` in order to:
1. Add a method `.number_of_activities()` to class `Farm` that returns the number of activities. Check the correctness of that method with a new test in `test_farm_carbon_footprint.py`.
2. Adapt the `Farm` class so  `ValueError` should be raised if the property `area_hectares` is negative when you try to create an instance of `Farm`. Check with a new test in `test_farm_carbon_footprint.py` that the behavior of the class is as expected when `area_hectares` is negative.


</details>

Assignment: *Cookie jar* problem described at (https://cs50.harvard.edu/python/psets/8/jar/). Create a script for the problem and test it with `check50 cs50/problems/2022/python/jar`. 

</details>

--- 


<details markdown="block">
 
<summary> Class 11 (November 28, 2025): Exercises </summary>

The class was used to revise previous topics and work on exercises, including assignment #4.

</details>

---

<details markdown="block">
<summary> Class 12 (December 5, 2025): Packing/unpacking, args and kwargs, map, filter, lambda </summary>

## The packing/unpacking operators *  and **

The packing/unpacking operators allows us to deal with structures of variable length. The example below illustrates *packing* several numbers into a list.
```python
x=[1,2,3,4,5,6,7,8,9]
a,*b,c=x # b is the list [2,3,4,5,6,7,8]
print(a,b,c)
```
The same operator can be used to *unpack*:
```python
list1=[1,2,3]
list2=[6,7,8]
new_list=[*list1,4,5,*list2] # values are unpacked
print(new_list)
```
The * and ** operator are mostly used as arguments of functions that can accept a variable number of arguments (like function `print`): the operator * allows to pack all positional arguments into a *tuple* and the operator ** allows to pack all named arguments into a *dictionary*. In the example below, the `args` refers to positional arguments and `kwargs` refers to keyword arguments (i.e named arguments) . Note that one can have a combination of regular arguments, regular named arguments, `*args`, and `**kwargs` as arguments of a function, as long as keyword arguments follow positional arguments (if you try to switch the order, Python raises a `SyntaxError`).

```python
def pack(*args, **kwargs):
    return args,kwargs

x,y=pack(1,2,10, num_years=10,rate=0.03)

print('Positional arguments are packed into tuple',x)
print('Named arguments are packed into dictionary',y)
```

<details markdown="block">
<summary>Exercises on *args* and *kwargs* </summary>

###  Summing Arguments with `*args`  
Write a function `sum_all` that takes any number of positional arguments and returns their sum.

```python
def sum_all(*args):
    print(args)
    pass  # Your code here

# Example usage:
print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(10, 20, 30, 5))  # Output: 65
```

### Concatenate Strings with `*args`
Create a function `concat_strings` that takes any number of string arguments using `*args` and concatenates them into a single string.

```python
def concat_strings(*args):
    pass  # Your code here

# Example usage:
print(concat_strings("Hello", " ", "world", "!"))  # Output: "Hello world!"
print(concat_strings("Python", " is", " fun!"))    # Output: "Python is fun!"
```

### Handling Default Keyword Arguments with `**kwargs`
Write a function `greet` that accepts a keyword argument `name` (default value: `"Guest"`) and an optional keyword argument `greeting` (default value: `"Hello"`). Return the formatted greeting message. Hint: consider the method `get` for dictionaries: `get(key,default)` allows to set a default value if the `key` is not present. 

```python
def greet(**kwargs):
    pass  # Your code here

# Example usage:
print(greet(name="Alice", greeting="Hi"))  # Output: "Hi Alice"
print(greet(name="Bob"))                   # Output: "Hello Bob"
print(greet())                             # Output: "Hello Guest"
```

### Combine `*args` and `**kwargs` in a descriptive string
Write a function `describe_person` that takes positional arguments (`*args`) for hobbies and keyword arguments (`**kwargs`) for personal details (e.g., name, age). Return a formatted string describing the person.

```python
def describe_person(*args, **kwargs):
    pass  # Your code here

# Example usage:
print(describe_person("reading", "traveling", name="Alice", age=30))
# Output: "Alice (30 years old) enjoys reading, traveling."
```

### Filter Keyword Arguments with `**kwargs`
Create a function `filter_kwargs` that takes any number of keyword arguments and returns a new dictionary containing only those with values greater than 10.

```python
def filter_kwargs(**kwargs):
    pass  # Your code here

# Example usage:
print(filter_kwargs(a=5, b=15, c=20, d=3))  # Output: {'b': 15, 'c': 20}
```

### Combine `*args` for values and `**kwargs` for parameters

Suppose you borrowed several amounts and you want to compute the accumulated interest over a certain number of years. Create code that is going to use the positional arguments of the function `main` below as the amounts, `num_years` as the loan duration, and `rate`as the annual interest rate.

```python
# your code

if __name__=='__main__':
    main(1,2,10,5,4,num_years=10, rate=0.05)
```
</details>

## List and dictionary comprehension, map, filter and lambda

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

<details markdown="block">
<summary>Further examples and exercises</summary>

### Convert yields and filter high producers

```python
# Base data: crop yields in kilograms per field
yields_kg = [8500, 12300, 6400, 10200, 7500]

# Step 1: Convert each yield to tons (1 ton = 1000 kg)
yields_tons = list(map(lambda y: y / 1000, yields_kg))

print("Yields in tons:", yields_tons)
```

**Challenges:**

- Filter only the fields with yield greater than 8 tons using `filter` and `lambda`.
- Combine `map` and `filter` to first convert to tons and then keep only fields between 7 and 10 tons.

***

### Filter suitable soil pH and tag fields

```python
# Soil pH values for different fields
soil_ph = [5.8, 6.3, 7.0, 4.9, 6.8, 7.5]

# Step 1: Keep fields with pH between 6.0 and 7.0
suitable_ph = list(filter(lambda p: 6.0 <= p <= 7.0, soil_ph))

print("Suitable pH values:", suitable_ph)
```

**Challenges:**

- Use `map` and `lambda` to transform each pH value into a label: `"low"`, `"ideal"`, or `"high"` based on simple thresholds.
- Create a list of tuples `(pH, is_suitable)` where `is_suitable` is a Boolean from a `lambda` passed to `map`.

***

### Predict yield growth and flag underperformers

```python
# Yields in tons this year for several fields
current_yields = [8.5, 6.0, 9.2, 5.5, 7.8]

# Step 1: Project next year with 5% growth
next_year_yields = list(map(lambda y: round(y * 1.05, 2), current_yields))

print("Projected yields:", next_year_yields)
```

**Challenges:**

- Use `filter` to select fields whose projected yield is still below 7 tons, marking them for improvement.
- Use `map` to build a list of strings like `"Field 1: 8.93 tons"` based on the projected yields.

***

### Filter crops needing irrigation and scale irrigation amount

```python
# Average rainfall (mm) received by each crop type
rainfall = [520, 680, 450, 800, 390, 710]

# Step 1: Crops that need irrigation (rainfall < 500 mm)
needs_irrigation = list(filter(lambda r: r < 500, rainfall))

print("Rainfall for crops needing irrigation:", needs_irrigation)
```

**Challenges:**

- Assume each crop needs at least 600 mm total; use `map` on `needs_irrigation` to compute how much extra water (in mm) each crop requires.

***

### Compute productivity and select top fields (example of use of zip)

```python
# Yields in tons and corresponding areas in hectares
yields = [8.5, 9.1, 6.3, 10.0]
areas = [2.0, 2.5, 1.8, 3.0]

# Step 1: Productivity = yield / area (tons per hectare)
productivity = list(map(lambda y_a: round(y_a[^0] / y_a[^1], 2), zip(yields, areas)))

print("Productivity (tons/ha):", productivity)
```

**Challenges:**

- Use `filter` to keep only fields with productivity above 3.5 tons/ha.
- Use `map` with `zip` to generate a list like `("Field 1", productivity_value)` and then `filter` to keep only “high productivity” fields.

</details>
</details>

---

<details markdown="block">
<summary>  Class 13 (December 12, 2025): Introduction to IoT with Raspberry Pi</summary>

Video suggestion: [Raspberry Pi for beginners](https://www.youtube.com/playlist?list=PLLSegLrePWgIDKJTkdLyyQskh2HDdEL3y)

We will use Python to control physical devices through GPIO (general-purpose input/output) ports on a Raspberry Pi microcomputer. We will rely on the `gpiozero` Python package [https://gpiozero.readthedocs.io/en/latest/recipes.html](https://gpiozero.readthedocs.io/en/latest/recipes.html).

Topics of the class:
- Raspberry Pi (RPi) and PiOS (Linux)
- Retrieve local address of the Raspberry Pi with `hostname -I`. To do this, open a terminal on RPi and type `hostname -I` to retrieve the IP address. Also, type in the terminal `whoiam` to retrieve the username, say 'pi'.
- Accessing RPi remotely with `ssh` (secure shell)
- Connecting RPi to a breadboard using the *gpio* pins
- Using the *nano* text editor to create scripts
- Running scripts in RPi with `sudo python3 test.py`
- Implementing some basic recipes from `gpio zero` documentation that use the following physical devices: leds, buttons, and a line sensor

To start (access RPi from local network):
- You need: RPi username, say 'pi'; RPi password; and the RPi IP address, say '10.17.99.160'
- Access RPi with `ssh`: open terminal (CRTL+R and type `cmd` in Windows) and at the terminal prompt `$` type smth like `$ssh pi@10.17.99.160` (replace by actual username and IP address). You will be prompted for the RPi password.
- Since all the class has access to the RPi, it is important that you only work on your own working directory. So, the next step is to create it: change directory with `$cd Documents/tests` and create your temp directory with, say, `$mkdir bob` (replace by your own name). The full path to  your own working directory should be smth like `~/Documents/tests/bob`
- Go to your directory with `$cd bob`. 
- To create a new Python script (or to edit an existing one) type `$nano test.py`
- Inside the file type `print('hello')`
- Save contents with `CTRL-X`
- Type on terminal `$sudo python3 test.py` to execute the file. This should print `hello` in the terminal. So, you have run a Python script in a Raspberry Pi.

### Exercises with Raspberry Pi, breadboard, leds, button and connection wires:

1. [Blink LED](https://gpiozero.readthedocs.io/en/latest/recipes.html#led). To determine what is the resistor to use for different types of leds, check (https://www.hobby-hour.com/electronics/ledcalc.php): recall that the RPi voltage at the GPIO pins is 3.3 v.
3. [Check if button is pressed](https://gpiozero.readthedocs.io/en/latest/recipes.html#button)
4. [Button controlled LED](https://gpiozero.readthedocs.io/en/latest/recipes.html#button-controlled-led)
5. [Reaction game](https://gpiozero.readthedocs.io/en/latest/recipes.html#reaction-game)
6. [LED board](https://gpiozero.readthedocs.io/en/latest/recipes.html#ledboard)

### Additional exercises for led board with gpiozero
1. [LED_board](https://gpiozero.readthedocs.io/en/latest/recipes.html#ledboard). Interpret the code and verify that it is behaving as expected.

2. Look at the [advanced recipes for LEDboard](https://gpiozero.readthedocs.io/en/latest/recipes_advanced.html#ledboard-advanced). Create a "pyramid" of lights 5-3-1-3-5, that turn on and off and pause 1 second. You can build a loop such that the pyramid runs only 4 times and the execution stops.

</details>

---

<details markdown="block">
<summary> Class 14 (December 19, 2025): Introduction to IoT with Raspberry Pi (cont'd)</summary>


There are many hardware adapters that make it easier to connect sensors to a microcomputer. Here we look at the *Raspberry Pi hat* included in the  [Grove_Base_Kit_for_Raspberry_Pi](https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi/). The [Grove Base Hat for Raspberry Pi](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/) provides Digital/Analog/I2C/PWM/UART [ports](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#hardware-overview) to the RPi allowing it to be connected a large range of modules. 

The following code show how to access a [temperature and humidity sensor](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT1-p-745.html) readings programmatically. The sensor is connected to digital port D5. This code also allows access to gpio pin 17 to power a LED. You can find a [picture of the circuit here](grove_temperature_humidity.jpeg).

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
2. Consider the circuit [pictured here](grove_ultrasonic_ranger.jpeg) that uses an ultrasonic ranger (range of 0-4 m). Interpret the code below. 

```python
import time
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from gpiozero import LED
led=LED(17)
# Grove - Ultrasonic Ranger connected to port D5
# resolution: 1 cm; range: 0-4 m
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

3. Create a new script that combines the temperature/humidity sensor with the ultrasonic ranger sensor and the LED.
</details>

-->
