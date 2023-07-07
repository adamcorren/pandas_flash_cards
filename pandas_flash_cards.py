import pandas as pd
from datetime import datetime

def main():

    while True:
        # access questions as answers
        df = pd.read_csv('questions_answers.csv')

        # ask random question
        question = df.sample()
        print('Question:', question.Question.item(), '|', question.Last_Try.item(),'|', question.Number_Tries.item(),
              '|', question.Last_Tried.item(),'|', (round(question.CorrectP.item())),'%')
        print('------------------------')
        
        # answer question
        answer = input("")
        print('------------------------')

        # show answer
        print('Answer:', question['Answer'].item())
        print('------------------------')
        
        while True:
            # did user get correct answer
            result = input('Did you get the question correct? (y/n): ')
            print('------------------------')
            # update stats
            if result == 'y':
                question['Last_Try'] = True
                question['Number_Correct'] = question.Number_Correct + 1
                break
            if result == 'n':
                question['Last_Try'] = False
                question['Number_Incorrect'] = question.Number_Incorrect + 1
                break
            else:
                print('Invalid result, try again')
        
        # update last tried, number of tries, correct percentage 
        question['Last_Tried'] = datetime.now().date()
        question['Number_Tries'] = question.Number_Tries + 1
        question['CorrectP'] = (question.Number_Correct.item() / question.Number_Tries.item())*100
        df = pd.concat([df, question]).drop_duplicates(subset='Question', keep='last')
        
        # update csv file
        df.to_csv('questions_answers.csv',mode='w', index=False)
        continue

if __name__ == '__main__':
    main()
