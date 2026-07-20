Here is the academic English translation of the lecture notes extracted directly from the provided images, maintaining strict mathematical notation in LaTeX as requested.

## Thermodynamics and Statistical Mechanics I

### Review: The First Law of Thermodynamics

$$U: \text{State Function}$$

$$dU = \delta w + \delta Q$$

For an isolated system (a system that exchanges neither energy nor particles with its environment):

$$dU = 0 \quad \text{or} \quad U = \text{const.}$$

#### Application of the First Law to a Simple System: Piston and Cylinder

Consider a gas enclosed in a cylinder with a piston. The system undergoes a quasi-static displacement where the piston moves by an infinitesimal distance $dx$ ($x \to x + dx$).

The work done on the system by an external force $\vec{F}$ is given by:

$$\delta w = \vec{F} \cdot d\vec{r} = F \, dx = -p A \, dx = -p \, dV$$

Where $A$ is the cross-sectional area of the piston and $dV = -A \, dx$ represents the change in volume.

The term $p$ refers to the pressure. In order to use a local coordinate like $p$ to define the state of the system during a transformation, the system must pass through a sequence of equilibrium states. This implies that the pressure must be uniform and global throughout the system ($p_{\text{gas}} \approx p_{\text{ext}}$).

#### Thermodynamic Constraints:

- The number of particles is constant ($N = \text{const.}$).
    
- No chemical reactions take place.
    
- The relevant state variables are $p$ and $V$.
    

When external forces act on the system, if the compression or expansion occurs too rapidly, the internal pressure will not remain uniform ($p(\vec{r}_1) \neq p(\vec{r}_2)$). For the pressure to be approximately uniform ($p(\vec{r}_1) \approx p(\vec{r}_2) \approx p(\vec{r}_3) \dots$), the process must be carried out infinitesimally slowly. This introduces the concept of **Reversibility**.

### Reversibility and Characteristic Timescales

To mathematically define a reversible process, we analyze the relationship between two characteristic times:

1. **Relaxation Time of the Gas ($\tau_s$):** The time required for the gas inside the cylinder to re-establish equilibrium after a local disturbance.
    
    $$\tau_s \approx \frac{\Delta x}{v_s}$$
    
    Where $v_s$ is the speed of sound in the gas, which governs the propagation of pressure equilibrium.
    
2. **Characteristic Time of the Process ($\tau_p$):** The time over which the external modification (e.g., piston displacement $\Delta x$) takes place.
    
    $$\tau_p \approx \frac{\Delta x}{v_p}$$
    
    Where $v_p$ is the velocity of the piston.
    

For a process to be considered quasi-static and reversible, the external change must happen much slower than the internal relaxation of the system:

$$v_p \ll v_s \iff \tau_p \gg \tau_s$$

Under these conditions, the system is always in a well-defined equilibrium state, meaning its path can be traced on a thermodynamic plane, and the equation of state holds at any point during the process:

$$p = p(V, T)$$

#### Definition of a Reversible Process:

A process is reversible if, after its completion, the system and its surroundings can be restored to their initial states by reversing the path (backward play) without leaving any net change in the universe.

_Example of an Irreversible Process:_ An object sliding on a rough surface with friction comes to rest ($v_0 \to v=0$). This mechanical work is dissipated into thermal energy. Reversing the time will not spontaneously convert the heat back into mechanical work to slide the block back to its starting position. Reversibility and irreversibility are macroscopic concepts, not microscopic ones.

### Microscopic Time-Reversal Symmetry

At the microscopic level, classical mechanics is governed by Hamiltonian equations:

$$H = H(\vec{r}(t), \vec{p}(t), t) \implies \begin{cases} \frac{d\vec{r}(t)}{dt} = \frac{\partial H}{\partial \vec{p}} \\ \frac{d\vec{p}(t)}{dt} = -\frac{\partial H}{\partial \vec{r}} \end{cases}$$

For microscopic time reversibility (microreversibility) to hold, the Hamiltonian must satisfy:

$$H(\vec{r}(t), \vec{p}(t), t) = H(\vec{r}(-t), -\vec{p}(-t), -t)$$

Under the time-reversal transformation:

$$\begin{cases} t \to -t \\ \vec{r} \to \vec{r} \\ \vec{p} \to -\vec{p} \end{cases}$$

The equations of motion remain invariant. Thus, all fundamental microscopic laws of nature are time-reversal symmetric, yet macroscopic thermodynamic processes are inherently irreversible.

### Heat Capacities ($C_V$ and $C_p$)

Let the internal energy be a function of temperature and volume, $U = U(T, V)$. Its total differential is written as:

$$dU = \left(\frac{\partial U}{\partial T}\right)_V dT + \left(\frac{\partial U}{\partial V}\right)_T dV$$

Substituting this into the differential form of the First Law of Thermodynamics ($dU = \delta Q - p \, dV$) yields:

$$\delta Q = \left(\frac{\partial U}{\partial T}\right)_V dT + \left[ \left(\frac{\partial U}{\partial V}\right)_T + p \right] dV$$

Dividing by $dT$ gives the general expression for the heat capacity:

$$\frac{\delta Q}{dT} = \left(\frac{\partial U}{\partial T}\right)_V + \left[ \left(\frac{\partial U}{\partial V}\right)_T + p \right] \frac{dV}{dT}$$

#### a) Heat Capacity at Constant Volume ($C_V$)

For an isochoric process, $V = \text{const.} \implies dV = 0$:

$$C_V = \left(\frac{\delta Q}{dT}\right)_{\text{isochoric}} = \left(\frac{\partial U}{\partial T}\right)_V$$

#### b) Heat Capacity at Constant Pressure ($C_p$)

For an isobaric process, $p = \text{const.} \implies dp = 0$:

$$C_p = \left(\frac{\delta Q}{dT}\right_{\text{isobaric}} = \left(\frac{\partial U}{\partial T}\right)_V + \left[ \left(\frac{\partial U}{\partial V}\right)_T + p \right] \left(\frac{\partial V}{\partial T}\right)_p$$

Substituting $C_V$ into the equation for $C_p$ leads to the fundamental relationship between the two heat capacities:

$$C_p - C_V = \left[ \left(\frac{\partial U}{\partial V}\right)_T + p \right] \left(\frac{\partial V}{\partial T}\right)_p$$

Where $\left(\frac{\partial U}{\partial V}\right)_T$ relates to internal structural forces, and $f(V, T, p) = 0$ represents the equation of state.