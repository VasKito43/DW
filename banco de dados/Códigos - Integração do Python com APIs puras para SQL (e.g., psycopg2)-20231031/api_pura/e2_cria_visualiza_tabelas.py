import psycopg2
from datetime import date
from e1_conexao_bd import get_conexao_postgres


def criar_tabela_aluno():
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


def visualizar_tabela_aluno():
    try:
        # Conexão com o banco de dados
        conexao = get_conexao_postgres("sql_python", "postgres", "admin")

        # Criação da tabela Aluno
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM Aluno;
        """)

        # Recuperação dos registros da tabela Aluno
        alunos = cursor.fetchall()

        # Exibição dos registros da tabela Aluno
        for aluno in alunos:
            print(aluno)

        # Fechamento da conexão
        cursor.close()
        conexao.close()
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao buscar a tabela Aluno: {erro}")

def main():
    criar_tabela_aluno()
    visualizar_tabela_aluno()


if __name__ == "__main__":
    main()


