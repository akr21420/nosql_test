from pymongo import MongoClient

def get_db():
    CONN = "mongodb+srv://admin:admin@sredb.rkqregw.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONN)
    return client['SRE_LIST']

if __name__ == "__main__":
    dbname = get_db()