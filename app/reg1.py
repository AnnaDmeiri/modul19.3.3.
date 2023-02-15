import kwargs
import requests

status = 'available'

res = requests.get(f'http://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})


res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})


res = requests.post(f"https://petstore.swagger.io/v2/pet/addPet", headers={'accept': 'application/json'}, data = {'key1': 'value1', 'key2': 'value2'})

#
# res = requests.delete(f"https://petstore.swagger.io/#/pet/deletePet", **kwargs)
#
#
# res = requests.put(f"https://petstore.swagger.io/v2/pet/updatePet", data={'key1': 'value1', 'key2': 'value2'})