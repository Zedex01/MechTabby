import sys
print("Python executable:", sys.executable)
print("sys.path:")
for p in sys.path:
    print(" ", p)
try:
    import requests
    print("requests imported successfully!")
except ModuleNotFoundError:
    print("requests NOT found!")
