#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_length = len(sentence)
    first_char = None if sentence_length == 0 else sentence[0]

    return (sentence_length, first_char)