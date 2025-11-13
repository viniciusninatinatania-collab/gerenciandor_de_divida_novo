from ..model.DividaModel import DividaModel
from ..view.DividaView  import DividaView

class DividaController:
    def __init__(self):
        self.view = DividaView()

    def adicionar_divida(self, nome, valor, descricao, data_vencimento):
       try:

        resultado = DividaModel.adicionar_divida( nome, valor, descricao, data_vencimento)

        if resultado is True:
           self.view.mostrar_sucesso(f"Dívida '{nome}' adicionada com sucesso.")
        
       except Exception as e:
        self.view.mostrar_erro(f"Erro inesperado ao adicionar dívida: {e}")

    def lista_todas_dividas(self):
        dividas = DividaModel.get_dividas()
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return 
        else:
            self.view.listar_dividas(dividas)

    def listar_dividas_pendentes(self):
        dividas = DividaModel.get_dividas()
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return 
        else:
            dividas_pendentes = [d for d in dividas if d.situacao == 'pendente']
            self.view.listar_dividas(dividas_pendentes)

    def listar_dividas_pagas(self):
        dividas = DividaModel.get_dividas();
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return
        else:
            dividas_pagas = [d for d in dividas if d.situacao == 'paga']
            self.view.listar_dividas(dividas_pagas)
    
    def mostrar_detalhes_divida(self, divida_id):
        divida_id = int(divida_id)
        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f"Dívida com ID {divida_id} não encontrada.")
            return
        else:
            self.view.mostrar_detalhes_divida(divida)

    def atualizar_situacao_divida(self, divida_id):
        divida_id = int(divida_id)

        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f"Dívida com ID {divida_id} não encontrada.")
            return
        if divida.situacao == 'paga':
            self.view.mostrar_erro(f"A dívida com ID {divida_id} já está marcada como paga.")
            return
        sucesso = DividaModel.atualizar_situacao_divida(divida_id)
        if sucesso:
            self.view.mostrar_sucesso(f"Dívida com ID {divida_id} marcada como paga com sucesso.")
        else:
            self.view.mostrar_erro(f"Erro ao marcar a dívida com ID {divida_id} como paga.")\
            
    def excluir_divida(self, divida_id):
        divida_id = int(divida_id)

        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f"Dívida com ID {divida_id} não encontrada.")
            return
        sucesso = DividaModel.excluir_divida(divida_id)
        if sucesso:
            self.view.mostrar_sucesso(f"Dívida com ID {divida_id} excluída com sucesso.")
        else:
            self.view.mostrar_erro(f"Erro ao excluir a dívida com ID {divida_id}.")
    def editar_divida():
        @staticmethod
        def atualizar_divida(id, nome=None, valor=None, descricao=None, data_vencimento=None, situacao=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Busca a dívida existente
        cursor.execute("SELECT * FROM dividas WHERE id = ?", (id,))
        divida = cursor.fetchone()
        if not divida:
            return f"Dívida com ID {id} não encontrada."

        # Preenche com os valores atuais caso não tenha sido passado
        nome = nome if nome is not None else divida["nome"]
        valor = float(valor) if valor is not None else divida["valor"]
        descricao = descricao if descricao is not None else divida["descricao"]
        data_vencimento = data_vencimento if data_vencimento is not None else divida["data_vencimento"]
        situacao = situacao if situacao is not None else divida["situacao"]

        # Validações básicas
        if not nome:
            raise ValueError("O nome é obrigatório.")
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        # Atualiza no banco
        cursor.execute("""
            UPDATE dividas
            SET nome = ?, valor = ?, descricao = ?, data_vencimento = ?, situacao = ?
            WHERE id = ?
        """, (nome, valor, descricao, data_vencimento, situacao, id))

        conn.commit()
        return True

    except Exception as e:
        return f"Erro ao atualizar dívida: {e}"

    finally:
        try:
            conn.close()
        except:
            pass
