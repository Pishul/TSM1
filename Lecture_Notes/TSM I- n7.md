Here is the precise, academic English transcription of the lecture notes extracted directly from the provided images, keeping strict structural layout and proper math notation in LaTeX.

## Thermodynamics and Statistical Mechanics I: Lecture 10

### Review

- **For an Isothermal Process involving an Ideal Gas:**
    
    $$\Delta Q \Big\vert{}_{\text{isothermal}} = R T \ln \frac{V_2}{V_1} \quad (\text{per mole, } n_m = 1)$$
    
    $$\Delta T = 0 \quad , \quad V_1 \to V_2 \quad (\text{Reversible Process})$$
    
- **For an Adiabatic Process involving an Ideal Gas:**
    
    $$\delta Q \Big\vert{}_{\text{ad.}} = 0 \implies dU = \delta w$$
    
    $$\begin{cases} dU = C_v \, dT \\ \delta w = -p \, dV \end{cases} \implies \left. T V^{\gamma-1} \right\vert{}_{\text{ad.}} = \text{const.}$$
    
    $$\gamma = \frac{C_p}{C_v} > 1$$
    

Since $C_p > C_v$ and $\gamma > 1$ for an ideal gas, calculating directly from $U_{\text{ideal}} = \frac{3}{2} n_m R T$ for a monatomic gas yields:

$$\left. p V^\gamma \right\vert{}_{\text{ad.}} = \text{const.}$$

On a $p\text{-}V$ plane, comparing an isotherm ($pV = \text{const.}$) and an adiabat ($pV^\gamma = \text{const.}$):

- The slope of the adiabat is steeper than the slope of the isotherm.
    

```
  p ^
    |    \  Isotherm (T2)
    |  .  \
    |   \  \  Adiabat
    |    \  \
    +-------------------> V
```

### The Second Law of Thermodynamics

#### Context

Recall that the First Law establishes the conservation of energy and introduces a state function, internal energy ($U$). However, it does not restrict the direction of natural processes. The objective of the Second Law is to define this directional constraint, particularly regarding heat engines.

A **Heat Engine** is a cyclic device operating between a temperature difference ($\Delta T$) that absorbs heat from a high-temperature reservoir ($T_h$) and converts a fraction of it into extracted work ($W$), rejecting the remainder to a low-temperature reservoir ($T_l < T_h$).

Historically, two primary, logically equivalent statements define the Second Law of Thermodynamics:

#### I. Clausius' Statement

> It is impossible to construct a device that operates in a cycle and produces no other effect than the transfer of heat from a cooler body to a warmer body.

Heat spontaneously flows from a hot body to a cold body. To reverse this process and move heat from a cold body to a hot body, external mechanical work must be performed on the system (e.g., a refrigerator). A refrigerator operating in isolation without external energy input is impossible.

#### II. Kelvin's Statement

> It is impossible to deliver a device that operates in a cycle and performs net mechanical work while exchanging heat with only a single thermal reservoir.

No thermodynamic process is possible whose sole result is the complete conversion of heat into work ($100\%$ efficiency).

- **Work $\to$ Heat:** Completely possible in a single direction.
    
- **Heat $\to$ Work:** Completely conversion in a continuous cycle is impossible.
    

The goal is to prove that these two statements are logically equivalent and represent the same physical limitation. Note that heat engines must perform cycles to ensure continuous operation, meaning the working material returns periodically to its initial state.

### The Carnot Engine

A Carnot engine is a idealized thermodynamic system that operates on a reversible cyclic sequence known as the **Carnot Cycle**. It contains a working substance (such as an ideal gas) and operates between two thermal reservoirs ($T_h$ and $T_l$).

The cycle consists of four distinct, reversible steps:

1. $\vec{AB}$: Isothermal expansion at $T_h = \text{const.}$ (system absorbs heat $Q_h$ from the hot reservoir).
    
2. $\vec{BC}$: Adiabatic expansion (temperature drops from $T_h$ to $T_l$, $\delta Q = 0$).
    
3. $\vec{CD}$: Isothermal compression at $T_l = \text{const.}$ (system rejects heat $Q_l$ to the cold reservoir).
    
4. $\vec{DA}$: Adiabatic compression (temperature rises from $T_l$ back to $T_h$, $\delta Q = 0$).
    

```
  p ^      A
    |     /  \   Isotherms: AB (Th), CD (Tl)
    |    D    B  Adiabats: BC, DA
    |     \  /
    |       C
    +-------------------> V
```

This path can be mapped onto a plane using an alternative set of state parameters, such as temperature ($T$) and a state function defined by the adiabat paths:

$$s = f(pV^\gamma) \implies \left. p V^\gamma \right\vert{}_{\text{ad.}} = \text{const.}$$

This state function $s$ corresponds to **Entropy**. Traced on a $T\text{-}s$ coordinate plane, the Carnot cycle forms a perfect rectangle:

```
  T ^
 Th |   A ------> B    (Heat Qh enters)
    |   ^         |
 Tl |   |         v
    |   D <------ C    (Heat Ql leaves)
    +-------------------> s
```

#### Mathematical Analysis of the Cycle

Comparing the slopes ($\frac{dp}{dV}$) of the paths:

- **Isotherm:** $pV = \text{const.} \implies \left. \frac{dp}{dV} \right\vert{}_{\text{isotherm}} = -\frac{pV}{V^2} = -\frac{p}{V}$
    
- **Adiabat:** $pV^\gamma = \text{const.} \implies p = \frac{\xi}{V^\gamma} \implies \left. \frac{dp}{dV} \right\vert{}_{\text{ad.}} = -\frac{\xi \gamma V^{\gamma-1}}{V^{2\gamma}} = -\frac{\gamma p}{V}$
    

