import quotes_flow as qf;
import data_manager as dm;
import random;

def validate_response(answer, options, quote):
    char_anwsered = options[int(answer) - 1];
    char_correct = quote['character'];
    if char_correct == char_anwsered:
        print('That\'s right!')
    else:
        print(f"Wrong! {char_correct} said that.")

def validate_continue_playing():
    print ('Would you like to play again?');
    print('1. Yes');
    print('2. No');
    response = input('Response: ');
    if response == '1' or response.lower() == 'yes':
        return True;
    else:
        return False;

        

def main():
    continue_playing = True;
    data = dm.read_data();
    while continue_playing:
        random_quote = qf.get_quote(data);
        options = qf.get_two_chars(data, random_quote['character']);
        options.insert(random.randint(0,2), random_quote['character']);

        print('-> Who say it? (The office version)\n');
        print(random_quote['reply']);
        print('1) ' + options[0]);
        print('2) ' + options[1]);
        print('3) ' + options[2]);

        answer = input('Response: ');
        validate_response(answer, options, random_quote);
        continue_playing = validate_continue_playing();

if __name__ == "__main__":
    main();