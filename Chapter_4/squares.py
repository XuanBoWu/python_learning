squares = []

for value in range(1,11):
	squares.append(value ** 2)

print(squares)

## 列表解析
squares = [value**3 for value in range(1, 11)]
print(squares)