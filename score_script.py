import pandas as pd

def load_sentences(sheet_name):
    df = pd.read_excel('labels_disagreement.xlsx', sheet_name=sheet_name)
    return df['Sentence'].tolist()



def ask_questions(sentence):
    score = 0
    acceptable_answers = ['Y', 'N']

    # Function to ask a question with a sentence
    def ask_question_with_sentence(question, sentence):
        while True:
            print(f"{sentence}")
            answer = input(question).strip().upper()
            if answer in acceptable_answers:
                return answer
            else:
                print("\033[91mInvalid input. Only Y or N are acceptable answers. Please try again.\033[0m")

    # First question
    context_answer = ask_question_with_sentence("\033[92mDoes this need more context? Y or N: \033[0m", sentence)
    if context_answer == 'Y':
        return -1, True  # Score is -1, skip to next sentence

    # Second question
    ableist_answer = ask_question_with_sentence("\033[92mIs this sentence \033[91mableist\033[92m? Y or N: \033[0m", sentence)
    if ableist_answer == 'Y':
        score += 1
    else:  # If answer is 'N', skip to question 4
        explicit_answer = ask_question_with_sentence("\033[92mIs this sentence \033[91mexplicit\033[92m? Y or N: \033[0m", sentence)
        if explicit_answer == 'Y':
            score += 1
        return score, False

    # Third question
    anti_autistic_answer = ask_question_with_sentence("\033[92mIs this sentence \033[91manti-autistic\033[92m? Y or N: \033[0m", sentence)
    if anti_autistic_answer == 'Y':
        score += 1

    # Fourth question
    explicit_answer = ask_question_with_sentence("\033[92mIs this sentence \033[91mexplicit\033[92m? Y or N: \033[0m", sentence)
    if explicit_answer == 'Y':
        score += 1

    return score, False  # Continue to next sentence


def main():
    initials = input("Please enter your initials: ").strip()
    filename = f"{initials}_s_scores.xlsx"
    sentences_and_scores = []

    #all_sentences = load_sentences('Reddit Disagreement') + load_sentences('Twitter Disagreement')
    all_sentences = load_sentences('Reddit Disagreement') + load_sentences('Twitter Disagreement')

    total = len(all_sentences)

    for i, sentence in enumerate(all_sentences, 1):
        print(f"Sentence {i} out of {total}")
        score, _ = ask_questions(sentence)
        sentences_and_scores.append((sentence, score))

    results_df = pd.DataFrame(sentences_and_scores, columns=['Sentence', 'Score'])
    results_df.to_excel(filename, index=False)
    print(f"Responses saved to {filename}")

if __name__ == "__main__":
    main()
