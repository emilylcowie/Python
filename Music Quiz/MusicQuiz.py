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
        self.questions_asked = 0

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
            self.questions_asked += 1
            hint_choice = input("Do you want a hint, this will deduct your score? (yes/no): ")
            if hint_choice.lower() == 'yes':
                self.give_hint(i)
            song_answer = input('Enter song:    ')
            artist_answer = input('Enter artist:    ')
            self.check_answer(i, song_answer, artist_answer)
            self.continue_or_exit()
        self.finish()
            

    def check_answer(self, question, song_answer, artist_answer):
        for correct_pair in self.answers:
            if question == correct_pair:
                correct_song, correct_artist = self.answers[correct_pair]
                if song_answer.lower() == correct_song.lower() and artist_answer.lower() == correct_artist.lower():
                    self.score += 1
                    print("Correct!\n")
                else:
                    print(
                        f"Incorrect! The correct answer is: '{correct_song}' by '{correct_artist}'.\n")
    
    def continue_or_exit(self):
        print(f"Current Score: {self.score}/{self.questions_asked}\n")
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() == 'yes':
            return 
        print(f"Your final score is: {self.score}/{self.questions_asked}")
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == 'yes':
            self.score = 0
            self.questions_asked = 0
            self.menu()
        else:
            exit("Thank you for playing!")

    def give_hint(self, question):
        for correct_pair in self.answers:
            if question == correct_pair:
                correct_song, correct_artist = self.answers[correct_pair]
                song_hint = ""
                artist_hint = ""
                for word in correct_song.split(' '):
                    song_hint += word[0:3] + '*' * (len(word) - 3) + ' '
                for word in correct_artist.split(' '):
                    artist_hint += word[0:3] + '*' * (len(word) - 3) + ' '
                print(f"Hint - Song: {song_hint}, Artist: {artist_hint}\n")
                self.score -= 0.5

    def finish(self):
        print(f"Quiz Over! Your final score is: {self.score}/{self.questions_asked}")
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == 'yes':
            self.score = 0
            self.questions_asked = 0
            self.menu()
        else:
            exit("Thank you for playing!")
# ----------------------------------------------------


questions = Questions()
quiz = Quiz(questions.formatted_questions, questions.answer_sheet_dict(
    questions.formatted_questions, questions.formatted_answers))
quiz.menu()
