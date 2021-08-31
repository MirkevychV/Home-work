import re


def words_counter(text):
    """
    16. Написати функцію, яка буде рахувати частоту використання слів у
    тексті. Функція повинна роздрукувати слова і частоту в алфавітному
    порядку.
    """
    words_dict = {}
    match_template = re.findall(r'\w+', text)

    for word in match_template:
        count = words_dict.get(word, 0)
        words_dict[word] = count + 1

    result = '\n'.join([f'{word} {freq}' for word, freq in sorted(words_dict.items())])
    return result
