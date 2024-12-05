Here are 5 simple exercises that focus on converting basic Python code into list or dictionary comprehensions:

---

### **Exercise 1: Convert a For Loop to List Comprehension**
Convert the following for loop into a list comprehension:

```python
result = []
for x in range(10):
    result.append(x**2)
```

---

### **Exercise 2: Filter Numbers with List Comprehension**
Rewrite this code using a list comprehension:

```python
result = []
for x in range(20):
    if x % 2 == 0:
        result.append(x)
```

---

### **Exercise 3: Dictionary Comprehension**
Convert the following code to a dictionary comprehension:

```python
squares = {}
for x in range(5):
    squares[x] = x**2
```

---

### **Exercise 4: Nested Loops with List Comprehension**
Rewrite the nested loop as a list comprehension:

```python
pairs = []
for x in range(3):
    for y in range(2):
        pairs.append((x, y))
```

---

### **Exercise 5: Conditional Dictionary Comprehension**
Transform the following code into a dictionary comprehension with a condition:

```python
filtered_squares = {}
for x in range(10):
    if x % 2 == 0:
        filtered_squares[x] = x**2
```

---

Certainly! Here's a set of slightly more challenging exercises involving list and dictionary comprehensions:

---

### **Exercise 1: Conditional Transformation in List Comprehension**  
Convert the following loop into a list comprehension that includes a conditional transformation:

```python
result = []
for x in range(15):
    if x % 3 == 0:
        result.append(x**2)
    else:
        result.append(x)
```

---

### **Exercise 2: Dictionary Comprehension with String Keys**  
Transform the following loop into a dictionary comprehension, using strings as keys:

```python
word_lengths = {}
words = ["apple", "banana", "cherry", "date"]
for word in words:
    word_lengths[word] = len(word)
```

---

### **Exercise 3: Flatten a Nested List with List Comprehension**  
Rewrite this code using a single list comprehension to flatten the nested list:

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = []
for sublist in nested_list:
    for item in sublist:
        flattened.append(item)
```

---

### **Exercise 4: Conditional Dictionary Comprehension with Nested Loops**  
Convert the following nested loop into a dictionary comprehension with a condition:

```python
result = {}
for i in range(3):
    for j in range(3, 6):
        if j % i != 0:  # Avoid division by zero
            result[(i, j)] = i + j
```

---

### **Exercise 5: Filter and Transform Nested Dictionaries**  
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
```

---

These exercises require a bit more thinking about conditions, transformations, and handling nested structures, but they're still approachable for intermediate learners!
