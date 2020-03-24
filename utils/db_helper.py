import cx_Oracle

def get_dictformat(cur):
    data = {}
    num_of_record = 0
    for implicitCursor in cur.getimplicitresults():
        for row in implicitCursor:
            data[num_of_record] = list(row)
            num_of_record += 1
    if len(data.keys()) == 0:
        data = None
    return data

def get_listformat(cur):
    data = []
    for implicitCursor in cur.getimplicitresults():
        for row in implicitCursor:
            data.append(list(row))
    if len(data) == 0:
        data = None
    return data
