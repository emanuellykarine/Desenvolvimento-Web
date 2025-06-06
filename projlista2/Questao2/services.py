# regras de negócio, cálculos e lógicas
class Cidade:
    def __init__(self, nome, previsao):
        self.nome = nome
        self.previsao = previsao

    @staticmethod
    def cidade_encontrar(nome):
        cidades =[
            Cidade("Natal", "Chuva demais"),
            Cidade("Rio de Janeiro", "Sol quente"),
            Cidade("Salvador", "Neblina"),
            Cidade("Brasília", "Sol"),
            Cidade("Parnamirim", "Nublado"),
            Cidade("Mossoró", "Seco"),
            Cidade("Touros", "Ventando"),
            Cidade("Veneza", "Chuvoso"),
            Cidade("Paris", "Frio"),
            Cidade("Roma", "Ensolarado")
            ]
        
        for cidade in cidades:
            if cidade.nome == nome:
                return cidade.previsao
            
        return None
    
    @staticmethod
    def lista():
        return [
            Cidade("Natal", "Chuva demais"),
            Cidade("Rio de Janeiro", "Sol quente"),
            Cidade("Salvador", "Neblina"),
            Cidade("Brasília", "Sol"),
            Cidade("Parnamirim", "Nublado"),
            Cidade("Mossoró", "Seco"),
            Cidade("Touros", "Ventando"),
            Cidade("Veneza", "Chuvoso"),
            Cidade("Paris", "Frio"),
            Cidade("Roma", "Ensolarado")
            ]