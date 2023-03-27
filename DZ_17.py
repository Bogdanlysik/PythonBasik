def expanded_form(num):
    if num <= 0:
        raise ValueError("Число має бути більше 0")

    num_str = str(num)
    result = []
    for i in range(len(num_str)):
        if num_str[i] == '0':
            continue
        result.append(num_str[i] + '0' * (len(num_str) - i - 1))
    print(' + '.join(result))


if __name__ == '__main__':
    expanded_form(12)
    expanded_form(42)
    expanded_form(70304)