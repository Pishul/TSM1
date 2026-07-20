Here is the precise, academic English transcription of the lecture notes extracted directly from the provided images, keeping strict structural layout and proper math notation in LaTeX.

---

## Thermodynamics and Statistical Mechanics 1: Lecture 8

### Review

Recall the general relation derived for a hydrostatic system under the constraint $N = \text{const.}$:


$$C_p - C_v = \left[ \left(\frac{\partial U}{\partial V}\right)_T + p \right] \left(\frac{\partial V}{\partial T}\right)_p$$

We define the heat capacity subject to a generalized constraint $X = \text{const.}$ as:


$$C_X \equiv \left. \frac{\delta Q}{dT} \right\vert{}_{X = \text{const.}}$$

$$C_v = \left. \frac{\delta Q}{dT} \right\vert{}_{V = \text{const.}} = \left(\frac{\partial U}{\partial T}\right)_V$$

Given our physical understanding of structural expansion, it follows naturally that:


$$C_p - C_v > 0$$

#### Physical Interpretation for a Hydrostatic System (e.g., An Ideal / Perfect Gas)

Consider two distinct ways to supply heat to a gas system:

1. **Constant Volume ($V = \text{const.}$):** The gas is locked inside a rigid, immovable cylinder. As heat $Q$ is absorbed, the temperature rises entirely via the internal energy because no boundary work is permitted.
2. **Constant Pressure ($p = \text{const.}$):** The gas is housed in a cylinder where the top piston is free to move. The external pressure balances the environment ($p = p_{\text{outside}} = p_{\text{bath}}$). When heat $Q$ is added, the volume expands, driving the piston upward. As a result, the system performs mechanical work against the surroundings.

**Conclusion:**


$$C_p > C_v$$


To achieve the same temperature variance $\Delta T$, an isobaric path ($p = \text{const.}$) requires more net energy input than an isochoric path ($V = \text{const.}$) because additional energy is expended on external boundary expansion work.

---

### The Ideal Gas: The Simplest Thermodynamic System

An ideal gas represents a simple system modeling macroscopic parameters. It consists of a large collection of point-like particles (atoms or molecules) that move freely through space without interacting chemically or experiencing mutual attractive or repulsive forces. Their collisions with the system boundaries give rise to a measurable pressure.

*Examples of Real Gases under Mild Conditions (Noble/Rare Gases):*

* $\text{He}$, $\text{Ne}$, $\text{Ar}$, $\text{Kr}$, $\text{Xe}$ (Chemically inert gases).

#### Empirical Laws of the Ideal Gas:

Experimental data collected at constant mass ($N = \text{const.}$) yields:

* **Boyle-Mariotte Law:** $\left. p \right\vert{}_{T = \text{const.}} \propto \frac{1}{V}$
* **Charles's Law:** $\left. V \right\vert{}_{p = \text{const.}} \propto T$
* **Gay-Lussac's Law:** $\left. p \right\vert{}_{V = \text{const.}} \propto T$

Combining these individual variations produces the universal proportionality:


$$pV \propto T$$

This leads directly to the formulation:


$$pV = N k_B T$$


Where $N$ is the absolute total number of gas particles, and $k_B$ is the Boltzmann constant:


$$k_B = 1.38 \times 10^{-23} \text{ m}^2\text{kg}/\text{s}^2\text{K } [\text{SI}]$$

Expressing this in terms of molar units where $N = n_m N_A$:


$$pV = N k_B T = n_m R T$$


Where $R$ is the universal gas constant:


$$R = k_B N_A \approx 8.31 \text{ [SI]}$$

---

### Equation of State

An equation of state relates the fundamental macroscopic thermodynamic parameters of a system in equilibrium:


$$f(N, p, V, T) = 0$$

Through the framework of statistical mechanics, the macroscopic parameters can be directly derived from microscopic interactions. However, dimensional analysis can yield structural properties even without full macroscopic modeling.

