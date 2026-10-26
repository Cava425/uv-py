# Python 数据类型学习指南

运行示例：`uv run python python_datatypes/examples.py`

## 学习路线

1. 数字：`int` / `float` / `complex` / `bool`
2. 字符串：`str`
3. 序列：`list` / `tuple` / `range`
4. 映射：`dict`
5. 集合：`set` / `frozenset`
6. 空值：`None`
7. 可变 vs 不可变、类型转换

## 1. 数字与布尔

```python
a = 10          # int，任意精度
b = 3.14        # float
c = 2 + 3j      # complex
flag = True     # bool 是 int 的子类，True == 1
print(7 // 2, 7 % 2, 2 ** 10)   # 3 1 1024
print(0.1 + 0.2 == 0.3)         # False，浮点误差；用 math.isclose
```

## 2. 字符串 str（不可变）

```python
s = "Hello, Python"
s[0], s[-1], s[0:5]             # 索引与切片
s.upper(), s.split(","), " ".join(["a", "b"])
f"{s} has {len(s)} chars"       # f-string
```

## 3. 列表 list（可变、有序）

```python
nums = [3, 1, 2]
nums.append(4); nums.sort(); nums[1:3]
[x * x for x in nums]           # 列表推导式
```

## 4. 元组 tuple（不可变、有序）

```python
p = (1, 2)
x, y = p                        # 解包
```

## 5. 字典 dict（键值对，保持插入顺序）

```python
d = {"name": "Tom", "age": 18}
d["age"] += 1
d.get("city", "unknown")
for k, v in d.items(): ...
{k: v for k, v in d.items()}    # 字典推导式
```

键必须是可哈希（不可变）类型。

## 6. 集合 set（无序、去重）

```python
a, b = {1, 2, 3}, {2, 3, 4}
a | b, a & b, a - b, a ^ b      # 并 交 差 对称差
list(set([1, 1, 2]))            # 去重
```

## 7. None

```python
x = None
x is None                       # 判断用 is，不用 ==
```

## 8. 可变与不可变

| 不可变 | 可变 |
| --- | --- |
| int, float, bool, str, tuple, frozenset, None | list, dict, set |

```python
a = [1]; b = a; b.append(2)     # a 也变了（同一对象）
c = a.copy()                    # 浅拷贝；嵌套用 copy.deepcopy
```

## 9. 类型检查与转换

```python
type(1), isinstance(1, int)
int("42"), float("3.5"), str(10), list("abc"), tuple([1, 2]), set([1, 1])
bool(0), bool(""), bool([])     # 假值：0 "" [] {} set() None
```

## 练习

1. 统计一句话中每个单词出现次数（dict）。
2. 对列表去重并保持原顺序。
3. 求两个列表的交集与差集（set）。
4. 解释为何 `def f(x=[])` 是陷阱。
5. 把 `[("a", 1), ("b", 2)]` 转为字典再反转键值。
