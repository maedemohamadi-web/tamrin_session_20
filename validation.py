import re

def name_validator(name):
    if not isinstance(name,str) or  not re.match("^[a-zA-Z0-9\s]{3,50}$", name):
        raise ValueError("Invalid Name")
    return name

def teacher_validator(teacher):
    if not isinstance(teacher,str) or  not re.match("^[a-zA-Z0-9\s]{5,50}$", teacher):
        raise ValueError("Invalid Teacher")
    return teacher

def code_validator(code):
    if not isinstance(code, str) or not re.match("^[a-zA-Z]{3}-[a-zA-Z]{4}$",code) :
        raise ValueError("Invalid Code")
    return code

def unit_validator(unit):
    if not isinstance(unit, int) or unit not in [1,2,3,5] :
        raise ValueError("Invalid Unit")
    return unit
