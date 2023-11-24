# Introduction to Python 2023/2024

Masters in Data Science applied to agricultural and food sciences, environment, and forestry engineering.

Instructor: Manuel Campagnolo (mlc@isa.ulisboa.pt)

## Topics:

* [Course contents, documentation and tutorials](#python-documentation-and-tutorials)
* [Class 1](#class-1-september-15-2023)
* [Class 2](#class-2-september-22-2023)
* [Class 3](#class-3-september-29-2023)
* [Class 4](https://isa-ulisboa.github.io/greends-ipython/#class-4-october-6-2023)
* [Class 5](https://isa-ulisboa.github.io/greends-ipython/#class-5-october-13-2023)
* [Class 6]()
* [Class 7]()
* [Class 8]()
* [Class 9]()
* [Class 10]()
* 

## Install Python 3 and Visual Studio Code (VS Code)

[Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial):
  * Python 3 interpreter; For Windows, download either from python.org or from the Microsoft Store; For macOS install Python using Homebrew; Linux: built-in Python 3 installation
  * VS Code; Download from VS code site
  * VS Code Python extension: A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the language: >=3.7), including features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more!

## Python documentation and tutorials

### CS50P
The main tutorial for the class is [CS50P](https://cs50.harvard.edu/python/2022/weeks/). The table below compares the contents of that course with another well-known 
free online Python Programming course at [PP.fi](https://programming-23.mooc.fi/). The **CS50P** course problem sets tend to be difficult, while you can find at **PP.fi** a set of problems with a larger range of difficulty, from very easy to advanced. Both online courses provide a platform for coding and testing the corretness of the solutions. Both courses provide recorded lectures: [CS50P](https://cs50.harvard.edu/python/2022/weeks/) and [PP.fi](https://programming-23.mooc.fi/#lectures).

| CS50P     | Contents |  PP.fi | Contents |
| ----------- | ----------- |----------- | ----------- |
| Lecture 0    | Creating Code with Python; Functions; Bugs; Strings and Parameters; Formatting Strings; More on Strings; Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values    | Part 1 |     Information from the user; More about variables; Arithmetic operations; Conditional statements |
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




### Documentation
You can find information on basic concepts and features of the Python language and system at  [The Python Tutorial at python.org](https://docs.python.org/3/tutorial/index.html). 

### Tutorials

1. A nice interactive site is W3schools' [Python Tutorial](https://www.w3schools.com/python/default.asp) where you can find in particular an easy to use  [Python reference documentation](https://www.w3schools.com/python/python_reference.asp).

2. Another nice and very clear series of videos on Python are available in this Youtube channel: [Python Tutorials by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU). In particular, you might be interested in the following specific topics discussed in class:
* [text](https://docs.python.org/3/tutorial/introduction.html#text) and video [Python Tutorial for Beginners 2: Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2)
* [numbers](https://docs.python.org/3/tutorial/introduction.html#numbers) and video [Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data](https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3)
* [f-strings and other formatting options](https://docs.python.org/3/tutorial/inputoutput.html);
* [Lists](https://docs.python.org/3/tutorial/introduction.html#lists) and video [Python Tutorial for Beginners 4: Lists, Tuples, and Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4&t=1223s)
* [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), see video [Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs](https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5&pp=iAQB)
* I/O and csv files: [File Objects - Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25); [CSV Module - How to Read, Parse, and Write CSV Files](https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=28)

### Problem sets

1. List of both simple and more advanced programming exercises that you can run and test online: [programming-23.mooc.fi](https://programming-23.mooc.fi/all-exercises). Sign-in to have access to code editor and testing.
   
2. Compiled list of [CS50P proposed problems](https://raw.githack.com/isa-ulisboa/greends-ipython/main/problems.html)  (to be completed)

### Other links
1. PythonTutor: [Visualize code](https://pythontutor.com/visualize.html#mode=edit)

## Class 1 (September 15, 2023)

1. [CS50P](https://cs50.harvard.edu/python/2022/weeks/0/), Section on "Functions, Variables"
   * **Do before next class.** [Shorts: Visual Code for CS50P](https://cs50.harvard.edu/python/2022/shorts/visual_studio_code_for_cs50/)
    
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
    
## Class 2 (September 22, 2023)

1. Questionnaire Q0 (test) on the topics of the previous class;
2. Work on [Problem set 0](https://cs50.harvard.edu/python/2022/psets/0/): "indoor voice", "playback speed", and "making faces". For this last one, check [the emoji chart](https://unicode.org/emoji/charts/full-emoji-list.html) and follow the instructions: Every emoji has a unique Unicode assigned to it. When using Unicode with Python, replace "+" with "000" from the Unicode. And then prefix the Unicode with "\\". For example, "U+1F605" will be used as "\U0001F605". But there are alternative ways to encode emojis in your Python code: check [this link](https://www.makeuseof.com/how-to-include-emojis-in-your-python-code/)
4. **Do before next class.** Complete [Lecture 0](https://cs50.harvard.edu/python/2022/notes/0/) and video [CS50 Video Player](https://video.cs50.io/JP7ITIXGpHk) until the end, on the following topics: Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values
5. **Do before next class.** Study [Lecture 1](https://cs50.harvard.edu/python/2022/notes/1/) up to "Modulo" and watch video  [CS50 Video Player: Lecture 1](https://video.cs50.io/_b6NgY_pMdw) up to approximately 34' on the topics: Conditionals, if Statements, Control Flow, or, and.

**All topics to prepare before next class**: *Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values; Conditionals, if Statements, Control Flow, or, and, How to organize a program with `main()` and auxiliary functions.*

## Class 3 (September 29, 2023)

1. Questionnaire Q1 on the topics of the homework;
2. Work on [Problem set 0](https://cs50.harvard.edu/python/2022/psets/0/): Einstein. Work on [Problem set 1](https://cs50.harvard.edu/python/2022/psets/1/): The Hitchhiker’s Guide to the Galaxy's Deep Thought, Home Federal Savings Bank, File Extensions.
5. **Do before next class.** Study the remainder of [Lecture 1](https://cs50.harvard.edu/python/2022/notes/1/) starting at "Modulo" and watch video  [CS50 Video Player: Lecture 1](https://video.cs50.io/_b6NgY_pMdw) after 34'.
6. **Do before next class.** Study [Lecture 2](https://cs50.harvard.edu/python/2022/notes/2/) up to "More about lists" and "Length" and watch video  [CS50 Video Player: Lecture 2](https://video.cs50.io/-7xg8pGcP6w) up to approximately 45'.
7. **Do before next class.** Try solving problems from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/): Camel; Coke Machine; Just setting up my twttr

**Topics to prepare before next class**: *Modulo; Creating Our Own Parity Function; Pythonic; match, Loops; While Loops; For Loops; Improving with User Input; More About Lists; Length*

## Class 4 (October 6, 2023)

1. Questionnaire Q2 on the topics of the homework;
2. Work on problems from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/): Camel; Coke Machine; Just setting up my twttr (P1: submit in Fenix one of those problems to be indicated in class)
6. **Do before next class.** Study remainder of [Lecture 2](https://cs50.harvard.edu/python/2022/notes/2/)  watch video  [CS50 Video Player: Lecture 2](https://video.cs50.io/-7xg8pGcP6w) starting at Dictionaries (~45').
7. **Do before next class.** [Lecture 3](https://cs50.harvard.edu/python/2022/notes/3/) and video [CS50 Video Player: Lecture 3](https://video.cs50.io/LW7g1169v7w)
8. **Do before next class.** Try solving problems from [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/). Note: for the "Taqueria" problem: EOFError is the error raised by "CRTL-D" in Mac and "CTRL-Z" in Windows.
   
**Topics to prepare before next class**: *Dictionaries, More on code modularity (Mario example), Exceptions, Runtime Errors, try, else, Creating a Function to Get an Integer, pass*

## Class 5 (October 13, 2023)

1. Questionnaire Q3 on the topics of the homework (if you don't have access to your area in Fenix: [link](Q3_max_18.pdf))
2. Work on problems from [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/).
7. **Do before next class.** [Lecture 4](https://cs50.harvard.edu/python/2022/notes/4/) and video [CS50 Video Player: Lecture 4](https://video.cs50.io/MztLZWibctI)
8. **Do before next class.** Try solving problems from [Problem Set 4](https://cs50.harvard.edu/python/2022/psets/4/). Try problem "Guessing Game" (not hard) and "Little Professor" (group assignment). For the group assigment, the goal is to fill the missing code in [professor_incomplete.py](https://github.com/isa-ulisboa/greends-ipython-exercises/blob/main/professor_incomplete.py). The completed code should pass the correctness test in [https://cs50.dev/](https://cs50.dev/).
   
**Topics to prepare before next class**: *Libraries, Random, Statistics, Command-Line Arguments, slice, Packages, APIs, Making Your Own Libraries*

## Class 6 (October 20, 2023)

1. Questionnaire Q4 on the topics of the homework (if you don't have access to your area in Fenix: [link](q4.pdf))
2. Evaluated group assignment ("Little Professor") in class
3. Discussed references in Python with examples from Part 5 of [PP.fi](https://programming-23.mooc.fi/) and made experiments with PythonTutor: [Visualize code](https://pythontutor.com/visualize.html#mode=edit).
4. **Do before next class.** Some groups still have to improve the previous assignment. All groups should solve Problem P3 (also a group assigment):
   - [P3: Problem description](assignment_P3.pdf)
   - [Incomplete code](https://github.com/isa-ulisboa/greends-ipython-exercises/blob/main/distances_incomplete.py)
   - Groups members should try to collaborate by syncronizing their work through VSCode and GitHub using the Source Control menu in VSCode:
    * [Working with GitHub in VS Code (VSCode documentation)](https://code.visualstudio.com/docs/sourcecontrol/github)
    * Notes on [how to clone GitHub repository and syncronize it with local folder](Clone_GitHub_repository_and_syncronize_with_local_folder.pdf)
    * Notes on [how to publish a local folder to GitHub](VSCode_local_folder_to_GitHub.pdf)

## Class 7 (October 27, 2023)

1. Questionnaire Q5 on recent topics (if you don't have access to your area in Fenix: [link](Q5_max_12.pdf)
2. Evaluate group assignment P3 ("Distances") in class
3. Unit tests with `pytest`: examples 
4. **Do before next class (November, 11).**
   * [Lecture 5 on Unit tests](https://cs50.harvard.edu/python/2022/notes/5/) and video [CS50 Video Player: Lecture 5](https://video.cs50.io/tIrcxwLqzjQ)
   * Group assignment, which is mostly about creating unit tests for code. Groups members should collaborate through VSCode and GitHub using Source Control menu in VSCode or git command lines. [P4: Problem description](https://github.com/isa-ulisboa/greends-ipython-exercises/blob/main/assignment_P4.pdf); files: [myfunctions.py](https://github.com/isa-ulisboa/greends-ipython-exercises/blob/main/myfunctions.py); [myhaversine.py](https://github.com/isa-ulisboa/greends-ipython-exercises/blob/main/myhaversine.py); [some_distances.py](https://github.com/isa-ulisboa/greends-ipython-exercises/blob/main/some_distances.py)
   * [Lecture 6 on File I/O](https://cs50.harvard.edu/python/2022/notes/6/) and video [CS50 Video Player: Lecture 6](https://video.cs50.io/KD-Yoel6EVQ)

## Class 8 (November 10, 2023)

1. Questionnaire Q6 on recent topics. If you don't have access to your area in Fenix: [link](Q6_max_12.pdf)
2. Evaluate group assignment P4 on Unit Tests ("Haverside") in class
3. Pandas: series and dataframes; I/O; first examples
4. **Do before next class (November 17).**
   * [Pandas documentation/getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) up to section "How to combine data from multiple tables".
   * Optional: Check videos on Pandas on [Python Tutorials by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU): from [Python Pandas Tutorial (Part 2): DataFrame and Series Basics - Selecting Rows and Columns](https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=129) to [Python Pandas Tutorial (Part 6): Add/Remove Rows and Columns From DataFrames](https://www.youtube.com/watch?v=HQ6XO9eT-fc).

## Class 9 (November 17, 2023)

1. Questions about Pandas.
2. Questionnaire Q7 on recent topics. If you don't have access to your area in Fenix: [link](Q7_max_12.pdf)
3. Finish to evaluate group assignment P4 on Unit Tests ("Haverside") in class (remaining groups)
4. Regular expressions (regex)
5. **Do before next class (November 24).**
 * [Lecture 7](https://cs50.harvard.edu/python/2022/notes/7/) and video [CS50 Video Player: Lecture 7](https://video.cs50.io/hy3sd9MOAcc)
 * Solve problems from [Problem Set 7](https://cs50.harvard.edu/python/2022/psets/7/). In particular, you should solve problems "NUMB3RS" and "Regular, um, Expressions", following the instructions (i.e. solve and test your solution).
 * Try [https://regex101.com/](https://regex101.com/) to do experiments and understand better how "regex" works.
