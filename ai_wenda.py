import requests
import json
key = "sk-ws-H.EDHIDXE.cEaH.MEUCIHFUlEA12_CnDkb8lQKTJU-dRSC1MLZvRXpd3B7Yjd77AiEAtsVL_UqofUuZxx9JudnuPfg-NAut9BJMUCBHOMW0A8c"
url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
def duqv(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        return data
    except:
        return "知识库不存在"
def diaoyong(user, txt):
    prompt = f"""你现在是一个学校的事务助手。你的任务是根据用户的问题，从知识库中提取相关信息，回答用户的问题。
    如果用户的问题与知识库中的内容不相关，返回“根据学校规则，无法回答您的问题”。
    知识库内容如下：
    {txt}
    用户问题：{user}
    请回答用户的问题，保持回答的准确性和完整性。
    回答："""
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"错误：{e}"
if __name__ == "__main__":
    duq = duqv("test.txt")
    print("------智能问答系统------")
    print("输入'exit'退出")
    while True:
        user = input("请输入您的问题：")
        if user == "exit":
            print("谢谢使用！")
            break
        if not user.strip():
            continue

        print("正在查询...")
        huida = diaoyong(user, duq)
        print(f"回答：{huida}")
