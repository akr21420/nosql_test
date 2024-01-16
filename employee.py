from main import get_db


class Employee:
    def __init__(self):
        dbname = get_db()
        emp_schema = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["emp_id"],
                "properties": {
                    "emp_id": {
                        "bsonType": "string",
                        "description": "required string"
                    },
                    "emp_name": {
                        "bsonType": "string",
                        "description": "required string"
                    },
                    "group": {
                        "bsonType": "string",
                        "description": "required"
                    },
                    "email": {
                        "bsonType": "string",
                        "description": "required"
                    },
                    "password": {
                        "bsonType": "string",
                        "description": "required"
                    }
                }
            }
        }
        dbname.command("collMod", "employees", validator = emp_schema)
        employees = dbname.employees
        print(employees.options())
        employees.create_index([("emp_id",1)], unique = True)
        self.db = employees

    def insert(self,obj):
        self.db.insert_one(obj)

    def get_employee_id(self):
        return self.db.find({"emp_id":"104427"})