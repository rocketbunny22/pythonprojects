import bcrypt

max_attempts = 3
attempts = 0
user_database = {'user1': bcrypt.hashpw('password1'.encode('utf-8'), bcrypt.gensalt()),
                 'user2': bcrypt.hashpw('password2'.encode('utf-8'), bcrypt.gensalt())}
while attempts < max_attempts:
 username = input("Enter your username:")
 password = input("Enter your password:")
 hashed_passwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  
 if username in user_database and bcrypt.checkpw(password.encode('utf-8'), user_database[username] == password:
    print("Login successful! Welcome, " + username + "!")
    break
 else:
    print("Invalid credentials. Accesss denied.")
    attempts += 1
else:
    print("Max login attempts reached. Account locked.")    
   
