
import myfunctions
import myforge.myotherfunctions
import myforge.myotherfunctions as mof
from myforge.myotherfunctions import *

# the way to access the functions depends on how you import them

#res = myforge.myotherfunctions.myspecialfunction()
#res = mof.myspecialfunction()
res = myspecialfunction(3, 4)
print(res)

res = myfunctions.myfirstgreendsfunction()
print(res)

res = myfunctions.mysecondgreendsfunction()
print(res)

print(myforge.myotherfunctions.val1)
print(myforge.myotherfunctions.val2)
print(myforge.myotherfunctions.val3)

res = myfunctions.VolWaterContent(0.2, 1.3, 0.2, 0.05, 1)
print(res)