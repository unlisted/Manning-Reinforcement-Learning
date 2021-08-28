
# Agent class for Manning Reinforcement Learning live class
# Morgan Baron <morgan@unlisted.org>
class Agent:
    def __init__(self):
        self.state_history = []

    def choose_action(self, action):
        pass

    def update(self, new_state):
        self.state_history.append(new_state)

    def learn(self):
        pass
