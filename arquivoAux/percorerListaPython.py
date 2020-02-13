#Testando os metodos read(), readline(), readlines()
"""
manipulador = open("professoresES.txt", "r" )
print("\n Metodo read():\n")
print(manipulador.read())
#manipulador.seek(0); #Volte para o inicio do arquivo 
"""
"""
manipulador = open("professoresES.txt", "r" )
print("\n Metodo readlines():\n")
professor = {manipulador+","}
for c in professor:
    print(professor)
    """
#manipulador.close();
#print(manipulador.readline())
#manipulador.seek(0);
"""
print("\n Metodo readlines():\n")
print(manipulador.readlines())
manipulador.close();
"""

"""
#01
print("Teste de abertura de arquivos em Python")
print("Tentando abrir um arquivo de texto armazendo no PC:\n")
manipulador1 = open("professoresES.txt","r")
manipulador2 = open("cursoSoftware.txt","r")
for linha in manipulador1:
   # linha = linha.rstrip() #metodo que retira a quebra de linah
    for linha2 in manipulador2:
      linha2 = linha2.rstrip() 
      print(linha.readline()+"_"+ linha2)
    
manipulador1.close()
manipulador2.close()



print("Contador de linahs do arquvivo:\n")
contador = 0
arq = open("professoresES.txt","r")
for linha in arq:
    contador=contador+1
print("Numero de linhas no arquivo: ", contador)

arq.close()


print("Retornando apenas linhas que tenham uma palavra especifica:\n")
contador = 0
arq = open("professoresES.txt","r")
for linha in arq:
    linha = linha.rstrip()
    if "Python" in linha:
         contador=contador+1
        print(linha)
print("Foram retornadas:", contador, "linhas")

arq.close()
"""