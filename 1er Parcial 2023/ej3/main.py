from Banco import Banco
from BilleteraVirtual import BilleteraVirtual
from Impuesto import Impuesto
import random

CuentaBanco = Banco(200000,'Samuel Eto',123)
CuentaVirtual = BilleteraVirtual(180000,'wolfav',321)

tipo_impuesto = ['ISR','IVA','IBI','Impuesto a la Ganancia','ITP','IDCB']
montos = [35000, 50000, 65000]
impuestos = []

for i in range(1,20):
    nuevoImpuesto = Impuesto(random.choice(tipo_impuesto),random.choice(montos),random.randint(1,12))
    impuestos.append(nuevoImpuesto)
random.shuffle(impuestos)

for i in range(1,20):
    pago = random.randint(1,2)
    if pago == 1:
        CuentaBanco.debito(random.choice(impuestos).getMonto())
    else:
        CuentaBanco.credito(random.choice(impuestos).getMonto(),random.choice([1,2,3,6,9,12]))