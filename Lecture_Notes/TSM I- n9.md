Here is the precise, academic English transcription of the lecture notes extracted directly from the provided images, maintaining strict mathematical notation in LaTeX and a clean, structural layout.

## Thermodynamics and Statistical Mechanics I: Lecture 15

### Rigorous Derivation of Temperature ($T$) as a Thermodynamic State Coordinate

The objective is to prove the existence of "Temperature" as a valid, uniquely defined state parameter using the mathematical structure of the Zeroth Law of Thermodynamics.

Consider three independent hydrostatic systems denoted as $1$, $2$, and $3$. The state of any hydrostatic system is uniquely defined by two independent macroscopic variables, pressure and volume: $(p, V)$.

Let system $3$ be selected as a reference system. Suppose system $1$ is placed in thermal equilibrium with a fixed state of system $3$. By systematically varying the coordinates of system $1$ while maintaining equilibrium with system $3$, we map a specific path on the $p_1\text{-}V_1$ coordinate plane. This path forms a curve of constant thermal state, defined as an **isotherm**. Repeating this process for different states of the reference system generates a family of isotherms for system $1$:

$$p_1^{(1)} \implies V_1^{(1)}, \quad p_1^{(2)} \implies V_1^{(2)}, \quad \dots$$

Similarly, if system $2$ is placed in thermal equilibrium with the same reference states of system $3$, we generate a corresponding family of isotherms for system $2$ on the $p_2\text{-}V_2$ plane.

According to the **Zeroth Law of Thermodynamics**, if system $1$ and system $2$ are each in thermal equilibrium with system $3$, they must also be in thermal equilibrium with each other.

### Mathematical Proof of Separation of Variables

The condition for thermal equilibrium between system $1$ and system $3$ can be expressed as a functional constraint:

$$F_1(p_1, V_1, p_3, V_3) = 0$$

Similarly, the equilibrium condition between system $2$ and system $3$ is written as:

$$F_2(p_2, V_2, p_3, V_3) = 0$$

Solving each of these independent relationships explicitly for the reference parameter $p_3$ yields:

$$p_3 = f_1(p_1, V_1, V_3)$$

$$p_3 = f_2(p_2, V_2, V_3)$$

Equating these two expressions gives a combined constraint relation:

$$f_1(p_1, V_1, V_3) = f_2(p_2, V_2, V_3)$$

However, by the transitivity of the Zeroth Law, systems $1$ and $2$ are in direct thermal equilibrium with each other, meaning their mutual equilibrium condition must be expressible strictly in terms of their own coordinates, without reference to system $3$:

$$F_{12}(p_1, V_1, p_2, V_2) = 0$$

Solving this relation for $p_1$ yields:

$$p_1 = f_3(V_1, p_2, V_2)$$

For the equation $f_1(p_1, V_1, V_3) = f_2(p_2, V_2, V_3)$ to be functionally compatible with $f_3(V_1, p_2, V_2)$, the independent parameter $V_3$ must mathematically separate and cancel out from the expression. Therefore, the functions $f_1$ and $f_2$ must possess a product or separable structure such that:

$$\Phi_1(p_1, V_1) = \Phi_2(p_2, V_2)$$

### Empirical Temperature ($\Theta$) and Equation of State

Because this equality holds for any pair of systems in mutual thermal equilibrium, the value of the function $\Phi(p, V)$ must be identical across all equilibrium states. This shared functional value is defined as the **Empirical Temperature**, denoted by $\Theta$:

$$\Phi(p, V) = \Theta$$

This mathematical structure guarantees that an **Equation of State** exists for any hydrostatic system in equilibrium. It relates pressure, volume, and temperature within a well-defined state space: $(p, V, \Theta)$.

_Example (Ideal Gas):_ $pV = N k_B T$, where $T$ represents the absolute mapping of $\Theta$.

### Thermometric Scales

To construct a practical scale for measuring empirical temperature ($\Theta$), we choose a functional mapping to assign numerical values to isotherms. The simplest choice is a linear relationship:

$$\Theta(x) = a x$$

