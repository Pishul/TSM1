

---

## ترمودینامیک و مکانیک آماری ۱: پتانسیل‌های ترمودینامیکی

### تابع حالت

* قانون اول $\longleftarrow U$
* قانون دوم $\longleftarrow S$
* مختصات ترمودینامیکی $\longleftarrow p, V, T, \dots$

> **تعریف:** تابع حالت تنها به وضعیت تعادلی سیستم ترمودینامیکی ربط دارد، نه به راهی که به آن وضعیت رسیده است.

### سؤال: آیا جز ویژگی‌های منحصر به فرد $S$ و $U$ تابع دیگری هم ترکیب از توابع بالا وجود دارد؟

**مثال:** $\Delta F = \Delta U - T \Delta S$ در استخراج کار ماکزیمم (کار تک‌دمایی)


$$\Delta W_c \ge \Delta F$$

```
   c
 /   \
i     f

```

### پتانسیل‌ها / انرژی‌های ترمودینامیکی فرضی دیگر:

* $U + TS$
* $U - pV$
* $U + 2pV - 3TS$
* $\dots$

سه پتانسیل ترمودینامیکی مبنا هستند که تعریف می‌شوند:

1. **انرژی آزاد هلمولتز (کار آزاد):**

$$F := U - TS$$


2. **انرژی آزاد گیبس (کار آزاد پیستون):**

$$G := U + pV - TS = H - TS$$


3. **آنتالپی:**

$$H := U + pV$$



### قانون اول و دوم ترکیبی:

$$dU = T dS - p dV + \dots$$


(عبارت‌های بعد مربوط به تغییر ذره‌ها مانند $\mu dN$ است)


$$\implies U = U(S, V, N, \dots) \quad \text{:متغیر طبیعی}$$

**از طرفی دیفرانسیل کامل یک تابع حالت:**


$$dU = \left(\frac{\partial U}{\partial S}\right)_{V, N, \dots} dS + \left(\frac{\partial U}{\partial V}\right)_{S, N, \dots} dV + \left(\frac{\partial U}{\partial N}\right)_{S, V, \dots} dN + \dots$$

---

اگر $N = \text{const.} \implies dN = 0$:


$$\begin{cases} T = \left(\frac{\partial U}{\partial S}\right)_{V, N} \\ p = -\left(\frac{\partial U}{\partial V}\right)_{S, N} \end{cases} \implies \frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{N, V}$$

### فرآیند هم‌حجم (Isochoric)

$$V = \text{const.} \implies dV = 0 \quad (dN = 0) \implies dU = T dS$$

در فرآیند برگشت‌پذیر تک‌دمایی داریم:


$$dS = \frac{\delta Q_{\text{rev.}}}{T}$$

$$\implies \left. dU \right\vert{}_{V = \text{const.}} = \left. \delta Q \right\vert{}_{V = \text{const.}} = C_v dT \implies \Delta U = \int_{T_1}^{T_2} C_v(T) dT \quad \text{at } V = \text{const.}$$

می‌خواهیم یک چنین رابطه‌ای برای فرآیند هم‌فشار ($p = \text{const.}$) تعریف کنیم. دلیل این کار این است که تغییرات ساختاری کار شیمیایی معمولاً در $p = \text{const.}$ است.


$$H = U + pV \implies dH = dU + dp \, V + p dV = T dS - p dV + dp \, V + p dV = T dS + V dp$$

$$\implies H = H(S, p) \quad \text{:متغیر طبیعی}$$

دیفرانسیل کامل تابع حالت:


$$dH = \left(\frac{\partial H}{\partial S}\right)_p dS + \left(\frac{\partial H}{\partial p}\right)_S dp + \dots$$

---

$$\implies \begin{cases} T = \left(\frac{\partial H}{\partial S}\right)_p \\ V = \left(\frac{\partial H}{\partial p}\right)_S \end{cases}$$

### برای فرآیند هم‌فشار (Isobaric)

