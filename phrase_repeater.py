inputstr = input("Input your phrase:")
counter = 0
inputval = eval(input("How many times should it be repeated?"))
for i in range(inputval):
  counter = counter + 1
  print(counter, inputstr)