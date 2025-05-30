import gooeypie as gp

def check_password_length(event):
    password = password_input.text
    if len(password) >= 8 and any(char.isdigit() for char in password):
        result_lbl.text = "√ Password is strong enough."
    elif len(password) < 8:
        result_lbl.text = "× Password doesn't match the rule——(min 8 characters)."
    else:
        result_lbl.text = "× Password is not strong enough."

# Create the app window
app = gp.GooeyPieApp("Password Length Checker")

# Create widgets
prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Textbox(app)
submit_btn = gp.Button(app, "Check", check_password_length)
result_lbl = gp.Label(app, "")  # Define result_lbl

# Set up a grid layout with 3 rows and 2 columns
app.set_grid(3, 2)

# Add widgets to the grid
app.add(prompt_lbl, 1, 1)
app.add(password_input, 1, 2)
app.add(submit_btn, 2, 1, column_span=2)
app.add(result_lbl, 3, 1, column_span=2)

# Run the application
app.run()
