from PIL import Image

class Steganography():
    def __init__(self, image_path=None):
        if image_path is not None:
            print("Setting Path on creation")
            self.set_image(image_path)
        else:
            self.image_width = None
            self.image_height = None
            self.image = None
        self.rgba_data = None
        self.rosl = None
        self.bytes = None
        self.ascii = None
        self.dec = None

#Functions & Methods:
    def red_only_single_lsb(self):

        #reset list
        self.rosl = []

        for val in self.rgba_data:
            #val contains the rgba data for the pixel, val[0] is the red data, [-1] is the lsb of said value
            red_lsb = val[0][-1]
            self.rosl.append(red_lsb)
        
        #print("".join(self.rosl))
        
        self._seperate_bits("".join(self.rosl))

        self.bin_to_ascii(self.bytes)
        self.bin_to_dec(self.bytes)


    def rgba(self):
        self.rgba_ctx = []
        #For each value in in the rgba data
        for val in self.rgba_data:
            for index in range(4):
                bit = val[index][-1] 
                self.rgba_ctx.append(bit)

        self._seperate_bits("".join(self.rgba_ctx))

        self.bin_to_ascii(self.bytes)


    def rgb(self):
        self.rgb_ctx = []
        #For each value in in the rgba data
        for val in self.rgba_data:
            for index in range(3):
                bit = val[index][-1] 
                self.rgb_ctx.append(bit)
        self._seperate_bits("".join(self.rgb_ctx))
        self.bin_to_ascii(self.bytes)
        

    def _seperate_bits(self, bits: str):
        self.bytes = []
        for i in range(0, len(bits),8):
            byte = []
            for bit in range(i,i+8):
                byte.append(bits[bit])
            byte = "".join(byte)
            self.bytes.append(byte)

    def get_bytes(self):
        return self.bytes
    
    def bin_to_ascii(self, list_of_bytes: list):
        self.ascii = []
        for byte in list_of_bytes:
            self.ascii.append(chr(int(byte,2)))

    def bin_to_dec(self, list_of_bytes: list):
        self.dec = []
        for byte in list_of_bytes:
            self.dec.append(int(byte,2))

    def output_printable(self):
        message = ""
        for char in self.ascii:
            if char.isprintable():
                message += char

        print(message)



        

#Getters & Setters:
    def  get_dec(self):
        return self.dec

    def get_ascii(self):
        return self.ascii
    
    def get_image(self):
        return self.image
    
    def set_image(self, image_path):
        try:
            #Create image item
            self.image = Image.open(image_path)
            #Store size of image
            self.image_width, self.image_height = self.image.size

        except FileNotFoundError:
            print("File Not Found!")

    def set_rgba(self):
        #Reset Data List
        self.rgba_data = []

        #Convert image to RGB
        if self.image.mode != 'RGBA':
            self.image = self.image.convert('RGBA')

        #itterate through all pixels
        for y in range(self.image_height):
            for x in range(self.image_width):
                
                #Get the RBGA values for a given pixel
                r, g, b, a = self.image.getpixel((x, y))
                
                r = f'{r:08b}'
                g = f'{g:08b}'
                b = f'{b:08b}'
                a = f'{a:08b}'

                #Appends a list
                self.rgba_data.append([r, g, b, a])

    def get_rgba(self):
        return self.rgba_data

