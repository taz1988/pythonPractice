import sys
#boolean data type
thisIsBoolean = False
print(thisIsBoolean)
print(thisIsBoolean or True)
print(thisIsBoolean and false)
print(not thisIsBoolean)
# numeric types
print("floating point representation is depend on machine")
print(sys.float_info)
thisIsClassicInt = 1_000_000
print(thisIsClassicInt)
thisIsFloat = 1.34
print(thisIsFloat)
thisIsComplex = complex(1, 0)
print(thisIsComplex)
#Python automatically convert the types to wider
print(thisIsClassicInt + thisIsFloat)
print(thisIsFloat + thisIsComplex)
#numeric converting functions
print(int("20"))
print(float("3.14"))
#sequence types
myFirstList = [1 , 2, 3, "abc"]
myFirstTuple = ("cheese", "milk")
myFirstRange = range(2,4)
print(myFirstList)
print(myFirstTuple)
print(myFirstRange)
#common sequence operators
print("milk" in myFirstTuple)
print("mice" in myFirstTuple)
#Dictionary
myFirstDictionary = {"key" : "value"}
print(myFirstDictionary)
#classic set
myFirstSet = set([1 , 1, 2, 2, 3])
print(myFirstSet)
