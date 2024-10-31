import os, azureopenai, config
from flask import Flask, render_template, session, url_for, jsonify, request, send_from_directory

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'BAD_SECRET_KEY'


mysession ={}

@app.route('/')
def index():
    mode = request.args.get('mode')
    if mode == None:
        mode = "gpt"
    mysession['chathistory'] = [{
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": config.system_prompt
            }
        ]
    }]
    print(mysession['chathistory'])
    return render_template('index.html', mode=mode, speech_key=config.speech_key, speech_region=config.speech_region, speech_language=config.speech_language, speech_voice=config.speech_voice)  


@app.route('/generate', methods=['POST'])
def generate_response():
	data = request.get_json()
	message_input = data['text']
	mysession['chathistory'].append(
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": message_input
            }
        ]
        }
    )
	response = azureopenai.get_openai_response(mysession['chathistory'])
	return jsonify(response)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

