listx = [1,5,22,34,57,89,39,66,19,23,85]

result=filter(lambda x:True if x%2==0 else False,listx)
print(list(result))

result2 = filter(lambda x:True if x>50 else False,listx)
print(list(result2))
#filter also needs a callback to be passed
# the callback has to return boolean and the callback will be called for each
# each element in the collection if the callback returns true the element
# would be kept in tact otherwise filter will be called
# in the result only filtered elements ll be present 
# if the input list has n elements output list will have <=n elements