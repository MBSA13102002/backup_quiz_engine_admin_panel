import json,ast

# # some JSON:
x =  ''
data_dict = ast.literal_eval(x)
# # parse x:
# y = json.loads(x)
print(data_dict)
# # the result is a Python dictionary:
# print(y["age"])