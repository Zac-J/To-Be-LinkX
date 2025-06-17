import gooeypie as gp
import pygame
from PIL import Image

# 初始化 pygame 音频模块
pygame.mixer.init()

# **定义图片路径**
default_bg = "背景_resized.png"  # 默认背景图片
strong_bg = "strong_password.png"  # 强密码对应的背景
medium_bg = "medium.png"
weak_bg = "weak.png"
# **调整默认背景图片尺寸**
image = Image.open("背景.png")  
image = image.resize((400, 300))  
image.save(default_bg)  # 保存调整后的默认背景

# 读取常见密码文件
def load_common_passwords(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return set()

# 加载密码列表
common_passwords = load_common_passwords("usual_password.txt")

def check_password_strength(event):
    password = password_input.text.strip()
    password_length = len(password)

    length_lbl.text = f"Password Length: {password_length} characters"

    if not password:
        result_lbl.text = "✘ Password cannot be empty!"
        result_lbl.text_color = 'red'
        return

    if password in common_passwords:
        result_lbl.text = "⚠ This is a common password. Please choose a stronger one!"
        result_lbl.text_color = 'red'
        return

    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    strength = sum([
        password_length >= 8,
        any(char.isdigit() for char in password),
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char in special_chars for char in password)
    ])

    # **根据强度切换背景图片**
    if strength == 5:
        result_lbl.text = "✔ Strong Password!"
        strength_lbl.text = "Strength Level: █████ (Strong)"
        result_lbl.text_color = 'green'
        bg_image.image = strong_bg  # **修改背景图片**
    elif strength >= 3:
        result_lbl.text = "⚠ Medium Strength Password."
        strength_lbl.text = "Strength Level: ████░ (Medium)"
        result_lbl.text_color = 'orange'
        bg_image.image = medium_bg  # **恢复medium背景**
    else:
        result_lbl.text = "✘ WEAK and USUAL Password! Use uppercase, lowercase, number & special characters."
        strength_lbl.text = "Strength Level: ██░░░ (Weak)"
        result_lbl.text_color = 'red'
        bg_image.image = weak_bg  # **恢复weak and usual背景**

def play_music(event):
    try:
        pygame.mixer.music.load("Speed Of Light.mp3")  
        pygame.mixer.music.play()
    except pygame.error:
        print("Error: Unable to play music. Check the file path.")

def stop_music(event):
    pygame.mixer.music.stop()

# **创建应用窗口**
app = gp.GooeyPieApp("To Be PasswordX——Strength Checker")

# **设置网格布局**
app.set_grid(8, 2)  

# **初始化背景图片**
bg_image = gp.Image(app, default_bg)  # 默认背景图片
app.add(bg_image, 1, 1, column_span=2)  
# **创建控件**
prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Textbox(app)
password_input.secret = True  
password_input.width = 30  

submit_btn = gp.Button(app, "Check", check_password_strength)
play_btn = gp.Button(app, "Play BGM", play_music)
stop_btn = gp.Button(app, "Stop BGM", stop_music)

length_lbl = gp.Label(app, "Password Length: 0 characters")
result_lbl = gp.Label(app, "")
result_lbl.font = ('Arial', 12, 'bold')

strength_lbl = gp.Label(app, "Strength Level: █░░░░ (Very Weak)")

# **添加控件**
app.add(prompt_lbl, 2, 1)
app.add(password_input, 2, 2)
app.add(length_lbl, 3, 1, column_span=2)
app.add(submit_btn, 4, 1, column_span=2)
app.add(strength_lbl, 5, 1, column_span=2)
app.add(result_lbl, 6, 1, column_span=2)
app.add(play_btn, 7, 1)
app.add(stop_btn, 7, 2)

# **运行应用**
app.run()



