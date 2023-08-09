"""This module is for the Hybrid Compression."""


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


class BWT:
    """Class implementation for BWT."""

    def bw_transform(self, data):
        """Encode the given data with BWT encoding."""
        str_in = '^' + data + '|'
        str_list = []
        result = ''
        for _ in range(len(str_in)):
            str_in = str_in[1:] + str_in[0]
            str_list.extend([str_in])
        str_list.sort()
        for _, mystr in enumerate(str_list):
            result += mystr[-1]
        return result

    def bw_inv_transform(self, encoding):
        """Decode the input encoding with BWT decoding."""
        enc_len = len(encoding)
        decoding = [''] * enc_len
        answer = ''
        for _ in range(enc_len):
            for i in range(enc_len):
                decoding[i] = encoding[i] + decoding[i]
            decoding.sort(key=lambda x: x[0])
        answer = [x for x in decoding if x[0] == '^' and x[-1] == '|']
        mystr = answer[0]
        mystr = mystr[1:len(mystr)-1]
        return mystr


class Hybrid:
    """Class implementation for Hybrid."""

    def hybrid_encode(self, data):
        """Encode the given data with Hybrid encoding."""
        bwt = BWT()
        rle = RLE()
        encoding_bwt = bwt.bw_transform(data)
        encoding_rle = rle.rle_encode(encoding_bwt)
        return encoding_rle

    def hybrid_decode(self, encoding):
        """Decode the input encoding with Hybrid decoding."""
        bwt = BWT()
        rle = RLE()
        decoding_rle = rle.rle_decode(encoding)
        decoding_bwt = bwt.bw_inv_transform(decoding_rle)
        return decoding_bwt
