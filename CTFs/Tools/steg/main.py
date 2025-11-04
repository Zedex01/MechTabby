from src.Steganography import Steganography
import argparse

def main():

    
    
    parser = argparse.ArgumentParser(description="Steganography decryption tool")


    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--analyze', action="store_true", help="Prints out the rgba of all pixels")
    group.add_argument('-rgba', '--rgba', action="store_true", help="Applies rgba steg algorithm")
    group.add_argument('-rgb', '--rgb', action="store_true", help="Applies rgb steg algorithm")

    parser.add_argument('-p', '--printable', "Only outputs printable text")
    
    parser.add_argument('image', help="path to the image")

    args = parser.parse_args()


    steg = Steganography(args.image)

    try: 

        if args.rgba:
            steg.set_rgba()
            steg.rgba()

        elif args.rgb:
            steg.set_rgba()
            steg.rgb()
            
            
        elif args.analyze:
            steg.set_rgba()

            data = steg.get_rgba()
            for pxl in data:
                print(pxl)

    except Exception as e:
        print(f"Err: {e}")
        exit()

    try:
        if args.p:
            print()

        else:
            print("".join(steg.get_ascii()))

    except Exception as e:
        print(f"Err: {e}")
        exit()

if __name__ == "__main__":
    main()
