from src.Crypto import Base64
import argparse, os

def main():



    b64 = Base64()
    
    parser = argparse.ArgumentParser(description="Base64 crypto tool")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decode', action="store_true", help="decodes the given content using base64")
    group.add_argument('-e', '--encode', action="store_true", help="encodes the given content to base64")
    
    parser.add_argument('-f', '--file')

    parser.add_argument('content', nargs="?", help="The message or content")

    args = parser.parse_args()



    try: 
        if args.file:

            cwd = os.getcwd()  # working directory where the program is run
            base_name = os.path.basename(args.file)
            name, ext = os.path.splitext(base_name)

            output_file = os.path.join(cwd, f"{name}_decoded.txt")

            if args.decode:
                b64.decode_file(args.file, output_file)

        else:
            cxt = args.content
        
            if args.encode:
                print(b64.encode(cxt))

            elif args.decode:
                print(b64.decode(cxt))

    except Exception as e:
        print(f"Err: {e}")
        exit()

if __name__ == "__main__":
    main()
