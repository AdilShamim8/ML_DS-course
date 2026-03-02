# Default settings
defaults = {"theme": "light", "audio": "on"}

# User preferences (partial override)
user_pref = {"theme":  "dark"}

merged1 = defaults | user_pref


print(f"  Result: {merged1}")