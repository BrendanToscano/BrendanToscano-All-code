import tkinter as tk
import sys
import random
import openai
import textwrap
import ast
import uuid
import os
import threading
from tkinter import simpledialog,messagebox
from PIL import Image, ImageTk
# Base directory of the program
base_dir = os.path.dirname(os.path.abspath(__file__))

apiKey = None
retryCount = 0
# Function to ask user for API key (Can be removed based on user review)
def getApiKey():
    global apiKey, retryCount
    apiKey = simpledialog.askstring("API Key Required", "Please enter your OpenAI API key to continue:", show="*")
    if not apiKey:
        retryCount += 1
        if retryCount >= 3:
            messagebox.showerror("Error", "Too many failed attempts. Exiting the application.")
            sys.exit()
        messagebox.showerror("Error", "API key is required to use the application.")
        getApiKey()
    else:
        if apiKey == "2000":
            openai.api_key = ""
            return
        testApiKey(apiKey)

# Function to check if api key is valid
def testApiKey(apiKey):
    """ Check if API key is valid, if repeated false entries 3 times then program will quit"""
    global retryCount
    openai.api_key = apiKey
    try:
        openai.Model.list()
        messagebox.showinfo("Success", "API key validated!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid API key. Try Again\n{e}")
        retryCount += 1
        if retryCount >= 3:
            messagebox.showerror("Error", "Too many failed attempts. Exiting the application.")
            sys.exit()
        getApiKey()

getApiKey()

# Base screen
root = tk.Tk()
root.title("AI Quiz Game")
root.geometry("600x600")
root.config(bg="light blue")

# Importing all images to use for the program
rootBg = Image.open(os.path.join(base_dir, "rootBg1.jpg"))
rootBg = rootBg.resize((600,600), Image.LANCZOS)
bgPhoto = ImageTk.PhotoImage(rootBg) 

rootBg2 = Image.open(os.path.join(base_dir, "rootBg2.jpg"))
rootBg2 = rootBg2.resize((600,600), Image.LANCZOS)
bgPhoto2 = ImageTk.PhotoImage(rootBg2) 

rootBg3 = Image.open(os.path.join(base_dir, "rootBg3.jpg"))
rootBg3 = rootBg3.resize((600,600), Image.LANCZOS)
bgPhoto3 = ImageTk.PhotoImage(rootBg3) 

menuButton1 = Image.open(os.path.join(base_dir, "menuButton1.png"))
menuButton1 = menuButton1.resize((303,113), Image.LANCZOS)
buttonMenu1 = ImageTk.PhotoImage(menuButton1)

menuButton2 = Image.open(os.path.join(base_dir, "menuButton1.png"))
menuButton2 = menuButton2.resize((223,98), Image.LANCZOS)
buttonMenu2 = ImageTk.PhotoImage(menuButton2)

correctButton = Image.open(os.path.join(base_dir, "correctButton.png"))
correctButton = correctButton.resize((223,98), Image.LANCZOS)
buttonCorrect = ImageTk.PhotoImage(correctButton)

wrongButton = Image.open(os.path.join(base_dir, "wrongButton.png"))
wrongButton = wrongButton.resize((223,98), Image.LANCZOS)
buttonWrong = ImageTk.PhotoImage(wrongButton)

menuButton2 = Image.open(os.path.join(base_dir, "menuButton1.png"))
menuButton2 = menuButton2.resize((223,98), Image.LANCZOS)
buttonMenu2 = ImageTk.PhotoImage(menuButton2)

infoImage = Image.open(os.path.join(base_dir, "information.png"))
infoImage = infoImage.resize((30, 30), Image.LANCZOS)
imageInfo = ImageTk.PhotoImage(infoImage)

infoImageDim = Image.open(os.path.join(base_dir, "informationDim.png"))
infoImageDim = infoImageDim.resize((30, 30), Image.LANCZOS)
imageInfoDim = ImageTk.PhotoImage(infoImageDim)

startButton = Image.open(os.path.join(base_dir, "startButton.png"))
startButton = startButton.resize((400,300), Image.LANCZOS)
buttonStart = ImageTk.PhotoImage(startButton)

nextButton = Image.open(os.path.join(base_dir, "nextButton.png"))
nextButton = nextButton.resize((200, 125), Image.LANCZOS)
buttonNext = ImageTk.PhotoImage(nextButton)

nextButtonDim = Image.open(os.path.join(base_dir, "nextButtonDim.png"))
nextButtonDim = nextButtonDim.resize((200, 125), Image.LANCZOS)
buttonNextDim = ImageTk.PhotoImage(nextButtonDim)

backButton = Image.open(os.path.join(base_dir, "backButton.png"))
backButton = backButton.resize((30, 30), Image.LANCZOS)
buttonBack = ImageTk.PhotoImage(backButton)

backButtonDim = Image.open(os.path.join(base_dir, "backButtonDim.png"))
backButtonDim = backButtonDim.resize((30, 30), Image.LANCZOS)
buttonBackDim = ImageTk.PhotoImage(backButtonDim)

submitButton = Image.open(os.path.join(base_dir, "submitButton.png"))
submitButton = submitButton.resize((200,150), Image.LANCZOS)
buttonSubmit = ImageTk.PhotoImage(submitButton)

submitButtonDim = Image.open(os.path.join(base_dir, "submitButtonDim.png"))
submitButtonDim = submitButtonDim.resize((200,150), Image.LANCZOS)
buttonSubmitDim = ImageTk.PhotoImage(submitButtonDim)

exitButton = Image.open(os.path.join(base_dir, "exitButton.png"))
exitButton = exitButton.resize((30, 30), Image.LANCZOS)
buttonExit = ImageTk.PhotoImage(exitButton)

exitButtonDim = Image.open(os.path.join(base_dir, "exitButtonDim.png"))
exitButtonDim = exitButtonDim.resize((30, 30), Image.LANCZOS)
buttonExitDim = ImageTk.PhotoImage(exitButtonDim)

homeButton = Image.open(os.path.join(base_dir, "homeButton.png"))
homeButton = homeButton.resize((30, 30), Image.LANCZOS)
buttonHome = ImageTk.PhotoImage(homeButton)

