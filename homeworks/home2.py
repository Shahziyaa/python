para ="""   Python is a
 powerful programming language. 
This Python course helps beginners 
learn how to code easily.   """
print(para)

len=len(para)
print("Length of the paragraph is:",len)
print("first character is:",para[0])
print("last character is:",para[-1])

pre= para[0:50]
print("First 50 characters are:",pre)

paraa= para.replace("Python","PYTHON")
print(paraa)

para = para.lower()
print (para)

CLEAN = para.strip()
print(CLEAN)

word = para.split()
print(word)

if "course" in para:
    print("Yes, 'course' is present in the paragraph.")

print("\nThe course description is {} chars long and has {} words.".format(len(para), len(word)))
