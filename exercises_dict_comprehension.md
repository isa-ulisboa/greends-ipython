- Increase fertilizer dosage by 10%: given a dictionary of field names and fertilizer dosage (in kg/hectare), write a dictionary comprehension which increases every dosage by 10%.

 ```python
 fertilizer_dosage = {
     "Field A": 100,
     "Field B": 90,
     "Field C": 110
 }
 ```
Two possible solutions:
```
increased_dosage = {key: fertilizer_dosage[key] * 1.10 for key in fertilizer_dosage} # accessing value with '[key]'
increased_dosage = {key: value * 1.10 for key, value in fertilizer_dosage.items()} # using '.items()'
```

 - Create a crop area dictionary: given lists of `crop_names` and `areas`, make a dictionary comprehension that pairs each crop with its area.

 ```python
 crop_names = ["maize", "soybean", "rice"]
 areas = [12, 8, 15]  # Area in hectares
 ```

Solution:
```
crop_area = {crop: area for crop, area in zip(crop_names, areas)} # 'zip' combines multiple iterators into an iterator of tuples
```

 - Select only large fields: given a dictionary below, rewrite the code as a dictionary comprehension, selecting only fields above 10 hectares.

 ```python
 fields = {"North": 12, "South": 7, "East": 15, "West": 9}  # values are hectares
 large_fields = {}
 for field, area in fields.items():
     if area > 10:
         large_fields[field] = area
```
Solution:
```
large_fields = {field: area for field, area in fields.items() if area > 10}
```