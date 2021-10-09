# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:23:16 2021

@author: vegeta
"""

import re                                 # for performing regex expressions

tokens = []                               # for string tokens
source_code = 'int A * b = 66 '.split() # turning source code into list of words

# Loop through each source code word
for word in source_code:
    
    # This will check if a token has datatype decleration
    if word in ['str', 'int', 'bool']: 
        tokens.append(['DATATYPE', word])
    
    # This will look for an identifier which would be just a word
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])
    
    # This will look for an operator
    elif word in '*-/+%=':
        tokens.append(['OPERATOR', word])
    
    # This will look for integer items and cast them as a number
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';': 
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else: 
            tokens.append(["INTEGER", word])

print(tokens) # Outputs the token array