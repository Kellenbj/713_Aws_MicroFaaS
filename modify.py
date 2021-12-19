import random
from datetime import datetime
import string

start = datetime.now()
x = ""

for _ in range(10):
    x = x.join(random.choice(["Jenny", "Jack", "Joe"]))
    y= str(random.randint(0,999))

            
end = datetime.now()
diff = end-start
ex = diff.total_seconds()*1000

print("Total ex time:", ex, "ms")