homeButtonDim = Image.open(os.path.join(base_dir, "homeButtonDim.png"))
homeButtonDim = homeButtonDim.resize((30, 30), Image.LANCZOS)
buttonHomeDim = ImageTk.PhotoImage(homeButtonDim)

# Using canvas for the background
canvas = tk.Canvas(root, width=610, height=610)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bgPhoto, anchor="nw")

pulseSize = 300
pulseIncreasing = True

# Function for pulse effect on start screen
def startPulse():
    """ Start text pulse effect """
    global pulseSize, pulseIncreasing, buttonStart

    if pulseIncreasing:
        pulseSize += 2
        if pulseSize >= 320: 
            pulseIncreasing = False
    else:
        pulseSize -= 2
        if pulseSize <= 300:
            pulseIncreasing = True

    resizedImage = startButton.resize((pulseSize+100, pulseSize+10), Image.LANCZOS)
    buttonStart = ImageTk.PhotoImage(resizedImage) 

    canvas.itemconfig(startText, image=buttonStart)

    root.after(100, startPulse)

score = 0

# The quiz screen where the questions and options are displayed
def quizQA(qNum = 0, num = 0, gptList = None, answers = None):
    """ Screen where the quiz questions and options are displayed """
    # qNum is tracking the question number.
    qNum += 1
    quizSize = answers[0]
    quizDifficulty = answers[1]
    quizTime = answers[2]
    if num == 1:
        questions = [
        "What is your favorite color?",
        "What is your favorite food?",
        "Where were you born?",
        "What is your hobby?",
        "What is your pet's name?",
        "What is your favorite movie?",
        "What is your favorite book?",
        "What is your dream job?",
        "What is your favorite place?",
        "What is your favorite sport?"
        ]
        ansLists = gptList

    elif num == 2 or num == 3:
        questions = [item[0] for item in gptList]
        ansLists = [item[1:] for item in gptList]

    ansList = None
    for i,ans in enumerate(ansLists):
        if qNum == i+1:
            print(qNum, i+1)
            ansList = ans
            break
    
    questionText = "Q" + str(qNum) + ": " + questions[qNum - 1]
    correctAnswer = ansList.pop()

    global quizQAWindow 
    # Removes last quiz screen window.
    if qNum > 1:
        quizQAWindow.withdraw()
    # Creating the window 
    quizQAWindow = tk.Toplevel(root)
    quizQAWindow.geometry("600x600")
    quizQAWindow.title("Game Screen")

    canvas = tk.Canvas(quizQAWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto3, anchor="nw")

    timerText = canvas.create_text(570, 30, text=f"Time left: {quizTime} sec", font=("Comic Sans MS", 14), fill="red", anchor="ne")
        
    def onEnter(e):
        e.widget.config(fg=buttonHoverFg)

    def onLeave(e):
        e.widget.config(fg=buttonFg)

    def startTimer(quizTime):
        global timeTaskQA
        if quizTime > 0:
            canvas.itemconfig(timerText, text=f"Time left: {quizTime} sec")
            timeTaskQA = quizQAWindow.after(1000, lambda: startTimer(quizTime - 1))
        else:
            canvas.itemconfig(timerText, text="Time's up!")
            answerCheck()

    def normalizeText(text):
        return " ".join(text.split())

    def correctAns():
        for button in buttons:
            if normalizeText(button["text"]) == normalizeText(correctAnswer):
                button.config(image=buttonCorrect)

    def answerCheck(answer = None, selectedButton = None):
        for button in buttons:
            button.config(command=lambda: None, fg= "#ffffff", activeforeground= "#ffffff")
            button.bind("<Enter>", onLeave)
            button.bind("<Leave>", onLeave)
            button.bind("<Button-1>", lambda e: "break")

        quizQAWindow.after_cancel(timeTaskQA)

        if answer == correctAnswer:
            global score
            score += 1
            canvas.itemconfig(timerText, text="Choice Selected")
            selectedButton.config(image=buttonCorrect)
        elif selectedButton != None:
            canvas.itemconfig(timerText, text="Choice Selected")
            selectedButton.config(image=buttonWrong)
            correctAns()
        else:
            canvas.itemconfig(timerText, text="No Selection Made")
            correctAns()

        if qNum == quizSize:
            # Submit Button
            submit = canvas.create_image(300, 550, image=buttonSubmit, anchor="center")
            canvas.tag_bind(submit, "<Button-1>", lambda event: submitQuiz(score, quizSize, quizDifficulty, quizTime))
            # Responsive effect changing to dimmer image.
            canvas.tag_bind(submit, "<Enter>", lambda event: canvas.itemconfig(submit, image=buttonSubmitDim))
            canvas.tag_bind(submit, "<Leave>", lambda event: canvas.itemconfig(submit, image=buttonSubmit))
        else:
            nextButton = canvas.create_image(300, 550, image=buttonNext, anchor="center")
            canvas.tag_bind(nextButton, "<Button-1>", lambda event: quizQA(qNum, num, gptList, answers))
            canvas.tag_bind(nextButton, "<Enter>", lambda event: canvas.itemconfig(nextButton, image=buttonNextDim))
            canvas.tag_bind(nextButton, "<Leave>", lambda event: canvas.itemconfig(nextButton, image=buttonNext))

    startTimer(quizTime)

    exitButton = canvas.create_image(30, 30, image=buttonExit, anchor="nw")
    canvas.tag_bind(exitButton, "<Button-1>", lambda event: winManagerBack(4))
    canvas.tag_bind(exitButton, "<Enter>", lambda event: canvas.itemconfig(exitButton, image=buttonExitDim))
    canvas.tag_bind(exitButton, "<Leave>", lambda event: canvas.itemconfig(exitButton, image=buttonExit))

    buttonFont = ("Comic Sans MS Italic", 16, "bold")
    buttonImage = buttonMenu2
    buttonFg = "#ffffff"
    buttonHoverFg = "#999999"
    buttons = []

    canvas.create_text(300, 140, text=questionText, font=("Comic Sans MS", 14), fill="black", width=500, anchor="center")

    x_positions = [0.27, 0.72]
    y_start = 280
    y_spacing = 110

    def wrapTextToFit(text, maxWidth):
        """ Wraps text to fit within a button's width without splitting words."""
        wrappedLines = textwrap.wrap(text, width=maxWidth)
        return "\n".join(wrappedLines)

    for i, answer in enumerate(ansList):
        col = i % 2  
        row = i // 2
        x = x_positions[col]
        y = y_start + (row * y_spacing)

        wrappedAnswer = wrapTextToFit(answer, maxWidth=15)

        button = tk.Button(quizQAWindow, text=wrappedAnswer, image=buttonImage, compound="center", font=buttonFont, fg=buttonFg, 
        activeforeground=buttonHoverFg, borderwidth = 0, highlightthickness=0, width=220, height=60)
        button.config(command = lambda answer=answer, button=button: answerCheck(answer, button))
        button.place(relx=x, y=y, anchor="center")
        button.bind("<Enter>", onEnter)
        button.bind("<Leave>", onLeave)
        buttons.append(button)

