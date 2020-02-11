import pandas as pd,numpy as np

class Q_brain:
       def __init__(self,learningrate,actions,discount):
              self.lr=learningrate
              self.actions=actions
              self.discount=discount
              self.i=0
              self.stateind=[]
              self.stateind.append(self.i)
              self.q_table=pd.DataFrame(columns=[0,1])
       def choose_action(self,observations):
          if (np.random.uniform() < 0.9):
            
             print('reached1\n')    
             self.check_if_state_exist(observations)

             state_action=self.q_table.loc[observations,:]
             state_action=np.random.permutation(state_action.index)
            


             action=np.argmax(state_action)

          else: action=np.random.choice(self.actions)
          return action
       def learn(self,s,a,r,s1):  #q-learning policy
           try:
              self.q_table[s,a]+=self.lr(r+self.discount*self.q_table[s1,:].max()-self.q_table[s,a])
           except KeyError:pass
       def check_if_state_exist(self,state):
           try:
               print(self.q_table.columns)
               if state not in self.q_table.index:
                     self.q_table = self.q_table.append(pd.Series([0]*len(self.actions),index=self.q_table.columns,name=state,))
           except (KeyError,TypeError,ValueError): 
                    print('ignore')
                    pass
     

