def func1():
  value = 10
  return value

def func2(input_value):
  result = input_value * 2
  print(result)

# Call func1 and pass its result to func2
func2(func1())  # Output: 20