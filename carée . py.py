import turtle

# 1. Gadou l-mousha (turtle)
bidawi = turtle.Turtle()
bidawi.shape("turtle") # Bach t-ban lik mousha nit
bidawi.color("blue")    # Lon li bghiti

# 2. Rsem l-morabba3 (4 dyal l-adla3)
for i in range(4):
    bidawi.forward(100) # t-zid l-qdām b 100
    bidawi.left(90)     # t-dor b 90 daraja

# 3. Khalli l-fenêtre m-hloula
turtle.done()