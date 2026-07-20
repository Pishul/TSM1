- ترمودینامیک و مکانیک آماری ۱ : 27 اردیبهشت

- مثال : $R$ آن قدر بزرگ باشد که با سطح تماس اندکی
با $S$ هر دو در نهایت به دمای برابر $T_R$ هم‌دما (تعادل) شوند

R
T_S
S
T_R

گرما منتقل شده از
$\Delta Q = C^{(S)} (T_R - T_S)$
منبع $R$ به سیستم $S$
(فرض : ظرفیت گرمایی سیستم در این رنج مستقل از دماست)

(a)
$T_R > T_S \Rightarrow \Delta Q > 0 \Rightarrow \Delta T > 0$
یعنی انرژی به سیستم می‌رود
سیستم گرم می‌شود
$\Delta S^{(S)} > 0$ ، $\Delta S^{(R)} < 0$ چون گرما از آن به بیرون شارش یافته است

(b)
$T_R < T_S \Rightarrow \Delta Q < 0 \Rightarrow \Delta T < 0$
سیستم سرد می‌شود
$\Delta S^{(S)} < 0$ ، $\Delta S^{(R)} > 0$ چون گرما از سیستم به آن شارش یافته است

$T_R = \text{Const.}$

سؤال : $\Delta S^{(\text{universe})} \ge 0$ ؟

$\Delta S^{(R)} = \int \frac{đQ}{T_R} = \frac{1}{T_R} \int đQ = \frac{-\Delta Q}{T_R} = \frac{C^{(S)} (T_S - T_R)}{T_R}$

$\Delta S^{(S)} = \int \frac{đQ}{T} = \int_{T_S}^{T_R} C^{(S)} \frac{dT}{T} = C^{(S)} \ln \frac{T_R}{T_S}$
دمای سیستم که از $T_S$ به $T_R$ تغییر می‌کند

$\Delta S^{(\text{universe})} = \Delta S^{(S)} + \Delta S^{(R)} = C^{(S)} \left[ \ln \frac{T_R}{T_S} + \frac{T_S}{T_R} - 1 \right] \ge 0$
مستقل از اینکه در a یا b
for $x > 0 : \ln x + 1/x - 1 \ge 0$


- ترکیب کردن قانون اول با قانون دوم : $\quad$ به دست آوردن روابط ترمودینامیکی

قانون اول : $\quad dU = \bar{d}Q + \bar{d}W \quad$ (معتبر برای هر فرآیندی)

لحاظ کردن فرآیند برگشت‌پذیر (در اینجا)
$\begin{cases} \bar{d}W = -p dV + \dots & \text{برای کار هیدروستاتیکی} \\ \bar{d}Q_{\text{rev}} = T dS & \text{(قانون دوم)} \end{cases} \implies \text{معتبر برای فرآیند برگشت‌پذیر}$

$\implies \quad dU = T dS - p dV + \dots \quad \bigstar$

دقت کنید با اینکه فرض کردیم که فرآیند تغییر حالت، برگشت‌پذیر است

تذکر : همه عبارات در رابطه $\bigstar$ فقط تابعی از وضعیت‌اند (متغیر حالت‌اند)

$\impliedby$ این عبارت برای هر فرآیندی (چه برگشت‌پذیر، چه برگشت‌ناپذیر) درست است!

برگشت‌ناپذیر :
$\begin{cases} \bar{d}Q < T dS \\ \bar{d}W > -p dV \end{cases} \quad \text{(قانون دوم)}$
$U \to U + dU$
$i \to f$

$\bar{d}Q + \bar{d}W = dU = T dS - p dV + \dots$

حالت‌های $i$ و $f$ باید دو حالت تعادلی باشند.
اما چون هر سه کمیت رابطه $\bigstar$ همگی متغیر حالت‌اند
چه اینکه مسیر $i$ تا $f$ واقعی باشد، چه یک مسیر برگشت‌پذیر
را بجای مسیر واقعی در تعیین (مقادیر) اعمال کنند.

(در نمودار مسیرها:)
مسیر واقعی فرآیند (برگشت‌ناپذیر)
برگشت‌پذیر (فرضی) فرآیند جانشین

