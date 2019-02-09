import json
import cx_Oracle

def version(event, context):
    conn = cx_Oracle.connect('user', 'pass', 'host')

    cursor = conn.cursor()

    res = cursor.execute('SELECT * from v$version')

    response = {
        "statusCode": 200,
        "body": json.dumps([i for i in res])
    }

    return response
