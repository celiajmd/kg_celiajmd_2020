# kg_celiajmd_2020
Kargo online assessment



## Requirement:
 Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.

## Tips for run:
Please input s1. 
Press 'Enter'.
Then input s2.
Press 'Enter' again.
The result will come out.

## Seudocode:
```
if the lengh(s1) != lengh(s2):
then return False
create a dictionary to store each mapping charater in s2 for s1
loop the s1 by character
if the mapping character not exist yet: add it
if the mapping character exists and same with the current mapping character: continue to loop
if the mapping character exists and different with the current mapping character: return False
return True
```

## Complexity
### Time complexity
O(n)+O(1) >> O(n) , where O(n) is  for loop in the s1, and O(1) is for searching in the dictionary.
### Space complexity
O(n), where n is the number of characters in s1. The extra space is for the dictionary storage.



