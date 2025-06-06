class Capital:
    def __init__(self, nome):
        self.nome = nome

    @staticmethod
    def lista():
        return [
            Capital("Salvador"),
            Capital("São Luis"),
            Capital("Fortaleza"),
            Capital("Teresina"),
            Capital("Natal"),
            Capital("João Pessoa"),
            Capital("Recife"),
            Capital("Maceió"),
            Capital("Aracaju")
        ]
    
class Frete:
    @staticmethod
    def calculo(origem, destino):
        distancias = {
            ('Aracaju', 'Aracaju'): 0, #tupla como chave
            ('Aracaju', 'Fortaleza'): 1183,
            ('Aracaju', 'João Pessoa'): 611,
            ('Aracaju', 'Natal'): 788,
            ('Aracaju', 'Recife'): 501,
            ('Aracaju', 'Salvador'): 356,
            ('Aracaju', 'São Luis'): 1578,
            ('Aracaju', 'Maceió'): 294,
            ('Aracaju', 'Teresina'): 1142,
            ('Fortaleza', 'Fortaleza'): 0,
            ('Fortaleza', 'João Pessoa'): 688,
            ('Fortaleza', 'Maceió'): 1075,
            ('Fortaleza', 'Natal'): 537,
            ('Fortaleza', 'Recife'): 800,
            ('Fortaleza', 'Salvador'): 1389,
            ('Fortaleza', 'São Luis'): 1070,
            ('Fortaleza', 'Teresina'): 634,
            ('João Pessoa', 'João Pessoa'): 0,
            ('João Pessoa', 'Maceió'): 395,
            ('João Pessoa', 'Natal'): 185,
            ('João Pessoa', 'Recife'): 120,
            ('João Pessoa', 'Salvador'): 949,
            ('João Pessoa', 'São Luis'): 1660,
            ('João Pessoa', 'Teresina'): 1224,
            ('Maceió', 'Maceió'): 0,
            ('Maceió', 'Natal'): 572,
            ('Maceió', 'Recife'): 285,
            ('Maceió', 'Salvador'): 632,
            ('Maceió', 'São Luis'): 1672,
            ('Maceió', 'Teresina'): 1236,
            ('Natal', 'Natal'): 0,
            ('Natal', 'Recife'): 297,
            ('Natal', 'Salvador'): 1126,
            ('Natal', 'São Luis'): 1607,
            ('Natal', 'Teresina'): 1171,
            ('Recife', 'Recife'): 0,
            ('Recife', 'Salvador'): 839,
            ('Recife', 'São Luis'): 1573,
            ('Recife', 'Teresina'): 1137,
            ('Salvador', 'Salvador'): 0,
            ('Salvador', 'São Luis'): 1599,
            ('Salvador', 'Teresina'): 1163,
            ('São Luis', 'São Luis'): 0,
            ('São Luis', 'Teresina'): 446,
            ('Teresina', 'Teresina'): 0
        }
        
        if (origem, destino) in distancias:
            return distancias[origem, destino] * 0.8
        
        elif (destino, origem) in distancias:
            return distancias[destino, origem] * 0.8
