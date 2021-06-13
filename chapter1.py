# Cracking Codes with Python
# Chapter 1 notes and exercises
import re


caesars_nums = {1: "a", 2: 'b', 3: 'c', 4: 'd',
                5: 'e', 6: 'f', 7: 'g', 8: 'h',
                9: 'i', 10: 'j', 11: 'k', 12: 'l',
                13: 'm', 14: 'n', 15: 'o', 16: 'p',
                17: 'q', 18: 'r', 19: 's', 20: 't',
                21: 'u', 22: 'v', 23: 'w', 24: 'x',
                25: 'y', 26: 'z'}


def valid_rot(rot):
    if rot > 26:
        rot = rot % 26
        return rot
    else:
        return rot


def caes_encode(plaintext, rot):
    rot = valid_rot(rot)
    output = []
    for char in plaintext:
        if re.match('[A-Za_z]', char):
            char_orig_num = list(caesars_nums.values()).index(char.lower())+1
            if char_orig_num+rot > 26:
                output.append(caesars_nums[char_orig_num+rot-26])
            else:
                output.append(caesars_nums[char_orig_num+rot])
        else:
            output.append(char)
    ciphertext = "".join(output)
    return ciphertext


def caes_decode(ciphertext, rot):
    rot = valid_rot(rot)
    output = []
    for char in ciphertext:
        if re.match('[A-Za-z]', char):
            char_orig_num = list(caesars_nums.values()).index(char.lower())+1
            if char_orig_num-rot < 0:
                output.append(caesars_nums[char_orig_num-rot+26])
            else:
                output.append(caesars_nums[char_orig_num-rot])
        else:
            output.append(char)
    plaintext = "".join(output)
    return plaintext
