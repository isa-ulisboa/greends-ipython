# greends-ipython 2023/2024

## Install Python 3 and Visual Studio Code (VS Code)

[Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial):
  * Python 3 interpreter; For Windows, download either from python.org or from the Microsoft Store; For macOS install Python using Homebrew; Linux: built-in Python 3 installation
  * VS Code; Download from VS code site
  * VS Code Python extension: A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the language: >=3.7), including features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more!

## Python documentation and tutorials
The main tutorial for the class is [CS50](https://cs50.harvard.edu/python/2022/).

You can find information on basic concepts and features of the Python language and system at  [The Python Tutorial at python.org](https://docs.python.org/3/tutorial/index.html). In particular, you might be interested in the following specific topics discussed in class:
* [text](https://docs.python.org/3/tutorial/introduction.html#text);
* [numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
* [f-strings and other formatting options](https://docs.python.org/3/tutorial/inputoutput.html);

A nice interactive site is W3schools' [Python Tutorial](https://www.w3schools.com/python/default.asp) where you can find in particular an easy to use  [Python reference documentation](https://www.w3schools.com/python/python_reference.asp).

## Class 1 (September 15, 2023)

1. [CS50](https://cs50.harvard.edu/python/2022/), Section on "Functions, Variables"
   * **Do before next class.** [Shorts: Visual Code for CS50](https://cs50.harvard.edu/python/2022/shorts/visual_studio_code_for_cs50/)
    
2. Some useful keyworks for the command line interface in terminal:
* `echo > filename` to create a new file (same as `code filename` in CS50 videos); to create an empty file, just press return when asked for the argument.
* `ls` to list files in folder
* `cp filename newfilename` to copy a file, e.g. `cp ..\hello.py  farewell.py` (`..` represents parent folder)
* `mv filename newfilename` to rename or move file, e.g. `my farewell.py goodbye.py` or `mv farewell.py ..` (move one folder up)
* `rm filename` to delete (remove) file
* `mkdir foldername` to create new folder
* `cd foldername` change directory, e.g. `cd ..` 
* `rmdir foldername` to delete folder
* `clear` to clear terminal window

3. [CS50](https://cs50.harvard.edu/python/2022/), Section on "Functions, Variables"
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

1. Questionnaire Q1 on the topics of the previous class;
2. Work on [Problem set 0](https://cs50.harvard.edu/python/2022/psets/0/): "indoor voice", "playback speed", and "making faces". For this last one, check [the emoji chart](https://unicode.org/emoji/charts/full-emoji-list.html) and follow the instructions: Every emoji has a unique Unicode assigned to it. When using Unicode with Python, replace "+" with "000" from the Unicode. And then prefix the Unicode with "\\". For example, "U+1F605" will be used as "\U0001F605". Here, "+" is replaced with "000" and "\" is prefixed with the Unicode. But there are alternative ways to encode emojis in your Python code: check [this link](https://www.makeuseof.com/how-to-include-emojis-in-your-python-code/)
3. Presentation of topics to prepare for next class, namely Integers; Floats; Def; and Returning Values. How to organize a program with `main()` and auxiliary functions.
4. **Do before next class.** Complete [Lecture 0](https://cs50.harvard.edu/python/2022/notes/0/) and video [CS50 Video Player](https://video.cs50.io/JP7ITIXGpHk) until the end, on the following topics: Integers or int; Readability Wins; Float Basics; More on Floats; Def; Returning Values
5. **Do before next class.** Study [Lecture 1](https://cs50.harvard.edu/python/2022/notes/1/) up to "Modulo" and watch video  [CS50 Video Player](https://video.cs50.io/_b6NgY_pMdw) up to approximately 34' on the topics: Conditionals, if Statements, Control Flow, or, and.
