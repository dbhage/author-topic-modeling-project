import re

# match alphabets
alphabet_re = re.compile(r"[a-zA-Z]")

# match things like "&Ccacute;", \1 then holds 'C'
ampersand_alphabets_semicolon_pattern = re.compile(r"&([a-zA-Z])[a-z]+;")

# match whitespaces
space_re = re.compile(r"\s+")

# name split regexp
name_split_re = re.compile(r"[^a-zA-Z-']")