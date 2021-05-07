## Sistema de bancos



Repositório cooperativo para criação de sistema bancário


```python
#classe conta

class Conta:
    def __init__(self, numero, clientes, saldo):
        self.numero = numero
        self.clientes = clientes
        self.saldo = saldo
        self.abertura = datetime.datetime.today()
        self.extrato = Extrato()
```


**ATENÇÃO NAS PR'S**



*dúvidas criar um comentário na pr*
