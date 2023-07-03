# Pandas Flash Cards
#### Introducing my very first program, created with Excel and pandas.

This program utilizes pandas and Excel files to create custom flashcards.

The program will keep track of your progress by tracking the following stats:

- Counting the number of times each question has been asked
- Calculating the success rate for each question
- Recording the date of the most recent attempt

## Prerequisite Software

- [Python 3](https://www.python.org/) (make sure to add Python to PATH/environment variables when installing)
- [pandas](https://pandas.pydata.org/)
- [datetime](https://github.com/SeleniumHQ/selenium/](https://docs.python.org/3/library/datetime.html))


### Windows installation

You can install the prerequisites double-clicking `install_prerequesites.bat` after installing Python 3.

## Usage
     
Follow the instructions for your operating system below.

### Windows

Once you've installed the [prerequisites](#prerequisite-software), double click `start_windows.bat`. That's it. 

### Using the program
Input your quesitons and answers in the 'question_answers' csv file. Make sure to save and close the csv file BEFORE running the program.
When adding a new quesiton fill in the columns as follows:

- Question: your question
- Answer: answer to question
- Number_Tries: 0
- Last_Try: TRUE
- Number_Correct: 0
- Number_Incorrect: 0
- CorrectP: 0
- Last_Tried: leave blank
  
The program will present you with a question and display the results of your last attempt, including the number of tries and the date of your most recent attempt. You will input your answer to the question. The program will reveal the correct answer and prompt you to indicate whether your answer was correct or not by entering 'y' for yes or 'n' for no. Based on your response, the program will update the 'question_answers' CSV file. The program will then proceed to the next question, repeating the process.



## License

Licensed under [MIT]((https://opensource.org/license/mit/)).
