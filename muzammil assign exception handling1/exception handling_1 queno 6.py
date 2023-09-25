class NumberError(Exception):
    "Raised when series is higher than 200"
    pass

try:
        series=int(input("Enter the number:"))
        if(series > 200):
             raise NumberError
except NumberError:
     print("number crossed more than 200 not allowed")
else:
     print("number is eligible")
         
        
        
        
