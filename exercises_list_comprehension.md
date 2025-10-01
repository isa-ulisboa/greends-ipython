- Given a list of daily temperatures (in Celsius), Use a list comprehension to make a new list with these values converted to Fahrenheit. *Hint: The formula is `(C * 9/5) + 32`.*
 ```python
 celsius = [19, 21, 24, 18, 22]
 ```
Solution:
```
fahrenheit = [(c * 9/5) + 32 for c in celsius]
```


 - Given the following loop, rewrite this code using a list comprehension.
 ```python
 areas = [100, 150, 120, 180]
 squared = []
 for a in areas:
     squared.append(a ** 2)
 ```

 - Convert the loop below into a list comprehension.
 ```python
 crops = ["maize", "wheat", "rice", "bean", "barley"]
 filtered = []
 for crop in crops:
     if "a" in crop:
         filtered.append(crop)
 ```
Solution:
```
filtered = [crop for crop in crops if "a" in crop]
```

 - Convert the loop below into a list comprehension.
 ```python
plot_counts = [11, 15, 18, 22, 27, 30]
evens = []
for count in plot_counts:
    if count % 2 == 0:
        evens.append(count)
```
 
- Given nested lists, convert this double loop into a single list comprehension that flattens the soil samples list.
```python
soil_samples = [
    [2.1, 2.3, 2.4],
    [2.2, 2.7],
    [2.5, 2.6]
]
flat_samples = []
for sublist in soil_samples:
    for sample in sublist:
        flat_samples.append(sample)
```
Solution:
```
flat_samples = [sample for sublist in soil_samples for sample in sublist]
```


 - (advanced) The following code creates a Python `generator` and converts its content into a list. Adapt this code to some new application where it is not trivial to convert a `while` loop (which is not allowed in list comprehensions) into a `for` loop.
 ```python
 def gen():
     i = 5
     while i <= 20:
         yield i
         i += 10
 lst = [x for x in gen()]  # Now a list comprehension over a generator
 ```