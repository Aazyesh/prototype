from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Cryptographic Algorithm Identifier API"


@app.route('/identify', methods=['POST'])
def identify_algorithm():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Reading file content
    data = file.read().decode('utf-8')
    print(f"Raw data read from file: {data}")   # Debug

    # (TO BE IMPLEMENTED) Call the algorithm identification function
    algorithm, data_length = identify_cryptographic_algorithm(data)

    return jsonify({"algorithm": algorithm, "data_length": data_length})


def clean_data(data):
    return data.strip().replace('\n', '').replace('\r', '')


def ensure_even_length(hex_data):
    if len(hex_data) % 2 != 0:
        hex_data = '0' + hex_data
    return hex_data


def identify_cryptographic_algorithm(data):
    # Example logic

    cleaned_data = clean_data(data)
    cleaned_data = ensure_even_length(data)

    # hex to bytes
    try:
        decoded_data = bytes.fromhex(cleaned_data)
    except ValueError as e:
        return f'Error decoding hex data: {e}', None

    data_length = len(decoded_data)

    # DEBUG
    print(f'Clean data length: {data_length}')

    # hex_data = data.hex()

    # Rule based identification (Dummy example)
    if data_length % 16 == 0:     # AES contains 16 bytes (32 chars) block size
        return "AES", data_length
    elif data_length % 8 == 0:
        return "DES", data_length
    elif 128 <= data_length <= 512:    # RSA-2048
        return "RSA", data_length
    else:
        return "Unknown algorithm", data_length


if __name__ == "__main__":
    app.run(debug=True)

