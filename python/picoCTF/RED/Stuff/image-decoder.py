from PIL import Image

#picCTF{Flag} is hidden in the image using LSB of steagongraphy



#open the image file:
try:
    img = Image.open(r'C:\Users\mmoran\Projects\Git-Repos\MechTabby\python\picoCTF\RED\Provided\red.png')
except Exception as e:
    print(f"ERR: {e}")
    exit()

#Convert image to RGB
if img.mode != 'RGBA':
    img = img.convert('RGBA')

#get dim of image
width, height = img.size
print(f"Image Size: {width}x{height}")

index = 0
output = []

for y in range(height):
    for x in range(width):
        #print(f"========= Y Row: {y} ==========")
        #print(f"X col: {x}")
        r, g, b, a = img.getpixel((x, y))
        r = f'{r:08b}'
        g = f'{g:08b}'
        b = f'{b:08b}'
        a = f'{a:08b}'
        print(f'{r}, {g}, {b}, {a}')

        #Write out the least signifigant byte of each
        #print(f"LSB: {r[-1]}, {g[-1]}, {b[-1]}")
        
        #Store the correct bit to output:
        #match index:
        #    case 0:
        #        output.append(r[-1])
        #        index += 1
        #    case 1:
        #        output.append(g[-1])
        #        index += 1
        #    case 2:
        #        output.append(b[-1])
        #        index +=1
        #    case 3:
        #       output.append(a[-1])
        #       index=0
        #    case _:
        #        print("Index Error")
        #        exit()
        output.append(r[-1])
        #output.append(g[-1])
        #output.append(b[-1])
        #output.append(a[-1])
    

output = "".join(output)
print(output)
#Split back into groups of 8 digits:

print(len(output))
group_size = 8

bytes = int(len(output)/group_size)

data = []

for byte in range(bytes):
    val = []
    for bit in output[(1*byte):(1*byte + group_size)]: #Reads 8 Bits
        val.append(bit)
    val = "".join(val)
    data.append(val)
#print(data)

#for val in data:
    #print(f"{int(val,2)}")

for val in data:
    try:
        print(f"Binary: {val} | Decimal: {int(val,2)} | Char: {chr(int(val,2))}")
    except Exception as e:
        pass



