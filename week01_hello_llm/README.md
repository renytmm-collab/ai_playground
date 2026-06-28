# Week01: Hello LLM Chatbot

这是 AI Playground 的第一个练习项目：用 Python 调用兼容 OpenAI API 的大语言模型，完成一个最小可运行的命令行聊天机器人。

项目重点不是做复杂功能，而是理解一次 LLM API 调用从配置、请求、响应到异常处理的完整流程。

## 功能

- 启动后进入命令行聊天模式
- 使用 DeepSeek OpenAI-compatible API
- 支持连续多轮对话
- 使用内存保存本次运行期间的聊天上下文
- 输入 `exit` 或 `quit` 退出程序
- 使用 `.env` 管理 API Key、Base URL 和模型名
- 对缺少依赖、缺少 API Key、认证失败、网络失败、模型不存在和请求失败做友好提示

## 项目结构

```text
week01_hello_llm/
|-- main.py
|-- config.py
|-- .env.example
|-- requirements.txt
|-- README.md
`-- .gitignore
```

## 环境要求

- Python 3.11+
- DeepSeek API Key

## 安装依赖

建议先创建虚拟环境：

```bash
python -m venv .venv
```

Windows PowerShell 激活虚拟环境：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装依赖：

```bash
pip install -r requirements.txt
```

## 配置 DeepSeek API

复制 `.env.example` 为 `.env`：

```bash
copy .env.example .env
```

然后把 `.env` 里的 `API_KEY` 改成你的 DeepSeek API Key：

```env
API_KEY=your_deepseek_api_key_here
BASE_URL=https://api.deepseek.com
MODEL=deepseek-v4-flash
```

注意：不要把 `.env` 提交到 GitHub。项目已经在 `.gitignore` 中忽略 `.env`。

## 运行方式

```bash
python main.py
```

运行后会看到：

```text
Hello LLM Chatbot
Type exit or quit to leave.
You:
```

输入消息后，程序会调用 DeepSeek 并输出模型回复。输入 `exit` 或 `quit` 可以退出。

## 示例

```text
Hello LLM Chatbot
Type exit or quit to leave.
You: My name is Reny. Reply OK only.
Bot: OK
You: What is my name? Reply with the name only.
Bot: Reny
You: exit
Goodbye!
```

## 项目截图

后续补充。

## 学习收获

- 学会了使用 `openai` SDK 调用兼容 OpenAI API 的模型
- 学会了用 `.env` 管理敏感配置，避免把 API Key 写死在代码里
- 理解了多轮对话的核心是把历史消息列表一起传给模型
- 练习了基本的命令行输入循环、退出条件和异常处理
- 理解了失败请求不应该写入聊天记忆，避免污染上下文

## 当前进度

- [x] 可以启动程序
- [x] 可以正常调用 LLM
- [x] 可以连续聊天
- [x] 可以记住上下文
- [x] 可以正常退出
- [x] 使用 `.env` 管理配置
- [ ] GitHub 成功提交
