Telegram Username Availability Checker

This Python script checks the availability of usernames on both Telegram and Fragment. It's useful if you're looking to claim or purchase a clean username.

🔧 How to Use

Install dependencies (only requests is required):

pip install requests

Run the script:

python check_usernames.py

You can paste your list of usernames in one of two formats:

    Comma-separated:
    username1, username2, username3

    Line-separated (one per line):

    username1  
    username2  
    username3  

💡 For line-separated mode, make sure to use the built-in line input parser instead of the list-checker block.

The script will check each username and show which ones are available and which are taken.

📋 Example Output

🔍 Check 1/3: username1  
✅ Available: username1  
🔍 Check 2/3: username2  
❌ Unavailable: username2  
...
🎉 Free usernames:
@username1

🚫 Taken usernames:
@username2

⚠️ Known Issue
I'm aware of a bug where the script may incorrectly mark usernames from banned Telegram accounts as taken. This is due to the way Telegram displays such profiles. A fix is in progress and will be released soon.

📌 Features

    Checks both https://t.me/username and https://fragment.com/username

    Includes a 1-second delay between requests to avoid being rate-limited or blocked

    Lightweight and easy to use

    Supports both comma-separated and line-separated input formats
