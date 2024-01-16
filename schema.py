schema = {
    "bsontype": "object",
    "required": [],
    "properties": {
        "emp_id": {
            "bsontype": "string",
            "description": "required string"
        },
        "emp_name": {
            "bsontype": "string",
            "description": "required string"
        },
        "group": {
            "bsontype": "string",
            "description": "required"
        },
        "email": {
            "bsontype": "string",
            "description": "required"
        },
        "password": {
            "bsontype": "string",
            "description": "required"
        },
        "shift": {
            "bsontype": "array",
            "description": "shift array",
            "items": {
                "bsontype": "string",
                "description": "S1/S2/Pd1/Pd2/Pd3"
            }
        },
        "date":{
            "bsontype": "array",
            "description": "array of dates",
            "items": {
                "bsontype": "date",
                "description": "date of corresponding shift"
            }
        }
    }
}