# Final screen after quiz ends
# (Might add a total time taken later)
def submitQuiz(score, quizSize, quizDifficulty, quizTime):
    """ Screen displays number of questions, difficulty, time per question and number of wrong answers, and final score at the end of the quiz."""
    global submitQuizWindow 
    quizQAWindow.withdraw()
    # Creating the window 
    submitQuizWindow = tk.Toplevel(root)
    submitQuizWindow.geometry("600x600")
    submitQuizWindow.title("Game Screen")

    canvas = tk.Canvas(submitQuizWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto3, anchor="nw")

    # Home Button
    homeButton = canvas.create_image(30, 30, image=buttonHome, anchor="nw")
    canvas.tag_bind(homeButton, "<Button-1>", lambda event: winManagerBack(6))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(homeButton, "<Enter>", lambda event: canvas.itemconfig(homeButton, image=buttonHomeDim))
    canvas.tag_bind(homeButton, "<Leave>", lambda event: canvas.itemconfig(homeButton, image=buttonHome))

    canvas.create_text(300, 40, text="Quiz Summary", font=("Comic Sans MS Italic", 24), fill="black", anchor="n")

    # Questions for the personalized Quiz.
    summaryText = [
        f"Number of questions                       : {quizSize}",
        f"Difficulty of Quiz from 1 to 10       : {quizDifficulty}",
        f"Time given per question                   : {quizTime}",
        f"Number of Question Answer Wrong : {quizSize-score}",
    ]
    
    # Setting the starting positions
    positionY = 200
    positionX = 150

    # Displaying the Summary.
    for i, question in enumerate(summaryText):
        canvas.create_text(positionX, positionY, text=question, font=("Comic Sans MS", 12), fill="black", anchor="w")
        positionY += 40

    canvas.create_text(300, positionY-15, text="Score", font=("Comic Sans MS Bold Italic", 46), fill="black", anchor="n")
    canvas.create_text(300, positionY+60, text=f"{score}/{quizSize}", font=("Comic Sans MS Bold Italic", 36), fill="black", anchor="n")

    print(score)
    score = 0

# 1/3 Personalized quiz window
def personalizedQuiz():
    """ Personalized quiz window with 10 questions."""
    # Removing the previous window from view
    quizWindow.withdraw()
    global perQuizWindow
    # Creating the window 
    perQuizWindow = tk.Toplevel(root)
    perQuizWindow.geometry("600x600")
    perQuizWindow.title("Personalized Quiz")

    canvas = tk.Canvas(perQuizWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto, anchor="nw")

    # Information text when the info button is clicked
    def infoText():
        messagebox.showinfo("Information", """       Enter the answers to these questions 
        in the blanks below. Enter atleast 5 answers
        and we will deal with the rest. 
        Note: Information provided here is not used 
        by us but may be used by OpenAI, by clicking
        submit you agree to OpenAI's ToS.""")

    # Information Button
    informationButton = canvas.create_image(570, 30, image=imageInfoDim, anchor="ne")
    canvas.tag_bind(informationButton, "<Button-1>", lambda event: infoText())
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(informationButton, "<Enter>", lambda event: canvas.itemconfig(informationButton, image=imageInfo))
    canvas.tag_bind(informationButton, "<Leave>", lambda event: canvas.itemconfig(informationButton, image=imageInfoDim))

    # Back Button
    backButton = canvas.create_image(30, 30, image=buttonBack, anchor="nw")
    canvas.tag_bind(backButton, "<Button-1>", lambda event: winManagerBack(1))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(backButton, "<Enter>", lambda event: canvas.itemconfig(backButton, image=buttonBackDim))
    canvas.tag_bind(backButton, "<Leave>", lambda event: canvas.itemconfig(backButton, image=buttonBack))

    # Submit Button
    submit = canvas.create_image(300, 550, image=buttonSubmit, anchor="center")
    canvas.tag_bind(submit, "<Button-1>", lambda event: submitAnswersPerQuiz(entryBoxes))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(submit, "<Enter>", lambda event: canvas.itemconfig(submit, image=buttonSubmitDim))
    canvas.tag_bind(submit, "<Leave>", lambda event: canvas.itemconfig(submit, image=buttonSubmit))

    canvas.create_text(300, 40, text="Personal Questions", font=("Comic Sans MS Italic", 24), fill="black", anchor="n")

    # Questions for the personalized Quiz.
    questions = [
        "What is your favorite color?",
        "What is your favorite food?",
        "Where were you born?",
        "What is your hobby?",
        "What is your pet's name?",
        "What is your favorite movie?",
        "What is your favorite book?",
        "What is your dream job?",
        "What is your favorite place?",
        "What is your favorite sport?"
    ]
    
    # Setting the starting positions
    positionY = 120
    positionX = 60
    positionXE = 350

    # Being sent to submitAnswerPerQuiz function under submit button
    entryBoxes = []

    # Displaying the questions along with entry boxes.
    for i, question in enumerate(questions):
        canvas.create_text(positionX, positionY, text=question, font=("Comic Sans MS", 12), fill="black", anchor="w")

        entryBox = tk.Entry(perQuizWindow, font=("Comic Sans MS", 12))
        canvas.create_window(positionXE, positionY, window=entryBox, anchor="w")

        entryBoxes.append(entryBox)

        positionY += 40