$$p = \text{const.} \implies dp = 0 \implies \left. dH \right\vert{} = T dS \Big\vert{}_{p = \text{const.}}$$

از طرفی در یک فرآیند برگشت‌پذیر داریم:


$$T dS = \delta Q_{\text{rev.}}$$

$$\implies \left. dH \right\vert{}_{p = \text{const.}} = \delta Q_{\text{rev.}} = C_p dT \implies \Delta H = \int_{T_1}^{T_2} C_p(T) dT \quad \text{at } p = \text{const.}$$

* $\left. dU \right\vert{}_{V = \text{const.}} = \delta Q_{\text{rev.}}$: انرژی درونی معادل است با گرمایی که در فرآیند برگشت‌پذیر هم‌حجم با محیط تبادل شده است.
* $\left. dH \right\vert{} = \delta Q_{\text{rev.}}$: آنتالپی معادل است با گرمایی که در فرآیند برگشت‌پذیر هم‌فشار با محیط تبادل شده است.

> **تذکر:** علی‌رغم تغییر بین $U$ و $H$، این دو هنوز یک ویژگی بنیادی مشترک دارند: حضور $S$ به عنوان متغیر طبیعی در $U$ و $H$.
> 
> $$U = U(S, V, N)$$
> 
> 
> $$H = H(S, p, N)$$
> 
> 
> 
> این کار سخت است، چرا که نمی‌توانیم در آزمایشگاه متغیر آنتروپی را کنترل کنیم (تغییر آنتروپی در یک فرآیند بسیار پیچیده و مبهم است).

---

تغییر متغیر از متغیر طبیعی سخت مثل $S$ به یک متغیر آسان‌تر مثل $T$ یا $p$ و یا لااقل در آزمایشگاه راحت‌تر با کمک **تبدیل لژاندر**:


$$F = U - TS$$

$$\implies dF = dU - d(TS) = dU - T dS - S dT = T dS - p dV - T dS - S dT = -S dT - p dV$$

$$\implies F = F(T, V, N) \quad \text{:یافتن متغیر طبیعی}$$

$$dF = \left(\frac{\partial F}{\partial T}\right)_V dT + \left(\frac{\partial F}{\partial V}\right)_T dV + \dots$$

$$\implies \begin{cases} S = -\left(\frac{\partial F}{\partial T}\right)_V \\ p = -\left(\frac{\partial F}{\partial V}\right)_T \end{cases}$$

### در فرآیند هم‌دما:

$$T = \text{const.} \implies dT = 0 \implies \left. dF \right\vert{}_{T = \text{const.}} = -p dV \implies \left. \Delta F \right\vert{}_{T = \text{const.}} = -\int_{V_1}^{V_2} p(V) dV = \Delta W$$

$\Delta F$ میزان کار برگشت‌پذیری است که در محیط هم‌دما می‌توان انجام داد، یا به عبارتی تغییرانرژی سیستم آزاد می‌شود.

> **پایستگی کار ماکزیمم:** $\Delta W_{i \to f} \ge \Delta F$ (کار انجام شده روی سیستم باید بزرگتر یا مساوی تغییرات انرژی آزاد هلمولتز در فرآیند $i \to f$ باشد).

> **تذکر:** تعریف پتانسیل‌ها بسیار کارآمد است برای درک ترجیح دادن یک مسیر فرآیند مکانیکی یا شیمیایی توسط خود سیستم (ترمودینامیک شیمیایی).

---

```
 To = Const.
 po = Const.
  ___   ___
 | o | |   |
 |___| |___|
   |

```

پس پتانسیل‌های بهتری می‌خواهیم تا طبق آزمایش‌های ترمودینامیکی بتوان کارهایی انجام داد که $T$ و $p$ متغیرهای طبیعی آن باشند.

### انرژی آزاد گیبس

$$G \equiv H - TS = U + pV - TS$$

