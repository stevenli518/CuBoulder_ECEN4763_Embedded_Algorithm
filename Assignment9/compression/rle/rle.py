"""This module is for the RLE."""


class RLE:
    """Class implementation for RLE."""

    def rle_encode(self, data):
        """Encode the given data with RLE encoding."""
        i = 0
        count = 1
        result = ''
        flag = True
        while i < len(data):
            while flag:
                if (i+1 < len(data)) and data[i] == data[i+1]:
                    count += 1
                    i += 1
                else:
                    flag = False
            if count > 1:
                result += (str(count) + data[i])
                count = 1
                flag = True
            else:
                result += data[i]
                flag = True
            i += 1
        return result

    def rle_decode(self, encoding):
        """Decode the input encoding with RLE decoding."""
        i = 0
        result = ''
        num = ''
        while i < len(encoding):
            while (i+1 < len(encoding)) and encoding[i].isnumeric():
                num += encoding[i]
                i += 1
            if encoding[i-1].isnumeric():
                result += (int(num) * encoding[i])
                num = ''
                i += 1
            else:
                result += encoding[i]
                i += 1
        return result
