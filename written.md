# 程序部国庆作业
# 选择题 + 简答题
## 一、选择题（每题 2 分，共 10 题，满分 20 分）
1. 依次执行以下代码，输出是什么？
   def f(x, lst=[]):
       lst.append(x)
       return lst

   a = f(1)
   b = f(2)
   print(b)
   - A. `[2]`
   - B. `[1, 2]`
   - C. `[1]`
   - D. `TypeError: 'list' object is not callable`
2. 依次执行以下代码，输出是什么？
   a = [1, 2, 3]
   b = a
   c = a.copy()
   a.append(4)
   print(b, c)
  - A. `[1, 2, 3, 4]  [1, 2, 3, 4]`
   - B. `[1, 2, 3, 4]  [1, 2, 3]`
   - C. `[1, 2, 3]  [1, 2, 3, 4]`
   - D. `[1, 2, 3]  [1, 2, 3]`

3. 依次执行以下代码，输出是什么？
   try:
       x = 1 / 0
   except ZeroDivisionError:
       print("A")
   else:
       print("B")
   finally:
       print("C")
   - A. 只输出 `C`
   - B. 输出 `A` 和 `C`
   - C. 输出 `B` 和 `C`
   - D. 输出 `A`、`B` 和 `C`

4. 依次执行以下代码，输出是什么？
   s = " hello "
   print(len(s))
   print(len(s.strip()))
   - A. `7  7`
   - B. `7  5`
   - C. `5  5`
   - D. `5  7`

5. 以下代码的执行结果是？
   for i in range(5):
       if i == 3:
           break
   else:
       print("done")
   print("end")
   - A. 输出 `done` 和 `end`
   - B. 只输出 `end`
   - C. 只输出 `done`
   - D. 什么都不输出

6. 依次执行以下代码，输出是什么？
   class Animal:
       def __init__(self, name):
           self.name = name

       def speak(self):
           print("...")

   class Dog(Animal):
       def speak(self):
           print(f"{self.name}: woof")

   d = Dog("Rex")
   d.speak()
   - A. `...`
   - B. `Rex: woof`
   - C. 输出两行：`...` 和 `Rex: woof`
   - D. `AttributeError: 'Dog' object has no attribute '__init__'`

7. 以下代码中，`d` 的值是什么？
   d = {"a": 1, "b": 2}
   d = {k: v for k, v in d.items() if v > 1}
   print(d)
    - A. `{'a': 1, 'b': 2}`
   - B. `{'b': 2}`
   - C. `{1: 'a', 2: 'b'}`
   - D. `SyntaxError: invalid syntax`

8. 依次执行以下代码，输出是什么？
   import json
   s = json.dumps({"name": "张三", "age": 18})
   print(type(s))
  - A. `<class 'dict'>`
   - B. `<class 'str'>`
   - C. `<class 'bytes'>`
   - D. `TypeError: dump() missing 1 required positional argument: 'fp'`

9. 依次执行以下代码，输出是什么？
   def f(x):
       return x + 1

   f(5)
   print(f(5))
   - A. 输出两行：`None` 和 `6`
   - B. 只输出 `6`
   - C. 只输出 `None`
   - D. 输出 `6` 两次

10. 以下代码中，`user.get("city")` 和 `user["city"]` 的区别是什么？
    user = {"name": "张三", "age": 18}
  - A. 没有区别，两者行为完全一致
    - B. `get()` 返回默认值 `None`，`[]` 抛出 `KeyError`
    - C. `get()` 抛出 `KeyError`，`[]` 返回 `None`
    - D. `get()` 只能用于字符串键，`[]` 可以用于任意键

### 答案
'1.B 2.B 3.B 4.B 5.B 6.B 7.B 8.B 9.B 10.B
## 二、简答题（每题 10 分，共 3 题，满分 30 分）
### 第 1 题：浅拷贝与深拷贝

以下代码中，`a`、`b`、`c` 三者之间的关系是什么？执行 `a[0].append(99)` 后，`b` 和 `c` 分别变成什么？请解释原因。
a = [[1, 2], [3, 4]]
b = a.copy()
import copy
c = copy.deepcopy(a)
（在此作答）
a是原始列表，b是a的浅拷贝，c是a的深拷贝。b变为[[1,2,99],[3,4]],c变为[[1,2],[3,4]],原因：列表为可变对象，a[0]代表在a列表中第一个元素后加99，a和b共用一个子列表，b也会跟着a变，c为深拷贝,有自己独立的子列表副本，因此不会随a改变。

### 第 2 题：字典与列表的综合应用

以下代码模拟"从日志中提取用户信息"，请回答：
logs = [
    {"user": "张三", "action": "login", "level": "INFO"},
    {"user": "李四", "action": "logout", "level": "INFO"},
    {"user": "张三", "action": "error", "level": "ERROR"},
    {"user": "王五", "action": "login", "level": "INFO"},
    {"user": "李四", "action": "error", "level": "ERROR"},
]
1. 写出表达式，找出所有 `level` 为 `"ERROR"` 的日志（返回字典列表）。
2. 写出表达式，统计每个用户出现了几次（返回字典，键为用户名，值为次数）。
3. 解释为什么第 2 问不能直接用 `len(logs)` 得到结果，需要什么遍历结构？

（在此作答）
1.error_logs=()
  for log in logs:
      if log("level")=="ERROR"
        error_logs.append(log)
  return error_logs  

2.count={}
  for log in logs:
      a=log("user")
      count(a)=count.get(a,0)+1
   print(count)
 3.len(logs)是显示列表中字典的个数，不能查看到字典内部的信息，可以用for循环遍历。  
  
### 第 3 题：异常处理设计

Day_10 中你写过 `safe_int(s)` 函数：能转就返回整数，不能转就返回 `None`。

现在请你设计一个 `safe_divide(a, b)` 函数：

- 输入两个字符串 `a` 和 `b`
- 尝试将它们转为数字并计算 `a / b`
- 如果转换失败（`ValueError`）或除数为零（`ZeroDivisionError`），返回 `None`
- 否则返回商（`float`）

请写出函数代码，并说明：为什么这里用 `try/except` 比先用 `if` 判断再计算更好？

（在此作答）

 
def safe_divide(a,b)
    try:
        n1=float(a)
        n2=float(b)
        c=n1/n2
        return c
    except(ValueError or ZeroDivisionError):
        return None
此题条件比较多，若用if函数,代码会很长，因此用“try/except”  较为妥当。      
        











