class Solution(object):
    def interpret(self, command):
       command= command.replace("()", "o").replace("(al)","al")
       return command
        