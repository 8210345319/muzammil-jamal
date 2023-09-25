#a new class that is derived from builtin Exception class is defined as custom exception.
#custom exception can make code more readable and reduce amount of code we write later to try and figure out what happened.
class WordError(Exception):
    "Raised when word limit is more than 500"
    pass
try:
     wordlimit=int(input("enter the limit:"))
     if(wordlimit > 500):
            raise WordError
except WordError:
            print("limit is crossed")
else:
            print("limit is bearable")