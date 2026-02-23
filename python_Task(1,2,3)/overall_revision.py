#Week-1 Question-5
def counting():
    sentence=input("Enter the String: ")
    vow_count=0
    cons_count=0
    n=len(sentence)
    vows=["a","e","i","o","u","A","E","I","O","U"]
    for i in range(n):
        if sentence[i].isalpha():
            if sentence[i] in vows:
                vow_count=vow_count+1
            else:
                cons_count=cons_count+1
    print("Vowel Count is:",vow_count)
    print("Consonants Count is:",cons_count)

counting()

