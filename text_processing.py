#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    normalized_string = input_string.strip().lower()
    normalized_string = " ".join(normalized_string.split())
    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호로 이루어진 string
            ex - "This is an example."

        Returns:
            no_vowel_string (string): 모든 모음 (a, e, i, o, u)를 제거시킨 스트링
            ex - "Ths s n xmpl."

        Examples:
            # >>> import text_processing as tp
            # >>> input_string1 = "This is an example."
            # >>> tp.normalize(input_string1)
            # "Ths s n xmpl."
            # >>> input_string2 = "We love Python!"
            # >>> tp.normalize(input_string2)
            ''W lv Pythn!'
    """

    no_vowel_string = ''.join([i for i in input_string if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']])
    return no_vowel_string
