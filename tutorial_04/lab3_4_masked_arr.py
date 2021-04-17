#masked arrays
import numpy as np
import numpy.ma as ma

arr = np.arange(9)
marr = ma.array(arr, mask=[0,0,1,1,0,0,0,0,0], fill_value=[0,0,8989,54,00,0,0,0,0])
#marr2 = ma.masked_array(arr, mask=[0,0,1,0,0,0,0,0,0], fill_value=-999)
print("Array:  ",arr,"    ",type(arr))
print("Masked Array:  ",marr,"    " ,type(marr))
print("Filled Array:  ",marr.filled(),"   ",type(marr.filled()))
