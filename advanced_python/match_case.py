#match_case is similar to switch case in java and c
#it is a new feature in python 3.10
#it is used to handle multiple conditions in a single if-elif-else statement


#example
def http_status(status):
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not found")
        case 500:
            print("Internal server error")
        case _:
            print("unkown status")
            
http_status(200)
http_status(404)
http_status(500)
http_status(600)