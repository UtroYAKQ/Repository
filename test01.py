import re

# 示例正则表达式：匹配一个或多个数字
pattern = r'\d+'

# 测试字符串
test_string = "这是一个包含数字123和456的字符串"

# 使用正则表达式查找所有匹配项
matches = re.findall(pattern, test_string)

# 输出匹配结果
print(matches)