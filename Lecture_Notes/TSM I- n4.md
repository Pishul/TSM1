Here is the precise, academic English translation of the lecture notes extracted directly from the provided images, without any added explanations.

## Thermodynamics and Statistical Mechanics I

### State Function

A state function is a property used to describe the macroscopic state of a system in equilibrium. To specify the equilibrium state, it is sufficient to determine a set of macroscopic variables. Subsequently, the remaining variables adjust such that the system is driven toward a well-defined subsequent equilibrium state until a new equilibrium is established.

The macroscopic coordinates of the system can be represented as a vector:

$$\vec{X} = (X_1, X_2, \dots)$$

**Thermodynamic State:** Macroscopic variables of the system, such as $N$, $V$, $p$, and $T$, describe its equilibrium state.

For a state function $g(\vec{X})$, the variation between an initial state ($i$) and a final state ($f$) is independent of the path taken:

$$\Delta g \Big\vert{}_{i \xrightarrow{\text{I, II}} f} = g(\vec{X}_f) - g(\vec{X}_i)$$

The line integral of a state function over a closed path is identically zero:

$$\oint d g = 0$$

> **Property:** A state function possesses an exact differential ($d$).

### The First Law of Thermodynamics

There exists a thermodynamic state function termed **Internal Energy**, denoted by $U$.

$$\exists U \text{ State function, s.t. } \Delta U_{i \to f} = U(f) - U(i) = \int_i^f dU$$

The mathematical statement of the First Law of Thermodynamics for finite changes is written as:

$$\Delta U = \Delta W + \Delta Q$$

- $\Delta W$: Work done on the system.
    
- $\Delta Q$: Heat supplied to the system.
    

#### Sign Convention:

- $\Delta W > 0$: Work is done on the system.
    
- $\Delta W < 0$: Work is done by the system on the environment.
    
- $\Delta Q > 0$: Heat is absorbed by the system (endothermic).
    
- $\Delta Q < 0$: Heat is released by the system (exothermic).
    

The differential form of the First Law for a process $i \to f$ is expressed as:

$$du = \delta w + \delta q$$

> **Note:** Work ($\delta w$) and heat ($\delta q$) are inexact differentials ($\delta$) and are path-dependent. Therefore, for a closed path:
> 
> $$\oint \delta q \neq Q(f) - Q(i) \quad (?!)$$

### Forms of Work and Energy

In the general case, the work done on a system is defined as:

$$\Delta W = \int_i^f \vec{F}(\vec{r}, \vec{v}) \cdot d\vec{r}$$

If the forces acting on the system are conservative, they can be expressed as the gradient of a potential function:

$$\vec{F} = -\vec{\nabla} V(\vec{r})$$

For a purely mechanical system, by the work-energy theorem, the work done changes the mechanical energy (kinetic and potential energy):

$$\Delta E_{\text{mech}} = \Delta E_k + \Delta E_p = \Delta [ \frac{1}{2} m \vec{v}^2 + V(\vec{r}) ]$$

In general thermodynamic systems, $\Delta E_{\text{mech}} \neq 0$. Thus, the generalized law of conservation of energy incorporating thermal effects is defined as:

$$E := E_{\text{mech}} + E_{\text{heat}}$$

Where $E_{\text{heat}} = \Delta E_{\text{mech}}$. For an isolated system, the total energy variation is zero:

$$\Delta E = 0 \quad \text{(Conservation of Energy)}$$

#### Mechanical Work in Physical Systems:

Work done on the environment or system involves the displacement of real boundaries (e.g., the boundary of a gas).

For a constant or average force:

$$\Delta W_{\text{mech}} \approx \vec{F}_{\text{mech}} \cdot \Delta \vec{r}$$

$$\Delta W \approx F \, \Delta X$$

In differential form, the work done is an inexact differential and not a state function:

$$\delta w = F \, dx \neq d(\dots)$$

For multiple forces, the total differential work is the sum:

$$\delta w = \sum_i F_i \, dx_i$$

### Particular Thermodynamic Processes

#### 3. Isobaric Process

A process during which the pressure of the system remains constant:

$$\Delta p \Big\vert{} = 0$$

_Example:_ Chemical experiments conducted in open containers in the presence of air are isobaric, meaning the equilibrium pressure of the system equals the atmospheric pressure.

#### 4. Adiabatic Process

A process during which no heat exchange occurs between the system and its environment:

$$\Delta Q \Big\vert{} = 0$$

This process transitions the system between equilibrium states: $i \xrightarrow{\text{process}} f$.

- **Adiabatic Wall:** A boundary enclosing thick insulation that prevents heat transfer (e.g., glass wool). (An ideal thermal insulator does not exist).
    
- **Diathermal Wall:** Thermally perfectly conducting boundaries that permit heat exchange.
    

**The First Law in an Adiabatic Process:**

Since $\Delta Q = 0$, the change in internal energy is strictly equal to the work performed:

$$\Delta U = \Delta W + \cancel{\Delta Q}^0 \implies \Delta W = \Delta U$$

$$\delta w = dU$$

In this process, work is converted into a state function.

#### Operational Definition of Heat:

From $\Delta U = \Delta W + \Delta Q \Rightarrow \Delta U - \Delta W = \Delta Q$.

By bringing a system to its final state via an arbitrary open process and then via an adiabatic path, we obtain:

$$\Delta Q = \Delta W \Big\vert{}_{\text{ad.}} - \Delta W \Big\vert{}_{\text{open}}$$

This provides an operational definition of heat solely based on the measurement of work.

### Are Heat and Work Fundamentally Identical?

Considering the First Law ($\Delta U = \Delta W + \Delta Q$), the change in internal energy depends only on the net sum of work and heat. Are work and heat completely interconvertible?

- **Recall:** For a cyclic process ($\Delta U = 0$): $1. \ \Delta Q \neq 0$ and $2. \ \Delta W \neq 0$.
    
- **Question:** Can work and heat be converted into each other in any arbitrary ratio within a cycle? (This leads to the **Second Law of Thermodynamics**).
    

#### Conversion Limitations:

- The conversion of work into heat is easily achievable and complete:
    
    $$W \xrightarrow{\text{conversion}} Q \implies Q = W$$
    
- The conversion of heat into work cannot be complete within a cycle:
    
    $$Q \xrightarrow{\text{conversion}} W \implies W \neq Q \quad (W < Q)$$
    

_Example:_ Dragging an object across a rough surface converts work entirely into heat via friction, stopping the motion. However, supplying that generated heat back to the object cannot fully convert it back into mechanical work or motion. This governs the operation of locomotives and heat engines; heat cannot be completely converted to work without a cold reservoir (temperature drop).

### Thermodynamic Coordinates of a Simple System

For a simple system (such as a gas confined within a cylinder with a moving piston), the thermodynamic state is defined by the coordinates $(p, V, T)$.

For this system, we aim to evaluate the following quantities across various processes:

$$\delta w = ?$$

$$\delta q = ?$$

$$dU = ?$$