$$dG = dU + d(pV) - d(TS) = T dS - p dV + p dV + V dp - T dS - S dT = -S dT + V dp$$

$$\implies dG = -S dT + V dp \implies G = G(T, p, N)$$

دیفرانسیل کامل تابع حالت گیبس:


$$dG = \left(\frac{\partial G}{\partial T}\right)_p dT + \left(\frac{\partial G}{\partial p}\right)_T dp + \dots$$

$$\implies \begin{cases} S = -\left(\frac{\partial G}{\partial T}\right)_p \\ V = \left(\frac{\partial G}{\partial p}\right)_T \end{cases}$$

این پتانسیل به راحتی کنترل می‌شود (در آزمایشگاه)؛ چرا که در آزمایش‌های روزمره معمولاً:

* $p = \text{const.}$ (فشار اتمسفر)
* $T = \text{const.}$ (دمای اتاق)

در این شرایط $dG = 0$ است:


$$\left. G \right\vert{} = \text{const.} \quad \text{:تعادل شیمیایی}$$

---

$$\left. G \right\vert{}_{\text{فاز ۱}} = \left. G \right\vert{}_{\text{فاز ۲}}$$


به عنوان مثال، در فرآیند آزمایش‌های تغییر فاز، وقتی مایع تبدیل به گاز می‌شود در یک دما و فشار مشخص (دما و فشار آزمایشگاه):


$$G_1(T_{\text{lab}}, p_{\text{lab}}) = G_2(T_{\text{lab}}, p_{\text{lab}})$$


در این فازها تغییر فاز با کمک "کار آزاد پیستون" پایدار است.

---

### اندازه‌گیری کمیت‌های بنیادی:

کافی است بتوانیم سه بردار ملکول، زمان و حرارت را بسنجیم تا بارها تغییر در خواص مادی را بدست آوریم: $L, M, T, Q$

### برای انتخاب پتانسیل‌های ترمودینامیکی از قانون اول و قانون دوم ترمودینامیک:

قانون دوم:


$$dS \ge \frac{\delta Q}{T} \implies \delta \sigma \equiv dS - \frac{\delta Q}{T} \ge 0$$

* $\delta \sigma$: تولید آنتروپی درونی
* $dS$: تغییر آنتروپی

اگر فرآیند به صورت بی‌دررو انجام شود، سیستم با محیط تبادل گرما ندارد ($\delta Q = 0$):


$$\delta Q = 0 \implies \left. \delta \sigma \right\vert{}_{\delta Q = 0} = dS \ge 0$$


در فرآیندی که در یک سیستم منزوی بسته رخ می‌دهد، آنتروپی سیستم همواره افزایش می‌یابد یا ثابت می‌ماند.

> **نگاه فرضی به قانون دوم و بازگشت به پتانسیل‌های شیمیایی:**
> به جای بررسی یک سیستم که با محیط رابطه ندارد، یک سیستم **باز** در نظر می‌گیریم که می‌تواند با محیط، اطلاعات، تبادل کار و انرژی کند.

---

```
   -----------------------
  |  محیط                 |  To
  |  environment          |  po
  |                       |
  |        -------        |
  |       |سیستم  |======>|
  |       |System |       |
  |        -------        |
   -----------------------

```

**محیط بسیار صلب:**


$$\text{(Themally isolated + rigid)}$$


طبیعی است که گستره تغییرات سیستم به محیط اطراف تبادل پیدا می‌کند:


$$\Delta (\text{Environment}) = -\Delta (\text{System})$$

سؤال: قانون دوم برای این سیستم چگونه است؟


$$\delta \sigma = dS_{\text{System}} - \frac{\delta Q}{T} \ge 0 \longrightarrow dS_{\text{System}} \ge \frac{\delta Q}{T}$$


تولید آنتروپی درونی ($System$) به افزایش یا تغییر تدریجی منجر می‌شود.


$$dS_{\text{tot}} = dS_{\text{System}} + dS_{\text{environment}} \ge 0$$