# 1.1 Personalized Quiz submit handling.
def submitAnswersPerQuiz(entryBoxes):
    """ Handling the data received from the personalized quiz screen. """\
    # Checking if the user entered atleast 5 entry boxes.
    count = 0
    for entry in entryBoxes:
        if entry.get().strip() == "":
            count += 1
    if count > 5:
        messagebox.showinfo("Try again", "You need to fill atleast 5, otherwise it is no fun")
        return

    # Getting the answers from the entry boxes and storing it.
    answers = [entry.get().strip() if entry.get().strip() else "none of the options" for entry in entryBoxes]
    
    def generateQuiz(callback):
        try:
            quizLoadingScreen()
            response = openai.ChatCompletion.create(
                model="gpt-4o", 
                messages= [{"role": "system", "content": (
                    "You are an assistant that generates quiz options for given questions and answers.\n"
                    "Questions:\n"
                    "1. What is your favorite color?\n"
                    "2. What is your favorite food?\n"
                    "3. Where were you born?\n"
                    "4. What is your hobby?\n"
                    "5. What is your pet's name?\n"
                    "6. What is your favorite movie?\n"
                    "7. What is your favorite book?\n"
                    "8. What is your dream job?\n"
                    "9. What is your favorite place?\n"
                    "10. What is your favorite sport?\n\n"
                    "For each question Your task:\n"
                    "- Generate exactly three plausible but incorrect options.\n"
                    "- Every now and then throw in a \"none of the options\" option instead of the answer.\n"
                    "- Include the correct answer (provided by the user) in the set of options.\n"
                    "- Randomly shuffle the four options, ensuring the correct answer appears in a different position each time for each question.\n"
                   "- Do not modify or alter the correct answer provided by the user, even if it doesn't make sense.\n\n"
                    "Formatting:\n"
                    "- Return the output as a Python list of lists.\n"
                    "- Each inner list should contain exactly four options, with the correct answer in a random position.\n"
                    "- Example format:\n"
                    "[\n"
                    "  [option1, option2, option3, option4],\n"
                    "  [option1, option2, option3, option4],\n"
                    "  ...\n"
                    "]\n"
                    " The user should give you the answers to the question in the format [answerToQuestion1, answerToQuestion2, answerToQuestion3 ...]"
                    "No extra explanations, only return the Python list. No text outside the list shoudl exist as it will be fed directly to python"
                    )},
                    {"role": "user", "content": f"The answers for the questions provided by the user {', '.join(answers)}"}
                    ]
                )
            rawOutput = response['choices'][0]['message']['content']
            print("GPT Raw Output:", rawOutput)
            try:
                callback(ast.literal_eval(rawOutput))
            except Exception as e:
                messagebox.showinfo("Error", "ChatGpt failed generation. Click submit button again or try again with other values.")
                print("Error with parsing GPT output:", e)
                return None

        except Exception as e:
            print(f"Error generating quiz: {e}")
            return None
        finally:
            closeLoadingScreen()
            global score
            score = 0

    response = messagebox.askyesno("Start confirmation", "Is your friend/family ready to answer the quiz?")
    if not response:
        return None


    def postGptProcess(gptList):
        if gptList:
            # Removing the previous window from view
            perQuizWindow.withdraw()
            gptListWAnswers = [options + [answer] for options, answer in zip(gptList, answers)]
            gptList = gptListWAnswers
            print("Quiz generated successfully:", gptList)
            quizProcessing(1, gptList, [10, 5, 30, str(uuid.uuid4().int)[:8]])  
        else:
            print("Quiz generation failed.")

        print("Answers recieved:", answers)

    #Tkinter is not thread safe so we are basically running the gptcall in another and then using callback to run the fucntion above.
    #Generate and check the quiz
    threading.Thread(target=generateQuiz, args=(postGptProcess,)).start()

# 2/3 Custom quiz window
def customQuiz():
    """ Window for creating custom quiz with the option for the user to choose size, difficulty and time per question"""
    # Removing the previous window from view
    quizWindow.withdraw()
    global cusQuizWindow
    # Creating a window
    cusQuizWindow = tk.Toplevel(root)
    cusQuizWindow.geometry("600x600")
    cusQuizWindow.title("Custom Quiz")

    canvas = tk.Canvas(cusQuizWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto, anchor="nw")

    # Information text when the info button is clicked
    def infoText():
        messagebox.showinfo("Information", """   Enter the text in the 
        in the blanks below. You don't have to 
        provide a answer to the first 4 questions.
        Provide some text in the quiz detail box.
        If you want a random quiz enter a random
        character and click submit
        and we will deal with the rest. 
        Note: Information provided here is not used 
        by us but may be used by OpenAI, by clicking
        submit you agree to OpenAI's ToS.   """)

    # Information Button
    informationButton = canvas.create_image(570, 30, image=imageInfoDim, anchor="ne")
    canvas.tag_bind(informationButton, "<Button-1>", lambda event: infoText())
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(informationButton, "<Enter>", lambda event: canvas.itemconfig(informationButton, image=imageInfo))
    canvas.tag_bind(informationButton, "<Leave>", lambda event: canvas.itemconfig(informationButton, image=imageInfoDim))

    # Back Button
    backButton = canvas.create_image(30, 30, image=buttonBack, anchor="nw")
    canvas.tag_bind(backButton, "<Button-1>", lambda event: winManagerBack(2))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(backButton, "<Enter>", lambda event: canvas.itemconfig(backButton, image=buttonBackDim))
    canvas.tag_bind(backButton, "<Leave>", lambda event: canvas.itemconfig(backButton, image=buttonBack))

    # Submit Button
    submit = canvas.create_image(300, 550, image=buttonSubmit, anchor="center")
    canvas.tag_bind(submit, "<Button-1>", lambda event: submitAnswersCusQuiz(entryBoxes))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(submit, "<Enter>", lambda event: canvas.itemconfig(submit, image=buttonSubmitDim))
    canvas.tag_bind(submit, "<Leave>", lambda event: canvas.itemconfig(submit, image=buttonSubmit))

    canvas.create_text(300, 40, text="Customized Quiz", font=("Comic Sans MS Italic", 24), fill="black", anchor="n")

    # Questions
    questions = [
        "Quiz Size (Max 30)\n(Default 10)",
        "Quiz Difficulty (1-10)\n(Default 5)",
        "Time per Question (5-60 sec)\n(Default 30)",
        "Enter a Quiz Title"
    ]
    
    # Start positions
    positionY = 120
    positionX = 60
    positionXE = 350

    # Being sent to submitAnswerPerQuiz function under submit button
    entryBoxes = []

    # Displaying the questions along with entry boxes.
    for i, question in enumerate(questions):
        canvas.create_text(positionX, positionY, text=question, font=("Comic Sans MS", 12), fill="black", anchor="w")

        entryBox = tk.Entry(cusQuizWindow, font=("Comic Sans MS", 12))
        canvas.create_window(positionXE, positionY, window=entryBox, anchor="w")

        entryBoxes.append(entryBox)

        positionY += 60

    # Quiz box to enter custom details
    canvas.create_text(positionX, positionY, text="Enter what you want the quiz to be about in as much detail as possible", font=("Comic Sans MS", 12), fill="black", anchor="w")
    entryBox = tk.Text(cusQuizWindow, font=("Comic Sans MS", 12), wrap="word", width=50, height=5)
    positionY += 20
    canvas.create_window(310, positionY, window=entryBox, anchor="n")
    entryBoxes.append(entryBox)

