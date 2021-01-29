class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #n parentheses > n pairs
        final = []
        #l
        def traverse(s, openp, closedp):
            #leaf, finished
            if len(s) == 2*n:
                final.append(s)
                return
            #if we have open parenthesis left to place
            #branch into opening another or closing this one
            if openp < n:
                traverse(s+'(', openp+1, closedp)
            if closedp < openp:
                traverse(s+')', openp, closedp+1)
        traverse('', 0, 0)
        return final