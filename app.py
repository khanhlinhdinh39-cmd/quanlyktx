from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'khanhlinh_secret' # Khóa bảo mật cho session

# Giả lập dữ liệu người dùng (Bạn có thể sửa lại cho khớp với users.txt)
users = {
    "admin1": {"password": "123", "role": "admin"},
    "manager1": {"password": "123", "role": "manager"},
    "sv001": {"password": "123", "role": "student"}
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username]["password"] == password:
            session['user'] = username
            role = users[username]["role"]
            return redirect(f"/{role}")
        return "Sai tài khoản hoặc mật khẩu!"
    return render_template("login.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/manager")
def manager():
    return render_template("manager.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
