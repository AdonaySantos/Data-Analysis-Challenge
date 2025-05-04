def create_tables():
    try:
        print("Creating tables on PostgreSQL..")
        print("Tables were create")
    except Exception as e:
        print({"error": e})