# 2.1 Custom Quiz submit handling.
def submitAnswersCusQuiz(entryBoxes):
    inputValue1 = entryBoxes[0].get().strip()
    inputValue2 = entryBoxes[1].get().strip()
    inputValue3 = entryBoxes[2].get().strip()
    inputValue4 = entryBoxes[3].get()

    # Default Quiz Size 10
    try:
        inputValue1 = int(inputValue1)   
    except ValueError:
        inputValue1 = 10

    # Default Quiz Difficulty
    try:
        inputValue2 = int(inputValue2)
    except ValueError:
        inputValue2 = 5

    # Default Quiz Time
    try:
        inputValue3 = int(inputValue3)
    except ValueError:
        inputValue3 = 30

    # Keeping quiz size between 1 and 30
    if inputValue1 > 30:
        inputValue1 = 30
    elif inputValue1 < 0:
        inputValue1 = 1

    # Keeping Quiz Difficulty between 1 and 10
    if inputValue2 > 10:
        inputValue2 = 10
    elif inputValue2 < 1:
        inputValue2 = 1

    # Keeping Quiz Time between 1 and 60
    if inputValue3 > 60:
        inputValue3 = 60
    elif inputValue3 < 5:
        inputValue3 = 5 
    
    if entryBoxes[3].get().strip() == "":
        inputValue4 = str(uuid.uuid4().int)[:8]

    # Incase user enters nothing
    if entryBoxes[4].get("1.0", "end-1c").strip() == "":
        messagebox.showinfo("Information", """       Enter what you would like the quiz
        to be about. If you wish for a random quiz 
        you can enter a random character above and will
        be given a random quiz.""")
        return

    answers = [inputValue1, inputValue2, inputValue3, inputValue4, entryBoxes[4].get("1.0", "end-1c").strip()]
    quizLoadingScreen()

    def generateQuiz(callback):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": (
                    "You are an assistant that generates quiz questions. "
                    "Please provide the quiz questions in this exact Python list format:\n\n"
                    "[[question, option1, option2, option3, option4, answer], "
                    "[question, option1, option2, option3, option4, answer], ...]\n\n"
                    "For each question:\n"
                    "- Include exactly four answer options.\n"
                    "- The correct answer should be the sixth element in each list.\n\n"
                    "Additional parameters:\n"
                    f"- Quiz size: {answers[0]} questions\n"
                    f"- Difficulty: {answers[1]} out of 10\n"
                    "Adjust quiz difficulty based on a scale of 1 to 10"
                    f"- Time per question: {answers[2]} seconds\n"
                    "If the user requests something that violates OpenAI's policy or invalid data, "
                    "generate a random quiz using the default values. "
                    "Return only the list in the specified format without extra explanations."
                    )},
                    {"role": "user", "content": f"Quiz Title: {answers[3]}\nQuiz Data: {answers[4]}"}
                ]
            )
    
            rawOutput = response['choices'][0]['message']['content']
   
            try:
                quizData = ast.literal_eval(rawOutput)

                # Validate response format
                if all(isinstance(q, list) and len(q) == 6 for q in quizData):
                    callback(quizData)
                else:
                    raise ValueError("Incorrect format: Each question should have exactly 6 elements.")

            except (ValueError, SyntaxError) as e:
                # Handle parsing errors or format issues
                messagebox.showinfo("Error", "ChatGpt failed generation. Click submit button again or try again with other values.")
                print("Error parsing quiz data:", e)
                print("Response received:", rawOutput)
                return None
        
        except openai.error.OpenAIError as e:
            messagebox.showinfo("Error", "ChatGpt failed generation. Click submit button again or try again with other values.")
            # Handle API-specific errors
            print("Error communicating with OpenAI API:", e)
            return None
        finally:
            closeLoadingScreen()
            global score
            score = 0 

    def postGptProcess(gptList):
        if gptList:
            # Removing the previous window from view
            cusQuizWindow.withdraw()
            print("Quiz generated successfully:", gptList)
            quizProcessing(2, gptList, answers)
        else:
            print("Quiz generation failed.")

        print("Answers recieved:", answers)

    #Tkinter is not thread safe so we are basically running the gptcall in another and then using callback to run the fucntion above.
    #Generate and check the quiz
    threading.Thread(target=generateQuiz, args=(postGptProcess,)).start()

