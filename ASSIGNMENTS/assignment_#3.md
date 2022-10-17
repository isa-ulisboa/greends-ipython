# ASSIGNMENT #3 - create a project to interact with your namespaces
## Difficulty (1-5): 2 
- Sync your Fork
- in your fork, within the FORGE folder, create a folder called YOURNAME
- in this new folder create another folder called "myForge"
- move the file you created before (yourname.py) into the new folder YOURNAME your created
- create :
    - a file called myFunctions.py into the folder YOURNAME
    - a file called myOtherFunctions.py into the folder YOURNAME/myForge
- in the file myFunctions.py create
    - two different functions returning two different strings
- in the file myOtherFunctions.py create
    - one function returning a string
    - assign to variables (val1, val2, val3) , 3 different datatypes (int, string, list)
- in yourname.py file add code to:
   a - import your myfunctions module
   b - how would you do to import your module myOtherFunctions ?
   c - assign to a variable called res the result of the first function of myFunctions module
   d - print the res variable
   e - assign to a variable called res the result of the second function of myFunctions module
   f - print the res variable
   g - print the variable val1, val2 and val3 from the module myOtherFunctions
   h - create an alias of the myOtherFunctions module and redo steps c, d, f, g, using the alias 
   i - add this line of code: from myForge.myOtherFunctions import *  
        - how to redo steps c, d and g following logic?
   j - add this line of code: from myForge import myOtherFunctions
        - how to redo steps c, d and g following logic?
   k - Final note: This code flow is only to explain and demonstrate namespaces. 
                   In your code, you only use one style and place all imports in 
                   the beginning of the code
- Commit (after checking there are no errors), Push, Create PR (Pull Request)