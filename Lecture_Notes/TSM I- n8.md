Here is the precise, academic English transcription of the lecture notes extracted directly from the provided images, keeping strict structural layouts and math notation in LaTeX.

## Thermodynamics and Statistical Mechanics I: Lecture 13

### Logical Proof of Carnot's Theorem (Continued)

Consider a composite engine consisting of a super-efficient engine $E$ coupled with a reversed Carnot engine acting as a refrigerator. Under the assumption that $\eta_E > \eta_{\text{Carnot}}$, let both systems operate such that the net extracted work is zero ($W_{\text{composite}} = 0$).

The heat exchange variations with the thermal reservoirs yield:

- Hot reservoir ($T_h$): $Q_h - Q_h' > 0$
    
- Cold reservoir ($T_l$): $Q_l - Q_l' > 0$
    

If such a system were to exist, it would extract a net heat quantity from the cold reservoir ($T_l$) and deliver it to the hot reservoir ($T_h$) in a complete continuous cycle without requiring any net external work input.

This directly violates the Clausius statement of the Second Law of Thermodynamics. Because the Clausius statement is established as an absolute truth, our initial premise must be false. Therefore:

$$\eta_E \le \eta_{\text{Carnot}}$$

> **Carnot's Theorem:** No engine operating between two specific thermal reservoirs ($T_h$ and $T_l$) can have a higher efficiency than a reversible Carnot engine operating between those same boundaries.
> 
> **Corollaries:**
> 
> 1. All reversible engines operating between the same two thermal reservoirs have identical thermal efficiencies, regardless of their internal configuration or working substance.
>     
> 2. The maximum potential efficiency is given precisely by the Carnot formula:
>     
>     $$\eta_{\text{Carnot}} = 1 - \frac{Q_l}{Q_h} = 1 - \frac{T_l}{T_h}$$
>     

### Extended Characteristics of Reversibility

From Carnot's theorem, we establish that for any fully reversible transformation path:

$$\eta_{\text{reversible}} = \eta_{\text{Carnot}} = 1 - \frac{T_l}{T_h}$$

#### Structural Proof Details:

1. All reversible engines operating between the same thermal boundaries must share a single, unique maximum efficiency.
    
2. No irreversible engine can match this bound; any source of dissipation inevitably lowers thermal performance.
    
3. For a system to trace an exact path on a thermodynamic plane ($p\text{-}V$), the transformation must occur infinitesimally slowly in the absolute absence of friction.
    

```
  p ^  i
    |   * .
    |    \  .   Dissipative / Irreversible Fluctuations
    |     \   * f
    +-------------------> V
```

If friction or sudden unconstrained expansions are present, the system deviates into non-equilibrium states, making it impossible to map via distinct state variables. A fully reversible path allows heat $Q_h$ to be absorbed or rejected along a precisely inverted sequence without changing the net state of the universe.

### Equivalence of Clausius ($C$) and Kelvin ($K$) Statements

Let $C$ denote the Clausius statement and $K$ denote the Kelvin statement. To demonstrate their logical equivalence ($C \iff K$), we must prove that a violation of one statement implies a violation of the other:

$$(\cancel{C} \implies \cancel{K}) \;\land\; (\cancel{K} \implies \cancel{C})$$

#### Part 1: Proving $\cancel{C} \implies \cancel{K}$

Assume an anti-Clausius device exists ($\cancel{C}$). This device can spontaneously transfer a quantity of heat $Q_l$ from a cold reservoir ($T_l$) to a hot reservoir ($T_h$) without any external work input.

Now, introduce a standard heat engine $E$ operating between the same two reservoirs, which extracts heat $Q_h$ from the hot reservoir, performs work $W = Q_h - Q_l$, and rejects heat $Q_l$ to the cold reservoir.

```
  Th  __________________________________________
         ^ Ql                  | Qh
         |                     v
    [ Device 1 ]             [ Engine E ] ----> W = Qh - Ql
         ^                     |
         | Ql                  v Ql
  Tl  __________________________________________
```

