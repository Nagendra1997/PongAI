def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    if paddle_frect.pos[1]< ball_frect.pos[1]:
        return "down"
    else:
        return "up"
	
