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

'1.B 2.B 3.B 4.B 5.B 6.B 7.B 8.B 9.B 10.B
