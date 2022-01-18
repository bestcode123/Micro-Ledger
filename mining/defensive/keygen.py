class Keygen:
    def __init__(self, type):
        self.type = type  # 'alphabet', 'numbers', etc.
    def gen_key(self, length):
        import random
        if(self.type == 'alphabet'):
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','o','q','r','s','t','u','v','w','x','y','z']
            ret = ''
            for i in range(length):
                ret += alphabet[random.randint(0, len(alphabet) - 1)]
            return ret