# 3/3 Random quiz window
def randomQuiz():
    # Removing the previous window from view
    quizWindow.withdraw()
    global ranQuizWindow
    # Creating the window
    ranQuizWindow = tk.Toplevel(root)
    ranQuizWindow.geometry("600x600")
    ranQuizWindow.title("Random Quiz")

    canvas = tk.Canvas(ranQuizWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto, anchor="nw")

     # Information text when the info button is clicked
    def infoText():
        messagebox.showinfo("Information", """Select a topic that you want to be quized on""")

    # Information Button
    informationButton = canvas.create_image(570, 30, image=imageInfoDim, anchor="ne")
    canvas.tag_bind(informationButton, "<Button-1>", lambda event: infoText())
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(informationButton, "<Enter>", lambda event: canvas.itemconfig(informationButton, image=imageInfo))
    canvas.tag_bind(informationButton, "<Leave>", lambda event: canvas.itemconfig(informationButton, image=imageInfoDim))

    # Back Button
    backButton = canvas.create_image(30, 30, image=buttonBack, anchor="nw")
    canvas.tag_bind(backButton, "<Button-1>", lambda event: winManagerBack(3))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(backButton, "<Enter>", lambda event: canvas.itemconfig(backButton, image=buttonBackDim))
    canvas.tag_bind(backButton, "<Leave>", lambda event: canvas.itemconfig(backButton, image=buttonBack))

    canvas.create_text(300, 40, text="Randomized Quiz", font=("Comic Sans MS Italic", 24), fill="black", anchor="n")

    # 100 random topics
    randomTopics100 = [
    "Space", "Ancient History", "Capitals", "Inventors", "Literature", 
    "Anatomy", "Math Basics", "World War II", "Mythology", "Shakespeare", 
    "Scientists", "Geography", "Movies", "Animals", "Oceans", 
    "History", "Physics", "Chemistry", "Art", "Computer Science", 
    "Music", "Explorers", "Environment", "Egypt", "Astronomy", 
    "Psychology", "Technology", "Health", "Sports", "Olympics", 
    "Landmarks", "Renaissance", "Painters", "Religions", "Evolution", 
    "Energy", "Architecture", "Medieval Era", "Politics", "Marine Biology", 
    "Creatures", "Climate", "Botany", "Cloud Tech", "Programming", 
    "Space Missions", "Robotics", "Musicians", "Economics", "Poetry", 
    "Battles", "US Presidents", "Royalty", "Endangered Animals", "Languages", 
    "Quantum Physics", "Discoveries", "Solar System", "Math Theorems", "Philosophy", 
    "Ecosystems", "Fashion", "Cuisine", "Novels", "Dinosaurs", 
    "AI", "Electric Cars", "Monuments", "Medieval Europe", "Rivers", 
    "Nutrition", "Parks", "Engineers", "TV Shows", "Physics Laws", 
    "Cryptos", "Mathematicians", "Telescopes", "Human Rights", "Biochemistry", 
    "Politics", "Jazz", "India", "Global Economics", "Philosophers", 
    "Social Media", "Heritage Sites", "Sculptures", "Renewables", "Warfare", 
    "Conservation", "Festivals", "Disorders", "Machine Learning", "Algebra", 
    "European Union", "Board Games", "Agriculture", "Genetics", "Rome", 
    "Classical Music", "Inventions", "Algorithms", "Sound Physics", "Mountains"
    ]
    # Getting 10 random topics
    randomTopics = random.sample(randomTopics100, 10)

    buttonFont = ("Comic Sans MS Italic", 16, "bold")
    buttonImage = buttonMenu2
    buttonFg = "#ffffff"
    buttonHoverFg = "#999999"

    # Responsive effect changing to dimmer image.
    def onEnter(e):
        e.widget.config(fg=buttonHoverFg)

    def onLeave(e):
        e.widget.config(fg=buttonFg)

    # Displaying the questions along with entry boxes.
    for i, randomVal in enumerate(randomTopics):
        if i < 5:
            relxPos = 0.25
            relyPos = 0.15 * (i + 1.6)
        else:
            relxPos = 0.75
            relyPos = 0.15 * ((i - 5) + 1.6)

        button = tk.Button(ranQuizWindow, text=randomVal, image=buttonImage, compound="center", font=buttonFont, fg=buttonFg, 
        activeforeground=buttonHoverFg, borderwidth = 0, highlightthickness=0, width=220, height=60, command=lambda randomVal=randomVal:submitAnswersRanQuiz(randomVal))
        button.place(relx=relxPos, rely=relyPos, anchor="center") 
        button.bind("<Enter>", onEnter)
        button.bind("<Leave>", onLeave)


    print(randomTopics)

def submitAnswersRanQuiz(ranTopic):
    # Removing the previous window from view
    ranQuizWindow.withdraw()
    global ranQuizWindow2
    # Creating the window
    ranQuizWindow2 = tk.Toplevel(root)
    ranQuizWindow2.geometry("600x600")
    ranQuizWindow2.title("Random Quiz")

    canvas = tk.Canvas(ranQuizWindow2, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto, anchor="nw")

    # Information text when the info button is clicked
    def infoText():
        messagebox.showinfo("Information", """   Enter the text in the 
        in the blanks below. You don't have to 
        provide a answer. It will default to 
        certain values if you dont.
        Note: Information provided here is not used 
        by us but may be used by OpenAI, by clicking
        submit you agree to OpenAI's ToS.   """)

    # Information Button
    informationButton = canvas.create_image(570, 30, image=imageInfoDim, anchor="ne")
    canvas.tag_bind(informationButton, "<Button-1>", lambda event: infoText())
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(informationButton, "<Enter>", lambda event: canvas.itemconfig(informationButton, image=imageInfo))
    canvas.tag_bind(informationButton, "<Leave>", lambda event: canvas.itemconfig(informationButton, image=imageInfoDim))

    # Back Button
    backButton = canvas.create_image(30, 30, image=buttonBack, anchor="nw")
    canvas.tag_bind(backButton, "<Button-1>", lambda event: winManagerBack(5))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(backButton, "<Enter>", lambda event: canvas.itemconfig(backButton, image=buttonBackDim))
    canvas.tag_bind(backButton, "<Leave>", lambda event: canvas.itemconfig(backButton, image=buttonBack))

    # Submit Button
    submit = canvas.create_image(300, 550, image=buttonSubmit, anchor="center")
    canvas.tag_bind(submit, "<Button-1>", lambda event: submitAnswersRanQuiz2(entryBoxes, ranTopic))
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(submit, "<Enter>", lambda event: canvas.itemconfig(submit, image=buttonSubmitDim))
    canvas.tag_bind(submit, "<Leave>", lambda event: canvas.itemconfig(submit, image=buttonSubmit))

    canvas.create_text(300, 40, text="Random Quiz Settings", font=("Comic Sans MS Italic", 24), fill="black", anchor="n")

    # Questions
    questions = [
        "Quiz Size (Max 30)\n(Default 10)",
        "Quiz Difficulty (1-10)\n(Default 5)",
        "Time per Question (5-60 sec)\n(Default 30)"
    ]
    
    # Start positions
    positionY = 225
    positionX = 90
    positionXE = 330

    # Being sent to submitAnswerRanQuiz2 function under submit button
    entryBoxes = []

    # Displaying the questions along with entry boxes.
    for i, question in enumerate(questions):
        canvas.create_text(positionX, positionY, text=question, font=("Comic Sans MS", 12), fill="black", anchor="w")

        entryBox = tk.Entry(ranQuizWindow2, font=("Comic Sans MS", 12))
        canvas.create_window(positionXE, positionY, window=entryBox, anchor="w")

        entryBoxes.append(entryBox)

        positionY += 60
    
