"""
    CSP|1.2.1 - Catch a Turtle Activity
"""

#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
color = ("red")
size = 5
shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
random_colors = ["orange", "black", "green", "magenta", "yellow", "indigo", "violet"]
random_shapes = ["square", "arrow", "triangle", "turtle"]
player_name = input("What is your name? ")
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []


#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()
spot.color(color)
spot.pensize(size)
spot.shape(shape)

# Score writer set up
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-50,-250)
score_writer.pendown()

# Counter set up
counter.hideturtle()
counter.penup()
counter.goto(50,-250)
counter.pendown()

#-----game functions--------
def spot_clicked (x,y):
  global timer
  if timer != 0:
    update_score_for_spot()
    change_position()
  else:
    spot.hideturtle()

def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.color(rand.choice(random_colors))
  spot.shape(rand.choice(random_shapes))
  spot.stamp()
  spot.color("red")
  spot.shape("circle")
  spot.penup()
  spot.hideturtle()
  spot.goto(new_xpos, new_ypos)
  spot.pendown()
  spot.showturtle()

def update_score_for_spot():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def start_game():
  global start
  if start == ("Start"):
    start = True
  else:
    start = False

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


#-----events----------------

start = input(" If you would like to play type 'Start' ")
start_game()
if start == True:
  print ("Enjoy")
elif start == False:
  print ("Okay... ;C")
  exit()

wn = trtl.Screen()
wn.bgcolor("blue")
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
