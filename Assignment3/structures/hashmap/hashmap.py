"""This module is for the hashmap implementation."""


class Hashmap:
    """Class implementation for Hashmap."""

    def __init__(self, size):
        """Construct a Hashmap."""
        self.size = size
        self.hashmap = [[] for i in range(size)]

    def _get_hash(self, key):
        """Get hash value of key."""
        user_hash = 0
        for char in str(key):
            user_hash += ord(char)
        return user_hash % self.size

    def add_value(self, key, value):
        """Add key and value (updates if key is identical)."""
        index = self._get_hash(key)
        bucket = self.hashmap[index]
        flag = False
        for i, val in enumerate(bucket):
            str_, val_ = val
            val = val_
            if str_ == key:
                bucket[i] = (key, value)
                flag = True
                break
        if flag is False:
            bucket.append((key, value))

    def delete_value(self, key):
        """Delete a key and returns value if delete, None if key does not exist."""
        index = self._get_hash(key)
        bucket = self.hashmap[index]
        for i, val in enumerate(bucket):
            str_, val_ = val
            if str_ == key:
                bucket.pop(i)
                return val_
        return None

    def get_value(self, key):
        """Return the value in the specified key."""
        index = self._get_hash(key)
        bucket = self.hashmap[index]
        for val in bucket:
            str_, val_ = val
            if str_ == key:
                return val_
        return None

    def get_keys(self):
        """Return all keys in the form ['A', 'B', etc]."""
        lst = []
        for i in range(self.size):
            bucket = self.hashmap[i]
            for val in bucket:
                str_, val_ = val
                print(val_)
                lst.append(str_)
        return lst

    def get_as_str(self):
        """Return the hashmap."""
        return self.hashmap

    def get_as_dict(self):
        """Return the hashmap."""
        my_dict = {}
        for i in range(self.size):
            bucket = self.hashmap[i]
            temp_dict = {}
            for val in bucket:
                str_, val_ = val
                temp_dict[str_] = val_
            my_dict[i] = temp_dict
        return my_dict


def get_space_complexity():
    """Return the space complexity of the data structure."""
    return 'O(n)'


def get_time_complexity():
    """Return the time complexity of get_value in the data structure."""
    return 'O(n) as worst case, O(1) as best case'
