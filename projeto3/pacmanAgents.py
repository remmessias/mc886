# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from pacman import Directions
from game import Agent
import random
import game
import util

class LeftTurnAgent(game.Agent):
    "An agent that turns left at every opportunity"

    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        current = state.getPacmanState().configuration.direction
        if current == Directions.STOP: current = Directions.NORTH
        left = Directions.LEFT[current]
        if left in legal: return left
        if current in legal: return current
        if Directions.RIGHT[current] in legal: return Directions.RIGHT[current]
        if Directions.LEFT[left] in legal: return Directions.LEFT[left]
        return Directions.STOP

class GreedyAgent(Agent):
    def __init__(self, evalFn="scoreEvaluation"):
        self.evaluationFunction = util.lookup(evalFn, globals())
        assert self.evaluationFunction != None

    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if Directions.STOP in legal: legal.remove(Directions.STOP)

        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.evaluationFunction(state), action) for state, action in successors]
        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        return random.choice(bestActions)

class GeneticAgent(Agent):
    def __init__(self, passos= ""):
        self.passos = passos
        self.posicao = 0

    def getAction(self, state):
        if self.posicao == len(self.passos):
            self.posicao = 0
        acoesPossiveis = state.getLegalPacmanActions()
        atual = state.getPacmanState().configuration.direction

        if atual == Directions.STOP: 
            atual = Directions.NORTH

        proximaAcao = self.passos[self.posicao]
        if proximaAcao == 'L':
            proximaAcao = Directions.LEFT[atual]
        else:
            proximaAcao = Directions.RIGHT[atual]

        if proximaAcao in acoesPossiveis:
            self.posicao = self.posicao + 1
            return proximaAcao

        if atual in acoesPossiveis: 
            return atual

        return Directions.REVERSE[atual]
    
    def init_state(self):
        self.posicao = 0

def scoreEvaluation(state):
    return state.getScore()
    
def timeEvaluation(state):
    return state.getScore()
