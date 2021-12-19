import random
from datetime import datetime
import string
#from numpy import random as nprand

matrix_sizes = list([random.randint(2,10) for _ in range(10)])

start = datetime.now()
for n in range(10):
    random((matrix_sizes[n], matrix_sizes[n])).tolist()
    random((matrix_sizes[n], matrix_sizes[n])).tolist()
    

end = datetime.now()

diff = end-start
ex = diff.total_seconds()*1000

print("Total ex time:", ex, "ms")

