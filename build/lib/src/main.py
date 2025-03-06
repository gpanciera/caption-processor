import argparse
import sys
from src.processor import process_captions

def main():
    parser = argparse.ArgumentParser(description='Process SMPTE Timecode-based Captions')
    parser.add_argument('input_file', help='Input file containing captions')
    parser.add_argument('output_file', help='Output file to write processed captions')
    
    args = parser.parse_args()
    
    try:
        process_captions(args.input_file, args.output_file)
        print(f"Successfully processed captions from {args.input_file} to {args.output_file}")
    except Exception as e:
        print(f"Error processing captions: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())