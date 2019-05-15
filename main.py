import pickle
import json
from flask import Flask, request, Response

app = Flask(__name__)  


def get_all_users(): # GET
    print(request.args)   
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)  
    js = json.dumps(data_new)  
    pickle_in.close()
    return Response(js, status=200, mimetype='application/json')


def create_user(): # POST
    data = request.data
    data = json.loads(request.data)  
    data = request.args
    
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)   
    data_new['name'] = data['name']
    data_new['age'] = data['age']

    pickle_out = open('data.pickle', 'wb')
    pickle.dump(data_new, pickle_out)    
    pickle_out.close()
    return Response('{"Success": "ok"}', status=200, mimetype='application/json')



def update_user(): # PATCH
    data = request.data
    if 'name' not in data or 'age' not in data:
        return Response('{"status": "error", "error": "Bad request"}', status=400, mimetype='application/json')

    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)

    [{'id': 1, 'name': '123'}, {'id': 1, 'name': '321'}]

    for user in data_new:
        if user['id'] == data['id']:
            user['name'] = data['name']
            user['...'] = data['...']

    pickle_in.close()
    return Response('{"status": "ok"}', status=200, mimetype='application/json')



@app.route('/users/', methods=['GET', 'POST'])
@app.route('/users/<id>', methods=['GET', 'POST', 'PATCH'])
def users(*args, **kwargs):

    if request.method == 'GET':
        return get_all_users()

    elif request.method == 'POST':
        return create_user()

    elif request.method == 'PATCH':
        return update_user()

    else:
        pass


if __name__ == '__main__':
    app.run(port=80)