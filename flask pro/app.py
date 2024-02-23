from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/user', methods=['POST', 'GET'])
def user_page():
    if request.method == 'POST':
        name = request.form.get('name')
        branch = request.form.get('branch')
        date = request.form.get('date')
        place = request.form.get('place')
        reason = request.form.get('reason')
        address = request.form.get('address')
        return render_template('user_page.html',name=name,branch=branch,date=date, place=place, reason=reason, address=address)
   
@app.route('/admin', methods=['POST', 'GET'])
def admin_page():
    if request.method == 'POST':
        name = request.form.get('name')
        branch = request.form.get('branch')
        date = request.form.get('date')
        place = request.form.get('place')
        reason = request.form.get('reason')
        address = request.form.get('address')
        return render_template('admin.html', name=name, branch=branch, date=date, place=place, reason=reason, address=address)

    return render_template('admin.html')  
@app.route('/approve', methods=['POST'])
def approve_leave():
    return "Leave request approved."

@app.route('/reject', methods=['POST'])
def reject_leave():
    return "Leave request rejected."
   
    
if __name__ == '__main__':
    app.run(debug=True)

