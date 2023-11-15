import psycopg2
from datetime import date
from e1_conexao_bd import get_conexao_postgres


def cria_tabela_aluno():
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Criação da tabela Aluno
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE Aluno (
                RA INTEGER PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                endereco VARCHAR(200) NOT NULL,
                data_nasc DATE NOT NULL
            );
        """)

        ra = 100001
        nome = 'Ana da Silva'
        endereco = 'Rua Bahia, 123'
        data_nasc = date(1999, 1, 1)

        cursor.execute("""
            INSERT INTO Aluno (RA, nome, endereco, data_nasc)
            VALUES (%s, %s, %s, %s);
        """, (ra, nome, endereco, data_nasc))

        # Inserção de 10 registros na tabela Aluno
        alunos = [
            (123456, 'João da Silva', 'Rua A, 123', date(1995, 5, 10)),
            (234567, 'Maria Oliveira', 'Rua B, 456', date(1998, 8, 15)),
            (345678, 'Pedro Santos', 'Rua C, 789', date(1997, 3, 20)),
            (456789, 'Ana Souza', 'Rua D, 321', date(1996, 7, 25)),
            (567890, 'Lucas Pereira', 'Rua E, 654', date(1999, 10, 30)),
            (678901, 'Julia Costa', 'Rua F, 987', date(1994, 1, 5)),
            (789012, 'Fernando Alves', 'Rua G, 246', date(1993, 4, 10)),
            (890123, 'Mariana Rodrigues', 'Rua H, 369', date(1992, 9, 15)),
            (901234, 'Rafaela Nunes', 'Rua I, 582', date(1991, 12, 20)),
            (123345, 'Gabriel Silva', 'Rua J, 753', date(1990, 6, 25))
        ]
        cursor.executemany("""
            INSERT INTO Aluno (RA, nome, endereco, data_nasc)
            VALUES (%s, %s, %s, %s);
        """, alunos)

        # Confirmação da transação
        conexao.commit()

        # Fechamento da conexão
        cursor.close()
        conexao.close()

        print("Tabela Aluno criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela Aluno: {erro}")


def createAluno(RA, nome, endereco, data_nasc):
    print(f"(createAluno) Criando o aluno {nome}...")
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Inserção do aluno na tabela Aluno
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO Aluno (RA, nome, endereco, data_nasc)
            VALUES (%s, %s, %s, %s);
        """, (RA, nome, endereco, data_nasc))

        # Confirmação da transação
        conexao.commit()

        # Fechamento da conexão
        cursor.close()
        conexao.close()

        print(f'Aluno com nome {nome}, e RA {RA} criado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar o aluno: {erro}")


def deleteAluno(RA):
    print(f"(deleteAluno) Removendo o aluno {RA}...")
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Remoção do aluno da tabela Aluno
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM Aluno WHERE RA = %s;
        """, (RA,))

        # Confirmação da transação
        conexao.commit()

        # Fechamento da conexão
        cursor.close()
        conexao.close()

        print(f'Aluno com RA {RA} removido com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao remover o aluno: {erro}")


def updateAluno(RA, nome, endereco, data_nasc):
    print(f"(updateAluno) Atualizando o aluno {nome}...")
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Atualização dos dados do aluno na tabela Aluno
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE Aluno SET nome = %s, endereco = %s, data_nasc = %s WHERE RA = %s;
        """, (nome, endereco, data_nasc, RA))

        # Confirmação da transação
        conexao.commit()

        # Fechamento da conexão
        cursor.close()
        conexao.close()

        print(f'Aluno com RA {RA}  atualizado com sucesso!')
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao atualizar o aluno: {erro}")


def readAluno(nome):
    print(f"(readAluno) Buscando o aluno {nome}...")
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Busca dos alunos com o nome informado
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM Aluno WHERE nome = %s;
        """, (nome,))

        # Leitura dos resultados
        alunos = cursor.fetchall()

        for aluno in alunos:
            print(aluno)

        # Fechamento da conexão
        cursor.close()
        conexao.close()

        return alunos
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os alunos: {erro}")


def readAllAlunos():
    print("(readAllAlunos) Buscando todos os alunos...")
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Busca de todos os alunos
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM Aluno;
        """)

        # Leitura dos resultados
        alunos = cursor.fetchall()

        for aluno in alunos:
            print(aluno)

        # Fechamento da conexão
        cursor.close()
        conexao.close()

        return alunos
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar os alunos: {erro}")

def main():
    # cria_tabela_aluno()

    readAllAlunos()
    print()
    readAluno('João da Silva')
    print()
    createAluno(100002, 'Pernalonga', 'Rua das cenouras, 23', date(1895, 2, 12))
    readAluno('Pernalonga')
    print()
    updateAluno(100002, 'Pernalonga', 'Rua das couves, 55', date(1895, 2, 12))
    readAluno('Pernalonga')
    print()
    readAllAlunos()
    deleteAluno(100002)
    readAllAlunos()


    

if __name__ == "__main__":
    main()