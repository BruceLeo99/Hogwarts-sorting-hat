from nltk import word_tokenize
from nltk.stem import PorterStemmer

# Load the stemmer
stemmer = PorterStemmer()

# Gryffindor keywords
Gryffindor_keywords = [
    "Courageous", "Brave", "Chivalrous", "Daring", "Bold",
    "Adventurous", "Loyal", "Impulsive", "Reckless", "Leadership",
    "Determined", "Honorable", "Fearless", "Heroic", "Energetic"
]

# Hufflepuff keywords
Hufflepuff_keywords = [
    "Loyal", "Hardworking", "Kind", "Patient", "Fair",
    "Friendly", "Honest", "Compassionate", "Trustworthy", "Generous",
    "Tolerant", "Empathetic", "Humble", "Dedicated", "Reliable"
]

# Ravenclaw keywords
Ravenclaw_keywords = [
    "Intelligent", "Wise", "Creative", "Curious", "Analytical",
    "Knowledgeable", "Innovative", "Logical", "Independent", "Perceptive",
    "Academic", "Eccentric", "Studious", "Intellectual", "Reflective"
]

# Slytherin keywords
Slytherin_keywords = [
    "Ambitious", "Cunning", "Resourceful", "Determined", "Strategic",
    "Leadership", "Self-Preservation", "Clever", "Ambitious", "Competitive",
    "Proud", "Charismatic", "Assertive", "Sophisticated", "Discerning"
]

# Turn the keywords into lower-case stems
Gryffindor_keywords = [stemmer.stem(word.lower()) for word in Gryffindor_keywords]
Hufflepuff_keywords = [stemmer.stem(word.lower()) for word in Hufflepuff_keywords]
Ravenclaw_keywords = [stemmer.stem(word.lower()) for word in Ravenclaw_keywords]
Slytherin_keywords = [stemmer.stem(word.lower()) for word in Slytherin_keywords]

# # Word indices of each house as a dictionary, where
# # key is a keyword and value is an integer of the occurrence of that keyword in a sentence
# Gryffindor_word_index = defaultdict(int)
# Hufflepuff_word_index = defaultdict(int)
# Ravenclaw_word_index = defaultdict(int)
# Slytherin_word_index = defaultdict(int)

Gryffindor_tfscore = 0
Hufflepuff_tfscore = 0
Ravenclaw_tfscore = 0
Slytherin_tfscore = 0

def restart_or_exit():

    """
    Asks users to press either 'r' or 'e'.
    If 'r' is pressed, the prgram will reset the global tf-scores and restart.
    If 'e' is pressed, the program will terminate.
    """
    print("Please press 'r' to restart, and press 'e' to exit:")
    key = input(" ")
    if key =="e":
        return False

    else:

        global Gryffindor_tfscore, Hufflepuff_tfscore, Ravenclaw_tfscore, Slytherin_tfscore

        Gryffindor_tfscore = 0
        Hufflepuff_tfscore = 0
        Ravenclaw_tfscore = 0
        Slytherin_tfscore = 0

        print("Start sorting again")

        return True

def tf_score_calc():

    """
    Calculates the tf-scores of each house based on the user's input.

    House with the maximum tf-score will be announced as the selected house of the user.

    If there exists more than one maximum score, the user will be asked to write
    something more about him/her self to gain more information about the user, and
    ft-scores of each house will be continously summed.

    """

    global Gryffindor_tfscore, Hufflepuff_tfscore, Ravenclaw_tfscore, Slytherin_tfscore

    self_intro = input("Please briefly describe yourself! \n")

    tokenized_self_intro = word_tokenize(self_intro)
    stemmed_self_intro = [stemmer.stem(word.lower()) for word in tokenized_self_intro]

    has_result = True
    # Check the occurrence of word

    for word in stemmed_self_intro:

        if word in Gryffindor_keywords:
            Gryffindor_tfscore += 1

        if word in Hufflepuff_keywords:
            Hufflepuff_tfscore += 1

        if word in Ravenclaw_keywords:
            Ravenclaw_tfscore += 1

        if word in Slytherin_keywords:
            Slytherin_tfscore += 1

    score_list = [Gryffindor_tfscore, Hufflepuff_tfscore, Ravenclaw_tfscore, Slytherin_tfscore]
    winner = max(score_list)
    print(score_list)

    # Check duplicates: IF there are duplicates, then ask the user to say more about him/herself
    if len([index for index, value in enumerate(score_list) if value == winner]) >1:
        print("Hmm, it's very hard to decide! Could you please tell me more about yourself?")
        return tf_score_calc()

    else:

        if winner == Gryffindor_tfscore:
            return "Gryffindor"

        elif winner == Hufflepuff_tfscore:
            return "Hufflepuff"

        elif winner == Ravenclaw_tfscore:
            return "Ravenclaw"

        elif winner == Slytherin_tfscore:
            return "Slytherin"

def tf_idf_score_calc():
    """
    Save for future use.
    """
    pass

def run_tf():

    """
    Executes the sorting based on the house tf-scores.

    After the result, users will be asked to continue or exit the App.
    """

    result = tf_score_calc()
    print(f"\nCongratulations!! You are in {result}")
    to_restart = restart_or_exit()

    if to_restart:
        run_tf()

    elif not to_restart:
        exit(1)

def run_tf_idf():
    """
    Save for future use.
    """
    result = tf_idf_score_calc()
    print(f"\nCongratulations!! You are in {result}")
    to_restart = restart_or_exit()

    if to_restart:
        run_tf_idf()

    elif not to_restart:
        exit(1)


