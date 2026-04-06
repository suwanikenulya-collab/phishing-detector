url = input("Enter a URL: ")

suspicious = 0

# Rule 1: Check for @
if "@" in url:
    print("Contains @ symbol ❌")
    suspicious += 1

# Rule 2: Length check
if len(url) > 75:
    print("URL is too long ❌")
    suspicious += 1

# Rule 3: Hyphen check
if "-" in url:
    print("Contains hyphen ❌")
    suspicious += 1

# Rule 4: Suspicious keywords
keywords = ["login", "secure", "verify", "bank"]
for word in keywords:
    if word in url.lower():
        print(f"Contains suspicious word: {word} ❌")
        suspicious += 1

# Final result
print("\n--- Result ---")
if suspicious >= 2:
    print("⚠️ This URL may be PHISHING")
else:
    print("✅ This URL seems SAFE")