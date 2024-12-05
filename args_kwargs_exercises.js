Here’s a list of 5 simple exercises to practice using `*args` and `**kwargs` in Python:

---

### **Exercise 1: Summing Arguments with `*args`**  
Write a function `sum_all` that takes any number of positional arguments and returns their sum.

```python
def sum_all(*args):
    pass  # Your code here

# Example usage:
print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(10, 20, 30, 5))  # Output: 65
```

---

### **Exercise 2: Concatenate Strings with `*args`**  
Create a function `concat_strings` that takes any number of string arguments using `*args` and concatenates them into a single string.

```python
def concat_strings(*args):
    pass  # Your code here

# Example usage:
print(concat_strings("Hello", " ", "world", "!"))  # Output: "Hello world!"
print(concat_strings("Python", " is", " fun!"))    # Output: "Python is fun!"
```

---

### **Exercise 3: Handling Default Keyword Arguments with `**kwargs`**  
Write a function `greet` that accepts a keyword argument `name` (default value: `"Guest"`) and an optional keyword argument `greeting` (default value: `"Hello"`). Return the formatted greeting message.

```python
def greet(**kwargs):
    pass  # Your code here

# Example usage:
print(greet(name="Alice", greeting="Hi"))  # Output: "Hi Alice"
print(greet(name="Bob"))                   # Output: "Hello Bob"
print(greet())                             # Output: "Hello Guest"
```

---

### **Exercise 4: Combine `*args` and `**kwargs`**  
Write a function `describe_person` that takes positional arguments (`*args`) for hobbies and keyword arguments (`**kwargs`) for personal details (e.g., name, age). Return a formatted string describing the person.

```python
def describe_person(*args, **kwargs):
    pass  # Your code here

# Example usage:
print(describe_person("reading", "traveling", name="Alice", age=30))
# Output: "Alice (30 years old) enjoys reading, traveling."
```

---

### **Exercise 5: Filter Keyword Arguments with `**kwargs`**  
Create a function `filter_kwargs` that takes any number of keyword arguments and returns a new dictionary containing only those with values greater than 10.

```python
def filter_kwargs(**kwargs):
    pass  # Your code here

# Example usage:
print(filter_kwargs(a=5, b=15, c=20, d=3))  # Output: {'b': 15, 'c': 20}
```

---

These exercises progressively build skills in handling `*args` and `**kwargs`, covering positional and keyword arguments, defaults, and combining both!
