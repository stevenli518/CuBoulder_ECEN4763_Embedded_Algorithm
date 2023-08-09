"""This module is for the LZSS."""
# pylint: disable = R0915


class LZSS:
    """Class implementation for LZSS."""

    def lzss_encode(self, data):
        """Encode the given data with LZSS encoding."""
        i = 0
        # buffer
        buffer = data
        # prefix
        prefix = ''
        # index of the first appearance of substring
        index = 0
        # match string
        flag = True
        substring = ''
        sub_len = 0
        output = ''
        str_len = ''
        str_idx = ''
        while buffer != '':
            # Find the first occurrence.
            if buffer[0] not in prefix:
                output += buffer[0]
                prefix += buffer[0]
                buffer = buffer[1:]
                i += 1
            else:
                j = 0
                tempprefix = prefix
                while flag:
                    # Try next char
                    # index of starting point
                    if j < len(buffer):
                        substring += buffer[j]
                    else:
                        flag = False
                        substring = substring[: len(substring)]
                        index = data.index(substring)
                        str_len = str(sub_len)
                        str_idx = str(index)
                        break
                    if (j > len(buffer)-1) or substring not in tempprefix:
                        flag = False
                        substring = substring[: len(substring)-1]
                        index = data.index(substring)
                        str_len = str(sub_len)
                        str_idx = str(index)
                        break
                    j += 1
                    sub_len += 1
                    tempprefix += buffer[j-1]
                if flag is False and (len(substring) >= (len('(' + str_idx + ',' + str_len + ')'))):
                    output += '(' + str_idx + ',' + str_len + ')'
                    prefix += substring
                    buffer = buffer[sub_len:]
                    i += sub_len
                    flag = True
                    substring = ''
                    sub_len = 0
                else:
                    output += buffer[0]
                    prefix += buffer[0]
                    buffer = buffer[1:]
                    i += 1
                    flag = True
                    substring = ''
                    sub_len = 0
        return output

    def lzss_decode(self, encoding):
        """Decode the input encoding with LZSS decoding."""
        i = 0
        output = ''
        count = 0
        length = 0
        offset = 0
        lenofencoding = len(encoding)
        while i < lenofencoding:
            j = i
            comma = 0
            if encoding[j] == '(':
                while encoding[j] != ')':
                    if encoding[j] == ',':
                        comma = j
                        j += 1
                    else:
                        j += 1
                offset = int(encoding[i+1:comma])
                length = int(encoding[comma+1:j])
                while count < length:
                    output += output[offset+count]
                    count += 1
                if count >= length:
                    i += 3 + len(str(offset)) + len(str(length))
                    count = 0
                    length = 0
                    offset = 0
            else:
                output += encoding[i]
                i += 1
        return output
