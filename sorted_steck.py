from Stack import Stack


def check_line(input_line):
    st = Stack([])
    key_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    inx = 0

    for elem in input_line:
        inx += 1
        if elem not in key_dict.keys():
            st.push(elem)
        elif st.is_empty():
            return 'Неупорядоченный. Ошибка первого элемента'
        elif key_dict[elem] == st.peek():
            st.pop()
        else:
            return f'Неупорядоченный. Ошибка элемента {elem}  позиция {inx}'
    return 'Список упорядоченный'


if __name__ == '__main__':
    print(check_line('[([])((([[[]]])))]{()}[((([{}])))]'))
