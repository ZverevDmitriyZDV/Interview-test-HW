class Stack:

    def __init__(self, list_input):
        self.list_input = list_input

    def is_empty(self):
        return self.list_input == []

    def push(self, elem):
        self.list_input.insert(0, elem)

    def pop(self):
        return self.list_input.pop(0)

    def peek(self):
        return self.list_input[0]

    def size(self):
        return len(self.list_input)


if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7]
    st = Stack(input_data)
    print(st.is_empty())

    st.push('12')
    print(st.list_input)

    st.push('12')
    print(st.list_input)

    print(st.pop())
    print(st.list_input)

    print(st.peek())
    print(st.list_input)

    print(st.size())
    print(st.list_input)
