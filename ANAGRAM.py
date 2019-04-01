## Python code to check whether 2 strings are ANAGRAMS or Not
from numpy import prod
strA = "ABFN"
strB = "AAHM"
sum_StrA = sum(map(ord, strA))
print("sum of Ascii values of strA is ={}".format(sum_StrA))
sum_StrB = sum(map(ord, strB))
print("sum of Ascii values of strB is ={}".format(sum_StrB))
list_StrA = (list(map(ord, strA)))
list_StrB = (list(map(ord, strB)))
print("StrA in Ascii is ={}".format(list_StrA))
print("StrB in Ascii is = {}".format(list_StrB))
prod_StrA=prod(list_StrA)
prod_StrB=prod(list_StrB)
print("product of Ascii values of StrA is = {}".format(prod_StrA))
print("product of Ascii values of StrB is = {}".format(prod_StrB))
sq_StrA = []
sq_StrB = []
for i in list_StrA :
    sq_StrA.append(i**2)
print("squares of Ascii values of strA is ={}".format(sq_StrA))
for i in list_StrB :
    sq_StrB.append(i**2)
print("squares of Ascii values of strB is ={}".format(sq_StrB))
sum_sq_StrA = sum(sq_StrA)
print("Sum of squares of ASCII values of strA = {}".format(sum_sq_StrA))
sum_sq_StrB = sum(sq_StrB)
print("Sum of squares of ASCII values of strB = {}".format(sum_sq_StrB))
if sum_StrA == sum_StrB and prod_StrA == prod_StrB and sum_sq_StrA == sum_sq_StrB:
  print("Given strings are Anagrams")
else:
  print("Given strings are not Anagrams")