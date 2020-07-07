# Split 함수

items = 'zero one two three'.split()  # 빈칸을 기준으로 문자열 나누기
print(items)  # ['zero', 'one', 'two', 'three']

example = 'python, jquery, javascript'
example.split(",")  # ","을 기준으로 문자열 나누기
a, b, c = example.split(",")  # 리스트에 있는 각 값을 a,b,c 변수로 unpacking
print(a)  # python
