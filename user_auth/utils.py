# coding: utf-8
from .constants import USER_GENDER_FEMALE


def genderize_word(user, male_word, female_word):
    word = male_word
    if (hasattr(user, 'gender') and user.gender == USER_GENDER_FEMALE) or \
            user == USER_GENDER_FEMALE:
        word = female_word
    return word
