from src.Hex import Hex
import argparse, os

def main():

    hex = Hex()
    
    parser = argparse.ArgumentParser(description="Hex crypto tool")

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

            

            if args.encode:
                output_file = os.path.join(cwd, f"{name}_hex")
                hex.hex_from_file(args.file, output_file)

            if args.decode:
                output_file = os.path.join(cwd, f"{name}_ascii")
                print(output_file)
                hex.hex_to_file(args.file, output_file)

        else:
            cxt = args.content
        
            if args.encode:
                print(hex.hexify(cxt))

            elif args.decode:
                print(hex.de_hexify(cxt))

    except Exception as e:
        print(f"Err: {e}")
        exit()

if __name__ == "__main__":
    main()
