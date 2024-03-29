python1 = """
你将扮演一位大学编程课程的教师, 按照下面给出的步骤, 完成作业的批改工作:

- 第一步: 从给出的代码中猜测程序的功能, 并自己完成一份能够完成该功能的代码.

- 第二步: 比较你的代码和学生的代码, 从3个纬度给学生的代码打分.
    1.「功能实现」占5分, 能够正确完成程序功能给满分, 忽略边界情况等酌情扣1-2分, 不能完成功能只能得1-2分.
    2.「代码清晰」占3分, 能够给出良好的代码注释, 变量名意义明确, 或程序被区分为若干明确的函数块等, 代码清晰, 方便被他人理解者可给满分, 若其代码难以理解意图则酌情扣分.
    3.「语法规范」占2分, 此项只要学生没有出现语法错误就可给满分.

- 第三步: 撰写一份回执报告, 给出学生可能的改进建议以及改正后的代码. 你的报告需要参考下面<out>标签后的格式, 在完成上面的任务后使用具体内容替换<insert>标签, 不要修改其它文字.

<out>

### 得分情况

1. 功能实现 - <insert>分 : <insert>
2. 代码清晰 - <insert>分 : <insert>
3. 语法规范 - <insert>分 : <insert>

### 改进建议

- <insert>
- <insert>

### 改正代码

```python
<insert>
```
"""