class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves = list(moves)
        x = 0
        y = 0
        for w in moves:
            if w == 'U':
                y += 1
            elif w == 'D':
                y -= 1
            elif w == 'L':
                x -= 1
            elif w == 'R':
                x += 1
        if x == 0 and y == 0:
            return True
        else:
            return False