Coupling these two systems together, the net heat rejected to the cold reservoir is completely cancelled ($Q_{l,\text{net}} = Q_l - Q_l = 0$). The composite device now extracts a net heat amount ($Q_h - Q_l$) from a single reservoir ($T_h$) and converts it entirely into mechanical work $W = Q_h - Q_l$. This directly violates the Kelvin statement ($\cancel{K}$).

#### Part 2: Proving $\cancel{K} \implies \cancel{C}$

Assume an anti-Kelvin engine exists ($\cancel{K}$). This engine absorbs heat $Q_h'$ from a single hot reservoir ($T_h$) and converts it completely into work $W = Q_h'$ without rejecting any heat to a colder boundary.

Now, use this extracted work $W$ to drive a standard reversible heat pump or refrigerator operating between the same reservoirs. The refrigerator absorbs heat $Q_l$ from the cold reservoir and rejects heat $Q_h = W + Q_l$ to the hot reservoir.

```
  Th  __________________________________________
         ^ Qh' = W             ^ Qh = W + Ql
         |                     |
    [ Engine K ] ----( W )---> [ Refrigerator ]
                               ^
                               | Ql
  Tl  __________________________________________
```

Looking at the net energy balance of the combined setup:

- Net work required from external sources: $W_{\text{net}} = 0$.
    
- Net heat extracted from the cold reservoir: $Q_l$.
    
- Net heat delivered to the hot reservoir: $Q_h - Q_h' = (W + Q_l) - W = Q_l$.
    

The combined system successfully moves a net heat quantity $Q_l$ from a cold reservoir to a hot reservoir without any external work input. This directly violates the Clausius statement ($\cancel{C}$).

### Classification of Perpetual Motion Machines (PMM)

The constraints of thermodynamic principles categorize hypothetical machines based on which laws they violate (Impossibility/No-go Theorems):

- **Perpetual Motion Machine of the First Kind (PMM1):** A device that creates energy out of nothing, delivering continuous work without consuming any net fuel or heat input. This is fundamentally banned by the **First Law of Thermodynamics** (Conservation of Internal Energy).
    
- **Perpetual Motion Machine of the Second Kind (PMM2):** A device that conserves energy perfectly but converts ambient thermal energy completely into mechanical work within a cycle ($\eta = 1$) without a temperature gradient. This is banned by the **Second Law of Thermodynamics**.
    

```
============================================================
  Type  | Violates                 | Physical Meaning
--------+--------------------------+------------------------
  PMM1  | First Law ($dU \neq 0$)  | Creates energy
  PMM2  | Second Law ($\eta = 1$)  | Eliminates cold bath
============================================================
```

#### Real-World Limits and Apparent Reversibility

Can any real macroscopic machine achieve perfect reversibility or avoid dissipation entirely? Phenomena such as internal friction, viscous resistance, electrical resistance, and structural relaxation paths generate entropy continuously.

However, specialized quantum systems under precise conditions can eliminate certain classic dissipative mechanisms:

- **Superconductors ($R = 0$):** Below a critical temperature $T_c$, materials following the BCS (Bardeen-Cooper-Schrieffer) theory lose all direct electrical resistance, allowing persistent, non-dissipative charge currents to circulate indefinitely.
    

### The Zeroth Law of Thermodynamics

While the First and Second Laws restrict energy and direction, the formulation of temperature as a valid state parameter requires a underlying postulatory framework:

```
  First Law + Second Law  ==> Quantify energy and path limitations
  Zeroth Law              ==> Validates the concept of Temperature (T)
```

#### Statement of the Zeroth Law:

> If two thermodynamic systems, $1$ and $2$, are each in thermal equilibrium with a third system, $3$, then they are in thermal equilibrium with each other.

This implies that thermal equilibrium is a transitive mathematical relation:

$$(\text{System 1} \sim \text{System 3}) \;\land\; (\text{System 2} \sim \text{System 3}) \implies (\text{System 1} \sim \text{System 2})$$

#### Proof and Application:

Let systems $1$, $2$, and $3$ be hydrostatic setups governed by coordinates $(p, V)$. By adjusting their properties experimentally, we can map their equilibrium interfaces mathematically. The transitivity guaranteed by the Zeroth Law confirms that a scalar state function exists, which must be equal for all systems at equilibrium:

$$\exists T \iff \text{Thermal Equilibrium}$$
