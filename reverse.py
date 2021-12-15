def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Geeksforgee"
  
print ("The original string  is : ",s)

  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))
