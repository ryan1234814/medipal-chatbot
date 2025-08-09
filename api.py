
from flask import Flask, request, jsonify, send_from_directory, Response
from chatbot import get_response
from db import get_medicine_info
import os
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"message": "MediPal Flask backend is running."})
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/medicine_info',methods=['POST'])
def medicine_info():
    medicine_name=request.json.get('medicine_name')
    info=get_medicine_info(medicine_name)
    return jsonify({'info': info})

@app.route('/favicon.ico')
def favicon():
    favicon_path = os.path.join(app.root_path, 'static', 'favicon.ico')
    if os.path.exists(favicon_path):
        return send_from_directory(
            os.path.join(app.root_path, 'static'),
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )
    else:
        # Return 204 No Content if favicon does not exist
        from flask import Response
        return Response(status=204)



if __name__ == '__main__':
    app.run(debug=False)
