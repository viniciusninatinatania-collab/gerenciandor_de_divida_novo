from datetime import datetime

FORMATO_DATA = "%d/%m/%Y"

class DividaView:

    def listar_dividas(self, dividas):
        input()
        # Cabeçalho
        print("\n--- Lista de Dívidas ---")
        print("ID | NOME (Dívida)       | VALOR    | VENCIMENTO | STATUS")
        print("---|--------------------|----------|------------|---------")
        
        for divida in dividas:
            # Formatando o valor para duas casas decimais
            print(
                f"[{divida.id}] {divida.nome:20.20s} | R$ {divida.valor:8.2f} | "
                f"Venc: {divida.data_vencimento or 'N/A'} | {divida.situacao}"
            )

    def mostrar_detalhes_divida(self, divida):
        input()
        print(
            f"Detalhes da Dívida ID: {divida.id}, Nome: {divida.nome}, "
            f"Valor: {divida.valor}, Data de Vencimento: {self.ler_data(divida.data_vencimento)}, "
            f"Descrição: {divida.descricao}, Criado em: {self.ler_data(divida.criado_em)}"
        )

    def mostrar_erro(self, mensagem):
        input()
        print(f"[ERRO] {mensagem}")

    def mostrar_sucesso(self, mensagem):
        input()
        print(mensagem)

    def ler_data(self, texto):
        if not texto:
            return ""
        try:
            data = datetime.strptime(texto, "%Y-%m-%d").date()
            return data.strftime("%d/%m/%Y")
        except:
            return ""
