data = [
      
       {"name":"saurabh","age":23},
       {"name":"rahul","age":25.50},
       {"name":"kunal","age":"thirty"},
       {"name":"abhay","age":""},
       {"name":"pankaj"}
    
    
    ]


def valid_data(data):
    invalid = []
    for i in data:
        if "age" not in i:
            invalid.append(i)
        elif type(i['age']) != int:
            invalid.append(i)
    return invalid


obj = valid_data(data)
print("invalid data list :",obj)