def submitAnswersRanQuiz2(entryBoxes, ranTopic):
    inputValue1 = entryBoxes[0].get().strip()
    inputValue2 = entryBoxes[1].get().strip()
    inputValue3 = entryBoxes[2].get().strip()
    inputValue4 = ranTopic

    # Default Quiz Size 10
    try:
        inputValue1 = int(inputValue1)   
    except ValueError:
        inputValue1 = 10

    # Default Quiz Difficulty
    try:
        inputValue2 = int(inputValue2)
    except ValueError:
        inputValue2 = 5

    # Default Quiz Time
    try:
        inputValue3 = int(inputValue3)
    except ValueError:
        inputValue3 = 30

    # Keeping quiz size between 1 and 30
    if inputValue1 > 30:
        inputValue1 = 30
    elif inputValue1 < 0:
        inputValue1 = 1

    # Keeping Quiz Difficulty between 1 and 10
    if inputValue2 > 10:
        inputValue2 = 10
    elif inputValue2 < 1:
        inputValue2 = 1

    # Keeping Quiz Time between 1 and 60
    if inputValue3 > 60:
        inputValue3 = 60
    elif inputValue3 < 5:
        inputValue3 = 5 

    answers = [inputValue1, inputValue2, inputValue3, inputValue4]

    ranQuizWindow.withdraw()
    quizLoadingScreen()

    def generateQuiz(callback):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": (
                    "You are an assistant that generates quiz questions. "
                    "Please provide the quiz questions in this exact Python list format:\n\n"
                    "[[question, option1, option2, option3, option4, answer], "
                    "[question, option1, option2, option3, option4, answer], ...]\n\n"
                    "For each question:\n"
                    "- Include exactly four answer options.\n"
                    "- The correct answer should be the sixth element in each list.\n\n"
                    "Additional parameters:\n"
                    f"- Quiz size: {answers[0]} questions\n"
                    f"- Difficulty: {answers[1]} out of 10\n"
                    f"- Time per question: {answers[2]} seconds\n"
                    "Return only the list in the specified format without extra explanations."
                    )},
                    {"role": "user", "content": f"Generate a quiz on {answers[3]}"}
                ]
            )
    
            rawOutput = response['choices'][0]['message']['content']
            print("GPT Raw Output:", rawOutput)
   
            try:
                quizData = ast.literal_eval(rawOutput)

                # Validate response format
                if all(isinstance(q, list) and len(q) == 6 for q in quizData):
                    callback(quizData)
                else:
                    raise ValueError("Incorrect format: Each question should have exactly 6 elements.")

            except (ValueError, SyntaxError) as e:
                messagebox.showinfo("Error", "ChatGpt failed generation. Click submit button again or try again with other values.")
                # Handle parsing errors or format issues
                print("Error parsing quiz data:", e)
                print("Response received:", rawOutput)
                return None
        
        except openai.error.OpenAIError as e:
            messagebox.showinfo("Error", "ChatGpt failed generation. Click submit button again or try again with other values.")
            print("Error communicating with OpenAI API:", e)
            return None
        finally:
            closeLoadingScreen()
            global score
            score = 0
    
    def postGptProcess(gptList):
        if gptList:
            # Removing the previous window from view
            ranQuizWindow2.withdraw()
            print("Quiz generated successfully:", gptList)
            quizProcessing(3, gptList, answers)
        else:
            print("Quiz generation failed.")

        print("Answers recieved:", answers)

    #Tkinter is not thread safe so we are basically running the gptcall in another and then using callback to run the fucntion above.
    #Generate and check the quiz
    threading.Thread(target=generateQuiz, args=(postGptProcess,)).start()

# Mostly for managing the windows from my end.
def quizProcessing(num = 0, gptList = None, answers = None):
    if num == 1:
        print("personalized quiz")
        quizQA(0, 1, gptList, answers)
    elif num == 2:
        print("Custom Quiz")
        quizQA(0, 2, gptList, answers)
    elif num == 3:
        print("Random Quiz")
        quizQA(0, 3, gptList, answers)