Applying the First Law ($dU = \delta w + \delta Q$) over the complete closed cycle $A \to B \to C \to D \to A$:

$$\Delta U_{A \to A} = 0 \implies (-W) + (Q_h - Q_l) = 0 \implies W = Q_h - Q_l > 0 \quad (\text{Net work extracted})$$

_Note on Sign Conventions:_ To ensure all variables ($W, Q_h, Q_l$) are treated as positive scalar magnitudes, we define them explicitly as absolute values: $W > 0$ is the work extracted, $Q_h > 0$ is the heat absorbed from the hot bath, and $Q_l > 0$ is the heat rejected to the cold bath.

Evaluating the heat exchanged during the isothermal stages:

- $A \to B$: $Q_h = R T_h \ln \frac{V_B}{V_A}$
    
- $B \to C$: $\frac{T_h}{T_l} = \left( \frac{V_C}{V_B} \right)^{\gamma-1}$
    
- $C \to D$: $Q_l = -R T_l \ln \frac{V_D}{V_C} = R T_l \ln \frac{V_C}{V_D}$
    
- $D \to A$: $\frac{T_l}{T_h} = \left( \frac{V_A}{V_D} \right)^{\gamma-1} \implies \frac{T_h}{T_l} = \left( \frac{V_D}{V_A} \right)^{\gamma-1}$
    

Equating the volume relations from the adiabatic steps:

$$\frac{V_C}{V_B} = \frac{V_D}{V_A} \implies \frac{V_B}{V_A} = \frac{V_C}{V_D}$$

Taking the ratio of $Q_h$ to $Q_l$ simplifies to:

$$\frac{Q_h}{Q_l} = \frac{T_h}{T_l} > 1$$

Therefore, the ratio of heat exchanged is determined strictly by the absolute thermodynamic temperatures of the two reservoirs.

### Thermal Efficiency ($\eta$)

A heat engine can be represented schematically as a "black box" operating between reservoirs $T_h$ and $T_l$:

```
     |||||||||||  High Temperature Reservoir (Th)
          |
          v Qh
        ( C ) ----> W (Net Work Out)
          |
          v Ql
     |||||||||||  Low Temperature Reservoir (Tl)
```

The thermal efficiency ($\eta$) is defined as the ratio of the net work obtained to the total heat energy input:

$$\eta \equiv \frac{\text{What we want (Net Work Out)}}{\text{What we pay for (Heat In)}} = \frac{W}{Q_h}$$

Since $W = Q_h - Q_l$, the efficiency of a Carnot engine becomes:

$$\eta_{\text{Carnot}} = \frac{Q_h - Q_l}{Q_h} = 1 - \frac{Q_l}{Q_h} < 1$$

Substituting the temperature relation $\frac{Q_h}{Q_l} = \frac{T_h}{T_l}$ yields the maximum theoretical efficiency formula:

$$\eta_{\text{Carnot}} = 1 - \frac{T_l}{T_h}$$

> **Physical Conclusion:** The efficiency of a Carnot engine depends exclusively on the absolute temperatures $T_l$ and $T_h$. It is entirely independent of the nature of the working substance used in the cycle.

#### Practical Examples:

1. **Steam Turbine Power Plant:**
    
    $$T_h \approx 800\text{ K} \quad , \quad T_l \approx 300\text{ K} \implies \eta_{\text{Carnot}} = 1 - \frac{300}{800} \approx 62.5\% \implies \eta_{\text{real}} \approx 45\%$$
    
2. **Internal Combustion Engine (Gasoline / Petrol):**
    
    $$\eta_{\text{real}} \approx 15\% - 25\%$$
    

_Question:_ Can we achieve $\eta = 1$ ($100\%$ efficiency)?

_Answer:_ This requires $T_l = 0\text{ K}$. However, the Third Law of Thermodynamics states that absolute zero cannot be reached in a finite number of steps. Thus, $100\%$ efficiency is physically impossible.

### Carnot's Theorem

> No heat engine operating between two thermal reservoirs can have a higher efficiency than a reversible Carnot engine operating between the same two reservoirs.

$$\eta_{\text{any engine}} \le \eta_{\text{Carnot}}$$

#### Proof by Contradiction (Assuming the existence of a super-efficient engine $E$):

Assume an engine $E$ exists such that its efficiency $\eta_E$ is strictly greater than the Carnot efficiency $\eta_{\text{Carnot}}$:

$$\eta_E > \eta_{\text{Carnot}}$$

Since a Carnot engine is fully reversible, it can be run backward as a Carnot refrigerator. Let both devices be coupled to the same reservoirs ($T_h$ and $T_l$). Scale the engines so they both exchange or produce the same net work $W$.

```
  Th  __________________________________________
         | Qh'                  ^ Qh
         v                      |
       [ E ] ----( W )----> [ Carnot Refrigerator ]
         |                      ^
         v Ql'                  | Ql
  Tl  __________________________________________
```

By definition of efficiency:

$$\eta_E > \eta_{\text{Carnot}} \implies \frac{W}{Q_h'} > \frac{W}{Q_h} \implies Q_h > Q_h'$$

Applying the First Law to both systems ($W = Q_h' - Q_l' = Q_h - Q_l$):

$$Q_h - Q_h' = Q_l - Q_l' > 0$$

This net result shows that the combined system transfers a positive amount of heat ($Q_l - Q_l'$) from the cold reservoir to the hot reservoir without requiring any net external work input ($W_{\text{net}} = 0$). This directly violates the **Clausius statement** of the Second Law. Thus, the initial assumption must be false, proving Carnot's theorem.