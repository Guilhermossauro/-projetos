#contar vogais de um texto

#input do texto
texto= input("\n digite o seu texto")
print ("Conta Vogais\n")
#converte para minúsculas
texto = texto.lower()
#removem espaços, linhas e símbolos de pontuação
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")
#removem acentos e cedilha
texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")
#finalizando mostrando o resultado final
print (texto)
vogais = 0
# separando a contagem das vogais
for caracter in texto:
    if caracter in 'aeiou':
        vogais= vogais + 1 
          
print ('\n total de vogais :', vogais)
input("\nPressione qualquer tecla para finalizar")

