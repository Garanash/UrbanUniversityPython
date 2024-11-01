def single_root_words(root_word: str, *other_words: list[str]) -> list:
    same_words = [wd for wd in other_words if root_word.lower() in wd.lower() or wd.lower() in root_word.lower()]
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)