به رابطه‌ی کلی زیر می‌رسیم :

$$dU = T dS - p dV + \dots$$


$$df = x_1 dy_1 + x_2 dy_2 + \dots \equiv f = f(y_1, y_2)$$

متغیر طبیعی (natural) $f$

$$U = U(S, V, \dots)$$

تابع پتانسیل $\longrightarrow dU = \left( \frac{\partial U}{\partial S} \right)_{V, \dots} dS + \left( \frac{\partial U}{\partial V} \right)_{S, \dots} dV + \dots$
$\equiv \quad T dS - p dV \quad \Bigg\} \implies$

$$
\begin{cases}
T = \left( \frac{\partial U}{\partial S} \right)_{V, \dots} \\
p = - \left( \frac{\partial U}{\partial V} \right)_{S, \dots}
\end{cases}
$$

$$\implies \frac{p}{T} = - \left( \frac{\partial U}{\partial V} \right)_S \Big/ \left( \frac{\partial U}{\partial S} \right)_V$$

if: $x = x(y, z) \implies dx = \left( \frac{\partial x}{\partial y} \right)_z dy + \left( \frac{\partial x}{\partial z} \right)_y dz \quad \text{[ یادآوری :}$

از قضیه تابع ضمنی $\swarrow$

$z = z(x, y) \implies dz = \left( \frac{\partial z}{\partial x} \right)_y dx + \left( \frac{\partial z}{\partial y} \right)_x dy \quad \Bigg\} \implies$

$\hookrightarrow dx = \left( \frac{\partial x}{\partial y} \right)_z dy + \left( \frac{\partial x}{\partial z} \right)_y \left[ \left( \frac{\partial z}{\partial x} \right)_y dx + \left( \frac{\partial z}{\partial y} \right)_x dy \right]$

$$= \underbrace{\left( \frac{\partial x}{\partial z} \right)_y \left( \frac{\partial z}{\partial x} \right)_y}_{=1} dx + \underbrace{\left[ \left( \frac{\partial x}{\partial y} \right)_z + \left( \frac{\partial x}{\partial z} \right)_y \left( \frac{\partial z}{\partial y} \right)_x \right]}_{=0} dy$$
$$
\Rightarrow \begin{cases} 
\left( \frac{\partial x}{\partial z} \right)_y = \frac{1}{\left( \frac{\partial z}{\partial x} \right)_y} & \text{reciprocal relation} \quad \text{رابطه وارونگی} \\ 
\\ 
\left( \frac{\partial x}{\partial y} \right)_z \left( \frac{\partial y}{\partial z} \right)_x \left( \frac{\partial z}{\partial x} \right)_y = -1 & \text{reciprocity relation} 
\end{cases}
$$

$$ x = x(y,z) \equiv f(x,y,z)=0 $$

$$ \frac{p}{T} = \left( \frac{\partial S}{\partial V} \right)_U $$

تذکر: به رابطه ی $T = \left( \frac{\partial U}{\partial S} \right)_{V,\dots}$ توجه کنید.

خواص ترمودینامیکی
$$ \Rightarrow \frac{1}{T} = \left( \frac{\partial S}{\partial U} \right)_{V,\dots} \quad (\text{رابطه } \square) $$

در وضعیت تعادلی که در اینجا داشتیم : حالت تعادل با حفظ دقیق حالت ماکروحالتی که تعداد میکرو حالت های سازگار با آن بیشینه بود $\Rightarrow$ (بقیه متغیرهای ماکرو حالت را ثابت میگیریم)

$$ \left( \frac{1}{\Omega} \frac{\partial \Omega}{\partial E} \right)_1 = \left( \frac{1}{\Omega} \frac{\partial \Omega}{\partial E} \right)_2 $$
(بقیه متغیرها ثابت)

[1] [2] در حالت تعادل
$\Omega$ : تعداد میکرو حالت های سازگار با ماکرو حالت تعادلی

$$ \frac{\partial \ln \Omega}{\partial E}\bigg|_1 = \frac{\partial \ln \Omega}{\partial E}\bigg|_2 $$
$T_1 = T_2$ : قانون صفرم
شرط تعادل

