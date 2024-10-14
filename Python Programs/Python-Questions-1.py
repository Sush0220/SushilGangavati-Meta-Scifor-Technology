#1. Find sum of list elements
list1 = [1,2,3,4,5]
sum = 0

for i in list1:
    sum = sum + i
print(sum)

#2. Find the maximum number in a list
list1 = [1,2,3,4,5,6,7, 10]
max = list1[0]
for i in list1:
    if(i > max):
        max = i
print(max)

#3. Remove Duplicates from list
list1 = [1,1,2,3,4,4,5,6,6,7]
for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)
print(list1)

#4. Check if elements in a list are unique
list1 = [1,2,3,4,5,6,7]
seen = []
unique = True
for i in list1:
    if i in seen:
        unique = False
    else:
        seen.append(i)
print(unique)

#5. Reverse a list
def reverse(list):
    return list[::-1]

list1 = [1, 2, 3, 4, 5]
print(reverse(list1))

#6. Count Even and Odd numbers in a list
list1 = [2,5,10,11,45,46,53]
def countEvenOdd(list):
    evenCount = 0
    oddCount = 0
    for i in list:
        if i%2==0:
            evenCount += 1
        else:
            oddCount += 1
    print("Even Count:", evenCount)
    print("Odd Count:", oddCount)

countEvenOdd(list1)    

#7. Check if List is subset of another list
list1 = [1,2,3]
list2 = [1,2,3,4,5]
def checkSubset(list1, list2):
    for i in list1:
        if(i not in list2):
            return False
    return True

print(checkSubset(list1, list2))

#8. Find Max Diff between two consecutive numbers in a list
list1 = [1,7,3,10,5]
def findMaxDiff(list):
    maxDiff = 0
    for i in range(1, len(list)):
        diff = abs(list[i] - list[i-1])
        maxDiff = max(maxDiff, diff)
    print(maxDiff)
findMaxDiff(list1)

#9. Merge Multiple Dictionaries
dict1 = {"Name": "Sushil"}
dict2 = { "Age": 20}
dict3 = {"City": "Mumbai"}
def mergeDict(dict1, dict2,dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1
print(mergeDict(dict1, dict2, dict3))

#10. Find Word Frequency in a sentence
def wordFreq(str):
    dict = {}
    words = str.split()
    for word in words:
        word = word.lower()
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

str = "I love Python. I love Java. I love C++"
print(wordFreq(str))