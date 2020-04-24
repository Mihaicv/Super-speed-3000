from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    table_header=['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
    return render_template('list.html', user_stories=user_stories, table_header=table_header)

@app.route('/story', methods=['GET','POST'])
def ad_story():
    if request.method=='POST':
        user_story={
            'id': data_handler.generate_id(),
            'title':request.form.get("title"),
            'user_story': request.form.get('user_story'),
            'acceptance_criteria': request.form.get('acceptance_criteria'),
            'business_value':request.form.get('business_value'),
            'estimation':request.form.get('estimation'),
            'status':request.form.get('status')
        }
        data_handler.add_on_csv(user_story),
        return redirect('/list')
    return render_template('story.html')

@app.route('/story/<id>', methods=['GET','POST'])
def update_story(id):
    status=data_handler.STATUSES
    if request.method == 'GET':
        file_data=data_handler.get_all_user_story(id)
    if request.method=='POST':
        user_story = {
            'id': id,
            'title': request.form.get("title"),
            'user_story': request.form.get('user_story'),
            'acceptance_criteria': request.form.get('acceptance_criteria'),
            'business_value': request.form.get('business_value'),
            'estimation': request.form.get('estimation'),
            'status': request.form.get('status')
        }
        data_handler.update_on_csv( id, user_story)
        return redirect('/list')

    return render_template('update.html', id=id, data=file_data, status=status)









if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
