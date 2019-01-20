
# [lc]
# lexical compile

from _require._objectframe import * # fuck import

def lc(s):
    whitechs = "\n\t\r "
    no_word = whitechs + "()[]:|"
    class Catch:    # 可推回的字符流
        def __init__(self,iter):
            self.iter = iter
            self.stack = []
        def __next__(self):
            if len(self.stack) == 0:
                return next(self.iter)
            else:
                return self.stack.pop()
        def push(self,a):
            self.stack.append(a)
    def get_atom(catch):
        def get_str(catch): #
            r = ""
            while True:
                try:
                    ch = next(catch)
                except StopIteration:
                    exit("未完成的字符串")
                if ch == "\"":
                    return r
                else:
                    r += ch
        def get_word(catch):
            r = ""
            while True:
                try:
                    ch =next(catch)
                except StopIteration:
                    return r
                if ch not in no_word:
                    r += ch
                else:
                    catch.push(ch)
                    return r
        ch = next(catch)    # 必定成功
        if ch == '"':
            return Literal(String(get_str(catch)))
        else:
            catch.push(ch)
            word = get_word(catch)
            if word == "true":return Literal(Bool(True))
            elif word == "false":return Literal(Bool(False))
            elif word.isdigit():return Literal(Int(int(word)))
            try:    # 也可以使用正则识别
                n = float(word)
                return Literal(Float(n))
            except: pass
            return Sign(word)



    class _0:
        def __init__(self):
            self.content = None
        def append(self,a):
            assert self.content is None, "代码包含了多于一个表达式"
            self.content = a
        def get_content(self):
            assert self.content is not None, "代码中没有表达式"
            return self.content
        def head(self):
            exit("此间禁止使用'|'")
        def call(self):
            exit("此间禁止使用':'")

    class _1:           # 小括号
        def __init__(self,type1):
            self.l = []
            self.type1 = type1  # 0 - '(', 1 - '['
            self.type2 = 0          # 0 - (nothing)， 1 - '|' ， 2 - ':'
        def append(self,a):
            self.l.append(a)
        def head(self):
            assert self.type2 == 0 , "仅允许一次修饰"
            self.type2 = 1
        def call(self):
            assert self.type2 == 0 , "仅允许一次修饰"
            self.type2 = 2
        def obj(self):
            if self.type2 == 0:
                if self.type1 == 0:return Literal(Tuple(self.l))        # 很有趣
                elif self.type1 == 1:return Literal(List(self.l))
            else:
                head, *tail = self.l
                if self.type2 == 1:
                    if self.type1 == 0:return Literal(Huple(head, tail))
                    elif self.type1 == 1:return Literal(Hist(head, tail))
                elif self.type2 == 2:
                    if self.type1 == 0:return Call(head, tail)
                    elif self.type1 == 1:return Cali(head, tail)

    ######################
    catch = Catch(iter(s))
    depth_stack = [_0()]
    while True:
        try:
            ch = next(catch)
        except StopIteration:
            assert len(depth_stack) == 1, "缺少后括号"
            return depth_stack[0].get_content()

        if ch in whitechs:
            pass
        elif ch == '(':
            depth_stack.append(_1(0))
        elif ch == '[':
            depth_stack.append(_1(1))
        elif ch == '|':
            depth_stack[-1].head()
        elif ch == ':':
            depth_stack[-1].call()
        elif ch == ')':
            _ = depth_stack.pop()
            assert _.type1 == 0, "')'无法匹配上文"
            depth_stack[-1].append(_.obj())   # 加强版应为 _.obj()
        elif ch == ']':
            _ = depth_stack.pop()
            assert _.type1 == 1, "']'无法匹配上文"
            depth_stack[-1].append(_.obj())
        else:   # 必定atom
            catch.push(ch)
            depth_stack[-1].append(get_atom(catch))