#### Dimensional Analysis Approach

Let a cubic container have a side length $L$, such that the volume is:


$$V = L^3$$

Assume the system scales uniformly by a parameter $\alpha$:


$$L \to L' = \alpha L \implies V \to V' = \alpha^3 V$$

Under this scaling, assume the temperature remains constant ($T = \text{const.}$). The momentum transfer per particle collision at the wall scales identically ($\Delta P' = \Delta P$). The timescale $\Delta t$ between successive wall collisions for a particle moving with velocity $v$ over a characteristic path length $d$ scales as:


$$\Delta t = \frac{d}{v} \implies \Delta t' = \frac{d'}{v'} = \frac{\alpha d}{v} = \alpha \Delta t$$

The average force exerted by a single particle scales as:


$$F = \frac{\Delta P}{\Delta t} \implies F' = \frac{\Delta P'}{\Delta t'} = \frac{\Delta P}{\alpha \Delta t} = \frac{1}{\alpha} F$$

Since pressure is force divided by area ($A = L^2 \to A' = \alpha^2 A$):


$$p = \frac{F}{A} \implies p' = \frac{F'}{A'} = \frac{\frac{1}{\alpha}F}{\alpha^2 A} = \frac{1}{\alpha^3} p$$

Therefore, under this geometric scaling constraint:


$$\begin{cases} p \to \frac{1}{\alpha^3} p \\ V \to \alpha^3 V \end{cases} \implies p'V' = \left(\frac{1}{\alpha^3} p\right) (\alpha^3 V) = pV = \text{const.}$$

$$pV = \text{const.} \propto T$$

---

### Standard Conditions (STP)

Standard parameters are defined as:

* $T_{\text{st.}} \equiv 0^\circ\text{C} = 273.15\text{ K}$
* $p_{\text{st.}} = 1\text{ atm} = 1.01 \times 10^5\text{ Pa}$

For $n_m = 1\text{ mole}$ of an ideal gas at STP, the molar volume is:


$$V_m \Big\vert{}_{\text{st.}} = \frac{R T_{\text{st.}}}{p_{\text{st.}}} \approx 22.4\text{ liters}$$

#### Additional Property of an Ideal Gas

The internal energy of an ideal gas is purely kinetic and depends exclusively on its temperature, making it completely independent of pressure or volume changes:


$$U_{\text{ideal}} = U(T)$$

---

### Molar Energy for Monatomic Ideal Gases

From experimental observation, the molar internal energy for a monatomic ideal gas is given by:


$$U_m(T) = \frac{3}{2} R T$$

This implies that:


$$\left(\frac{\partial U_m}{\partial V}\right)_T = 0$$

Applying the equation of state for one mole ($p_m V_m = R T \implies V_m = \frac{RT}{p_m}$), we evaluate the partial derivative:


$$\left(\frac{\partial V_m}{\partial T}\right)_p = \frac{R}{p_m}$$

Substituting these terms into the fundamental relationship for $C_p - C_v$:


$$C_{p,m} - C_{v,m} = \left[ \left(\frac{\partial U_m}{\partial V}\right)_T + p_m \right] \left(\frac{\partial V_m}{\partial T}\right)_p = [0 + p_m] \left(\frac{R}{p_m}\right) = R$$

Given that $C_{v,m} = \left(\frac{\partial U_m}{\partial T}\right)_V = \frac{3}{2} R$, we find:


$$\begin{cases} C_{v,m} = \frac{3}{2} R \\ C_{p,m} - C_{v,m} = R > 0 \end{cases}$$

For a general system containing $n_m$ moles:


$$\begin{cases} C_v = \frac{3}{2} n_m R \\ C_p - C_v = n_m R \end{cases}$$

*Example (Helium gas):* Measured values closely match these predictions:


$$C_{v,m} = 12.48 \text{ [SI]} \quad , \quad C_{p,m} = 20.76 \text{ [SI]}$$

Thus, the global internal energy of an ideal gas can be expressed as:


$$U_{\text{ideal gas}}(T) = C_v T$$

---

### Isothermal Process for an Ideal Gas

An isothermal process takes place at a constant temperature ($\Delta T \Big\vert{}_{\text{isothermal}} = 0$). Because the internal energy of an ideal gas depends solely on temperature, it remains unchanged during an isothermal transformation:


$$\left. \Delta U \right\vert{}_{\text{isothermal}} = C_v \Delta T = 0$$

Applying the First Law of Thermodynamics ($dU = \delta w + \delta Q = 0$):


$$\left. \delta w \right\vert{}_{\text{isothermal}} = - \left. \delta Q \right\vert{}_{\text{isothermal}}$$

The mechanical work performed during a volume change from $V_1$ to $V_2$ is:


$$\delta w = -p \, dV$$

$$\Delta Q \Big\vert{}_{\substack{\text{isothermal} \\ V_1 \to V_2 \\ T=\text{const.}}} = -\int_1^2 \delta w = +\int_{V_1}^{V_2} p \, dV$$

Substituting $p = \frac{n_m R T}{V}$ into the integral:


$$\Delta Q \Big\vert{}_{\substack{\text{isothermal} \\ V_1 \to V_2}} = \int_{V_1}^{V_2} \frac{n_m R T}{V} dV = n_m R T \int_{V_1}^{V_2} \frac{dV}{V} = n_m R T \ln \frac{V_2}{V_1}$$

> **Sign Interpretation:** If $V_2 > V_1$ (isothermal expansion), then $\Delta Q > 0$. Heat must enter the system to counter the mechanical work performed during expansion, keeping the internal energy and temperature stable ($\left. \Delta U \right\vert{}_{T=\text{const.}} = 0$).

---

### Adiabatic Process for an Ideal Gas

In an adiabatic process, there is no thermal exchange between the system and its environment ($\left. \Delta Q \right\vert{}_{\text{adiabatic}} = 0 \implies \delta Q = 0$).

The First Law simplifies to:


$$dU = \left. \delta w \right\vert{}_{\text{ad.}}$$

For a quasi-static process involving an ideal gas:


$$dU = C_v \, dT \quad \text{and} \quad \delta w = -p \, dV$$

$$C_{v,m} \, dT = -\frac{R T}{V} dV \implies C_{v,m} \frac{dT}{T} = -R \frac{dV}{V}$$

Integrating both sides from an initial state $(T_1, V_1)$ to a final state $(T_2, V_2)$:


$$\ln \frac{T_2}{T_1} = -\frac{R}{C_{v,m}} \ln \frac{V_2}{V_1}$$

We can rewrite the exponent using the relation $C_{p,m} - C_{v,m} = R$:


$$-\frac{R}{C_{v,m}} = -\frac{C_{p,m} - C_{v,m}}{C_{v,m}} = 1 - \frac{C_{p,m}}{C_{v,m}} = 1 - \gamma$$


Where $\gamma \equiv \frac{C_p}{C_v}$ represents the adiabatic index.

Substituting this back into the integrated equation:


$$\ln \frac{T_2}{T_1} = (1 - \gamma) \ln \frac{V_2}{V_1} = \ln \left( \frac{V_2}{V_1} \right)^{1-\gamma} = \ln \left( \frac{V_1}{V_2} \right)^{\gamma-1}$$

$$\implies \frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{\gamma-1} \implies T_1 V_1^{\gamma-1} = T_2 V_2^{\gamma-1}$$

Thus, along an adiabatic path:


$$\left. T V^{\gamma-1} \right\vert{}_{\text{ad.}} = \text{const.}$$

Using the ideal gas law ($pV = n_m R T \implies T = \frac{pV}{n_m R}$), we can express this condition in terms of pressure and volume:


$$\left. p V^\gamma \right\vert{}_{\text{ad.}} = \text{const.}$$