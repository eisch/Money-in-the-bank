import psycopg2

DB_NAME = "bank_accounts"
conn = psycopg2.connect(f"dbname={DB_NAME}")
cursor = conn.cursor()

types = ["SERIAL", "VARCHAR", "REAL", "TEXT"]

create_table_clients = f"""
    create table if not exists
    clients(id {types[0]} PRIMARY KEY,
    username {types[1]}(128),
    password {types[1]}(128),
    balance {types[2]} DEFAULT 0,
    message {types[3]})

"""

#counter and update_time za brute_force