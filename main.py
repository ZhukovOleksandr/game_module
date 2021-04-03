score_list = []
with open('score.txt', 'r') as score_result:
    for elem in score_result:
        score_list.append(elem.split(' '))
    score_result.close()
