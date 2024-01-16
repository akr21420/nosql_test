from main import get_db
class Holiday:
    def __init__(self):
        dbname = get_db()
        holiday_schema = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["date"],
                "properties": {
                    "date": {
                        "bsonType": "date",
                        "description": "Date of the shift"
                    },
                    "emp_id": {
                        "bsonType": "array",
                        "description": "employee_ids from employee collection",
                        "items": {
                            "bsonType": "string",
                            "description": "Employee ID of the employee"
                        }
                    },
                    "shift": {
                        "bsonType": "string",
                        "description": "pd1/pd2/pd3/s1/s2"
                    }
                }
            }
        }
        dbname.command("collMod", "holidays", validator = holiday_schema)
        holidays = dbname.holidays
        holidays.create_index([("date",1), ("shift", 1)], unique = True)
        self.db = holidays

    def create(self, dates, emps, shift):
        obj = {
            "date": dates,
            "emp_id": emps,
            "shift": shift
        }
        self.db.insert_one(obj)
    def get(self, date):
        return self.db.find_one({"date": date})

    def swap_giveaway(self, emp_id, date, shift, type):
        if type == "Giveaway":
            self.db.update_one({"date": date, "shift": shift}, {"$addToSet": {"giveaway": str(emp_id)}})
        else:
            self.db.update_one({"date": date, "shift": shift}, {"$addToSet": {"swap": str(emp_id)}})