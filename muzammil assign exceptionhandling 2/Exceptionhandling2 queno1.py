#clasc Exception and its subclasses are a form that indicates conditions a application want to catch.
class ValueError(Exception):
    "Raised when series is more than 200"
    pass
try:
    limit=int(input("enter the limit:"))   
    if(limit < 700):
        raise ValueError
except ValueError:
    print("value below the required limit")
else:
    print("value is in required limit")

