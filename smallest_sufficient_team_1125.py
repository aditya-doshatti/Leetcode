'''
1125. Smallest Sufficient Team
Hard

In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

https://leetcode.com/problems/smallest-sufficient-team/
'''
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        SkillIndex = dict()
        for i, skill in enumerate(req_skills):
            SkillIndex[skill] = i
        SKILLS = [0]*len(people)
        for i in range(len(people)):
            state = 0
            for skill in people[i]:
                state |= (1<<SkillIndex[skill])
            SKILLS[i] = state
        #print(SKILLS)
        Parent = dict()
        queue = collections.deque([0])
        visited = set([0])
        COMPLETE = (1 << len(req_skills))-1
        while queue:
            state = queue.popleft()
            if state == COMPLETE:
                break
            for i in range(len(people)):
                new_state = state | SKILLS[i]
                if new_state in visited:
                    continue
                visited.add(new_state)
                queue.append(new_state)
                Parent[new_state] = (state, i)
            
        ans = []
        state = COMPLETE
        while state:
            prev_state, person = Parent[state]
            ans.append(person)
            state = prev_state
        return ans
        # dic = {}
        # for i, pep in enumerate(people):
        #     dic[i] = pep
        # retVal = set()
        # for i in sorted(dic, key=lambda i: len(dic[i]), reverse=True):
        #     prev = len(req_skills)
        #     for skill in dic[i]:
        #         if skill in req_skills:
        #             req_skills.pop(req_skills.index(skill))
        #             retVal.add(i)
        #             if len(req_skills) == 0:
        #                 return retVal
