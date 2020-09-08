class BrainFuckEx:
    def __init__(self):
        self.values = [[0]*256 for _ in range(256)]
        self.vertical = 0
        self.horizontal = 0

    def loopHelper(self, code):
        book = {}
        q = Deque()
        for i in range(len(code)):
            if code[i] == "[":
                q.rightappend(i)
            elif code[i] == "]":
                idx = q.rightpop()
                book[idx] = i
                book[i] = idx
        return book

    def Clear(self): self.__init__()

    def compile(self, code):
        v = self.vertical
        h = self.horizontal
        x = 0
        cnt = 0
        y = len(code)
        z = self.loopHelper(code)
        data = []
        while x < y:
            v = v % 256
            h = h % 256
            p = code[x]
            if p == ">": v += 1
            elif p == "<": v -= 1
            elif p == "v": h += 1
            elif p == "^": h -=1
            elif p == "+": self.values[v][h] += 1
            elif p == "-": self.values[v][h] -= 1
            elif p == "*": self.values[v][h] += self.values[v][0]*self.values[0][h]
            elif p == "[": pass
            elif p == "]":
                if self.values[v][h]: x = z[x] - 1
            elif p == ".": data.append(chr(self.values[v][h]))
            elif p == ",": self.values[v][h] = ord(input()[0])
            elif p == "=": break;
            else: continue
            x += 1
            cnt += 1

            if cnt > 100000: print("LoopError!"); break;
        print(''.join(data))
