from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route('/byte_length', methods=['POST'])
def get_byte_length():
    # Check if the request contains JSON data
    if request.is_json:
        # Get the JSON data
        data = request.get_json()
        
        # Extract the text from the JSON data
        text = data.get('text', '')
        
        # Calculate the byte length of the text
        byte_length = len(text.encode('utf-8'))
        
        # Return the byte length as JSON
        return jsonify({'byte_length': byte_length})
    else:
        # Return an error message if the request is not JSON
        return jsonify({'error': 'Invalid input, expected JSON with "text" field'}), 400

#if __name__ == '__main__':
#    app.run(debug=True)
