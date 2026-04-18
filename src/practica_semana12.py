import pandas as pd 
import numpy as np 
import os 

#--------DATOS FICTICIOS---------#
# Catalogo de vendedores (Tabla principal - nunca debe perder registros)
df_vendedores = pd.DataFrame({
'id_vendedor': [1,2,3,4],
'nombre':  ['Ana Lopez', 'Luis Gomez','Marta Rios', 'Carlos Paz'],
'region': ['Norte', 'Sur', 'Norte', 'Sur']
})

# HIstorial de transacciones (Carlos no vendio nada este mes)
df_transacciones = pd.DataFrame ({
    'id_transaccion': [101, 102, 103, 104, 105],
    'id_vendedor': [1, 1, 2, 3, 1],
    'monto': [500.0, 750.0, 200.0, 1200.0, 300.0],
    'fecha': ['2025-01-05', '2025-01-12', '2025-01-08', '2025-01-15', '2025-01-20']
})

print('Vendedores:')
print(df_vendedores)
print()
print('Transacciones:')
print(df_transacciones)

#-------------AUDITORIA DE LLAVES-----------------#
print('\n=== AUDITORIA DE LLAVES ===')

# verificar quer id _vendedor es unico en el catalogo (debe ser PK)
duplicados_pk = df_vendedores['id_vendedor'].duplicated().sum()
if duplicados_pk == 0:
    print('OK - la llave primaria de vendedores esta limpia')
else:
    print(f'PELIGRO - Hay {duplicados_pk} duplicados en id_vendedor')


# Verificar que los id_vendedor en transacciones existen en el catalogo

ids_huerfanos = ~df_transacciones['id_vendedor'].isin(df_vendedores['id_vendedor'])
if ids_huerfanos.sum() == 0:
    print('OK - todos los id_vendedor en transaccines existen en el catalogo')
else:
    print(f'PROBLEMA - Hay {ids_huerfanos.sum()} transacciones con vendedor desconocido')    

    
