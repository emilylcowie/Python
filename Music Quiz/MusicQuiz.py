import csv

def get_questions():
    questions = []
    with open('Music Quiz/music.csv', 'r') as file:
        datareader = csv.reader(file, delimiter=',')
        for row in datareader:
            questions.append(row)
    return questions

def format_questions(questions):
    for i in questions:
        for j in i:
            for k in j:
                print(k)
            
        

def main():
    questions = get_questions()
    format_questions(questions)

main()