import json
import os
import google.generativeai as genai

# 設定 Gemini API Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def get_weather():
    # 這裡未來可以替換成真實氣象 API
    return "台北今天天氣晴朗，氣溫 26-30 度，降雨機率 10%"


def generate_script():
    weather_info = get_weather()

    prompt = f"""
    你是一個貼心的智慧居家語音助手。請根據以下資訊，寫一份約 100 字簡短親切的晨報廣播稿：
    - 天氣狀況：{weather_info}
    - 提醒：記得多喝水，祝你有美好的一天！
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    # 1. 產生播報文字
    script_text = generate_script()
    print("生成的晨報內容：\n", script_text)

    # 2. 存成 news.json 供網頁讀取
    data = {"text": script_text}
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ news.json 已成功更新！")
