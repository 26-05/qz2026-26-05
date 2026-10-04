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
'1.B 2.B 3.B 4.B
