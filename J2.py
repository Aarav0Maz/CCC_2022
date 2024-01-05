def FergusonballRating(players1):
    star_rated = 0
    for player in players1:
        calculations = player[0] * 5 - player[1] * 3
        if calculations > 40:
            star_rated += 1

    return star_rated
    

def main():
#input for number of players
    n = int(input())
#list to store player stats
    players = []

    for _ in range(n):
        #points input
        p = int(input().strip())
        #foul input
        f = int(input().strip())
        #put them in a list
        players.append([p ,f])
    result = FergusonballRating(players)
    if result == n:
        print(f"{result}+")
    else:
        print(result)



if __name__ == "__main__":
    main()