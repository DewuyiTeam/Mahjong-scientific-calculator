import streamlit as st
import math


st.title("宇宇运算器")

# creates a horizontal line
st.write("---")
st.write(
    """<style>
#MainMenu {visibility: hidden;}
.css-15zrgzn {display: none}
footer {visibility: hidtren;}
[data-testid="column"] {
    width: calc(25% - 1rem) !important;
    flex: 1 1 calc(25% - 1rem) !important;
    min-width: calc(20% - 1rem) !important;
}
.css-1l269bu {max-width:20% !important;}
[data-testid="stText"] {font-size: 45px}
.tiles {height:100%; overflow-x:scroll; overflow-y:hidden; white-space: nowrap;margin : 0px 0 5px 0;}
.tile {height:50px;margin:1px}
.blank-tile {width: 10px;height:50px;}
</style>
""",
    unsafe_allow_html=True,
)

def main():

    # 获取math模块中的所有函数名称
    math_functions = [name for name in dir(math) if callable(getattr(math, name))]

    expression = st.text_input("输入表达式:")
    
    if st.button("计算"):
        if expression == "雀魂，启动！":
            import webbrowser

            # 定义目标网站的URL
            url = "https://game.maj-soul.com/1/"

            # 使用webbrowser库打开网页
            webbrowser.open(url)
        elif expression == "原神，启动！":
            import webbrowser

            # 定义目标网站的URL
            url = "https://ys.mihoyo.com/"

            # 使用webbrowser库打开网页
            webbrowser.open(url)
        else:
            try:
                result = evaluate_expression(expression)
                st.success(f"结果: {result}")
            except Exception as e:
                st.error(f"错误: {e}")

def evaluate_expression(expression):
    # 创建一个包含math模块中所有函数的命名空间
    math_namespace = {"math": math}
    
    # 计算表达式
    result = eval(expression, math_namespace)

    return result

if __name__ == "__main__":
    main()
num1 = st.number_input(label="输入度数或数值")
st.write("三角函数与对数计算")

operation = st.radio("选择计算模式:",
                     ("sin", "cos", "tan", "asin", "acos", "atan", "lg", "ln"))
ans = 0


def calculate():
    if  operation == "sin":
        angle_radians = math.radians(num1)
        ans = math.sin(angle_radians)
    elif operation == "cos":
        angle_radians = math.radians(num1)
        ans = math.cos(angle_radians)
    elif operation == "tan":
        angle_radians = math.radians(num1)
        ans = math.tan(angle_radians)
    elif operation == "asin":
        ans = math.degrees(math.asin(num1))
    elif operation == "acos":
        ans = math.degrees(math.acos(num1))
    elif operation == "atan":
        ans = math.degrees(math.atan(num1))
    elif operation == "lg":
        ans = math.log(num1,10)
    elif operation == "ln":
        ans = math.log(num1)
    else:
          st.warning("输入错误")
          ans = "Not defined"

    st.success(f"结果: {ans}")


if st.button("计算结果"):
    calculate()

import random

# 打开文本文件并读取内容
with open('static/your_text_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化data列表
data = []

# 解析文本内容，提取题目和答案
for line in lines:
    line = line.strip()
    if line:
        # 查找包含"答案:"的行
        if "答案:" in line:
            parts = line.split("答案:")
            if len(parts) == 2:
                question = parts[0].strip()
                answer = parts[1].strip()
                data.append((question, answer))
        else:
            # 如果不包含"答案:"，假设这是题目的一部分
            if data:
                data[-1] = (data[-1][0] + " " + line, data[-1][1])

# 去掉题目中的数字
data = [(question.lstrip("1234567890. "), answer) for question, answer in data]

random_question, answer = random.choice(data)

# 创建Streamlit应用
st.title("神秘按钮")

if st.button("DONTOUCHME"):
    st.write(random_question)
    st.write(answer)