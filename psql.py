import random
from datetime import datetime
import string

start = datetime.now()
x = ""

for _ in range(10):
    a = 0;
    a = 1;
    a = 2;
    a = 3;
            
end = datetime.now()
diff = end-start
ex = diff.total_seconds()*1000

print("Total ex time:", ex, "ms")