Where $x$ is a measurable thermometric property of a substance, and $a$ is a scaling constant.

To determine the constant $a$ and establish a standardized scale, two primary criteria are typically used:

- **A.** Choosing a fixed reference temperature or a fixed phase transition point.
    
- **B.** Defining a standardized number of units or subdivisions between two fixed reference states.
    

#### Gas Thermometry

A gas thermometer utilizes a gas sample inside a container, monitoring either volume changes at constant pressure or pressure changes at constant volume:

1. **Constant-Pressure Gas Thermometer ($p = \text{const.}$):**
    
    $$\Theta = a V$$
    
    Defining a 100-unit interval between the ice point ($V_i$ at $1\text{ atm}$, melting ice) and the steam point ($V_s$ at $1\text{ atm}$, boiling water) yields:
    
    $$\Theta = \frac{100}{V_s - V_i} V$$
    
2. **Constant-Volume Gas Thermometer ($V = \text{const.}$):**
    
    $$\Theta = \frac{100}{p_s - p_i} p$$
    

#### The Ideal Gas Temperature Scale

Empirically, different real gases ($\text{He}, \text{N}_2, \dots$) yield slightly differing temperature readings at standard operational pressures due to molecular interactions ($\Theta_{\text{He}} \neq \Theta_{\text{N}_2}$).

However, as the operational pressure of the thermometer approaches zero ($p \to 0$), the molecular interactions vanish. In this limit, the readings of all real gas thermometers converge to a single, identical value. This defines the **Ideal Gas Temperature Scale** ($T$):

$$T \equiv \lim_{p \to 0} \frac{pV}{R} \quad (\text{for } n_m = 1\text{ mole})$$

Using the Kelvin scale convention, the reference point is fixed at the **triple point of water** ($T_{\text{tp}} = 273.16\text{ K}$):

$$T = 273.16 \frac{\lim_{p \to 0}(pV)}{\lim_{p \to 0}(pV)_{\text{triple point}}} \quad \text{[K]}$$

### The Thermodynamic Temperature Scale

To establish a temperature scale completely independent of the properties of any particular material, we utilize the properties of a reversible Carnot engine.

Consider a series of three operational temperatures ($\Theta_3 > \Theta_2 > \Theta_1$) and two coupled Carnot engines:

- Engine A operates between $\Theta_3$ and $\Theta_2$, absorbing heat $Q_3$ and rejecting $Q_2$.
    
- Engine B operates between $\Theta_2$ and $\Theta_1$, absorbing heat $Q_2$ and rejecting $Q_1$.
    

Their respective thermal efficiencies are written as:

$$\eta(\Theta_3, \Theta_2) = 1 - \frac{Q_2}{Q_3}$$

$$\eta(\Theta_2, \Theta_1) = 1 - \frac{Q_1}{Q_2}$$

A single composite engine operating directly between $\Theta_3$ and $\Theta_1$ would have the efficiency:

$$\eta(\Theta_3, \Theta_1) = 1 - \frac{Q_1}{Q_3}$$

Since $\frac{Q_2}{Q_3} \cdot \frac{Q_1}{Q_2} = \frac{Q_1}{Q_3}$, it follows that:

$$[1 - \eta(\Theta_3, \Theta_2)][1 - \eta(\Theta_2, \Theta_1)] = 1 - \eta(\Theta_3, \Theta_1)$$

This functional relationship requires that the ratio of heat exchanged depends on a single-variable function of temperature:

$$1 - \eta(\Theta, \Theta') = \frac{f(\Theta')}{f(\Theta)} \implies \frac{Q}{Q'} = \frac{f(\Theta)}{f(\Theta')}$$

Defining the absolute thermodynamic temperature $T$ directly proportional to this function ($f(\Theta) \equiv T$) establishes the **Absolute Thermodynamic Scale**:

$$\frac{Q_h}{Q_l} = \frac{T_h}{T_l}$$

This definition is completely independent of any working substance and matches the Ideal Gas Scale identically ($pV = N k_B T$).

Ready for the next set of pages whenever you want to send them over.