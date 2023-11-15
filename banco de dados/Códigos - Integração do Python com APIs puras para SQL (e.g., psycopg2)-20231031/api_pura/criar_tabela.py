import psycopg2
from datetime import date
from e1_conexao_bd import get_conexao_postgres

def criar_tabela_contatos():
    try:
        conexao = get_conexao_postgres('vaskito', 'postgres', '123456')

        cursor = conexao.cursor()
        cursor.execute("""
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
            (345678, 'Pedro Santos', date(1997, 3, 20), '99999-9999', 'Rua C', '789', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (456789, 'Ana Souza', date(1996, 7, 25), '99999-9999', 'Rua D', '321', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (567890, 'Lucas Pereira', date(1999, 10, 30), '99999-9999', 'Rua E', '654', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (678901, 'Julia Costa', date(1994, 1, 5), '99999-9999', 'Rua F', '987', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (789012, 'Fernando Alves', date(1993, 4, 10), '99999-9999', 'Rua G', '246', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (890123, 'Mariana Rodrigues', date(1992, 9, 15), '99999-9999', 'Rua H', '369', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (901234, 'Rafaela Nunes', date(1991, 12, 20), '99999-9999', 'Rua I', '582', '***', 'cianorte', 'Parana', 'Brasil', 87305050),
            (123345, 'Gabriel Silva', date(1990, 6, 25), '99999-9999', 'Rua J', '753', '***', 'cianorte', 'Parana', 'Brasil', 87305050)
            ]

        cursor.executemany("""
            INSERT INTO contatos (id, nome, data_nasc, telefone, rua, numero_residencia, complemento, cidade, estado, pais, cep)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, contatos)

        conexao.commit()

        cursor.close()
        conexao.close()

        print("Tabela Aluno criada e populada com sucesso!")
    except (Exception, psycopg2.DatabaseError) as erro:
        print(f"Erro ao criar a tabela Aluno: {erro}")

def main():
    criar_tabela_contatos()

if __name__ == "__main__":

    main()