import pgzrun

WIDTH = 1000
HEIGHT = 600

# Rect(x, y, width, height)
player_left = Rect(20, 20, 20, 50)
player_right = Rect(WIDTH - 20 - 20, 20, 20, 50)
ball = Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)

x_speed = 1
y_speed = 1

score_left = 0
score_right = 0

def update():
    global x_speed, y_speed, score_left, score_right

    if ball.right > WIDTH:
        score_left += 1
        ball.x = WIDTH / 2 - 10
        ball.y = HEIGHT / 2 - 10
        x_speed *= -1
    if ball.left < 0:
        score_right += 1
        ball.x = WIDTH / 2 - 10
        ball.y = HEIGHT / 2 - 10
        x_speed *= -1

    # Ball movement
    ball.x += x_speed
    ball.y += y_speed
    if ball.bottom > HEIGHT or ball.top < 0:
        y_speed *= -1
    if ball.colliderect(player_left) or ball.colliderect(player_right):
        x_speed *= -1

    # Players movement
    if keyboard.w:
        player_left.y -= 5
    if keyboard.s:    
        player_left.y += 5
    if keyboard.up:
        player_right.y -= 5
    if keyboard.down:    
        player_right.y += 5
    

    # Limit players movement
    if player_left.top < 0:
        player_left.top = 0
    if player_left.bottom > HEIGHT:
        player_left.bottom = HEIGHT
    if player_right.top < 0:
        player_right.top = 0
    if player_right.bottom > HEIGHT:
        player_right.bottom = HEIGHT


def draw():
    screen.clear()
    screen.fill('white')
    screen.draw.filled_rect(player_left, 'yellow')
    screen.draw.filled_rect(player_right, 'yellow')
    screen.draw.filled_rect(ball, 'red')

    screen.draw.text(
        str(score_left),
        (WIDTH / 2 - 50, 20),
        color = 'yellow',
        fontsize = 100
    )
    screen.draw.text(
        ':',
        (WIDTH / 2, 20),
        color = 'black',
        fontsize = 100
    )
    screen.draw.text(
        str(score_right),
        (WIDTH / 2 + 50, 20),
        color = 'yellow',
        fontsize = 100
    )

pgzrun.go()
