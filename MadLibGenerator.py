from tkinter import *


def Story1(win):
    def final(tl: Toplevel, name, sports,city,playername, drinkname,snacks):
        text=f'''One day me and my friend {name} decided to play a {sports} game in {city}.
            But we were not able to play.So, we went to watch the game and our favourite player {playername}.
            We drank {drinkname} and also ate some {snacks} 
            We really enjoyed it! We are looking forward to go again and enjoy'''
        #tl.geometry(newGeometry='600x550')

        Label(tl, text='Story:',  wraplength=tl.winfo_width(),font=("Times New Romans",15),background='grey',highlightthickness=2,highlightbackground="black").place(x=50, y=400)
        Label(tl, text=text,wraplength=tl.winfo_width(),highlightthickness=2,highlightbackground="black").place(x=10, y=450)
        
        

    NewScreen= Toplevel(win, bg='yellow')
    NewScreen.title("A Memorable Day")
    NewScreen.geometry('550x620')
    Label(NewScreen, text='A Memorable Day',font=("Times New Romans",20),background='greenyellow',highlightthickness=2,highlightbackground="red" ).place(x=100,y=10)
    Label(NewScreen, text='Name:',font=("Times New Romans",10)).place(x=10,y=85)
    Label(NewScreen, text='Enter a game:',font=("Times New Romans",10)).place(x=10,y=125)
    Label(NewScreen, text='Enter a city:',font=("Times New Romans",10)).place(x=10,y=165)
    Label(NewScreen, text='Enter the name of a player:',font=("Times New Romans",10)).place(x=10,y=205)
    Label(NewScreen, text='Enter the name of a drink:',font=("Times New Romans",10)).place(x=10,y=245)
    Label(NewScreen, text='Enter the name of a snack:',font=("Times New Romans",10)).place(x=10,y=285)
    #Input
    Name=Entry(NewScreen,width=17)
    Name.place(x=250, y=85)
    game = Entry(NewScreen, width=17)
    game.place(x=250, y=125)
    city = Entry(NewScreen, width=17)
    city.place(x=250, y=165)
    player = Entry(NewScreen, width=17)
    player.place(x=250, y=205)
    drink = Entry(NewScreen, width=17)
    drink.place(x=250, y=245)
    snack = Entry(NewScreen, width=17)
    snack.place(x=250, y=285)

    SubmitButton= Button(NewScreen, text="Submit", background='Blue',font=("times",15), command=lambda:final(NewScreen, Name.get(),game.get(), city.get(), player.get(), drink.get(),snack.get()))
    SubmitButton.place(x=150, y= 345)
    # create button to implement destroy() 
    SubmitButton=Button(NewScreen, text="Back", background='Blue',font=("times",15),command=NewScreen.destroy).place(x=250, y= 345)
    NewScreen.mainloop()


def Story2(win):
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):
        text = f'''When I was a child, I wanted to become a {profession}
            but as I grew up I got into the {noun} and decided to become an
                engineer. Then I went into a job that I was not {feeling} at.
                After getting {emotion} I decided to do what I love.
                Despite getting lower{verb} than I used to get in my previous job.I am very
                feeling '''

            #tl.geometry(newGeometry='550x550')

        Label(tl, text='Story:',  wraplength=tl.winfo_width(),font=("Times New Romans",15),background='grey',highlightthickness=2,highlightbackground="black").place(x=50, y=400)
        Label(tl, text=text,wraplength=tl.winfo_width(),highlightthickness=2,highlightbackground="black").place(x=10, y=450)


    NewScreen = Toplevel(win, bg='pink')
    NewScreen.title("Ambitions")
    NewScreen.geometry('550x620')
    Label(NewScreen, text='Ambitions',font=("Times New Romans",20),background='red',highlightthickness=2,highlightbackground="black" ).place(x=100,y=10)
    Label(NewScreen, text='Enter a profession:',font=("Times New Romans",10)).place(x=10, y=125)
    Label(NewScreen, text='Enter a noun:',font=("Times New Romans",10)).place(x=10, y=165)
    Label(NewScreen, text='Enter a feeling:',font=("Times New Romans",10)).place(x=10, y=205)
    Label(NewScreen, text='Enter a emotion:',font=("Times New Romans",10)).place(x=10, y=245)
    Label(NewScreen, text='Enter a verb:',font=("Times New Romans",10)).place(x=10, y=285)
    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=125)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=165)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=205)
    Emotion= Entry(NewScreen, width=17)
    Emotion.place(x=250, y=245)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=285)
    SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 15), command=lambda:final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=345)
    SubmitButton=Button(NewScreen, text="Back", background='Blue',font=("times",15),command=NewScreen.destroy).place(x=250, y= 345)
    NewScreen.mainloop()
    

Screen = Tk()
Screen.title("Mad Libs Generator")
Screen.geometry('700x500')
Screen.config(bg="skyblue")
Label(Screen, text='Mad Libs Generator',background='light blue',highlightthickness=1,highlightbackground="black", font=("Times New Roman",40)).place(x=150,y=20)
Story1Button=Button(Screen, text='Memorable Day',font=("Times New Roman",18),command=lambda:Story1(Screen),bg="red")
Story1Button.place(x=280,y=190)
Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 18),command=lambda:Story2(Screen), bg='Blue')
Story2Button.place(x=280, y=290)
#Screen.update()
Screen.mainloop()