# Loading screen that runs on a seperate thread while chatgpt processes quiz
def quizLoadingScreen():
    global loadingWindow
    loadingWindow = tk.Toplevel(root)
    loadingWindow.geometry("600x600")
    loadingWindow.title("Loading...") 

    canvas = tk.Canvas(loadingWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto, anchor="nw")

    canvas.create_text(300, 100, text="Generating Your Quiz...", font=("Comic Sans MS Italic", 24), fill="black")

    progressOutline = canvas.create_rectangle(100, 300, 500, 350, outline="black", width=3)
    progressFill = canvas.create_rectangle(100, 300, 100, 350, fill="blue")

    tips = [
    "Did you know? Octopuses have 3 hearts.",
    "Did you know? Honey never spoils, ever!",
    "Did you know? Bananas are actually berries.",
    "Did you know? A group of crows is a murder.",
    "Did you know? Butterflies taste with feet.",
    "Did you know? Pineapples grow from flowers.",
    "Did you know? Hot water freezes faster!",
    "Did you know? Sloths can swim three times.",
    "Did you know? Cows have best friends too.",
    "Did you know? Rain contains vitamin B12.",
    "Did you know? Bats are the only flying mammals.",
    "Did you know? Sloths hold breath for 40 min.",
    "Did you know? Tomatoes were feared foods!",
    "Did you know? Unicorn is Scotland's animal.",
    "Did you know? Camels have three eyelids.",
    "Did you know? A giraffe's tongue is black.",
    "Did you know? An octopus has nine brains.",
    "Did you know? Cows love music; it calms them.",
    "Did you know? Some turtles breathe via butts.",
    "Did you know? Frogs can freeze without harm.",
    "Did you know? Dalmatians are born spotless.",
    "Did you know? A shrimp’s heart is in its head.",
    "Did you know? Otters hold hands while sleeping.",
    "Did you know? Tigers have striped skin too!",
    "Did you know? Venus day is longer than year!",
    "Did you know? Sea sponges are animals too!",
    "Did you know? Narwhal tusks are giant teeth.",
    "Did you know? Ants never sleep at all!",
    "Did you know? Bats always turn left to fly.",
    "Did you know? Starfish regrow their lost arms.",
    "Did you know? Snails can have 25,000 teeth.",
    "Did you know? A baby panda fits in a hand!",
    "Did you know? Horses have huge land eyes!",
    "Did you know? Giraffes sleep 30 mins daily.",
    "Did you know? Elephants hear via their feet."
    ]

    tipLabel = canvas.create_text(300, 450, text=tips[0], font=("Comic Sans MS Italic", 16), fill="black")

    def progressUpdateAndTips(progress=0, tipIndex=random.randint(0,99)):
        # Update the progress bar fill
        new_width = 100 + (progress * 40)
        canvas.coords(progressFill, 100, 300, new_width, 350)
        
        # Switch the tip every 3 seconds
        if progress % 3 == 0 and progress > 0:
            tipIndex = (tipIndex + 1) % len(tips)
            canvas.itemconfig(tipLabel, text=tips[tipIndex])

        if progress < 10:
            # Schedule next update in 1 second
            loadingWindow.after(1000, progressUpdateAndTips, progress + 1, tipIndex)
        else:
            loadingWindow.destroy()

    progressUpdateAndTips()

def closeLoadingScreen():
    global loadingWindow
    if loadingWindow:
        loadingWindow.destroy()
    
def confirmExit():
    response = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit the Quiz?")
    if response:
        root.destroy()

# To manage the windows mostly for my convience
def winManagerBack(winNum = 0):
    if winNum == 1:
        perQuizWindow.withdraw()
        startQuiz()
    elif winNum == 2:
        cusQuizWindow.withdraw()
        startQuiz()
    elif winNum == 3:
        ranQuizWindow.withdraw()
        startQuiz()
    elif winNum == 4:
        confirmExit()
    elif winNum == 5:
        ranQuizWindow2.withdraw()
        randomQuiz()
    elif winNum == 6:
        submitQuizWindow.withdraw()
        startQuiz()
 
# Main menu screen
# (Might add score board that holds previous scores.)
def startQuiz(event=None):
    """ Main menu screen with 3 quiz options and info button """
    root.withdraw()
    global quizWindow
    quizWindow = tk.Toplevel(root)
    quizWindow.geometry("600x600")
    quizWindow.title("Quiz Menu")
    
    canvas = tk.Canvas(quizWindow, width=610, height=610)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgPhoto2, anchor="nw")

    buttonFont = ("Comic Sans MS Italic", 16, "bold")
    buttonImage = buttonMenu1
    buttonFg = "#ffffff"
    buttonHoverFg = "#999999"
    buttonWidth = 300
    buttonHeight = 70

    # Function to handle button hover effects
    def onEnter(e):
        e.widget.config(fg=buttonHoverFg)

    def onLeave(e):
        e.widget.config(fg=buttonFg)

    def infoText():
        messagebox.showinfo("Information", """Welcome to the AI Quiz Game
        1) If you select Personalized Quiz, you will
           be able to create a Quiz about yourself
           to give your friends or family. You can
           use this quiz to test how well they know you.
        2) If you select the Custom Quiz option, you
           will be able to create a quiz on any topic
           of your choice. You can also give it text 
           from which it will create a quiz.
           Note: If the Quiz does not follow the TOS
           you will not be able to make a Custom Quiz
           and will be given a Quiz of a random topic.
        3) If you select the Random Quiz option, you 
           will be given the option to choose from
           10 Quiz topics. These 10 Quiz Topics are 
           randomly selected from a currated database.
                                            """)
    
    # Information Button
    informationButton = canvas.create_image(570, 30, image=imageInfoDim, anchor="ne")
    canvas.tag_bind(informationButton, "<Button-1>", lambda event: infoText())
    # Responsive effect changing to dimmer image.
    canvas.tag_bind(informationButton, "<Enter>", lambda event: canvas.itemconfig(informationButton, image=imageInfo))
    canvas.tag_bind(informationButton, "<Leave>", lambda event: canvas.itemconfig(informationButton, image=imageInfoDim))

    button1 = tk.Button(quizWindow, text="Personalized Quiz", image=buttonImage, compound="center", font=buttonFont, fg=buttonFg, 
        activeforeground=buttonHoverFg, borderwidth = 0, highlightthickness=0, width=buttonWidth, height=buttonHeight, command=personalizedQuiz)
    button1.place(relx=0.5, rely=0.3, anchor="center") 
    button1.bind("<Enter>", onEnter)
    button1.bind("<Leave>", onLeave)

    button2 = tk.Button(quizWindow, text="Custom Quiz", image=buttonImage, compound="center", font=buttonFont, fg=buttonFg,
        activeforeground=buttonHoverFg, borderwidth = 0, highlightthickness=0, width=buttonWidth, height=buttonHeight, command=customQuiz)
    button2.place(relx=0.5, rely=0.5, anchor="center")
    button2.bind("<Enter>", onEnter)
    button2.bind("<Leave>", onLeave)

    button3 = tk.Button(quizWindow, text="Random Quiz", image=buttonImage, compound="center", font=buttonFont, fg=buttonFg, 
        activeforeground=buttonHoverFg, borderwidth = 0, highlightthickness=0, width=buttonWidth, height=buttonHeight, command=randomQuiz)
    button3.place(relx=0.5, rely=0.7, anchor="center")
    button3.bind("<Enter>", onEnter)
    button3.bind("<Leave>", onLeave)

startText = canvas.create_image(300, 300, image=buttonStart, anchor="center")
canvas.create_text(300, 500, text="Click anywhere to start", font=("Comic Sans MS Italic", 20), fill="#00eaa2")

startPulse()

root.bind("<Button-1>", startQuiz) 

root.mainloop()