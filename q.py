import gym
import numpy as np
from gym import spaces
from q_brain import Q_brain





if __name__ == "__main__":
 env = gym.make('ChopperCommand-ram-v0')
 #actions=env.action_spaces.sample()
 n=17   #no of actions
 actions=list(range(n))
 print(actions)
 q_brain=Q_brain(0.01,actions,0.9)
    
 for episode in range(100):
      observation=env.reset()
      while True:
    
        env.render()
        
       
        action=q_brain.choose_action(str(observation))

        observation_,reward,done,info= env.step(action)
    
        q_brain.learn(str(observation),action,reward,str(observation_))

        observation=observation_
        print('Observation {0} \nreward {1} \ndone {2}\n'.format(observation,reward,done))
       
        if done: 
           print('episode finished ')
           break
       
        
 print("GAME OVER\n")
 try:
    del env
 except ImportError:
    pass
 env.close()
 




    