تعریف دما
$$ \Rightarrow \frac{1}{T} := \left( \frac{\partial \ln \Omega}{\partial E} \right)_{\dots} \Leftrightarrow \left( \frac{\partial S}{\partial U} \right)_{\dots} $$
با $\square$


Here is the exact, unsummarized academic English transcription of the lecture notes extracted directly from your provided images, maintaining full structural integrity, intermediate derivations, and strict LaTeX mathematical formatting.

---

## Thermodynamics and Statistical Mechanics I: Lecture 15 (Continued)

### Mathematical Proof of the Separation of Variables in the Zeroth Law

The condition for thermal equilibrium between system $1$ and system $3$ can be expressed as a functional constraint:


$$F_1(p_3, V_3, p_1, V_1) = 0 \quad \text{or} \quad \text{Condition for equilibrium of systems 1 and 3}$$

Similarly, the equilibrium condition between system $2$ and system $3$ is written as:


$$F_2(p_3, V_3, p_2, V_2) = 0 \quad \text{or} \quad \text{Condition for equilibrium of systems 2 and 3}$$

Solving each of these independent relationships explicitly for the reference parameter $p_3$ yields:


$$\begin{cases} p_3 = f_1(p_1, V_1, V_3) \\ p_3 = f_2(p_2, V_2, V_3) \end{cases} \implies f_1(p_1, V_1, V_3) = f_2(p_2, V_2, V_3) \quad \text{(Equation 0)}$$

Therefore, from this equation, we can write $p_1$ as an explicit function of the remaining variables (by an implicit function theorem):


$$\implies p_1 = g(V_1, p_2, V_2, V_3) \quad \text{(Equation 1)}$$

On the other hand, according to the experimental statement of the Zeroth Law, if systems $1$ and $2$ are each in thermal equilibrium with a third system $3$, then they must be in equilibrium with each other when placed in thermal contact. This means their mutual equilibrium condition is expressible strictly in terms of their own coordinates:


$$F_{12}(p_1, V_1, p_2, V_2) = 0 \quad \text{or} \quad \text{Condition for equilibrium of 1 and 2}$$

From this relation, solving for $p_1$ yields:


$$\implies p_1 = f_3(V_1, p_2, V_2) \quad \text{(Equation 2)}$$

Now, look at the contradiction between Equation (1) and Equation (2):

* In Equation (2), $p_1$ is determined strictly by $V_1, p_2, V_2$.
* In Equation (1), $p_1$ apparently depends on $V_3$ as well.

For $p_1$ to be independent of $V_3$, the variable $V_3$ must mathematically cancel out from the functional structure of Equation (0). This requires that the functions $f_1$ and $f_2$ must possess a separable form such that:


$$\Phi_1(p_1, V_1) = \Phi_2(p_2, V_2)$$

---

### Functional Definition of Empirical Temperature ($\Theta$)

The condition of mutual equilibrium between systems $1$ and $2$ leads to:


$$\implies \Phi_1(p_1, V_1) = \Phi_2(p_2, V_2)$$

When two systems are in thermal equilibrium, there exists a shared functional value common to both systems, which depends strictly on their respective state coordinates. For a collection of any arbitrary systems in mutual thermal equilibrium, this common scalar function can be equated to a single value:


$$\Phi(p, V) = \Theta$$

Where $\Theta$ is defined as the **Empirical Temperature**.

> **Conclusion from the Zeroth Law:** The existence of an equation of state for a system in equilibrium is guaranteed, which relates the state parameters and the empirical temperature:
> 
> $$\Phi(p, V) = \Theta$$
> 
> 
> 
> For example, for an ideal gas, this parameter takes the form:
> 
> $$pV = N k_B T$$
> 
> 

---

### Temperature Scales ($\Theta$ / $T$)

**Question:** How can we construct a universal scale for temperature and implement a practical thermometer?

* $\Theta$ is simply a label assigned to a specific isotherm.
* To establish an empirical scale for temperature, we choose a specific system and relate $\Theta$ to a measurable geometric parameter $x$ via the simplest relationship—a linear function:

$$\Theta(x) = a \cdot x \quad \text{(Linear function)}$$



To find the scaling constant $a$, we can proceed via two primary methods:

* **A.** Select a single standard reference state (fixed point) and assign it a specific temperature value.
* **B.** Select two separate fixed points and divide the interval between them into a specified number of units.

Following method B, let us define a scale based on a 100-unit interval between two primary reference temperatures: the **Ice Point** ($1\text{ atm}$, where pure ice melts in water) and the **Steam Point** ($1\text{ atm}$, where pure water boils).

#### Gas Thermometry Scales

A gas thermometer utilizes a gas sample inside a container, monitoring either volume changes or pressure changes:

* **Constant-Pressure Gas Thermometer ($p = \text{const.}$):**
We select volume $V$ as the changing thermometric property $x$:

$$\Theta = \frac{100}{V_s - V_i} V \quad \text{where } V_s = \text{volume at steam point, } V_i = \text{volume at ice point}$$


* **Constant-Volume Gas Thermometer ($V = \text{const.}$):**
We select pressure $p$ as the changing thermometric property $x$:

$$\Theta = \frac{100}{p_s - p_i} p$$



**Crucial Note:** Empirically, different real gases (e.g., Helium, Nitrogen, air) yield slightly different empirical temperature readings under standard conditions:


$$\Theta_1 \neq \Theta_2 \implies \Theta_{\text{He}} \neq \Theta_{\text{N}_2} \neq \Theta_x \dots$$


This variation occurs because real gases possess unique intermolecular interaction profiles.

However, experimental tracking shows that as the operating pressure of the gas thermometer approaches zero ($\lim p \to 0$), the molecular interactions vanish. In this low-pressure limit, the readings of all real gas thermometers converge perfectly to a single, identical value. This defines the **Ideal Gas Temperature Scale** ($T$):


$$pV = RT \quad (\text{for } n_m = 1\text{ mole})$$

$$\Theta \equiv T = \lim_{p \to 0} \frac{pV}{R} \quad \text{(Universal property)}$$

Using the Kelvin scale convention, the reference parameter is pinned to a single highly stable state—the **Triple Point of Water** ($T = 273.16\text{ K}$):


$$T/\text{K} = 273.16 \frac{\lim_{p \to 0} (pV)}{\lim_{p \to 0} (pV)_{\text{triple point}}}$$

---

### Thermodynamic Temperature Scale Based on Carnot's Theorem

**Question:** Is it fundamentally possible to define a temperature scale that is completely independent of the properties of any substance?

* **Answer:** Yes, by utilizing the efficiency of a reversible Carnot engine.

According to Carnot's theorem, the efficiency of a reversible engine operating between two thermal reservoirs depends purely on the temperatures of those reservoirs, completely independent of the working material:


$$\eta = 1 - \frac{Q_l}{Q_h} = f(\Theta_h, \Theta_l)$$

Consider a series of three operational empirical temperatures ($\Theta_3 > \Theta_2 > \Theta_1$) and two coupled Carnot engines:

* Engine 1 operates between $\Theta_3$ and $\Theta_2$, absorbing heat $Q_3$ and rejecting $Q_2$.
* Engine 2 operates between $\Theta_2$ and $\Theta_1$, absorbing heat $Q_2$ and rejecting $Q_1$.

Their respective thermal efficiencies match the expressions:


$$\eta(\Theta_3, \Theta_2) = \frac{Q_3 - Q_2}{Q_3} = 1 - \frac{Q_2}{Q_3}$$

$$\eta(\Theta_2, \Theta_1) = \frac{Q_2 - Q_1}{Q_2} = 1 - \frac{Q_1}{Q_2}$$

A single composite engine operating directly between the limits $\Theta_3$ and $\Theta_1$ yields:


