import psycopg2
from e1_conexao_bd import get_conexao_postgres

def visualiza_tabela():
    try:
        conexao = get_conexao_postgres('exe5', 'postgres', '123')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM contatos;
        """)

        contatos = cursor.fetchall()

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

if __name__ == "__main__":
    print('• Todos os contatos na tabela.')
    visualiza_tabela()
    print()
    print('• Contatos de uma cidade específica.')
    visualiza_cidade()
    print()
    print('• Contatos que nasceram antes de uma determinada data.')
    visualiza_data()