import csv
import random


class Questions:
    def __init__(self):
        self.questions = self.get_questions()
        self.formatted_questions = self.format_questions(self.questions)
        self.formatted_answers = self.format_answers(
            self.questions, self.formatted_questions)

    def get_questions(self):
        questions = []
        with open('Music Quiz/music.csv', 'r') as file:
            datareader = csv.reader(file, delimiter=',')
            for row in datareader:
                questions.append(row)
        return questions

    def format_questions(self, questions):
        formatted_questions = []
        for pair in questions:
            song, artist = pair
            formatted_song = []
            formatted_artist = []

            for word in song.split(' '):
                formatted_word = word[0] + '*' * (len(word) - 1)
                formatted_song.append(formatted_word)

            for word in artist.split(' '):
                formatted_word = word[0] + '*' * (len(word) - 1)
                formatted_artist.append(formatted_word)

            formatted_questions.append(
                (' '.join(formatted_song), ' '.join(formatted_artist)))

        return formatted_questions

    def format_answers(self, questions, formatted_questions):
        formatted_answers = []
        for pair in questions:
            formatted_answers.append((pair[0], pair[1]))
        return formatted_answers

    def answer_sheet_dict(self, formatted_questions, formatted_answers):
        answer_sheet = {}
        for i in range(len(formatted_questions)):
            answer_sheet[formatted_questions[i]] = formatted_answers[i]
        return answer_sheet


class Quiz:
    def __init__(self, questions, answer_sheet):
        self.questions = questions
        self.answers = answer_sheet
        self.score = 0

    def menu(self):
        print("\n\nWelcome to the Music Quiz!\n ")
        print("1. Start Quiz")
        print("2. Exit\n")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            self.start_quiz(self.questions)
        elif choice == '2':
            exit("Thank you for playing!")
        else:
            print("Invalid choice. Please try again.")
            self.menu()

    def start_quiz(self, question_list):
        print("\nStarting the quiz...")
        print("\nEnter the correct song and artist: \n")
        random.shuffle(question_list)
        for i in question_list:
            print(i, '\n')
            song_answer = input('Enter song:    ')
            artist_answer = input('Enter artist:    ')
            self.check_answer(i, song_answer, artist_answer)

    def check_answer(self, question, song_answer, artist_answer):
        print(self.answers)
# ----------------------------------------------------


questions = Questions()
print(questions.formatted_questions)
quiz = Quiz(questions.formatted_questions, questions.answer_sheet_dict(
    questions.formatted_questions, questions.formatted_answers))
quiz.menu()
