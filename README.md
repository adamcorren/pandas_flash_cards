# Pandas Flash Cards

This is a basic program that uses pandas and excel files to create your own flash cards.

The program will keep track of your progress by tracking the following stats:
- Number of time question has been asked
- Questino success rate
- Date of last attempt


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
  
The program will ask you a question as well as showing your last attempt result, number of tries, last date tried.
You input your answer. The program will then display the correct answer and you answer if you got the correct answer with 'y' or 'n'. The program will then update the csv 'quesitons_answers' file and move on to the next quesiton



## License

Licensed under [MIT]((https://opensource.org/license/mit/)).
