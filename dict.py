def Tortoise(s,word):
    s = ((input('Ввеите строку ')).lower().split())
    word  = input('Введите слово ')
    return dict(key=s.count(word), word=word)

s=[]
word=''
print(Tortoise(s,word) )
