import os
import json
import tkinter as tk
from tkinter import *
import sys
import subprocess
from tkcalendar import *
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
import pandas as pd

#Few things to note:
#This program is excplicitly designed to run on MacOs. It might not size the app screens the same in windows.
#The images are included in the file the directory below has to be changed.
#Some part of the customer part of the code might give an error mostly at the end. The final text function hasnt been implemnted yet.
#Manegment part of the code should work as expected. Though I have not fully debugged most of this code.
#Like the assignment asked this is only the base source code and might not run as expected.

#Main app screen
app=Tk()
app.title("Movie Ticket System")
app.geometry("350x300")
app.config(bg="black")

#importing images as img0, img1, img2, img3, img4
#Included the images in the submission file. Have to change directory to run program
#img 4 isnt being used will implement later.
def load_image(label_width, label_height):
    Tk().withdraw()  # Hide the root Tkinter window
    img_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if img_path:
        img = Image.open(img_path)
        img = img.resize((label_width, label_height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
    else:
        return None

# Dynamically load images
img0 = load_image(350, 300)
Label(app, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

img1 = load_image(50, 50)
img2 = load_image(50, 50)
img3 = load_image(150, 100)
img4 = load_image(600, 25)

#To load data of the list of movies.
def loadData(file):
    try:
        with open(file, 'r') as file:
            return json.load(file)
    #All exceptions. Errors will be printed in message box.
    except json.JSONDecodeError:
        return
    except Exception as e:
        print(e)
        messagebox.showinfo("info", e)
        return

#Saves the data to the list of movies file.
def saveData(file, data):
    with open(file, 'w') as file:
        json.dump(data, file, indent=4)

#Location selection console for Customers
def CustomersLocationSelection():
    cusCon = Toplevel(app)
    cusCon.title("Select Cinema Branch")
    cusCon.geometry("350x300")
    #Bakcground image.
    Label(cusCon, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #Buttons to select between 3 locations
    b0 = Button(cusCon, text="New Minas", fg="red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: CustomerDateSelect("New Minas", cusCon))
    b0.grid(row=1, column=1, padx=100, pady=15)
    b0.config(borderwidth=2, relief="flat")
    b1 = Button(cusCon, text="Dartmouth", fg="red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: CustomerDateSelect("Dartmouth", cusCon))
    b1.grid(row=2, column=1, pady=15)
    b1.config(borderwidth=2, relief="flat")
    b2 = Button(cusCon, text="Halifax", fg="red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: CustomerDateSelect("Halifax", cusCon))
    b2.grid(row=3, column=1, pady=15)
    b2.config(borderwidth=2, relief="flat")

#Date selection from calender.
def CustomerDateSelect(cinema, cusCon):
    #Destroying previous window.
    cusCon.destroy()
    cusCon1 = Toplevel(app)
    cusCon1.title("Date selection")
    cusCon1.geometry("350x300")
    #Bakcground image.
    Label(cusCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #Debug
    print(cinema)

    #Label for date selection
    movieDate = Label(cusCon1, text="Select movie Date", fg="black", bg="#AADCF3", font=('Brush Script MT', 30))
    movieDate.grid(row=0, column=1, sticky=N)

    #Setting global to access later.
    global cusDateSel
    #Calender
    cusDateSel = Calendar(cusCon1, selectmode="day", year=2023, month=11, day=10)
    cusDateSel.grid(row=1, column=1)

    #Select date button moves to next function.
    getDateButton = Button(cusCon1, text="Select date", fg="blue", bg="#000066", font=('Brush Script MT', 30), command=lambda: CustomerSelection(cinema, cusCon1))
    getDateButton.grid(row=2, column=1, padx=100, pady=35)

#Movies selection for Customer using date and location.
def CustomerSelection(cinema, cusCon):
    #Getting the date from the global variable.
    date = cusDateSel.get_date()

    #debug statement.
    print(date)

    #Destroying the previous window.
    cusCon.destroy()
    cusCon1 = Toplevel(app)
    cusCon1.title("Movie selection")
    cusCon1.config(bg="navy blue")

    #Getting data from the file.
    data = loadData('movies.json')

    #Loading all movies of a specifc date and location to a list.
    movies = []
    for movie in data:
        if movie['cinema'] == cinema and movie['date'] == date:
            movies.append(movie)

    #If no movies were loaded into the list and it remains empty.
    if not movies:
        messagebox.showinfo("info", "No movies for selected cinema and date")
        cusCon1.destroy()
        return

    #Displaying the cinema location and date on top.
    Label(cusCon1, text=f"Cinema Location: {cinema}", font=('Calibri', 12)).grid(row=0, sticky=W)
    Label(cusCon1, text=f"Date: {date}", font=('Calibri', 12)).grid(row=1, sticky=W)

    #Creating a label and displaying it for all movies in the list.
    totalNumOfMovies = 0
    for index, movie in enumerate(movies):
        index = index + 2
        #Displays screenNum, movieId, title and director
        movieInfo = f"Screen: {movie['screenNum']}, Movie ID: {movie['movieId']}, Title: {movie['title']}, Director: {movie['title']}"
        Label(cusCon1, text=movieInfo, font=('Calibri', 12)).grid(row=index, sticky=W)
        totalNumOfMovies += 1

    #Creating buttons to set next to the labels
    btn1 = Button(cusCon1, text="Book this movie", command=lambda: movieBookingConsole(movies[0]), font=('Calibri', 12))
    btn1.grid(row=2, column=1, pady=5)
    btn2 = Button(cusCon1, text="Book this movie", command=lambda: movieBookingConsole(movies[1]), font=('Calibri', 12))
    btn2.grid(row=3, column=1, pady=5)
    btn3 = Button(cusCon1, text="Book this movie", command=lambda: movieBookingConsole(movies[2]), font=('Calibri', 12))
    btn3.grid(row=4, column=1, pady=5)
    btn4 = Button(cusCon1, text="Book this movie", command=lambda: movieBookingConsole(movies[3]), font=('Calibri', 12))
    btn4.grid(row=5, column=1, pady=5)

    #If only one movie exist will remove the button from the grid for the remaining 3
    if totalNumOfMovies == 1:
        btn2.grid_forget()
        btn3.grid_forget()
        btn4.grid_forget()
    #If only two movies exist will remove the button from the grid for the remaining 2
    elif totalNumOfMovies == 2:
        btn3.grid_forget()
        btn4.grid_forget()
    #If only three movies exist will remove the button from the grid for the remaining 1
    elif totalNumOfMovies == 3:
        btn4.grid_forget()

#Displaying all movie details, movie depends on what user selected in previous function.
def movieBookingConsole(movie):
    cusCon = Toplevel(app)
    cusCon.title("Movie selection")
    cusCon.config(bg="navy blue")

    #All information displayed in labels
    Label(cusCon, text=f"Date: {movie['date']}", font=('Calibri', 12)).grid(row=0, sticky=W)
    Label(cusCon, text=f"Location: {movie['cinema']}", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(cusCon, text=f"Screen: {movie['screenNum']}", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(cusCon, text=f"Movie ID: {movie['movieId']}", font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(cusCon, text=f"Movie Title: {movie['title']}", font=('Calibri', 12)).grid(row=4, sticky=W)
    Label(cusCon, text=f"Director: {movie['director']}", font=('Calibri', 12)).grid(row=5, sticky=W)
    Label(cusCon, text=f"Description: {movie['description']}", font=('Calibri', 12)).grid(row=6, sticky=W)
    Label(cusCon, text=f"Genre: {movie['genre']}", font=('Calibri', 12)).grid(row=7, sticky=W)
    Label(cusCon, text=f"Duration: {movie['duration']}", font=('Calibri', 12)).grid(row=8, sticky=W)

    #Button to move one to time select.
    Button(cusCon, text="Select time", command=lambda: timeSelection(movie, cusCon), font=('Calibri', 12)).grid(row=9, column=0, pady=5)

    #debug statement
    print(movie)

#Select a time for the seledcted movie
def timeSelection(movie, cusCon):
    #Destroying previous window
    cusCon.destroy()
    cusCon1= Toplevel(app)
    cusCon1.title("Time select")
    cusCon1.config(bg="navy blue")

    #Buttons to select time 6:00, 10:00, 14:00, 18:00, 22:00
    b0 = Button(cusCon1, text="6:00", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: seatSelection(movie, "6:00", cusCon1))
    b0.grid(row=0, column=0, pady=10)
    b0.config(borderwidth=2, relief="flat")
    b1 = Button(cusCon1, text="10:00", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: seatSelection(movie, "10:00", cusCon1))
    b1.grid(row=1, column=0, pady=10)
    b1.config(borderwidth=2, relief="flat")
    b0 = Button(cusCon1, text="14:00", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: seatSelection(movie, "14:00", cusCon1))
    b0.grid(row=2, column=0, pady=10)
    b0.config(borderwidth=2, relief="flat")
    b1 = Button(cusCon1, text="18:00", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: seatSelection(movie, "18:00", cusCon1))
    b1.grid(row=3, column=0, pady=10)
    b1.config(borderwidth=2, relief="flat")
    b1 = Button(cusCon1, text="22:00", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: seatSelection(movie, "22:00", cusCon1))
    b1.grid(row=4, column=0, pady=10)
    b1.config(borderwidth=2, relief="flat")

#Select a set for the movie at a specific time
def seatSelection(movie, time, cusCon):
    #Loading the data of the movies file
    data = loadData('movies.json')
    #Destroying previous window
    cusCon.destroy()
    cusCon1= Toplevel(app)
    cusCon1.title("Seat Selection")
    cusCon1.config(bg = "#BCE6FA")
    #Setting the screen image to the south second row and the seat image on top.
    Label(cusCon1, image=img3).grid(row=0, column=0, columnspan=10, pady=50, sticky=N)
    Label(cusCon1, image=img4).grid(row=2, column=0, columnspan=10, pady=100 , sticky=S)

    #Setting the 10 seats from A1-A10
    b0 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie ,"A1", time, cusCon1))
    b0.grid(row=1, column=0, padx=0, pady=0)
    b0.config(borderwidth=0, relief="flat")
    b1 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A2", time, cusCon1))
    b1.grid(row=1, column=1, padx=0, pady=0)
    b1.config(borderwidth=0, relief="flat")
    b2 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A3", time, cusCon1))
    b2.grid(row=1, column=2, padx=0, pady=0)
    b2.config(borderwidth=0, relief="flat")
    b3 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A4", time, cusCon1))
    b3.grid(row=1, column=3, padx=0, pady=0)
    b3.config(borderwidth=0, relief="flat")
    b4 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A5", time, cusCon1))
    b4.grid(row=1, column=4, padx=0, pady=0)
    b4.config(borderwidth=0, relief="flat")
    b5 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A6", time, cusCon1))
    b5.grid(row=1, column=5, padx=0, pady=0)
    b5.config(borderwidth=0, relief="flat")
    b6 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A7", time, cusCon1))
    b6.grid(row=1, column=6, padx=0, pady=0)
    b6.config(borderwidth=0, relief="flat")
    b7 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A8", time, cusCon1))
    b7.grid(row=1, column=7, padx=0, pady=0)
    b7.config(borderwidth=0, relief="flat")
    b8 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A9", time, cusCon1))
    b8.grid(row=1, column=8, padx=0, pady=0)
    b8.config(borderwidth=0, relief="flat")
    b9 = Button(cusCon1, image=img1, bg="#BCE6FA", height=50, width=50, command=lambda: BookingConfirmation(movie, "A10", time, cusCon1))
    b9.grid(row=1, column=9, padx=0, pady=0)
    b9.config(borderwidth=0, relief="flat")

    #Debug for later
    showTime = None
    for entry in data:
        if entry == movie:
            showTime = entry['showtimes'][time]
            break

    seats = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for seat, status in showTime:
        if status != "available":
            A1["unavailable"]
            if button:
                button.config(state="disabled", relief="sunken")

# Should create a txt file for the ticket and remove the selected seat from the options.
def BookingConfirmation(movie, seat, time, cusCon):
    cusCon.destroy()
    messagebox.showinfo("info", "Movie booked successfully!")
    #manCon1 = Toplevel(app)
    #manCon1.title("Date selection")
    #manCon1.geometry("350x300")

    data = loadData('movies.json')

    #Background set as image 0
    Label(manCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)
    # Debug for later
    for entry in data:
        if entry == movie:
            if showtimes == time:
                break

#Location selection console for Management.
def ManagementLocationSelection():
    manCon = Toplevel(app)
    manCon.title("Select Cinema Branch")
    manCon.geometry("350x300")
    #Setting background image using label
    Label(manCon, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #Buttons to select between 3 locations
    b0 = Button(manCon, text="New Minas", fg="red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: ManagementDateSelect("New Minas", manCon))
    b0.grid(row=1, column=1, padx=100, pady=15)
    b0.config(borderwidth=2, relief="flat")
    b1 = Button(manCon, text="Dartmouth", fg="red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: ManagementDateSelect("Dartmouth", manCon))
    b1.grid(row=2, column=1, pady=15)
    b1.config(borderwidth=2, relief="flat")
    b2 = Button(manCon, text="Halifax", fg="red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: ManagementDateSelect("Halifax", manCon))
    b2.grid(row=3, column=1, pady=15)
    b2.config(borderwidth=2, relief="flat")

#Date selection from calender.
def ManagementDateSelect(cinema, manCon):
    #Destroys previous window
    manCon.destroy()
    manCon1 = Toplevel(app)
    manCon1.title("Date selection")
    manCon1.geometry("350x300")
    #Background set as image 0
    Label(manCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    print(cinema)

    #Movie date selection label
    movieDate = Label(manCon1, text="Select movie Date", fg="black", bg="#AADCF3", font=('Brush Script MT', 30))
    movieDate.grid(row=0, column=1, sticky=N)

    #Setting to global to access the date in the next function
    global manDateSel
    manDateSel = Calendar(manCon1, selectmode="day", year=2023, month=11, day=10)
    manDateSel.grid(row=1, column=1)

    #Will go to the next function
    getDateButton = Button(manCon1, text="Select date", fg="blue", bg="#000066", font=('Brush Script MT', 30), command=lambda: ManagementSelection(cinema, manCon1))
    getDateButton.grid(row=2, column=1, padx=100, pady=35)

#Selection between 3 option addMovie, removeMovie and showMovie
def ManagementSelection(cinema, manCon):
    #Getting date from the global varriable and setting it
    dateForUse = manDateSel.get_date()

    #debug statement
    print(dateForUse)

    #Destoying previous window
    manCon.destroy()
    manCon1 = Toplevel(app)
    manCon1.title("Date selection")
    manCon1.geometry("350x300")
    #Background image
    Label(manCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #Buttons to go to the add movie function, remove movie fucntion and show movies function respt.
    btn0 = Button(manCon1, text="Add a Movie", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: AddMovie(cinema, dateForUse, manCon1))
    btn0.grid(row=0, column=1, padx=100, pady=15)
    btn0.config(borderwidth=2, relief="flat")
    btn1 = Button(manCon1, text="Remove a Movie", fg="blue", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: RemoveMovie(cinema, dateForUse, manCon1))
    btn1.grid(row=1, column=1, pady=15)
    btn1.config(borderwidth=2, relief="flat")
    btn2 = Button(manCon1, text="Show Movies", fg="blue", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=lambda: ShowMovie(cinema, dateForUse, manCon1))
    btn2.grid(row=2, column=1, pady=15)
    btn2.config(borderwidth=2, relief="flat")

#Add movie screen selection
def AddMovie(cinema, date, manCon):
    #Destroying previous window.
    #manCon.destroy()
    manCon1 = Toplevel(app)
    manCon1.title("Add selection")
    #Setting background image.
    Label(manCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #Creating 4 buttons for the 4 screens the button will be diabled i the screen is not available. We check screen avalibility using next function
    btn1 = Button(manCon1, text="Screen 1", command=lambda: AddMovieContinued(cinema, date, 1, manCon1), font=('Calibri', 12))
    btn1.grid(row=0, column=0, pady=5)
    if not screenAvailabilityCheck(cinema, date, 1):
        btn1.config(state='disabled')
    btn2 = Button(manCon1, text="Screen 2", command=lambda: AddMovieContinued(cinema, date, 2, manCon1), font=('Calibri', 12))
    btn2.grid(row=1, column=0, pady=5)
    if not screenAvailabilityCheck(cinema, date, 2):
        btn2.config(state='disabled')
    btn3 = Button(manCon1, text="Screen 3", command=lambda: AddMovieContinued(cinema, date, 3, manCon1), font=('Calibri', 12))
    btn3.grid(row=2, column=0, pady=5)
    if not screenAvailabilityCheck(cinema, date, 3):
        btn3.config(state='disabled')
    btn4 = Button(manCon1, text="Screen 4", command=lambda: AddMovieContinued(cinema, date, 4, manCon1), font=('Calibri', 12))
    btn4.grid(row=3, column=0, pady=5)
    if not screenAvailabilityCheck(cinema, date, 4):
        btn4.config(state='disabled')

    #To go back to previous date selection screen.
    btn5 = Button(manCon1, text="Go back(if no screens)", command=lambda: ManagementDateSelect(cinema, manCon1),font=('Calibri', 12))
    btn5.grid(row=4, column=0, pady=5)

#Checks if screen selection used in the above function
def screenAvailabilityCheck(cinema, date, screen):
    #Getting data from file
    data = loadData('movies.json')
    screen = f"Screen {screen}"

    #Checking if cinema, date, screenNum match and if they do returns false
    for entry in data:
        if entry['cinema'] == cinema and entry['date'] == date and entry['screenNum'] == screen:
            return False
    return True

#App screen to enter all movie details to add to movie list for specific day and cinema.
def AddMovieContinued(cinema, date, screen, manCon):
    #Destroy window
    manCon.destroy()

    #Debug
    print(screen)

    manCon1 = Toplevel(app)
    manCon1.title("Add selection")
    #Background set
    Label(manCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #All labels on the left of the screen before the entries. First 3 are already filled. Last 2 are also set by default.
    Label(manCon1, text="Cinema Location", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(manCon1, text="Date", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(manCon1, text="Screen Number", font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(manCon1, text="Unique Movie ID", font=('Calibri', 12)).grid(row=4, sticky=W)
    Label(manCon1, text="Title", font=('Calibri', 12)).grid(row=5, sticky=W)
    Label(manCon1, text="Director", font=('Calibri', 12)).grid(row=6, sticky=W)
    Label(manCon1, text="Description", font=('Calibri', 12)).grid(row=7, sticky=W)
    Label(manCon1, text="Genre", font=('Calibri', 12)).grid(row=8, sticky=W)
    Label(manCon1, text="Duration", font=('Calibri', 12)).grid(row=9, sticky=W)
    Label(manCon1, text="Show Times", font=('Calibri', 12)).grid(row=10, sticky=W)
    Label(manCon1, text="All Seats", font=('Calibri', 12)).grid(row=11, sticky=W)

    #ALready selected data auto displayed.
    Label(manCon1, text=cinema, font=('Calibri', 12)).grid(row=1, column=1)
    Label(manCon1, text=date, font=('Calibri', 12)).grid(row=2, column=1)
    Label(manCon1, text=screen, font=('Calibri', 12)).grid(row=3, column=1)
    entry1 = cinema
    entry2 = date
    entry3 = screen
    entry4 = Entry(manCon1)
    #entries for rest of the data
    entry4.grid(row=4, column=1)
    entry5 = Entry(manCon1)
    entry5.grid(row=5, column=1)
    entry6 = Entry(manCon1)
    entry6.grid(row=6, column=1)
    entry7 = Entry(manCon1)
    entry7.grid(row=7, column=1)
    entry8 = Entry(manCon1)
    entry8.grid(row=8, column=1)
    entry9 = Entry(manCon1)
    entry9.grid(row=9, column=1)
    Label(manCon1, text="6:00, 10:00, 14:00, 18:00, 22:00", font=('Calibri', 12)).grid(row=10, column=1)
    Label(manCon1, text="A1-A10", font=('Calibri', 12)).grid(row=11, column=1)

    #Adding all data to a list called movie to add to file in next function
    movie = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9]

    #To next function
    Button(manCon1, text="Add data", command=lambda: AddMovieData(movie, manCon1), font=('Calibri', 12)).grid(row=12, column=0, pady=5)

#Adds the movie to the list in the file
def AddMovieData(movies, manCon):
    #Getting data
    data = loadData('movies.json')

    date = movies[1]
    movieId = movies[3].get()
    cinemaScreen = movies[0]

    #Making sure the unique id for the specified date and location is unique.
    for movie in data:
        if movie['movieId'] == movieId and movie['date'] == date and movie['cinema'] == cinemaScreen:
            messagebox.showinfo("info", "Try again with unique movie id")
            return

    #Movie will be stored in the for of nested dictionaries in the list in a file.
    newMovie = {
        "cinema": movies[0],
        "date": movies[1],
        "screenNum": f"Screen {movies[2]}",
        "movieId": movies[3].get(),
        "title": movies[4].get(),
        "director": movies[5].get(),
        "description": movies[6].get(),
        "genre": movies[7].get(),
        "duration": movies[8].get(),
        "showtimes": {
            "6:00": {"A1": "available", "A2": "available", "A3": "available", "A4": "available", "A5": "available",
                     "A6": "available", "A7": "available", "A8": "available", "A9": "available", "A10": "available"},
            "10:00": {"A1": "available", "A2": "available", "A3": "available", "A4": "available", "A5": "available",
                     "A6": "available", "A7": "available", "A8": "available", "A9": "available", "A10": "available"},
            "14:00": {"A1": "available", "A2": "available", "A3": "available", "A4": "available", "A5": "available",
                     "A6": "available", "A7": "available", "A8": "available", "A9": "available", "A10": "available"},
            "18:00": {"A1": "available", "A2": "available", "A3": "available", "A4": "available", "A5": "available",
                     "A6": "available", "A7": "available", "A8": "available", "A9": "available", "A10": "available"},
            "22:00": {"A1": "available", "A2": "available", "A3": "available", "A4": "available", "A5": "available",
                     "A6": "available", "A7": "available", "A8": "available", "A9": "available", "A10": "available"}
        }

    }

    #appending to all data and rewriting the file.
    data.append(newMovie)
    saveData('movies.json', data)
    messagebox.showinfo("info", "Movie Added successfully")

    #Destroying previous window
    manCon.destroy()

#Remove movies using the unque movie id
def RemoveMovie(cinema, date, manCon):
    #Destroys the previous window
    #manCon.destroy()
    manCon1 = Toplevel(app)
    manCon1.title("Remove selection")
    #Setting background
    Label(manCon1, image=img0).place(relx=0.5, rely=0.5, anchor=CENTER)

    #Display cinema and date using labels
    Label(manCon1, text="Cinema Location", font=('Calibri', 12)).grid(row=0, sticky=W)
    Label(manCon1, text="Date", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(manCon1, text="Unique Movie ID", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(manCon1, text=cinema, font=('Calibri', 12)).grid(row=0, column=1)
    Label(manCon1, text=date, font=('Calibri', 12)).grid(row=1, column=1)

    #Askign user for the unique movie id they want to remove
    entry3 = Entry(manCon1)
    entry3.grid(row=2, column=1)

    #Goes to next function
    Button(manCon1, text="Remove movie", command=lambda: RemoveMovieContinued(cinema, date, entry3, manCon1), font=('Calibri', 12)).grid(row=3, column=0, pady=5)

#Removes the movie from the list in the file
def RemoveMovieContinued(cinema, date, movieId, manCon):
    #Getting data
    data = loadData('movies.json')

    #Getting the index where the unique id for the date and location match
    indexPos = None
    for index, movie in enumerate(data):
        if movie['cinema'] == cinema and movie['date'] == date and movie['movieId'] == movieId.get():
            indexPos = index
            break
    #If an index is found will successfullly remove it from the list.
    if indexPos is not None:
        data.pop(indexPos)
        saveData('movies.json', data)
        messagebox.showinfo("info", "Movie removed successfully")
        #Destroys previous window
        manCon.destroy()
    #If index was not found
    else:
        messagebox.showinfo("info", "Movie not found, try again")

#Shows all movies for the location and date.
def ShowMovie(cinema, date, manCon):
    #Destroys previous window
    #manCon.destroy()
    manCon1 = Toplevel(app)
    manCon1.title("Show selection")
    manCon1.config(bg = "navy blue")

    #Getting data
    data = loadData('movies.json')

    #Adppeding all movies for the date and location to a list.
    movies = []
    for movie in data:
        if movie['cinema'] == cinema and movie['date'] == date:
            movies.append(movie)

    #If the list is still empty then it will destroy the current window and tell the user no movies available.
    if not movies:
        messagebox.showinfo("info", "No movies for selected cinema and date")
        manCon1.destroy()
        return

    #Will Display on top.
    Label(manCon1, text=f"Cinema Location: {cinema}", font=('Calibri', 12)).grid(row=0, sticky=W)
    Label(manCon1, text=f"Date: {date}", font=('Calibri', 12)).grid(row=1, sticky=W)

    #Will create labels for the number of movies that were in the list created above.
    for index, movie in enumerate(movies):
        index = index + 2
        movieInfo = f"Screen: {movie['screenNum']}, Movie ID: {movie['movieId']}, Title: {movie['title']}, Director: {movie['title']}"
        Label(manCon1, text=movieInfo, font=('Calibri', 12)).grid(row=index, sticky=W)

#If file doesn't exist will create new one
if not os.path.exists('movies.json'):
    with open('movies.json', 'w') as file:
        json.dump([], file)

#Customers_console and Mangement console app
Label(app, text="Movie Booking Console", fg="black", bg="#AADCF3", font=('Brush Script MT', 30)).grid(row=0, column=1, sticky=N)
btn0 = Button(app, text="Customers", fg="Red", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=CustomersLocationSelection)
btn0.grid(row=1, column=1, padx=100, pady=35)
btn0.config(borderwidth=2, relief="flat")
btn1 = Button(app, text="Management", fg="blue", bg="#000066", font=('Brush Script MT', 20), height=2, width=12, command=ManagementLocationSelection)
btn1.grid(row=2, column=1, pady=0)
btn1.config(borderwidth=2, relief="flat")






app.mainloop()