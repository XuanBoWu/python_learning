number_of_like = {
    'alex': [5, 11, 15],
    'chen': [7, 23, 32],
    'bob': [10, 1, 90],
}

for name in number_of_like:
    print(f"hey {name.title()}, your favorite number are:", end="")
    for number in number_of_like[name]:
        print(f"{number},", end=".")
    print()
    
# qwen给出的标准答案
# for name, numbers in number_of_like.items():
#     print(f"Hey {name.title()}, your favorite numbers are:")
#     for number in numbers[:-1]:
#         print(f"{number},", end="")
#     print(numbers[-1])  # 不需要end参数，直接打印最后一个数字并换行
#     print()  # 可选，为了增加额外的间隔，可以在每个人的数据后都添加一个空行