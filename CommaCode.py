def commaCode(list):
  res = ""
  for i in range(len(list) - 1):
    res += str(list[i]) + ", "
  res += "and " + str(list[len(list) - 1])
  return res

list = ["candy", "how", "are", "you"] 
print(commaCode(list))