def nota(n):
    cheia = "★"
    vazada = "☆"
    cheias = n
    vazadas = 10 - n
    res = str(f"|{cheias * cheia}{vazadas * vazada}|")
    print(res)


nota(0)
nota(3)
nota(7)