$$\eta(\Theta_3, \Theta_1) = \frac{W + W'}{Q_3} = \frac{Q_3 - Q_1}{Q_3} = 1 - \frac{Q_1}{Q_3}$$

Since the ratio of heat inputs satisfies the mathematical identity $\frac{Q_3}{Q_2} \cdot \frac{Q_2}{Q_1} = \frac{Q_3}{Q_1}$, it requires that:


$$[1 - \eta(\Theta_3, \Theta_2)] \cdot [1 - \eta(\Theta_2, \Theta_1)] = 1 - \eta(\Theta_3, \Theta_1)$$

This specific functional equation can only be solved if the efficiency expression separates into a single-variable function $f(\Theta)$:


$$1 - \eta(\Theta, \Theta') =: \frac{f(\Theta')}{f(\Theta)} \implies \frac{Q_h}{Q_l} = \frac{f(\Theta_h)}{f(\Theta_l)}$$

By choosing the absolute thermodynamic temperature scale $T$ such that it is directly proportional to this function ($f(\Theta) \equiv T$), we obtain:


$$\frac{f(\Theta')}{f(\Theta)} =: \frac{T'}{T} \implies \frac{Q_h}{Q_l} = \frac{T_h}{T_l}$$

This scale is the **Absolute Thermodynamic Scale**, which is completely independent of any physical material properties and perfectly matches the ideal gas scale.

---

### The Link to Statistical Mechanics: Boltzmann Relation

$$S \propto \ln \Omega$$


By selecting a constant multiplier to scale this microstate expression, we can fully align statistical mechanics with classical thermodynamics. This constant is the Boltzmann constant, $k_B$:


$$S = k_B \ln \Omega$$

From the definition of temperature via the total differential of entropy:


$$\frac{1}{k_B T} = \left( \frac{\partial S}{\partial U} \right)_{V, \dots} \quad (\text{where } k_B \text{ is a scaling constant})$$

This provides the complete formulation of the **Boltzmann Relation**, bridging classical thermodynamic parameters with the absolute number of microscopic configurations ($\Omega$) accessible to a macrostate:


$$S = k_B \ln \Omega(U, V, \dots)$$

---

### Irreversible Processes: Analysis of Joule's Free Expansion

Consider an application example of an irreversible process to evaluate global entropy shifts. A rigid, thermally isolated (adiabatic) container is divided into two symmetrical halves, Left ($L$) and Right ($R$).

* **Initial State ($i$):** One mole ($n_m = 1$) of an ideal gas is confined to chamber $L$ with initial coordinates $p_i, V_1 = V_0, T_i$. Chamber $R$ is completely evacuated ($p = 0$, vacuum).
* **Process ($i \to f$):** The valve separating the chambers is opened, allowing the gas to perform an unconstrained free expansion into the vacuum until it occupies the total volume $V_f = 2V_0$.

```
  Initial State (i)               Final State (f)
  +---------+---------+           +---------+---------+
  |  o o o  |         |  i -> f   |  o   o  |  o   o  |
  |  o gas o| vacuum  | ========> |    gas  |   gas   |
  |  o o o  |         |           |  o   o  |  o   o  |
  +---------+---------+           +---------+---------+
   p_i,V0,T_i  Rigid, Isolated     p_f, 2V0, T_f

```

#### Boundary Evaluation:

* No work is performed against the environment because the external boundaries are rigid ($\Delta W = 0$).
* No heat exchange occurs because the external walls are adiabatic ($\Delta Q = 0$).
* From the First Law of Thermodynamics ($\Delta U = \Delta Q + \Delta W$):

$$\Delta U_{\text{free expansion}} = 0$$



For an ideal gas, internal energy is strictly a function of temperature ($U = U(T)$). Therefore:


$$\Delta U = 0 \implies \Delta T = 0 \implies T_f = T_i$$

Evaluating the initial and final equilibrium points via the ideal gas law ($pV = RT$):


$$\begin{cases} p_i V_0 = R T_i \\ p_f (2V_0) = R T_f \end{cases} \implies p_f = \frac{p_i}{2}$$

---

### Calculation of Entropy Change ($\Delta S$) in Free Expansion

**Question:** What is the exact change in entropy ($\Delta S$) during this process?

* Because free expansion is highly irreversible, the intermediate states are not in equilibrium, meaning the process cannot be traced as a continuous line on a standard $p\text{-}V$ diagram.
* However, since entropy is a state function, its total change ($\Delta S$) depends exclusively on the initial and final endpoints ($i$ and $f$), completely independent of the path taken.
* Therefore, we can substitute the actual irreversible path with an imaginary, **reversible isothermal process** ($T = \text{const.}$) that connects the exact same initial volume $V_0$ to the final volume $2V_0$.

```
  p ^  i
    |   *
    |    \  Isothermal Path: T = const. (Calculated)
    |     \ . . . . .
    |               * f
    +-------------------> V

```

If $T = \text{const.}$, then $dU = 0$. From the fundamental thermodynamic relation ($dU = TdS - p dV$):


$$T dS = p dV \implies dS = \frac{p}{T} dV$$

Substituting the ideal gas state relation ($pV = RT \implies \frac{p}{T} = \frac{R}{V}$) into the integral:


$$\Delta S_{V_0 \to 2V_0} = \int_i^f dS = \int_{V_0}^{2V_0} \frac{p}{T} dV = \int_{V_0}^{2V_0} \frac{R \, dV}{V} = R \ln 2$$

$$\implies \Delta S_{\text{gas}} = R \ln 2 \quad \text{(Valid for the irreversible final state as well)}$$

#### Total Entropy Change of the Universe ($\Delta S_{\text{universe}}$):

* **If the expansion path were carried out reversibly:**
The system must absorb heat from an external reservoir to maintain temperature, meaning the environment experiences a negative entropy shift ($\Delta S_{\text{surr}} = -R \ln 2$).

$$\Delta S_{\text{universe}} = \Delta S_{\text{surr}} + \Delta S_{\text{gas}} = -R \ln 2 + R \ln 2 = 0$$


* **For the actual Joule free expansion process:**
Because the system is completely isolated from its surroundings, no heat passes through the boundaries, meaning the environment experiences no state change at all ($\Delta S_{\text{surr}} = 0$).

$$\Delta S_{\text{universe}} = \Delta S_{\text{surr}} + \Delta S_{\text{gas}} = 0 + R \ln 2 = R \ln 2 > 0$$



> Since $\Delta S_{\text{universe}} > 0$, the process is macroscopically proven to be completely irreversible.

---

### Macroscopic Comparison of Three Expansion/Mixing Scenarios

Let us evaluate three distinct configurations involving a partitioned two-chamber container:

1. **Scenario 1: Free Expansion of a Gas**
Initially, gas molecules occupy only one chamber, with a vacuum in the other. Removing the partition results in a classic unconstrained free expansion.

$$\Delta S_{\text{gas}} = N k_B \ln 2 \implies \Delta S_{\text{universe}} > 0 \quad (\text{Irreversible Process})$$


2. **Scenario 2: Mixing of Two Distinguishable Gases**
The left chamber contains blue gas molecules, and the right chamber contains red gas molecules. Removing the partition results in macroscopic mixing (diffusion). Reversing this process spontaneously to separate the components is impossible.

$$\Delta S_{\text{universe}} = 2 N k_B \ln 2 > 0 \quad (\text{Irreversible Process})$$


3. **Scenario 3: "Mixing" of Two Indistinguishable Gas Samples**
Both chambers contain identical particles of the exact same gas species at equal initial temperature and pressure. When the partition is removed, a microscopic exchange occurs, but no macroscopic or measurable parameters change ($\Delta \text{Macro} = 0$). Reinserting the partition restores the identical macroscopic configuration perfectly.

$$\Delta S_{\text{universe}} = 0 \quad (\text{Fully Reversible Process})$$



#### Analysis Summary:

* An irreversible process is always accompanied by a net increase in the total entropy of the universe.
* When a transition occurs between states that are macroscopically identical (such as the mixing of identical ideal gases at identical initial parameters), no thermodynamic state change occurs, and the entropy change is zero:

$$\Delta S = 0$$


* Conversely, if the mixing components are separate, distinct species (as in Scenario 2), the total entropy shift is the sum of their individual expansion contributions, leading to the entropy of mixing:

$$\Delta S_{\text{mixing}} = 2 \Delta S_{\text{Joule expansion}}$$
