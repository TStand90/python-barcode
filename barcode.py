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

    def __init__(self, data_string, height=60, ratio=2, border=10):
        self.data = self.encode(data_string)
        self.data_string = data_string
        self.height = height * ratio
        self.ratio = ratio
        self.border = border
        self.image = self.draw()

    def encode(self, barcode_string):
        encoded_string = '100101101101'			# Start code

        for char in barcode_string:
            encoded_string += self.CODE39[char.upper()]

        encoded_string += '100101101101'		# End code

        return encoded_string

    def decode(barcode_string):
        decoded_string = ''

        for char in barcode_string:
            # Need to find an 'invert method'
            # decoded_string += self.CODE128
            pass

        return decoded_string

    def draw(self):
        width = (self.border * 2) + len(self.data) * self.ratio

        img = Image.new("RGB", (width, self.height), "white")

        draw = ImageDraw.Draw(img)

        x = 10

        for char in self.data:
            if char == '1':
                draw.line((x, 10, x, self.height-30), "black",
                          width=self.ratio)
            x += self.ratio

        draw.text((20, self.height-20), self.data_string, (0, 0, 0))
        del draw

        return img

    def save(self):
        self.image.save(self.data_string + ".png")


class Code128:
    CODE128 = {
        0: '11011001100', 1: '11001101100', 2: '11001100110',
        3: '10010011000', 4: '10010001100', 5: '10001001100',
        6: '10011001000', 7: '10011000100', 8: '10001100100',
        9: '11001001000', 10: '11001000100', 11: '11000100100',
        12: '10110011100', 13: '10011011100', 14: '10011001110',
        15: '10111001100', 16: '10011101100', 17: '10011100110',
        18: '11001110010', 19: '11001011100', 20: '11001001110',
        21: '11011100100', 22: '11001110100', 23: '11101101110',
        24: '11101001100', 25: '11100101100', 26: '11100100110',
        27: '11101100100', 28: '11100110100', 29: '11100110010',
        30: '11011011000', 31: '11011000110', 32: '11000110110',
        33: '10100011000', 34: '10001011000', 35: '10001000110',
        36: '10110001000', 37: '10001101000', 38: '10001100010',
        39: '11010001000', 40: '11000101000', 41: '11000100010',
        42: '10110111000', 43: '10110001110', 44: '10001101110',
        45: '10111011000', 46: '10111000110', 47: '10001110110',
        48: '11101110110', 49: '11010001110', 50: '11000101110',
        51: '11011101000', 52: '11011100010', 53: '11011101110',
        54: '11101011000', 55: '11101000110', 56: '11100010110',
        57: '11101101000', 58: '11101100010', 59: '11100011010',
        60: '11101111010', 61: '11001000010', 62: '11110001010',
        63: '10100110000', 64: '10100001100', 65: '10010110000',
        66: '10010000110', 67: '10000101100', 68: '10000100110',
        69: '10110010000', 70: '10110000100', 71: '10011010000',
        72: '10011000010', 73: '10000110100', 74: '10000110010',
        75: '11000010010', 76: '11001010000', 77: '11110111010',
        78: '11000010100', 79: '10001111010', 80: '10100111100',
        81: '10010111100', 82: '10010011110', 83: '10111100100',
        84: '10011110100', 85: '10011110010', 86: '11110100100',
        87: '11110010100', 88: '11110010010', 89: '11011011110',
        90: '11011110110', 91: '11110110110', 92: '10101111000',
        93: '10100011110', 94: '10001011110', 95: '10111101000',
        96: '10111100010', 97: '11110101000', 98: '11110100010',
        99: '10111011110', 100: '10111101110', 101: '11101011110',
        102: '11110101110', 103: '11010000100', 104: '11010010000',
        105: '11010011100', 106: '1100011101011'
    }

    MAP_B = {
        ' ': 0, '!': 1, '"': 2, '#': 3, '$': 4, '%': 5, '&': 6,
        "'": 7, '(': 8, ')': 9, '*': 10, '+': 11, ',': 12, '-': 13,
        '.': 14, '/': 15, '0': 16, '1': 17, '2': 18, '3': 19,
        '4': 20, '5': 21, '6': 22, '7': 23, '8': 24, '9': 25,
        ':': 26, ';': 27, '<': 28, '=': 29, '>': 30, '?': 31,
        '@': 32, 'A': 33, 'B': 34, 'C': 35, 'D': 36, 'E': 37,
        'F': 38, 'G': 39, 'H': 40, 'I': 41, 'J': 42, 'K': 43,
        'L': 44, 'M': 45, 'N': 46, 'O': 47, 'P': 48, 'Q': 49,
        'R': 50, 'S': 51, 'T': 52, 'U': 53, 'V': 54, 'W': 55,
        'X': 56, 'Y': 57, 'Z': 58, '[': 59, '\\': 60, ']': 61,
        '^': 62, '_': 63, '`': 64, 'a': 65, 'b': 66, 'c': 67,
        'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73,
        'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79,
        'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85,
        'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90, '{': 91,
        '|': 92, '}': 93, '~': 94
    }

    def __init__(self, data_string, height=60, ratio=2, border=10):
        self.data = self.encode(data_string)
        self.data_string = data_string
        self.height = height * ratio
        self.ratio = ratio
        self.border = border
        self.image = self.draw()

    def encode(self, barcode_string):
        x = 1
        checksum = 104
        encoded_string = self.CODE128[104]     # Start code

        for char in barcode_string:
            encoded_string += self.CODE128[self.MAP_B[char]]
            checksum += (self.MAP_B[char] * x)
            x += 1

        encoded_string += self.CODE128[checksum % 103]
        encoded_string += self.CODE128[106]    # End code

        return encoded_string

    def decode(barcode_string):
        decoded_string = ''

        for char in barcode_string:
            # Need to find an 'invert method'
            # decoded_string += self.CODE128
            pass

        return decoded_string

    def draw(self):
        width = (self.border * 2) + len(self.data) * self.ratio

        img = Image.new("RGB", (width, self.height), "white")

        draw = ImageDraw.Draw(img)

        x = 10

        for char in self.data:
            if char == '1':
                draw.line((x, 10, x, self.height-30), "black",
                          width=self.ratio)
            x += self.ratio

        draw.text((20, self.height-20), self.data_string, (0, 0, 0))
        del draw

        return img

    def save(self):
        self.image.save(self.data_string + ".png")


def readInputFile(inputFile):
    with open(inputFile, 'r') as barcodeFile:
        for line in barcodeFile.read().splitlines():
            barcode_data = line
            barcode = Code39(barcode_data)
            barcode.save()


def readInputFileWithEncoding(inputFile, encoding):
    with open(inputFile, 'r') as barcodeFile:
        for line in barcodeFile.read().splitlines():
            barcode_data = line
            if encoding == 'Code39':
                barcode = Code39(barcode_data)
                barcode.save()
            elif encoding == 'Code128':
                barcode = Code128(barcode_data)
                barcode.save()


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
