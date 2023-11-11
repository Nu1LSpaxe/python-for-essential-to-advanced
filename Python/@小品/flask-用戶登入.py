from flask import Flask, request, make_response
import csv

app = Flask(__name__)

from flask import request
from flask import render_template

# 紀錄user.csv的使用者
users = {}

# 讀取user.csv建立users表單
def build_user(filename):
    file = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        users['user'+row[0]] = {'password': row[1], 'name': row[2], 'email': row[3]}
    
    return True


# 驗證登入函式
def valid_login(user, email, passwd):
    # 檢查使用者名稱和密碼是否有效
    for i in range(1, len(users)):
        id = users['user'+str(i)]
        print(id['name'], id['email'], id['password'])
        if user == id['name'] and email == id['email'] and passwd == id['password']:
            return True
    return False

# 使用者登入函式
def log_the_user_in(user):
    # 回傳登入成功訊息
    return user + " 登入成功"

@app.route('/login', methods=['POST', 'GET'])
#實作/login 可以吃POST、GET Method，login.html，若驗證成功顯示歡迎訊息
def login():
    error = None
    if request.method == 'POST':
        # POST method 會從form 進來
        # URL 從args 進來
        name = request.form['username']
        email = request.form['email']
        passwd = request.form['password']
        if valid_login(name, email, passwd):
            response = make_response(log_the_user_in(name))
            # response = log_the_user_in(name)
            # response.set_cookie('name', str(name))
            return response
        else:
            error = 'User not found, check if info is wrong. Please try again.'

    if request.cookies.get('name'):
        return "已經登入了"
        
    # 若為 GET 請求或登入驗證失敗，回傳登入頁面並傳遞錯誤訊息
    return render_template('login.html', error=error)


if __name__ == '__main__':
    try:
        build_user('users.csv')
    except Exception as e:
        print(e)
    else:
        app.run(debug=True)
