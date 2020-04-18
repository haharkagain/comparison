list1 = []
list2 = []

firstNotSecond = []
secondNotFirst = []

print (list1)
print (list2)

def checker(list1, list2, output): # checks whats in the first list but not the second and appdends to a third list
    for i in range(len(list1)):
        for j in range(len(list2)):
            if (list1[i] == list2[j]):
                break # gets out without recording
        else: # runs if the previous loop doesnt find any matches
            output.append(list1[i]) # adds to output list

checker(list1, list2, firstNotSecond)
checker(list2, list1, secondNotFirst)

print (firstNotSecond)
print (secondNotFirst)
