from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Đọc user từ file
def load_users():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password
    except:
        pass
    return users

# Lưu user
def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = load_users()
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return "Đăng nhập thành công!"
        else:
            return "Sai tài khoản hoặc mật khẩu!"
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        save_user(username, password)
        return redirect("/login")

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
