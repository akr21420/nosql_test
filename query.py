from main import get_db
from employee import Employee
from holiday import Holiday
import datetime as datetime

dbname = get_db()
 
try:
    dbname.create_collection("employees")
    dbname.create_collection("holidays")
except Exception as e:
    print(e)
    
# emp_schema = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": ["emp_id"],
#         "properties": {
#             "emp_id": {
#                 "bsonType": "string",
#                 "description": "required string"
#             },
#             "emp_name": {
#                 "bsonType": "string",
#                 "description": "required string"
#             },
#             "group": {
#                 "bsonType": "string",
#                 "description": "required"
#             },
#             "email": {
#                 "bsonType": "string",
#                 "description": "required"
#             },
#             "password": {
#                 "bsonType": "string",
#                 "description": "required"
#             }
#         }
#     }
# }

# weekend_schema = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": [],
#         "properties": {
#             "quarter": {
#                 "bsonType": "string",
#                 "description": "quarter which this belongs to"
#             },

#         }
#     }
# }

# dbname.command("collMod", "employees", validator = emp_schema)

# print(dbname.get_collection("employees").options())

# employees = dbname.employees
# employees.create_index([("emp_id",1)], unique = True)
test = {
    "emp_id": "104427",
    "emp_name": "Anantha",
    "group": "C",
    "email": "akrrao7@gmail.com",
    "password": "hashed"
}
# employees.insert_one(test)
test_emp = Employee()
# test_emp.insert(test)
# print(test_emp.get_employee_id()[0].get('emp_id'))

test_holiday = Holiday()

date = datetime.datetime(2024, 1, 26)
# test_holiday.create(date,[test_emp.get_employee_id()[0].get('emp_id')], "PD2")
test_holiday.swap_giveaway("123456", date, "PD2","Swap")
print(test_holiday.get(date))