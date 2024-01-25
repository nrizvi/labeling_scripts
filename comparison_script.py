import pandas as pd

def get_user_initials():
    return input("Please enter your initials: ")

def display_sentences_and_get_input(data):
    responses = []
    total_pairs = len(data)
    for index, row in data.iterrows():
        remaining = total_pairs - (index + 1)
        print(f"\033[92mSentence pair {index + 1} of {total_pairs}. {remaining} pairs remaining.\033[0m")
        print(f"1) {row['Sentence 1 (Reddit)']}")
        print(f"2) {row['Sentence 2 (Twitter)']}")

        while True:
            user_input = input("\033[92mWhich sentence is more anti-autistic? (Enter number only): \033[0m")
            if user_input in ["1", "2"]:
                print(f"You chose: {user_input}")
                responses.append({
                    'Sentence 1': row['Sentence 1 (Reddit)'],
                    'Sentence 2': row['Sentence 2 (Twitter)'],
                    'User Response': user_input
                })
                break
            else:
                # Displaying the error message in red
                print("\033[91mLooks like you entered the wrong character. Only 1 and 2 are acceptable answers. Please try again.\033[0m")
    return responses

if __name__ == "__main__":
    # Load the Excel file
    file_path = 'sentence_pairs_all.xlsx'
    data = pd.read_excel(file_path)
    initials = get_user_initials()

    # Run the function with the loaded data
    # Run the function with the loaded data
    responses = display_sentences_and_get_input(data)

    # Save responses to a new Excel file
    responses_df = pd.DataFrame(responses)
    output_file = f'{initials}_c_labels.xlsx'
    responses_df.to_excel(output_file, index=False)
    print(f"Responses saved to {output_file}")
