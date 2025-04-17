#=========================================================================

#Exercício 2

lista_gpu = [[12,34,54,95,37],
             [49,53,23,19,39],
             [45,96,85,432,35]]

def percntRegiao(lista, regiao):
  em_alerta = False 
  for i in range(len(lista)): 
    for j in range(len(lista[i])):
      valor = lista[i][j] 
      if valor >= 85:
         alerta = True  
         print(f" {i + 1} {valor} {alerta}")
      else:
         alerta = False
         print(f"{i + 1} {valor} {alerta}")

percntRegiao(lista_gpu, 1)

#=========================================================================