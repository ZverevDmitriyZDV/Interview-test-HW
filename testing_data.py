from sorted_steck import check_line


def test(test_line):
    for test_line in test_list:
        print(check_line(test_line))
    return None


if __name__ == '__main__':
    test_list = [
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '(((([{}]))))',
        '{{[(])]}}',
        '}{}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]
    test(test_list)
