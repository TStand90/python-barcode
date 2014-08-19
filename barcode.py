from PIL import Image, ImageDraw
import argparse


class Code39:
    CODE39 = {
        '0': '101001101101', '1': '110100101011', '2': '101100101011',
        '3': '110110010101', '4': '101001101011', '5': '110100110101',
        '6': '101100110101', '7': '101001011011', '8': '110100101101',
        '9': '101100101101', 'A': '110101001011', 'B': '101101001011',
        'C': '110110100101', 'D': '101011001011', 'E': '110101100101',
        'F': '101101100101', 'G': '101010011011', 'H': '110101001101',
        'I': '101101001101', 'J': '101011001101', 'K': '110101010011',
        'L': '101101010011', 'M': '110110101001', 'N': '101011010011',
        'O': '110101101001', 'P': '101101101001', 'Q': '101010110011',
        'R': '110101011001', 'S': '101101011001', 'T': '101011011001',
        'U': '110010101011', 'V': '100110101011', 'W': '110011010101',
        'X': '100101101011', 'Y': '110010110101', 'Z': '100110110101',
        '-': '100101011011', '.': '110010101101', ' ': '100110101101',
        '$': '100100100101', '/': '100100101001', '+': '100101001001',
        '%': '101001001001', '*': '100101101101'
    }

    def __init__(self, data_string, height=100, ratio=2, border=10):
        self.data = self.encode(data_string)
        self.data_string = data_string
        self.height = height
        self.ratio = ratio
        self.border = border

    def createBarcode(self):
        width = (self.border * 2) + (len(self.data) + (len(self.data) // 12)) * self.ratio

        img = Image.new("RGB", (width, self.height), "white")

        draw = ImageDraw.Draw(img)

        x = 10

        print(self.data)

        for char in self.data:
            if char == '1':
                draw.line((x, 10, x, self.height-30), "black", width=self.ratio)
            x += self.ratio

        draw.text((20, self.height-20), self.data_string, (0, 0, 0))
        del draw

        # write to stdout
        img.save(self.data_string + ".png")

    def encode(self, barcode_string):
        encoded_string = '100101101101'			# Start code

        for char in barcode_string:
            encoded_string += self.CODE39[char.upper()]

        encoded_string += '100101101101'		# End code

        return encoded_string


def readInputFile(inputFile):
    with open(inputFile, 'r') as barcodeFile:
        for line in barcodeFile.read().splitlines():
            barcode_data = line
            barcode = Code39(barcode_data)
            barcode.createBarcode()


def readInputFileWithEncoding(inputFile, encoding):
    with open(inputFile, 'r') as barcodeFile:
        for line in barcodeFile.read().splitlines():
            barcode_data = line
            if encoding == 'Code39':
                barcode = Code39(barcode_data)
                barcode.createBarcode()


def main():
    # Set up our argument parser to accept arguments like 'celsius' and 'sun'
    parser = argparse.ArgumentParser(description='Get the weather')
    parser.add_argument("-e", "--encoding",
                        help="""Select a barcode encoding, values are:
                        Code39""")
    parser.add_argument("-w", "--width",
                        help="Enter a custom width for bars")
    parser.add_argument("-t", "--text",
                        help="Enter custom text for barcode")
    parser.add_argument("-f", "--file",
                        help="Input file")
    parser.add_argument("-c", "--compress",
                        help="Flag for compressing image to minimum",
                        action="store_true")
    args = parser.parse_args()

    if args.file:
        if args.encoding:
            readInputFileWithEncoding(args.file, args.encoding)
        else:
            readInputFile(args.file)


if __name__ == '__main__':
    main()
