"""# on parle de list et chain de charctere
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
    
chaine = 'Hello'
start_check = 'He'
for i in range(len(start_check)):
    print()
    #   
    
print(chaine[:len(start_check)] == start_check)

lettres = 'aslkdjfsd'
for i in range(len(lettres)-1):
    if lettres[i] == lettres[i+1]:
        print(f"{lettres[i]} est egal a {lettres[i+1]}")
    else:
        print(f"{lettres[i]} different egal de {lettres[i+1]}")
        
"""

chain = "Andrew"

var = True
i=0 
while i < len(chain) and var :
    if 'a' == chain[i]:
        var = False
    i += 1 