(قانون دوم برای کل سیستم و محیط)

با فرض اینکه انتقال انرژی $dU$ در حجم جابجا شده اتفاق بیفتد:


$$\text{System} \iff \text{environment} \quad [ -dV \text{ حجم} ]$$


تغییرات انرژی محیط:


$$dU_0 = -dU_{\text{System}}$$


طبق قانون اول:


$$U_{\text{tot}} = \text{const.} = U_{\text{system}} + U_{\text{environment}}$$

کار و انرژی رد و بدل شده بین سیستم و محیط را می‌توان با کمک خواص محیط ($T_0$ و $p_0$) مشخص کرد:


$$\implies dU_0 = -dU = T_0 dS_0 - p_0 dV_0$$


که در آن $dV_0 = -dV$ است.

---

$$\implies dU_0 = -dU = T_0 dS_0 + p_0 dV \longrightarrow dS_0 = \frac{-dU - p_0 dV}{T_0}$$


از آنجا که:


$$dS_{\text{tot}} = dS_0 + dS \ge 0$$

$$\implies dS_{\text{tot}} = -\frac{1}{T_0} [dU + p_0 dV] + dS \ge 0$$


ضرب در $T_0$ (دمای محیط که مثبت است):


$$\implies T_0 dS_{\text{tot}} = -[dU + p_0 dV] + T_0 dS \ge 0$$

$$\implies dU + p_0 dV - T_0 dS \le 0$$

> این رابطه، بیان قانون دوم ترمودینامیک برای سیستم در حضور محیط است.

**یادآوری:** قانون دوم کلاسیک می‌گوید $dS \ge \frac{\delta Q}{T}$ (در صورتی که سیستم از محیط مجزا و منزوی باشد).

از این به بعد به جای بررسی خود قانون دوم ترمودینامیک، عبارتی را به نام $A$ برحسب پتانسیل‌های سیستم و مشخصات محیط تعریف می‌کنیم که به آن **Availability (قابلیت دسترسی)** می‌گویند:


$$A \equiv U + p_0 V - T_0 S$$

$$\implies dA \le 0$$

---

برای هر سیستم باز یا فرآیندی که در یک محیط با فشار و دمای ثابت رخ می‌دهد، قانون دوم ایجاب می‌کند که این تابع همواره نزولی یا ثابت باشد، یعنی "دسترس‌پذیری" باید کمینه شود:

```
  حالت تعادل سیستم باز <=====> کمینه‌شدن A

```

$$\iff \text{تولید آنتروپی درونی ماکزیمم}$$

1. **If $S, V = \text{const.}$:**

$$dS = dV = 0 \implies \left. dA \right\vert{}_{V = \text{const.}, S = \text{const.}} = dU \le 0$$



برای یک سیستم منزوی هم‌حجم و هم‌آنتروپی، انرژی درونی سیستم کمینه می‌شود.
2. **If $S, p = \text{const.}$:**

$$dS = dp = 0 \implies \left. dA \right\vert{}_{S = \text{const.}, p = \text{const.}} = dU + p_0 dV = dH \le 0$$



به طور نظری داریم:

$$dH = dU + p dV + V dp \xrightarrow{p = p_0 = \text{const.}} dH = dU + p_0 dV$$



در فشار ثابت و آنتروپی ثابت، آنتالپی رو به کاهش و کمینه شدن می‌رود.
3. **If Thermally isolated, $V = \text{const.}$:**

$$\delta Q = 0 , \ dV = 0 \implies dU = 0$$



---

$$\implies \left. dA \right\vert{}_{\substack{\text{thermally isolated} \\ V = \text{const.}}} = -T_0 dS \le 0 \implies \left. dS \right\vert{}_{\substack{\text{thermally isolated} \\ \text{rigid}}} \ge 0$$


(پیدایش شکل سنتی قانون دوم ترمودینامیک)

---