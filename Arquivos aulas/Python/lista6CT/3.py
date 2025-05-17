positivos = (12, 65, 14, 462, 12)

quant = len(positivos)
maior = 0

def procurar():
    for i in range(quant):    
        
        if positivos[i] > maior:
            maior = positivos[i]
        i += 1

print (procurar())
