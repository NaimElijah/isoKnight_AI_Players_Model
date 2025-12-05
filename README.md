## ♞ IsoKnight — Two-Player Adversarial Search Game

This project implements **search algorithms for the IsoKnight game**, a deterministic, turn-based, two-player strategy game inspired by the knight piece in chess.
Two players alternate turns moving across the board using knight-like moves, and **visited squares cannot be revisited**.
A player loses when they have **no legal moves left**.

The goal of this project is to implement and compare:

* Full **Minimax** search
* **Alpha-Beta Pruning** optimization
* **Heuristic Alpha-Beta Search** with depth limit
* Custom **heuristic evaluation functions**

---

# 📁 Project Structure

```
.
├── alpha_beta_isoKnight.py
├── heuristic_alpha_beta_isoKnight.py
├── heuristics.py
├── minimax_isoKnight.py
├── game_engine.py
├── game_state.py
├── player_agent.py
└── README.md
```

---

## 📌 File Overview

### **`game_state.py`**

Handles all game logic:

* Board representation
* Player locations
* Legal move generation (`potential_moves`)
* Game tree expansion (`get_moves`)
* Terminal state detection
* Applying moves
* Scoring terminal states (+1000 / –1000 from Player 1’s perspective)

Source: 

---

### **`player_agent.py`**

Implements the Strategy design pattern:

* `player_agent` → uses minimax / alpha-beta
* `player_agent_heuristics` → uses alpha-beta *with* heuristics and depth limit

Source: 

---

### **`minimax_isoKnight.py`**

Baseline full-search algorithm (no pruning):

* `maximin` → MAX (Player 1) node
* `minimax` → MIN (Player 2) node

Source: 

---

### **`alpha_beta_isoKnight.py`**

Optimized Minimax with **alpha-beta pruning**:

* `alphabeta_max` → entry point for Player 1
* `alphabeta_min` → entry point for Player 2
* `a_b_maximin` / `a_b_minimax` → recursive search with pruning
* Prunes branches using α ≥ β conditions
* Returns `(value, None)` when pruning (as required by assignment)

Source: 

---

### **`heuristic_alpha_beta_isoKnight.py`**

Depth-limited alpha-beta search with heuristic evaluation:

* Uses cutoff when `depth == 0`
* Returns heuristic score instead of terminal score
* Implements:

  * `alphabeta_max_h`
  * `alphabeta_min_h`
  * `a_b_heu_maximin`
  * `a_b_heu_minimax`

Source: 

---

### **`heuristics.py`**

Contains the project’s evaluation functions:

* **`base_heuristic`**

  * Computes: `p1_moves - p2_moves`
  * Measures immediate mobility advantage

* **`advanced_heuristic`**
  A stronger evaluation combining:

  * Direct mobility
  * Secondary mobility (future move potential)
  * Positional distance between players
  * Edge penalties
  * Weighted sum for improved tournament performance

Source: 

---

### **`game_engine.py`**

Provides a simple interface to **run matches** between strategies:

* `play_with_minimax()`
* `play_with_alpha_beta()`
* `play_with_heuristics()`
* `play_with_advanced_heuristics()`

Each mode initializes a board, creates player agents, and executes full gameplay with printed states.

Source: 

---

# 🎮 How to Run the Game

### 1. **Run using Minimax**

```bash
python game_engine.py
```

Uncomment inside `if __name__ == '__main__':`:

```python
play_with_minimax()
```

### 2. **Run using Alpha-Beta Pruning**

```python
play_with_alpha_beta()
```

### 3. **Run using Heuristic Alpha-Beta**

```python
play_with_heuristics()
```

### 4. **Run with Advanced Heuristics**

```python
play_with_advanced_heuristics()
```

---

# 🧠 Algorithms Implemented

## ✔️ Minimax (Exhaustive search)

* Explores full game tree
* Guarantees optimal play
* Used for very small boards (e.g., 3×3, 4×4)

---

## ✔️ Alpha-Beta Pruning

* Prunes branches that cannot affect the final result
* Greatly reduces computation
* Required for board sizes ≥ 5×5

---

## ✔️ Heuristic Alpha-Beta (Depth-Limited)

Used for larger boards (6×6 and above):

* Limited depth search
* Static evaluation at cutoff depth
* Faster and scalable

---

# 🤖 Heuristic Design

### **Base Heuristic**

`p1_moves - p2_moves`
Measures immediate mobility advantage.

### **Advanced Heuristic**

Weighted combination of:

* The Base Heuristic
* Mobility
* Future mobility
* Distance control
* Edge restriction
* Board-control balance

Designed to win head-to-head tournaments.

---

# 🧪 Testing

You can test different settings by:

* Changing board size
* Changing depth limits
* Switching base vs. advanced heuristics
* Running matches repeatedly to compare strategies

---

# 📜 License

This project is intended for educational and portfolio use.
Developed focusing on search algorithms and adversarial reasoning.

---
