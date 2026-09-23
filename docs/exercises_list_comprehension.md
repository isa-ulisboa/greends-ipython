### Given a list of daily temperatures (in Celsius), Use a list comprehension to make a new list with these values converted to Fahrenheit. 

*Hint: The formula is `(C * 9/5) + 32`.*
 
 ```python
 celsius = [19, 21, 24, 18, 22]
 ```

<details>

<summary> Possible solution: </summary>

```
fahrenheit = [(c * 9/5) + 32 for c in celsius]
```
</details>

---

 ### Convert the loop below into a list comprehension
 
 ```python
 areas = [100, 150, 120, 180]
 squared = []
 for a in areas:
     squared.append(a ** 2)
 ```

---

### Convert the loop below into a list comprehension

 ```python
 crops = ["maize", "wheat", "rice", "bean", "barley"]
 filtered = []
 for crop in crops:
     if "a" in crop:
         filtered.append(crop)
 ```
<details>

<summary> Possible solution: </summary>

```
filtered = [crop for crop in crops if "a" in crop]
```
</details>

---

### Convert the loop below into a list comprehension.
 
```python
plot_counts = [11, 15, 18, 22, 27, 30]
evens = []
for count in plot_counts:
    if count % 2 == 0:
        evens.append(count)
```

---
 
### Given nested lists, convert this double loop into a single list comprehension that flattens the soil samples list.

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

<details>
<summary> Possible solution: </summary>

```
flat_samples = [sample for sublist in soil_samples for sample in sublist]
```
Suggestion: try it on [Python tutor](https://pythontutor.com/visualize.html#code=soil_samples%20%3D%20%5B%0A%20%20%20%20%5B2.1,%202.3,%202.4%5D,%0A%20%20%20%20%5B2.2,%202.7%5D,%0A%20%20%20%20%5B2.5,%202.6%5D%0A%5D%0A%0Aflat_samples%20%3D%20%5Bsample%20for%20sublist%20in%20soil_samples%20for%20sample%20in%20sublist%5D%0A%0Aprint%28flat_samples%29&mode=edit&origin=opt-frontend.js&py=311)

</details>

