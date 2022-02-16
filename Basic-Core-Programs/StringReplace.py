txt = "Hello <<Username>>,How are you?"
username = input("Enter Your Name:")
if len(username) > 3:
    new_text = txt.replace("<<Username>>", username)
    print(new_text)
else:
    print("Enter Username of more than 3 characters")
