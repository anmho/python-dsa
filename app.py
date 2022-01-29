from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from data_structures.arraylist import ArrayList


arr = ArrayList()

arr.print()


arr.insert(1, 0)
arr.insert(2, 0)
arr.insert(3, 0)
arr.print()

arr.add(20)
arr.add(30)
arr.add(40)

arr.print()

arr.remove(0)
arr.print()

print(arr[2])
