import os
import json

# 获取%appdata%环境变量的值
appdata_path = os.getenv("APPDATA")

# 构建完整的Parsec路径
parsec_path = os.path.join(appdata_path, "Parsec")

# 构建config.json文件的完整路径
config_file_path = os.path.join(parsec_path, "config.json")

# 检查Parsec路径和config.json文件是否存在
if os.path.exists(parsec_path) and os.path.isfile(config_file_path):
    try:
        # 读取config.json文件内容
        with open(config_file_path, "r", encoding="utf-8") as file:
            config_data = json.load(file)

        # 遍历数组，找到对象并修改echo_app_selection字段的值
        for item in config_data:
            if isinstance(item, dict) and "echo_app_selection" in item:
                # 这里填写进程名，例如微信写"WeChat.exe", QQ写"QQ.exe"  
                item["echo_app_selection"]["value"] = "WeChat.exe"   
                break  # 找到后跳出循环
        else:
            print("config.json文件中未找到echo_app_selection字段。")

        # 将修改后的内容写回到config.json文件
        with open(config_file_path, "w", encoding="utf-8") as file:
            json.dump(config_data, file, ensure_ascii=False, indent=4)

        print("config.json文件已更新。")
    except json.JSONDecodeError as e:
        print(f"解析config.json文件时出错: {e}")
else:
    print("Parsec文件夹或config.json文件不存在。")
