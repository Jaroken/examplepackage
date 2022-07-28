import random
import pandas as pd

class random_dataframe:
    def __init__(self, length=10):
        """ generates an empty dataframe to be populated with random variables of x
        param: length: number rows to create for the dataframe (default 10)
        """

        self.df = pd.DataFrame()
        self.length = length

    def add_random_columns(self, n=1):
        """ make a random column of name, length, and number type.
         :param n: number of columns to add (int)"""

        pos1 = ['monkey', 'bug', 'ant', 'gorilla', 'banana', 'pizza', 'dog', 'fruit', 'topic', 'gentry']
        pos2 = ['yawn', 'jump', 'swim', 'run', 'walk', 'kick', 'punch', 'pick', 'stretch', 'break']
        pos3 = ['boy', 'girl', 'pasta', 'salad', 'rhino', 'youtube', 'google', 'apple', 'meta', 'netflix']

        def one_to_ten():
            """ returns a random number from 1 to 10"""
            x = random.randint(1,10)
            return(x)

        for k in range(n):

            rand_name = pos1[one_to_ten()-1]+'_'+pos2[one_to_ten()-1]+'_'+pos3[one_to_ten()-1]+'_'+str(one_to_ten())

            self.df[rand_name] = [one_to_ten() for i in range(self.length)]



