# This code is same as the Question-2. But Iam using Bubble Sort here.
class practice_ques:
    sum=0
    def __init__(self,sentence):
        self.sentence=list(sentence)
        
    def bubble_sort(self):
        n=len(self.sentence)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.sentence[j]>self.sentence[j+1]:
                    self.sentence[j],self.sentence[j+1]=self.sentence[j+1],self.sentence[j]
                    sum=sum+1
    def display(self):
        print(self.sentence)
        print(sum)
sen=input("Enter the Sentence to be sorted: ")
p=practice_ques(sen)
p.bubble_sort()
p.display()

