# Wordle Solver

Solver para [Wordle](https://www.nytimes.com/games/wordle/) escrito en Python. En cada turno elige la palabra que más reduce el número de respuestas posibles.

## Cómo funciona

1. Parte con las 2.314 respuestas posibles del juego (`answers.txt`) y las 12.971 palabras aceptadas como intento (`guesses.txt`).
2. Para cada intento candidato, simula el patrón de colores (verde, amarillo, gris) que daría contra cada respuesta que sigue siendo posible, y agrupa las respuestas según ese patrón.
3. Le asigna un puntaje al intento: el tamaño promedio de esos grupos (o, en modo peor caso, el tamaño del grupo más grande).
4. Juega el intento con menor puntaje, filtra las respuestas según los colores obtenidos y repite.

El primer intento está fijo en `arise` para no recalcularlo en cada partida. También hay un modo difícil, en que solo se usan palabras que todavía pueden ser la respuesta.

## Ejemplo

Respuesta `apple` (2 = verde, 1 = amarillo, 0 = gris):

| Intento | Resultado |
|---------|-----------|
| arise   | 20002     |
| blank   | 01100     |
| ample   | 20222     |
| apple   | 22222     |

## Uso

```bash
python game.py
```

Resuelve un rango de respuestas y guarda cada partida (intentos y colores) en `results_<palabra inicial>.txt`. Las opciones (`HARD_MODE`, `WORST_CASE`, `INITIAL_GUESS`) están al inicio de `game.py`.

Para usar el solver desde otro código:

```python
from wordle import ANSWERS, get_best_guess, get_remaining_possible_answers

restantes = get_remaining_possible_answers("arise", "20002", ANSWERS)
intento, puntaje = get_best_guess(restantes)
```

## Archivos

- `wordle.py`: lógica del solver (comparación, puntaje, filtro).
- `game.py`: juega partidas completas y guarda los resultados.
- `answers.txt`, `guesses.txt`: listas de palabras.
- `results_*.txt`: partidas resueltas.
