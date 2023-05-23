import random;
import data_manager as dm;

def get_random_quote(quotes):
    random_number = random.randint(0, len(quotes) - 1);
    return quotes[random_number];

def get_quote(data):
    quote = get_random_quote(data);
    quote = dm.parse_to_dict(data[0], quote);
    return quote;

def filter_characters(characters):
    filtered_chars = [];
    for char in characters:
        if char not in filtered_chars:
            filtered_chars.append(char);
    return filtered_chars;

def get_characters_list(quotes):
    chars_list = list(map(lambda quote: quote[3], quotes));
    chars_list.pop(0);
    chars_list = filter_characters(chars_list);
    return chars_list;

def get_two_chars(quotes, current_char):
    characters = get_characters_list(quotes);
    found = [];
    is_done = False;
    while not is_done:
        if len(found) == 2:
            is_done = True;
            break;
        character = random.choice(characters);
        if character not in found and character != current_char:
            found.append(character);
    return found;



