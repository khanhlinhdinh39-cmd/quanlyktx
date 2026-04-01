from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
# Khóa bí mật để quản lý phiên đăng nhập (session)
app.secret_key = 'quanlyktx_secret_key_123'

# Dữ liệu tài khoản mẫu khớp với sơ đồ chức năng của bạn
users = {
    "admin1": {"password": "123", "role": "admin"},
    "manager1": {"password": "123", "role": "manager"},
    "sv001": {"password": "123", "role": "student"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Kiểm tra tài khoản trong danh sách
        if username in users and users[username]['password'] == password:
            session['user'] = username
            session['role'] = users[username]['role']
            
            # Điều hướng dựa trên quyền hạn (role)
            if session['role'] == 'admin':
                return redirect(url_for('admin'))
            elif session['role'] == 'manager':
                return redirect(url_for('manager'))
            elif session['role'] == 'student':
                return redirect(url_for('student'))
        
        return "Sai tài khoản hoặc mật khẩu. Vui lòng thử lại!"
    
    return render_template('login.html')

@app.route('/admin')
def admin():
    if 'role' in session and session['role'] == 'admin':
        return render_template('admin.html')
    return redirect(url_for('login'))

@app.route('/manager')
def manager():
    if 'role' in session and session['role'] == 'manager':
        return render_template('manager.html')
    return redirect(url_for('login'))

@app.route('/student')
def student():
    if 'role' in session and session['role'] == 'student':
        return render_template('student.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Chạy ứng dụng
    app.run(debug=True)
