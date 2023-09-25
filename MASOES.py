import numpy as np
import matplotlib.pyplot as plt


class DynamicAgent:
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
        return np.clip(avg_memory * 0.4, -0.1, 0.1)

    def evaluate_adaptability(self):
        self.adaptability_score = np.var(self.memory) if self.memory else 0

    def add_stochastic_noise(self):
        self.emotion += np.random.uniform(-0.05, 0.05)


num_agents = 10
num_rounds = 50
dynamic_agents = [DynamicAgent() for _ in range(num_agents)]
dynamic_history = []
dynamic_adaptability_scores = []

for _ in range(num_rounds):
    emotions = [agent.emotion for agent in dynamic_agents]
    dynamic_history.append(emotions)

    for i in range(0, num_agents, 2):
        agent1, agent2 = dynamic_agents[i], dynamic_agents[i + 1]
        interaction = np.random.uniform(-0.2, 0.2)
        interaction += agent1.adapt_behavior() - agent2.adapt_behavior()
        interaction *= (1 + np.sin(agent1.emotion - agent2.emotion))
        agent1.update_memory(interaction)
        agent2.update_memory(-interaction)
        agent1.emotion, agent2.emotion = np.clip(
            agent1.emotion + interaction, -1, 1), np.clip(agent2.emotion - interaction, -1, 1)
        agent1.evaluate_adaptability()
        agent2.evaluate_adaptability()
        agent1.add_stochastic_noise()
        agent2.add_stochastic_noise()

    dynamic_adaptability_scores.append(
        [agent.adaptability_score for agent in dynamic_agents])

fig, axs = plt.subplots(2, 1, figsize=(10, 12))
dynamic_history = np.array(dynamic_history)
for i in range(num_agents):
    axs[0].plot(dynamic_history[:, i])
axs[0].set(xlabel="Ronda", ylabel="Estado Emocional",
           title="Evolución de los estados emocionales en MASOES dinámico")

dynamic_adaptability_scores = np.array(dynamic_adaptability_scores)
for i in range(num_agents):
    axs[1].plot(dynamic_adaptability_scores[:, i])
axs[1].set(xlabel="Ronda", ylabel="Puntuación de Adaptabilidad",
           title="Evolución de la adaptabilidad en MASOES dinámico")

plt.tight_layout()
plt.show()
