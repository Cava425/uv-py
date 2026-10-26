import copy

print("== 数字 ==", 7 // 2, 7 % 2, 2**10, 0.1 + 0.2 == 0.3)

s = "Hello, Python"
print("== 字符串 ==", s[0], s[-1], s[:5], s.upper(), s.split(","))

nums = [3, 1, 2]
nums.append(4)
nums.sort()
print("== 列表 ==", nums, [x * x for x in nums])

x, y = (1, 2)
print("== 元组 ==", x, y)

d = {"name": "Tom", "age": 18}
d["age"] += 1
print("== 字典 ==", d, d.get("city", "unknown"))

a, b = {1, 2, 3}, {2, 3, 4}
print("== 集合 ==", a | b, a & b, a - b, a ^ b)

m = [[1], [2]]
shallow, deep = copy.copy(m), copy.deepcopy(m)
m[0].append(9)
print("== 拷贝 ==", shallow, deep)

print("== 转换 ==", int("42"), list("abc"), bool([]), None is None)
