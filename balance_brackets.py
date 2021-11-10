class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if not self.stack:
            return True
        return False

    def push(self, element):
        self.stack.insert(0, element)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    line = list(input('Введите строку со скобками:\n'))
    group_1 = ['[', '(', '{']
    group_2 = {']': '[', ')': '(', '}': '{'}
    flag = True
    i = 0
    if line:
        while i < len(line):
            if line[i] in group_1:
                stack.push(line[i])
            else:
                if stack.isEmpty() or stack.pop() != group_2[line[i]]:
                    flag = False
                    break
            i += 1
    if flag and stack.isEmpty():
        print('Сбалансированно')
    else:
        print('Несбалансированно')