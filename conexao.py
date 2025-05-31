import psycopg2


def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="testes",
            user="postgres",           
            password="q1w2e3", 
            host="localhost",
            port="5432"
        )
        print("[OK] Conexão estabelecida com sucesso!, Ação bem sucedida!")
        return conexao
    except Exception as e:
        print(f"[ERRO] Falha na conexão: {e}")
        return None