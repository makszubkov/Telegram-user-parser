Telegram Username Availability Checker

This Python script checks the availability of usernames on both Telegram and Fragment. It's useful if you're looking to claim or purchase a clean username.
🔧 How to Use

    Install dependencies (only requests is required):

pip install requests

Run the script:

python check_usernames.py

Paste your list of usernames, separated by commas:

    username1, username2, username3

    The script will check each username and show which ones are available and which are taken.

📋 Example Output

🔍 Check 1/3: username1  
✅ Available: username1  
🔍 Check 2/3: username2  
❌ Unavailable: username2  
...
🎉 Free username's:  
@username1  

🚫 Taken username's:  
@username2

⚠️ Known Issue

I'm aware of a bug where the script may incorrectly mark usernames from banned Telegram accounts as taken. This is due to the way Telegram displays such profiles.
A fix is in progress and will be released soon.
📌 Features

    Checks both https://t.me/username and https://fragment.com/username/.

    Includes a 1-second delay between requests to avoid being rate-limited or blocked.

    Lightweight and easy to use.
