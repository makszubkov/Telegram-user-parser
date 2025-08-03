import time
import requests

def check_availability(username):
    headers = {"User-Agent": "Mozilla/5.0"}

    # Проверка на Telegram
    try:
        tg_resp = requests.get(f"https://t.me/{username}", headers=headers, timeout=10)
        if "If you have Telegram, you can contact" in tg_resp.text:
            return False  
    except Exception as e:
        print(f"[Error Telegram] {username}: {e}")
        return False

    # Проверка на Fragment
    try:
        fr_resp = requests.get(f"https://fragment.com/username/{username}", headers=headers, timeout=10)
        if "unavailable" not in fr_resp.text.lower():
            return False  
    except Exception as e:
        print(f"[Error Fragment] {username}: {e}")
        return False

    return True  

def main():
    user_input = input("Paste username list:\n")
    usernames = [u.strip().lower() for u in user_input.split(",") if u.strip()]

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

    print("\n🎉 Free username's:")
    for u in available:
        print(f"@{u}")

    print("\n🚫 Taken username's:")
    for u in taken:
        print(f"@{u}")

if __name__ == "__main__":
    main()

