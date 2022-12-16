print('-'*30)
print('Descubra um anagrama')
print('-'*30)

s = input("Digite uma palavra: ").strip()

t = input("Digite o anagrama: ").strip()
s_lower = s.lower()
t_lower = t.lower() 

if sorted(s_lower) == sorted(t_lower):

    print(True)
else:
    print(False)


