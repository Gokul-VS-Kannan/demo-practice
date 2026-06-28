def list_to_dict(key,value):
     
    new_dict={}

    for i in range(len(key)):
        if i < len(value):
            new_dict[key[i]]=value[i]

    return new_dict

key_list=['name','age','salary','sector']
value_list=['Gokul',26,15000,'Developer']

result=list_to_dict(key_list,value_list)

print(result)
