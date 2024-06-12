from flask import Flask, render_template, request
# flask is a framework used in python for web application development as a backend framework.
# support for working with regular expressions
import re

app = Flask(__name__)

# function to check the strength in terms of length, Uppercase & Lowercase letters, numeric characters, and special characters
def password_strength_checker(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    feedback = "Password Strength: "
    if strength_score == 5:
        feedback += "Very Strong"
    elif strength_score == 4:
        feedback += "Strong"
    elif strength_score == 3:
        feedback += "Moderate"
    elif strength_score == 2:
        feedback += "Weak"
    else:
        feedback += "Very Weak"

    if not length_criteria:
        feedback += "\n- Password should be at least 8 characters long."
    if not uppercase_criteria:
        feedback += "\n- Password should include at least one uppercase letter."
    if not lowercase_criteria:
        feedback += "\n- Password should include at least one lowercase letter."
    if not number_criteria:
        feedback += "\n- Password should include at least one number."
    if not special_char_criteria:
        feedback += "\n- Password should include at least one special character."

    return feedback

# flask framework to rout to html page for input and provide the output resp.
@app.route('/', methods=['GET', 'POST'])
def home():
    feedback = ''
    if request.method == 'POST':
        password = request.form['password']
        feedback = password_strength_checker(password)
    return render_template('index.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
