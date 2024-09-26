from Banco import Banco
from BilleteraVirtual import BilleteraVirtual
from Impuesto import Impuesto
import random

CuentaBanco = Banco(200000,'Samuel Eto',123)
CuentaVirtual = BilleteraVirtual(180000,'wolfav',321)

tipo_impuesto = ['ISR','IVA','IBI','Impuesto a la Ganancia','ITP','IDCB']
montos = [40000, 60000]
impuestos = []

for i in range(1,20):
    nuevoImpuesto = Impuesto(random.choice(tipo_impuesto),random.choice(montos),random.randint(1,4)) # de enero a abril
    impuestos.append(nuevoImpuesto)
random.shuffle(impuestos)

for i in range(1,20):
    nuevoImpuesto = random.choice(impuestos) # selecciona un impuesto aleatorio de la lista
    nuevoImpuesto.imprimir()
    nuevoImpuesto.validarPago(random.choice(montos),random.randint(1,4),random.randint(100,999))
    if nuevoImpuesto.getEstado(): # si se Valida el Pago, se descuenta por crédito o débito
        pago = random.randint(1,2) # elige la forma de pago de manera aleatoria
        if pago == 1:
            CuentaBanco.debito(nuevoImpuesto.getMonto())
        else:
            CuentaBanco.credito(nuevoImpuesto.getMonto(),random.choice([1,2,3,6,9,12])) # cantidad de cuotas aleatoria