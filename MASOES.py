import numpy as np
import matplotlib.pyplot as plt

# Definición de la clase DynamicAgent, que representa un agente en el modelo MASOES.
# Cada agente tiene un estado emocional, una memoria de interacciones y una puntuación de adaptabilidad.


class DynamicAgent:
    def __init__(self):
        # Estado emocional inicial aleatorio entre -1 y 1.
        self.emotion = np.random.uniform(-1, 1)
        # Lista vacía para almacenar las últimas 10 interacciones.
        self.memory = []
        # Puntuación inicial de adaptabilidad.
        self.adaptability_score = 0

    # Función para actualizar la memoria del agente con la interacción más reciente.
    def update_memory(self, interaction):
        self.memory.append(interaction)
        if len(self.memory) > 10:
            self.memory.pop(0)

    # Función que calcula el comportamiento adaptativo del agente basado en la media de las interacciones pasadas.
    def adapt_behavior(self):
        avg_memory = np.mean(self.memory) if self.memory else 0
        # Limita el impacto de la adaptabilidad para evitar cambios extremos.
        return np.clip(avg_memory * 0.4, -0.1, 0.1)

    # Función que evalúa la adaptabilidad usando la varianza de las interacciones almacenadas en la memoria.
    def evaluate_adaptability(self):
        self.adaptability_score = np.var(self.memory) if self.memory else 0

    # Función que añade un ruido estocástico al estado emocional para evitar el estancamiento.
    def add_stochastic_noise(self):
        self.emotion += np.random.uniform(-0.05, 0.05)


# Número de agentes y rondas en la simulación.
num_agents = 10
num_rounds = 50

# Inicialización de agentes.
dynamic_agents = [DynamicAgent() for _ in range(num_agents)]
# Listas para almacenar la historia de estados emocionales y puntuaciones de adaptabilidad.
dynamic_history = []
dynamic_adaptability_scores = []

# Bucle principal de la simulación.
for _ in range(num_rounds):
    # Almacenar los estados emocionales actuales de todos los agentes.
    emotions = [agent.emotion for agent in dynamic_agents]
    dynamic_history.append(emotions)

    # Bucle a través de pares de agentes para hacer que interactúen.
    for i in range(0, num_agents, 2):
        agent1, agent2 = dynamic_agents[i], dynamic_agents[i + 1]

        # Interacción básica aleatoria.
        interaction = np.random.uniform(-0.2, 0.2)

        # Ajuste de la interacción basado en el comportamiento adaptativo de los agentes.
        interaction += agent1.adapt_behavior() - agent2.adapt_behavior()

        # Ajuste adicional usando una función sinusoidal para capturar la dinámica social compleja.
        interaction *= (1 + np.sin(agent1.emotion - agent2.emotion))

        # Actualizar la memoria y el estado emocional de los agentes.
        agent1.update_memory(interaction)
        agent2.update_memory(-interaction)
        agent1.emotion, agent2.emotion = np.clip(
            agent1.emotion + interaction, -1, 1), np.clip(agent2.emotion - interaction, -1, 1)

        # Evaluar la adaptabilidad de los agentes.
        agent1.evaluate_adaptability()
        agent2.evaluate_adaptability()

        # Añadir ruido estocástico.
        agent1.add_stochastic_noise()
        agent2.add_stochastic_noise()

    # Almacenar las puntuaciones de adaptabilidad de todos los agentes.
    dynamic_adaptability_scores.append(
        [agent.adaptability_score for agent in dynamic_agents])

# Visualización de los resultados.
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Gráfico de la evolución de los estados emocionales.
dynamic_history = np.array(dynamic_history)
for i in range(num_agents):
    axs[0].plot(dynamic_history[:, i])
axs[0].set(xlabel="Ronda", ylabel="Estado Emocional",
           title="Evolución de los estados emocionales en MASOES dinámico")

# Gráfico de la evolución de las puntuaciones de adaptabilidad.
dynamic_adaptability_scores = np.array(dynamic_adaptability_scores)
for i in range(num_agents):
    axs[1].plot(dynamic_adaptability_scores[:, i])
axs[1].set(xlabel="Ronda", ylabel="Puntuación de Adaptabilidad",
           title="Evolución de la adaptabilidad en MASOES dinámico")

plt.tight_layout()
plt.show()
