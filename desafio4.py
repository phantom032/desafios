print('-------Desafio 04-------')

n = input('digite algo: ')
print ('o tipo primitivo do que digitou é :',type(n))
print('é numero?',n.isnumeric() )
print('é alfabético? ',n.isalpha())
print ('só tem espaços?',n.isspace())
print ('está em maiusculas?',n.isupper())
print ('está em minusculas?',n.islower())
print ('está capitalizada',n.istitle())