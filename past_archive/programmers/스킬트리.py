def solution(skill, skill_trees):
    lenOfSkill=len(skill)
    answer=0
    for i in skill_trees:
        isPossible=True
        learnPoint=0
        for skl in i:
            if skl in skill[learnPoint+1:]:
                isPossible=False
                break
            if skl==skill[learnPoint]:
                if learnPoint==lenOfSkill-1:
                    break
                else:
                    learnPoint+=1
        if (isPossible):
            answer+=1
    return answer