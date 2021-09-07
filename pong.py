# import libs
from time import sleep
from sense_hat import SenseHat

# init sensehat
sense = SenseHat()

# colors
background = (0, 0, 0)
white = (255, 255, 255)
blue = (5, 194, 252)

# score
score = 0

# bat
batX = 0
batY = 4
batSize = 3

# ball
ballPos = [3, 3]
ballVel = [1, 1]

# draw the bat
def drawBat():
  for tempBatY in range(batSize):
    sense.set_pixel(batX, batY + tempBatY - 1, white)

# move the bat
def moveUp(event):
  global batY
  if event.action == 'pressed' and batY > 1:
    batY -= 1

def moveDown(event):
  global batY
  if event.action == 'pressed' and batY < 6:
    batY += 1

# draw the ball
def drawBall():
  global score

  if ballPos[0] > 6:
    ballVel[0] = -ballVel[0]

  if ballPos[0] == 1 and (batY - 1) <= ballPos[1] <= (batY + 1):
    ballVel[0] = -ballVel[0]
    score += 1

  if ballPos[1] < 1:
    ballVel[1] = -ballVel[1]

  if ballPos[1] > 6:
    ballVel[1] = -ballVel[1]

  ballPos[0] += ballVel[0]
  ballPos[1] += ballVel[1]

  sense.set_pixel(ballPos[0], ballPos[1], blue)

# lose script
def checkLose():
  if ballPos[0] == 0:
    sense.set_pixel(ballPos[0], ballPos[1], blue)
    sleep(0.1)
    sense.set_pixel(ballPos[0], ballPos[1], background)
    sleep(0.1)
    sense.set_pixel(ballPos[0], ballPos[1], blue)
    sleep(0.1)
    sense.set_pixel(ballPos[0], ballPos[1], background)
    sleep(0.1)
    sense.set_pixel(ballPos[0], ballPos[1], blue)
    sleep(0.1)
    sense.set_pixel(ballPos[0], ballPos[1], background)
    sleep(0.1)

    sense.show_message("You lost. Score: " + str(score))

# main program
while True:
  sense.clear(background)

  # draw eveyrthing
  drawBat()
  drawBall()

  # check for losing position
  checkLose()

  # handle inputs
  sense.stick.direction_up = moveUp
  sense.stick.direction_down = moveDown

  # add timer
  sleep(0.25)