# response = (200, {'content-type' : 'applicant/json'}, '{"name" : "Alice"}')
# status_code, headers, body = response
# print(type(status_code), type(headers), type(body))

# def sum(num1, num2=5, num3=10):
#     return num1 + num2 +num3

# print(sum(2, 6))

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1, 2, 3, 4, 5))
# print(add(7, 4, 3))
# print(add(1, 3, 4, 5))

# def calculate(**kwargs):
#     print(kwargs)

# calculate(num_1=3, num_2=5, operator="+")

# def calculate(**kwargs):
#     for key, value in kwargs.items():
#         print(f"key={key}, value={value}")

# calculate(num_1=3, num_2=5, operator="+")