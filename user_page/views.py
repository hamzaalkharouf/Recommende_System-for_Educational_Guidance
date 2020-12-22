from flask import render_template, Blueprint,request

user = Blueprint('user_page', __name__, template_folder='templates', static_folder='static', url_prefix='/user', static_url_path='/static')


def personal(item_personal):
    list_item_personal1=['item_personal1','item_personal2','item_personal3','item_personal4','item_personal5']
    list_personal=[]
    for row_list_item_personal1  in list_item_personal1:
        if row_list_item_personal1 in item_personal:
            list_personal.append(1)
        else :
            list_personal.append(0)
    return list_personal



@user.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item_personal=request.form.getlist('item_personal1')
        item_personal2=personal(item_personal)

        print(item_personal2)
        return render_template('home.html')
    else:
        return render_template('home.html')


    # item_personal22=request.form['item_personal2']
    # item_personal33=request.form['item_personal3']
    # item_personal44=request.form['item_personal4']
    # item_personal55=request.form['item_personal5']
    # print((item_personal11,item_personal22,item_personal33))
