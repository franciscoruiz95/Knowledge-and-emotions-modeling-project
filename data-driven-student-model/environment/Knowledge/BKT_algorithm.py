import numpy as np
from  .initial_values import initial_values as I_V
import pprint
class BKT:
    def __init__(self, skill):
        #valores iniciales
        self.p_l_init = I_V[skill]['p_init']
        self.p_g = I_V[skill]['p_guess']
        self.p_s = I_V[skill]['p_slip']
        self.p_t = I_V[skill]['p_transit']
        
        self.p_l = self.p_l_init
        self.skill = skill

    def update(self, response):
        """
            P(Lt|obst = 1) = P(Lt)(1 - P(S)) / P(Lt)(1 - P(S)) + (1 - P(Lt))P(G)\n
            P(Lt|obst = 0) = P(Lt)P(S) / P(Lt)P(S) + (1 - P(Lt))(1 - P(G))\n
            \n
            P(Lt+1) = P(Lt|obst) + (1 - P(Lt|obst))P(T)
        """

        if response == 1: # Si la respuesta es correcta
            p_l_obs = (self.p_l * (1 -self.p_s)) / (self.p_l * (1 -self.p_s) + (1 -self.p_l) * self.p_g)
        else: # Si la respuesta es incorrecta
            p_l_obs = (self.p_l * self.p_s) / (self.p_l * self.p_s + (1 -self.p_l) * (1 - self.p_g))
        
        self.p_l = p_l_obs + (1 - p_l_obs) * self.p_t

    def probability(self):
        return (self.p_l * (1 -self.p_s) + (1 -self.p_l) * self.p_g)