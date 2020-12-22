from flask import render_template, Blueprint,request,redirect

user = Blueprint('user_page', __name__, template_folder='templates', static_folder='static', url_prefix='/user', static_url_path='/static')


def personal(item,list_item):
    list_result=[]
    for row_list_item  in list_item:
        if row_list_item in item:
            list_result.append(1)
        else :
            list_result.append(0)
    return list_result

def personal_favourites(item_personal,item_favourites,item_book_favourit):
    list_item_personal1=['item_personal1','item_personal2','item_personal3','item_personal4','item_personal5']
    list_item_favourites=['Drawing','Learn_programming','calculation','Read_news','Art','Sports','Search_and_read','Writing_poetry','Interest_gardening','Repair_phones','Visit','Web_design','Graphic_design','Photography','Biology','chemistry']
    list_item_book_favourit=['Geography_and_history','Management','English_Language','Engineering_drawing','design','Electricity','Maths','physics','chemistry','Life_Sciences','Reading_and_rules','Islamic_education']


    item_personal2=personal(item_personal,list_item_personal1)
    list_item_favourites2=personal(item_favourites,list_item_favourites)
    list_item_book_favourit2=personal(item_book_favourit,list_item_book_favourit)

    return (item_personal2,list_item_favourites2,list_item_book_favourit2)

@user.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item_personal=request.form.getlist('item_personal1')
        item_favourites=request.form.getlist('favourites')
        item_book_favourites=request.form.getlist('book_favourites')

        (item_personal2,list_item_favourites2,item_book_favourites2)=personal_favourites(item_personal,item_favourites,item_book_favourites)
        print(item_personal2)
        print(list_item_favourites2)
        print(item_book_favourites2)

        return render_template('mark.html')
    else:
        return render_template('home.html')


@user.route('/mark', methods=['GET', 'POST'])
def mark():
    if request.method == "POST":
        string=request.form.getlist('checkbox_name')
        number=request.form.getlist('number_name')
        average2=request.form.get('average')
        branch2=request.form.get('branch')

        # (item_personal2,list_item_favourites2)=personal_favourites(item_personal,item_favourites)

        return render_template('result.html')
    else:
        return render_template('mark.html')



@user.route('/result')
def result():
    return render_template('result.html')
    # http://127.0.0.1:5000/user/result




    # item_personal22=request.form['item_personal2']
    # item_personal33=request.form['item_personal3']
    # item_personal44=request.form['item_personal4']
    # item_personal55=request.form['item_personal5']
    # print((item_personal11,item_personal22,item_personal33))
