import binascii

class Hex:
    def __init__(self):
        self.ctx = None
        self.hex = None
        
    def hexify(self, ctx=None):
        if ctx is not None:
            self.ctx = ctx

        #Ensure it is a bytes type object
        if not isinstance(self.ctx, bytes):
            self.ctx = (self.ctx).encode("utf-8")

        self.hex = binascii.hexlify(self.ctx).decode("utf-8")
        return self.hex

    def de_hexify(self, hex=None):
        if hex is not None:
            self.hex = hex

        #Clean all whitespace
        self.hex =  "".join(self.hex.split())

        self.ctx = binascii.unhexlify(self.hex).decode("utf-8")
        return self.ctx


    def hex_from_file(self, file_in, file_out):
        with open(file_in, 'rb') as f:
            self.ctx = f.read()

        #Change to bytes
        if not isinstance(self.ctx, bytes):
            self.ctx = (self.ctx).encode("utf-8")

        #change to hex:
        self.hex = binascii.hexlify(self.ctx).decode("utf-8")

        with open(file_out, 'w') as f:
            f.write(self.hex)

    def hex_to_file(self, file_in, file_out):
        with open(file_in, 'r') as f:
            self.hex = f.read()
        
        #Clear all whitespace
        self.hex = "".join(self.hex.split())

        #Change to ascii
        self.ctx = binascii.unhexlify(self.hex)

        with open(file_out, 'wb') as f:
            f.write(self.ctx)
    