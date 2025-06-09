import gooeypie as gp

# 读取常见密码文件并调试输出
def load_common_passwords(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            passwords = set(line.strip() for line in file)
            print(f"Loaded {len(passwords)} common passwords:", passwords)  # 调试输出
            return passwords
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return set()

# 加载密码列表
common_passwords = load_common_passwords("usual_password.txt")

def check_password_strength(event):
    password = password_input.text.strip()  # 确保输入密码去除空格
    password_length = len(password)  # 计算密码字数
    length_lbl.text = f"Password Length: {password_length} characters"  # 更新字数显示
    print(f"User entered password ({password_length} chars): {password}")  # 调试输出

    # **检查是否为常见密码**
    if password in common_passwords:
        print("Password found in common passwords!")  # 调试输出
        result_lbl.text = "⚠ This is a common password. Please choose a stronger one!"
        result_lbl.text_color = 'red'
        return  # 直接返回，不执行后续强度检查

    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    
    strength = 0
    if password_length >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):  
        strength += 1
    if any(char in special_chars for char in password):
        strength += 1

    # **更新密码强度提示**
    if strength == 5:
        result_lbl.text = "✔ Strong Password!"
        result_lbl.text_color = 'green'
        strength_lbl.text = "Strength Level: █████ (Strong)"
        strength_lbl.text_color = 'green'
    elif strength >= 3:
        result_lbl.text = "⚠ Medium Strength Password."
        result_lbl.text_color = 'orange'
        strength_lbl.text = "Strength Level: ████░ (Medium)"
        strength_lbl.text_color = 'orange'
    else:
        result_lbl.text = "✘ Weak Password! Use uppercase, lowercase, number & special characters."
        result_lbl.text_color = 'red'
        strength_lbl.text = "Strength Level: ██░░░ (Weak)"
        strength_lbl.text_color = 'red'

def toggle_password_visibility(event):
    password_input.secret = not password_input.secret  

# **创建应用窗口**
app = gp.GooeyPieApp("To Be PasswordX Strength Checker")

# **创建控件**
prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Textbox(app)
password_input.secret = True  
password_input.width = 30  
password_input.add_event_listener('change', check_password_strength)  # **监听输入变化**

submit_btn = gp.Button(app, "Check", check_password_strength)

length_lbl = gp.Label(app, "Password Length: 0 characters")  # **新增：密码字数显示**
result_lbl = gp.Label(app, "")
result_lbl.font = ('Arial', 12, 'bold')

strength_lbl = gp.Label(app, "Strength Level: █░░░░ (Very Weak)")

# **设置网格布局**
app.set_grid(6, 2)

# **添加控件到网格**
app.add(prompt_lbl, 1, 1)
app.add(password_input, 1, 2)
app.add(length_lbl, 2, 1, column_span=2)  # **新增：密码字数显示**
app.add(submit_btn, 3, 1, column_span=2)
app.add(strength_lbl, 4, 1, column_span=2)  
app.add(result_lbl, 5, 1, column_span=2)

# **运行应用**
app.run()




