
tabela_inss = (
    (0.00, 1317.07, 0.08),
    (1317.08, 2195.12, 0.09),
    (2195.13, 4390.24, 0.11),
    (4390.25, float("inf"), 0.11)  
)

print("Tabela de INSS representada como tupla de tuplas:")
for linha in tabela_inss:
    print(linha)
