import numpy as np
import matplotlib.pyplot as plt


class AdvancedAgent:
    def __init__(self):
        self.emotion = np.random.uniform(-1, 1)
        self.memory = []
        self.adaptability_score = 0

    def update_memory(self, interaction):
        self.memory.append(interaction)
        if len(self.memory) > 10:
            self.memory.pop(0)

    def adapt_behavior(self):
        avg_memory = np.mean(self.memory) if self.memory else 0
        return avg_memory * 0.4

    def evaluate_adaptability(self):
        self.adaptability_score = np.var(self.memory) if self.memory else 0


num_agents = 10
num_rounds = 50

advanced_agents = [AdvancedAgent() for _ in range(num_agents)]
advanced_history = []
adaptability_scores = []

for _ in range(num_rounds):
    emotions = [agent.emotion for agent in advanced_agents]
    advanced_history.append(emotions)

    for i in range(0, num_agents, 2):
        agent1, agent2 = advanced_agents[i], advanced_agents[i + 1]
        interaction = np.random.uniform(-0.2, 0.2)
        interaction += agent1.adapt_behavior() - agent2.adapt_behavior()
        interaction *= (1 + np.abs(agent1.emotion - agent2.emotion))
        agent1.update_memory(interaction)
        agent2.update_memory(-interaction)
        agent1.emotion, agent2.emotion = np.clip(
            agent1.emotion + interaction, -1, 1), np.clip(agent2.emotion - interaction, -1, 1)
        agent1.evaluate_adaptability()
        agent2.evaluate_adaptability()

    adaptability_scores.append(
        [agent.adaptability_score for agent in advanced_agents])

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

advanced_history = np.array(advanced_history)
for i in range(num_agents):
    axs[0].plot(advanced_history[:, i])
axs[0].set(xlabel="Ronda", ylabel="Estado Emocional",
           title="Evolución de los estados emocionales en MASOES")

adaptability_scores = np.array(adaptability_scores)
for i in range(num_agents):
    axs[1].plot(adaptability_scores[:, i])
axs[1].set(xlabel="Ronda", ylabel="Puntuación de Adaptabilidad",
           title="Evolución de la adaptabilidad en MASOES")

plt.tight_layout()
plt.show()
