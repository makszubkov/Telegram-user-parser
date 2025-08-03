import time
import requests

def check_availability(username):
    headers = {"User-Agent": "Mozilla/5.0"}

    # check Telegram
    try:
        tg_resp = requests.get(f"https://t.me/{username}", headers=headers, timeout=10)
        if "If you have Telegram, you can contact" in tg_resp.text:
            return False  # username unavailable
    except Exception as e:
        print(f"[Ошибка Telegram] {username}: {e}")
        return False

    # Check Fragment
    try:
        fr_resp = requests.get(f"https://fragment.com/username/{username}", headers=headers, timeout=10)
        if "unavailable" not in fr_resp.text.lower():
            return False  # username unavailable
    except Exception as e:
        print(f"[Ошибка Fragment] {username}: {e}")
        return False

    return True  # username available

def main():
    print("Insert usernames one per line. Blank line - finish input.")
    usernames = []
    while True:
        line = input().strip()
        if not line:
            break
        usernames.append(line.lower())

    available = []
    taken = []

    for i, name in enumerate(usernames, 1):
        print(f"🔍 Check {i}/{len(usernames)}: {name}")
        if check_availability(name):
            print(f"✅ Available: {name}")
            available.append(name)
        else:
            print(f"❌ Unavailable: {name}")
            taken.append(name)
        time.sleep(1)

    print("\n🎉 Available username:")
    for u in available:
        print(f"@{u}")

    print("\n🚫 Unavailable username:")
    for u in taken:
        print(f"@{u}")

if __name__ == "__main__":
    main()

