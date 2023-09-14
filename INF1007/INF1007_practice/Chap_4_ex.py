# on parle de list et chain de charctere
#on va commence les problemes 

count = 0
chain = ''

for character in chain:
    if character >= 'a' and character <= 'z':
        count += 1 

if count == len(chain) and len(chain)>0:
    print(True)
else:
    print(False)
    
#option 2

result = True
for charac in chain:
    if 'A' <= charac <= 'Z':
        result = False
        break
        