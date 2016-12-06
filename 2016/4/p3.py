s='abcdefzyasdfasdfafddfsmnkasdfas'

for a in s:
    print chr((((ord(a)-97)+1)%26)+97)
