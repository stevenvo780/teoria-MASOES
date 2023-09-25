# Modelo MASOES con Simulación en Python

## ¿Qué es MASOES?

MASOES (Model of Adaptive Social and Emotional Organisms) es un modelo conceptual para simular sistemas compuestos por agentes que tienen estados emocionales y la capacidad de adaptarse a través de interacciones sociales. El modelo considera varios aspectos clave:

1. **Agente Adaptativo**: Los agentes adaptan su comportamiento en función de experiencias pasadas.
2. **Estados Emocionales**: Cada agente tiene un estado emocional que varía entre -1 (triste) y 1 (feliz).
3. **Interacción Social**: Los agentes interactúan entre sí, afectando mutuamente sus estados emocionales.
4. **Aprendizaje**: Los agentes mantienen una memoria de interacciones pasadas que influye en su comportamiento futuro.
5. **Reglas de Transición**: Se aplican reglas para modificar los estados emocionales de los agentes.
6. **Evaluación de la Adaptabilidad**: Se mide la capacidad de los agentes para adaptarse al entorno.
7. **Emergencia**: El comportamiento global del sistema emerge de las interacciones individuales de los agentes.

## Algoritmo en Python

El algoritmo en Python simula un sistema de agentes que siguen el modelo MASOES. Cada agente es modelado como una instancia de la clase `DynamicAgent`, que tiene métodos para actualizar la memoria (`update_memory`), adaptar el comportamiento (`adapt_behavior`), evaluar la adaptabilidad (`evaluate_adaptability`) y añadir ruido estocástico (`add_stochastic_noise`).

### Ejemplo de Código

```python
class DynamicAgent:
    def **init**(self):
        self.emotion = np.random.uniform(-1, 1)
        self.memory = []
        self.adaptability_score = 0
    # ... (otros métodos)
```

### Aspectos Matemáticos

- **Adaptación del Comportamiento**: Se utiliza la media de las últimas 10 interacciones, escalada por un factor de 0.4.

  ```python
  avg_memory = np.mean(self.memory) if self.memory else 0
  return np.clip(avg_memory * 0.4, -0.1, 0.1)
  ```

- **Evaluación de la Adaptabilidad**: Se usa la varianza de las interacciones pasadas como métrica de adaptabilidad.

  ```python
  self.adaptability_score = np.var(self.memory) if self.memory else 0
  ```

- **Ruido Estocástico**: Se añade un pequeño ruido aleatorio para hacer que el sistema sea más dinámico.

  ```python
  self.emotion += np.random.uniform(-0.05, 0.05)
  ```

## Visualización

El algoritmo también incluye una visualización usando Matplotlib para mostrar la evolución de los estados emocionales y las puntuaciones de adaptabilidad de los agentes a lo largo del tiempo.
