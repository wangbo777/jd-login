import requests
import subprocess
import time

# 青龙面板的 API 地址和 Token
ql_url = "http://你的青龙地址/open/envs"
ql_token = "你的Token"

def get_new_cookie():
    # 运行登录脚本并获取新的 Cookie
    result = subprocess.run(['python', '/app/login.py'], capture_output=True, text=True)
    if result.returncode == 0:
        new_cookie = result.stdout.strip()  # 假设登录脚本输出的是 Cookie
        return new_cookie
    else:
        print("登录失败:", result.stderr)
        return None

def update_cookie_in_qinglong(cookie):
    headers = {
        "Authorization": f"Bearer {ql_token}",
        "Content-Type": "application/json"
    }

    data = [{
        "name": "JD_COOKIE",
        "value": cookie,
        "remarks": "京东 Cookie"
    }]

    response = requests.put(ql_url, headers=headers, json=data)

    if response.status_code == 200:
        print("Cookie 更新成功")
    else:
        print("更新 Cookie 失败:", response.text)

def main():
    while True:
        new_cookie = get_new_cookie()
        if new_cookie:
            update_cookie_in_qinglong(new_cookie)
        time.sleep(86400)  # 每24小时更新一次

if __name__ == "__main__":
    main()
