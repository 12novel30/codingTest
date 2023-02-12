def solution(genres, plays):
    answer = []
    songs,playedNum = {},{}
    
    for i, genre in enumerate(genres):
        if genre not in songs:
            songs[genre] = [[plays[i], i]]
            playedNum[genre] = plays[i]
        else:
            songs[genre].append([plays[i], i])
            playedNum[genre] += plays[i]
    
    for genre in songs.keys():
        songs[genre] = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
    genreSorted = sorted(playedNum, key=lambda x: playedNum[x], reverse=True)

    for genre in genreSorted:
        answer.append(songs[genre][0][1])
        if len(songs[genre])>=2:
            answer.append(songs[genre][1][1])
    return answer