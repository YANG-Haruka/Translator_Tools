from flask import Flask, request, jsonify
import os
import requests
from datetime import datetime
import json

app = Flask(__name__)


""""
openAI_API refer: https://platform.openai.com/docs/models/gpt-3-5
"""
OPENAI_API_KEY = 'QAQ'

def translate_text(input_text, source_language, target_language):
    """
    API relative
    """
    api_key = OPENAI_API_KEY

    prompt = f"Translate this text from {source_language} to {target_language}. "+ \
            'Please preserve escape characters like \\r\\n or \\" and strictly keep the JSON format of the provided content. ' + \
        'Please directly give the translated content only. ' +\
        'Here are the conversations:\n'+ input_text
    # print(prompt)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    """"
    you can change your model, please refer at https://platform.openai.com/docs/models/gpt-3-5
    """
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    try:
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.RequestException as e:
        print(f"API error: {e}")
        return "Translation failed"

"""

"""
def process_json_translation(input_data, translated_file_dir, batch_size=15):
    """
    handle the input
    """
    source_language = input_data['source_language']
    target_language = input_data['target_language']
    text = input_data['content']

    lines = text.split('\n')
    batches = ['\n'.join(lines[i:i + batch_size]) for i in range(0, len(lines), batch_size)]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output_data_list = []
    for batch in batches:
        translated_batch = translate_text(batch, source_language, target_language)
        output_data = {
            "timestamp":timestamp,
            "source_language": source_language,
            "target_language": target_language,
            "content": batch,
            "post_translation": translated_batch
        }
        output_data_list.append(output_data)

    translated_file_path = os.path.join(translated_file_dir, f"{timestamp}.json")

    with open(translated_file_path, 'w', encoding='utf-8') as f:
        json.dump(output_data_list, f, ensure_ascii=False, indent=4)
    
    return output_data_list


@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        translated_file_dir = 'translated_files'
        output_data_list = process_json_translation(data, translated_file_dir)
        return jsonify(output_data_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)