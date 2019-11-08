# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
turtleshape = "turtle"
trutlecolor = "green"
turtlesize = 2
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#scoreboard varibles
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name")

#-----initialize turtle-----
joe = trtl.Turtle(shape = turtleshape)
joe.color(trutlecolor)
joe.shapesize(turtlesize)
joe.speed(0)

scoreboard = trtl.Turtle()
scoreboard.ht()
scoreboard.speed(0)
scoreboard.penup()
scoreboard.goto(-370,270)

font_setup = ("Arial", 30, "bold")
scoreboard.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.speed(0)
counter.goto(-270,270)
counter.ht()
counter.pendown

#------game functions------
def turtle_clicked(x,y): 
    print("joe got clicked")
    change_position()
    update_score()

def change_position():
    joe.penup()
    joe.ht()
    if not timer_up:
        joex = random.randint(-400,400)
        joey = random.randint(-300,300)
        joe.goto(joex,joey)
        joe.st()

def update_score():
    global score
    score += 1
    print(score)
    scoreboard.clear()
    scoreboard.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over ", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global joe

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, joe, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, joe, score)


#------events------

wn = trtl.Screen()
wn.bgcolor("lightblue")
joe.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()