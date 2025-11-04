import base64

class Base64:
    def __init__(self, data=None):
        self.data = None

        if data is not None:
            self.data = str(data)

        self.decoded_data = None
        self.encoded_data = None

    def decode(self, data=None):
        if data is not None:
            self.data = data
        decoded_bytes = base64.b64decode(self.data)
        self.decoded_data = decoded_bytes.decode('utf-8', errors='ignore')
        return self.decoded_data

    def encode(self, data=None):
        if data is not None:
            self.data = data
        encoded_bytes = self.data.encode("utf-8")
        self.encoded_data = base64.b64encode(encoded_bytes).decode("utf-8")
        return self.encoded_data

    def decode_file(self, file_in, file_out):
        with open(file_in, 'rb') as f:
            b64data = f.read()
        decoded = base64.b64decode(b64data)
        with open(file_out, 'wb') as f:
            f.write(decoded)


#getters & setters
    
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_encoded_data(self):
        return self.encoded_data

    def get_decoded_data(self):
        return self.decoded_data


