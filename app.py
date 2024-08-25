
from gpt4all import GPT4All  # 假设使用 GPT-4All 本地模型

# 设定模型目录和模型名称
model_path = "/Users/xuyuwei/Library/Application Support/nomic.ai/GPT4All/"
model_name = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"

from gpt4all import GPT4All

# 初始化 GPT-4all 实例
gpt = GPT4All(model_path = model_path,model_name=model_name)  # 请确保使用正确的模型名称

# 输入提示
prompt = "我想了解更多关于人工智能模型的具体功能和用途。你能详细说明一下吗？"

# 获取响应（使用正确的方法）
response = gpt.generate(prompt)  # 或者使用你查到的正确方法

# 打印响应
print("回答:", response)
