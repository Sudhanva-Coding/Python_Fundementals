fruits = ["Apple","Strawberry","Banana","Cherry","Lychee"]
print(type(fruits))
print(fruits[0])


print(fruits[3])
#use append
fruits.append("Mango")
print(fruits)



#delete items
fruits.remove("Banana")
print(fruits)


#changing items
fruits[3] = "Watermelon"
print(fruits)


for i in fruits:
    print(i)

print(len(fruits))