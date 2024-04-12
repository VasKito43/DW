import psycopg2
from datetime import date
from e1_conexao_bd import get_conexao_postgres

class Contato:
    def __init__(self, id, nome, data_nasc, telefone, rua, numero_residencia, complemento, cidade, estado, pais, cep):
        self.id = id
        self.nome = nome
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.rua = rua
        self.numero_residencia = numero_residencia
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.cep = cep

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Data de Nascimento: {self.data_nasc}, Telefone: {self.telefone}, Rua: {self.rua}, Número: {self.numero_residencia}, Complemento: {self.complemento}, Cidade: {self.cidade}, Estado: {self.estado}, País: {self.pais}, CEP: {self.cep}"


def criar_tabela_contatos():
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')

        cursor = conexao.cursor()
        cursor.execute("""
        drop table if EXISTS contatos;

        CREATE TABLE contatos (
        id int PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        data_nasc DATE NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        rua VARCHAR(100) NOT NULL,
        numero_residencia VARCHAR(20) NOT NULL,
        complemento VARCHAR(20),
        cidade VARCHAR(50) NOT NULL,
        estado VARCHAR(50) NOT NULL,
        pais VARCHAR(50) NOT NULL,
        cep int NOT NULL
        );
        """)

        contatos = [
            (123456, 'João da Silva', date(1995, 5, 10), '99999-9999', 'Rua A', '123', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (234567, 'Maria Oliveira', date(1998, 8, 15), '99999-9999', 'Rua B', '456', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (345678, 'Pedro Santos', date(1997, 3, 20), '99999-9999', 'Rua C', '789', '***', 'campo mourao', 'Parana', 'Brasil', 87305050),
            (456789, 'Ana Souza', date(1996, 7, 25), '99999-9999', 'Rua D', '321', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (567890, 'Lucas Pereira', date(1999, 10, 30), '99999-9999', 'Rua E', '654', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (678901, 'Julia Costa', date(1994, 1, 5), '99999-9999', 'Rua F', '987', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (789012, 'Fernando Alves', date(1993, 4, 10), '99999-9999', 'Rua G', '246', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (890123, 'Mariana Rodrigues', date(1992, 9, 15), '99999-9999', 'Rua H', '369', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (901234, 'Rafaela Nunes', date(1991, 12, 20), '99999-9999', 'Rua I', '582', '***', 'campo mourao', 'Parana', 'Brasil', 87305050),
            (123345, 'Gabriel Silva', date(1990, 6, 25), '99999-9999', 'Rua J', '753', '***', 'cianorte', 'Parana', 'Brasil', 87305050)
            ]

        cursor.executemany("""
            INSERT INTO contatos (id, nome, data_nasc, telefone, rua, numero_residencia, complemento, cidade, estado, pais, cep)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, contatos)

        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela Contatos criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela Contatos: {erro}")


def visualiza_tabela():
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM contatos;
        """)

        contatos = cursor.fetchall()
        contato_objs = [Contato(*contato) for contato in contatos]

        for contato_obj in contato_objs:
            print(contato_obj)

        print()

        print(contatos)

        cursor.close()
        conexao.close()
    
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar a tabela Contatos: {erro}")

def visualiza_cidade():
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * 
            FROM contatos
            WHERE cidade = 'campo mourao';
        """)

        contatos = cursor.fetchall()

        print(contatos)

        cursor.close()
        conexao.close()
    
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar a tabela Contatos: {erro}")

def visualiza_data():
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * 
            FROM contatos
            WHERE data_nasc < '1995-01-01';
        """)

        contatos = cursor.fetchall()

        print(contatos)

        cursor.close()
        conexao.close()
    
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar a tabela Contatos: {erro}")

def atualiza_registro(id):
    x = 1
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM contatos;
        """)
        
        contatos = cursor.fetchall()

        contato_objs = [Contato(*contato) for contato in contatos]

        for contato in contato_objs:
            if id == contato.id:
                contato.nome = input(f'qual o novo nome ({contato.nome}): ')
                contato.telefone = input(f'qual o novo telefone ({contato.telefone}): ')
                contato.rua = input(f'qual a nova rua ({contato.rua}): ')
                contato.numero_residencia = input(f'qual o novo numero de residencia ({contato.numero_residencia}): ')
                contato.complemento = input(f'qual o novo complemento ({contato.complemento}):')
                contato.cidade = input(f'qual a nova cidade ({contato.cidade}):')
                contato.estado = input(f'qual o novo estado ({contato.estado}):')
                contato.pais = input(f'qual o novo pais ({contato.pais}):')
                contato.cep = int(input(f'qual o novo cep ({contato.cep}):'))

                print(contato)

            elif x == len(contato_objs):
                print('id não encontrado')

            else:
                x += 1


        cursor.close()
        conexao.close()

    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar a tabela Contatos: {erro}")

def exclua_contato(dado):
    x = 1
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM contatos;
        """)
        
        contatos = cursor.fetchall()

        contato_objs = [Contato(*contato) for contato in contatos]

        for contato in contato_objs:
            if dado == contato.nome or dado == contato.telefone :
                cursor.execute("DELETE FROM contatos WHERE id = %s;", (contato.id,))
                conexao.commit()

                print('contato excluido com sucesso')

            elif x == len(contato_objs):
                print('contato não encontrado')

            else:
                x += 1


        cursor.close()
        conexao.close()

    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar a tabela Contatos: {erro}")


def main():
    criar_tabela_contatos()
    print()
    print('• Todos os contatos na tabela.')
    visualiza_tabela()
    print()
    print('• Contatos de uma cidade específica.')
    visualiza_cidade()
    print()
    print('• Contatos que nasceram antes de uma determinada data.')
    visualiza_data()
    print()
    atualiza_registro(int(input('qual o id que deseja modificar: ')))
    print()
    exclua_contato(input('digite o nome ou o telefone do contato que deseja excluir: '))


if __name__ == "__main__":

    main()