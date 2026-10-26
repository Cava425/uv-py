# Python 关键字 / 内置函数笔记

> 每学一个新的关键字或函数，在本文件末尾按相同格式追加一节，并更新目录。

## 目录

- [enumerate](#enumerate)
- [map](#map)

---

## enumerate

**作用**：遍历可迭代对象时，同时得到「序号」和「元素」，替代 `range(len(x))` 与手动计数器。

**签名**：`enumerate(iterable, start=0)` → 返回迭代器，每项是 `(index, item)` 元组。

```python
fruits = ["apple", "banana", "cherry"]

for i, f in enumerate(fruits):
    print(i, f)            # 0 apple / 1 banana / 2 cherry

for i, f in enumerate(fruits, start=1):   # 序号从 1 开始
    print(i, f)

list(enumerate("ab"))      # [(0, 'a'), (1, 'b')]
```

**常见用法**

```python
# 1. 替代 range(len(...))
for i in range(len(nums)): n = nums[i]      # 不推荐
for i, n in enumerate(nums): ...            # 推荐

# 2. 构造 值->下标 字典（两数之和常用）
pos = {v: i for i, v in enumerate(nums)}

# 3. 找满足条件的下标
idx = [i for i, v in enumerate(nums) if v > 0]

# 4. 解包嵌套结构，注意括号
for i, (k, v) in enumerate({"a": 1}.items()): ...
```

**注意**

- 返回的是惰性迭代器，只能遍历一次；需要复用用 `list(...)`。
- `start` 只改变序号，不跳过元素。
- 遍历时修改原列表长度容易出错，必要时遍历副本。

**项目中的例子**：`algorithms/permutations/solution.py` 中 `for i, n in enumerate(nums)` 用下标 `i` 查 `used[i]`，同时取值 `n`。

---

## map

**作用**：把函数依次应用到一个或多个可迭代对象的元素上，得到转换后的结果。适合表达“对每项做相同转换”。

**签名**：`map(function, iterable, *iterables)` → 返回惰性的 `map` 迭代器。

```python
numbers = ["1", "2", "3"]
converted = map(int, numbers)
list(converted)               # [1, 2, 3]

words = ["hello", "python"]
list(map(str.upper, words))   # ['HELLO', 'PYTHON']
```

**常见用法**

```python
# 1. 转换输入字符串中的每个数字
values = list(map(int, input().split()))

# 2. 对两个序列按位置同时计算；结果长度由较短的序列决定
bases = [2, 3, 4]
exponents = [3, 2]
list(map(pow, bases, exponents))  # [8, 9]

# 3. 需要自定义规则时，可以传 lambda
list(map(lambda n: n * n, [1, 2, 3]))  # [1, 4, 9]
```

**注意**

- `map` 是惰性的：创建时不会立即完成转换，遍历或调用 `list(...)` 时才逐项执行。
- `map` 迭代器只能消费一次；如果后续还要遍历结果，先保存为 `list`。
- 传入多个可迭代对象时，函数要能接收对应数量的参数；迭代在最短的可迭代对象耗尽时停止。
- 转换逻辑较复杂时，列表推导式通常更清晰，例如 `[int(s) for s in numbers]`；需要惰性结果时可用生成器表达式。

**与列表推导式对比**：`list(map(int, strings))` 与 `[int(s) for s in strings]` 都会得到转换后的列表；`map(...)` 本身则不立即生成整个列表。
