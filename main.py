def find_anagram(data1, data2):
    if (len(data1) != len(data2)):
        return False
    else:
        if(sorted(data1) == sorted(data2)):
            return True
        else:
            return False
print(find_anagram("below", "elbow"))



 





