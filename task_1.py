from hashlib import sha256

def Login (username,password):
    with open("userdata.txt","r") as f:
        hash=hashing(password)
        for line in f.readlines():
            data=line.split(",")
            if data[0]==username and data[1]==hash :
                print("Login successful!")
                return
    print("Login failed")       
        
def Register(username,password):
    with open("userdata.txt","a") as f:
        hash=hashing(password)
        f.write(f"{username},{hash}")
        print("Registration successful!")

def hashing(password):
    return sha256(password.encode('utf-8')).hexdigest()
        


while True:
    print("1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        Register(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        Login(username, password)
    elif choice == '3':
        break
    else:
        print("Invalid choice!")