#Code by Tejaswini
#Date 28 April,2020
#Released under GNU GPL

import numpy as np

#if using termux
import subprocess
import shlex
#end if

gain = 50				# higher order transfer function
num = [1,8,15]
char_eq = [1,12,94,448,750]
zeros=np.roots(num)			#zeros
poles=np.roots(char_eq)		#poles

print("poles are : " ,poles)
print("zeros are :",zeros )
