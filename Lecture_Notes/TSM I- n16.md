
## ترمودینامیک و مکانیک آماری ۱: ۱۵ خرداد

### فرآیندها در محیط‌های خاص (ادامه)

iv) $T, V = \text{const.} \implies dA = dU - T_0 dS \le 0$
در این حالت اگر فرض کنیم:


$$\begin{cases} T = T_0 \implies dT = 0 \\ dF = dU - T_0 dS - S dT = dU - T_0 dS \end{cases} \implies dA = dF \le 0$$

$$(F = U - T_0 S)$$

> یعنی برای یافتن جهت تعادل کافی است تغییرات تابع هلمولتز را بررسی کرد.

vi) $p, T = \text{const.}$


$$dA = dU - T_0 dS + p_0 dV$$

$$dG = dU + p_0 dV + V dp_0 - T_0 dS - S dT = dU - T_0 dS + p_0 dV \implies dA = dG \le 0$$

> شرايط آزمایشگاهی در آزمایشگاه‌های شیمی:
> برای یک واکنش شیمیایی با توجه به پتانسیل شیمیایی ترجیحاً داریم که واکنش به سمتی می‌رود که:
> 
> $$dG \le 0$$
> 
> 

در یک واکنش شیمیایی:


$$p = \text{const.} \implies \Delta H = \Delta Q_{\text{rev.}}$$


اگر واکنش فرضی داشته باشیم که به صورت زیر گرماگیر یا گرماده باشد:


$$\text{if } \begin{cases} \Delta H < 0 \implies \text{گرماده} \\ \Delta H > 0 \implies \text{گرماگیر} \end{cases}$$


با این حال $\Delta H$ نشان نمی‌دهد که آیا یک واکنش شیمیایی انجام خواهد شد یا خیر. به همین جهت باید تغییرات $\Delta G$ را بررسی کنیم تا جهت فرآیند مشخص شود.


$$\left. C, p, T \right\vert{}_{\text{const.}}$$

---

* **آیا فرآیند یا واکنش شیمیایی رو به کاهش $\Delta G < 0$ (یعنی کار ماکزیمم) انجام‌پذیر است؟**

$$\implies \text{if } \Delta G < 0 \implies \text{واکنش شیمیایی به جهت ظرفیت انرژی انجام خواهد شد}$$

```
  G ^
    |     .. (انرژی فعال‌سازی activation)
 G_i|---*    \
    |   |     \
    |   |      *--------
 G_f|---+---------------->
    |   |______/
    |     زمان t
    +------------------->

```

حالت مابین: metastable (ناپایدار)

```
  G ^
    |   *
    |    \
    |     *--->
    +----------> t

```

### شرایط عمومی تعادل ترمودینامیکی:

$$S = S(U, V, N)$$


سیستم منزوی و با محیط اطراف در تماس نیست.

دیواره صلب تنها برای عبور انرژی‌های حرارت:


$$U_1 + U_2 = \text{const.}$$

```
  +---------+---------+
  |   N1    |   N2    |
  |   V1    |   V2    |
  |   U1  <===> U2    |
  +---------+---------+
   عایق حرارتی + صلب

```

**سؤال:** وضعیت تعادل انرژی‌ها در دو سیستم چگونه خواهد بود؟


$$\begin{array}{c\|c} U_1 + U_2 & = U_1 + U_2 \\ t=0 & t \to \infty \end{array} \implies \text{حالت تعادل} \quad \left. \begin{array}{c} \text{شورای } \\ U_1 , U_2 \end{array} \right\vert{}_{t=\infty} ?$$

انرژی افزون‌بر این:


$$S_{\text{tot}} = S_1 + S_2 = S(U_1, N_1, V_1) + S(U_2, N_2, V_2)$$

---

تعادل زمانی رخ می‌دهد که آنتروپی سیستم کل بیشینه شود:


$$dS_{\text{tot}} \ge 0 \longrightarrow \left. dS_{\text{tot}} \right\vert{}_{\text{eq.}} = 0$$


چون فقط یک متغیر مستقل داریم (فرضاً $U_1$) و متغیر دیگر به صورت جابجایی صلب از رابطه $U_2 = \text{const.} - U_1$ تبعیت می‌کند:


$$\frac{\partial S(U_1, \dots)}{\partial U_1} + \frac{\partial S(U_2, \dots)}{\partial U_1} = 0 \equiv \frac{\partial S(U_1)}{\partial U_1} - \frac{\partial S(U_2)}{\partial U_2} = 0$$

$$dU_1 = -dU_2$$

$$\implies \left. \frac{\partial S(U_1, N_1, V_1, \dots)}{\partial U_1} \right\vert{}_{\text{تعادل}} = \left. \frac{\partial S(U_2, N_2, V_2, \dots)}{\partial U_2} \right\vert{}_{\text{تعادل}}$$

با توجه به تعریف دما:


$$\left(\frac{\partial S}{\partial U}\right)_{N, V, \dots} =: \frac{1}{T} \implies \left. \frac{1}{T_1} \right\vert{}_{\text{تعادل}} = \left. \frac{1}{T_2} \right\vert{}_{\text{تعادل}}$$

$$\implies \left. T_1 \right\vert{}_{\text{تعادل}} = \left. T_2 \right\vert{}_{\text{تعادل}}$$

> این تعریف که دو سیستم در صورتی دمای یکسانی دارند که وقتی در تماس جابجایی انرژی با یکدیگر قرار می‌گیرند (دیواره ثابت و رسانا)، جابجایی خالص رخ ندهد، ما را به همان قانون صفرم ترمودینامیک ارجاع می‌دهد.

```
  +---------+
  |    1    |
  +----+----+
  | 2  | 3  |
  +----+----+

```

$$\begin{cases} N_1, N_2, N_3 = \text{const.} \\ V_1, V_2, V_3 = \text{const.} \\ U_1 + U_2 + U_3 = \text{const.} \implies \text{اندک تغییر تعادلی سیستم وابسته به } (U_1, U_2) \end{cases}$$

---

$$S_{\text{tot}} = S_1 + S_2 + S_3 = S(U_1, N_1, V_1) + S(U_2, N_2, V_2) + S(U_3, N_3, V_3)$$

$$\text{تعادل:} \quad \begin{cases} \left( \frac{\partial S_{\text{tot}}}{\partial U_1} \right)_{U_2=\text{const.}} = 0 \implies \frac{\partial S(U_1, \dots)}{\partial U_1} + \frac{\partial S(U_3 = U - U_1 - U_2, \dots)}{\partial U_1} = 0 \\ \left( \frac{\partial S_{\text{tot}}}{\partial U_2} \right)_{U_1=\text{const.}} = 0 \implies \frac{\partial S(U_2, \dots)}{\partial U_2} + \frac{\partial S(U_3 = U - U_1 - U_2, \dots)}{\partial U_2} = 0 \end{cases}$$

$$\implies \begin{cases} \left. \frac{\partial S(U_1, \dots)}{\partial U_1} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S(U_3, \dots)}{\partial U_3} \right\vert{}_{\text{eq.}} \\ \left. \frac{\partial S(U_2, \dots)}{\partial U_2} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S(U_3, \dots)}{\partial U_3} \right\vert{}_{\text{eq.}} \end{cases} \implies \begin{array}{c} T_1 = T_3 \\ T_2 = T_3 \end{array} \implies$$

$$\text{ماتریس:} \quad \left. T_1 \right\vert{}_{\text{eq.}} = \left. T_2 \right\vert{}_{\text{eq.}} = \left. T_3 \right\vert{}_{\text{eq.}} \quad \longleftarrow \text{قانون صفرم ترمودینامیک}$$

> **نتیجه:** استخراج این نتیجه به این معنی است که تعریف مفهوم دما ظاهراً از قانون هشتم ترمودینامیک زائد است و یک متغیر ذاتی برای یافتن تعادل سیستم است که از تعریف کل ماکزیمم آنتروپی هم استخراج می‌شود.

### b) وضعیتی که دیواره در شرایط جابجایی و جابه‌جایی ذره‌ها می‌تواند تغییر کند:

```
  +---------+---------+
  |   N1    |   N2    |
  | V1 <===>|===> V2  |
  | U1 <===>|===> U2  |
  +---------+---------+

```

$$\Sigma_{\text{قید}} : \begin{cases} U_1 + U_2 = \text{const.} \quad \mathbf{1} \\ V_1 + V_2 = \text{const.} \quad \mathbf{2} \end{cases}$$


که برای یافتن حالت تعادل کلی کافی است پیوستگی دیفرانسیل جزئی نسبت به تک‌تک متغیرها را برابر با صفر قرار داد.


$$\left. \frac{\partial S(U_1, V_1, \dots)}{\partial U_1} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S(U_2, V_2, \dots)}{\partial U_2} \right\vert{}_{\text{eq.}} \implies T_1 = T_2$$

$$\left. \frac{\partial S(U_1, V_1, \dots)}{\partial V_1} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S(U_2, V_2, \dots)}{\partial V_2} \right\vert{}_{\text{eq.}}$$

---

با توجه به تعریف:


$$\frac{p}{T} = \left(\frac{\partial S}{\partial V}\right)_{N, U} \quad \text{تعریف فشار و فیزیک آن}$$

$$\implies \begin{cases} T_1 = T_2 \Big\vert{}_{\text{eq.}} \\ \left. \frac{p_1}{T_1} = \frac{p_2}{T_2} \right\vert{}_{\text{eq.}} \end{cases} \implies \begin{array}{\|c\|} \hline p_1 = p_2 \\ T_1 = T_2 \\ \hline \end{array}$$

### c) جابجایی ذره‌ها

$$\Sigma_{\text{قید}} : \begin{cases} U_1 + U_2 = \text{const.} \\ V_1 + V_2 = \text{const.} \implies dV_1 = -dV_2 \\ N_1 + N_2 = \text{const.} \implies dN_2 = -dN_1 \end{cases}$$

```
  +---------+---------+
  |   N1  <===> N2    |
  |   V1  <===> V2    |
  |   U1  <===> U2    |
  +---------+---------+

```

$$\text{پیوستگی} \implies \begin{cases} \left. \frac{\partial S_1(U_1, N_1, V_1)}{\partial U_1} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S_2(U_2, V_2, N_2)}{\partial U_2} \right\vert{}_{\text{eq.}} \\ \left. \frac{\partial S_1(U_1, N_1, V_1)}{\partial V_1} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S_2(U_2, V_2, N_2)}{\partial V_2} \right\vert{}_{\text{eq.}} \\ \left. \frac{\partial S_1(U_1, V_1, N_1)}{\partial N_1} \right\vert{}_{\text{eq.}} = \left. \frac{\partial S_2(U_2, V_2, N_2)}{\partial N_2} \right\vert{}_{\text{eq.}} \end{cases}$$

$$\implies \begin{cases} \left. \frac{1}{T_1} \right\vert{}_{\text{eq.}} = \left. \frac{1}{T_2} \right\vert{}_{\text{eq.}} \\ \left. \frac{p_1}{T_1} \right\vert{}_{\text{eq.}} = \left. \frac{p_2}{T_2} \right\vert{}_{\text{eq.}} \end{cases} \implies \dots$$

از طرفی تعریف تفاضلی:


$$\left(\frac{\partial S}{\partial N}\right)_{U, V} \equiv -\frac{\mu}{T} \implies \left. \frac{\mu_1}{T_1} \right\vert{}_{\text{eq.}} = \left. \frac{\mu_2}{T_2} \right\vert{}_{\text{eq.}}$$

> **شرط تعادل در وضعیت تبادل ذره و ذرات:**
> 
> $$T_1 = T_2 \ ; \ p_1 = p_2 \ ; \ \mu_1 = \mu_2$$
> 
> 
> 
> **تعادل کل ترمودینامیکی**

---

```
   +----------+
   | V1 | V2  | -> استدلال این که N و V به راحتی مستقل از هم هستند
   +----------+

```

پیدایش چهارمین پتانسیل بزرگ ترمودینامیکی خاص که از ویژگی‌های کلی بهره‌مند هستند:


$$U, S \quad \text{:توابع حالت مبنا} \implies F \equiv U - TS \quad \text{:تعریف هلمولتز}$$

$$G \equiv U - TS + pV \implies (dG = -S dT + V dp + \mu dN)$$

$$\Omega \equiv U - TS - \mu N \implies d\Omega = -S dT + p dV - N d\mu$$

$$\text{(پتانسیل بزرگ یا گرند پتانسیل)}$$

$$dU = T dS - p dV + \mu dN$$

$$B \equiv U - TS - \mu N + pV \implies \text{گرند گیبس فلوئیدی}$$


(این تک پتانسیل مجزا نیز در برخی محاسبات کارآمد است)

* $U$: فرومحور
* $-TS$: فرومحور
* $-\mu N$: فرومحور
* $+pV$: فرومحور

---

$$dB = -S dT - N d\mu + V dp$$


سیستم پتانسیل تغییرات ترمودینامیکی برای متغیرهای مستقل $(T, \mu, p)$ تغییر می‌کند.


$$\implies \left. dB \right\vert{}_{\begin{array}{c} T=\text{const.} \\ \mu=\text{const.} \\ p=\text{const.} \end{array}} = 0 \implies \left. B \right\vert{} = \text{const.}$$

$$\begin{cases} T = \text{const.} \\ \mu = \text{const.} \\ p = \text{const.} \end{cases}$$

سیستم همگن فرضی به این صورت است که دقیقاً مشابه یکسانی افزایش می‌یابند:

```
  +------+------+
  |  I   |  I'  |
  +------+------+

```

تغییرات فاز کلی مستقل از حجم است و به متغیرهای مقیاس‌پذیر وابسته نیست:


$$(T, p, \mu) \text{ هر سه اینها فشرده (مستقل از جرم) هستند}$$

$$\text{کلیت طرفین:} \quad \begin{cases} B_{II'} = B_I + B_{I'} \\ \left. B_{II'} \right\vert{}_{p, T, \mu = \text{const.}} = B_I = \text{const.} \implies \left. B \right\vert{} = 0 \end{cases}$$

$$\begin{cases} T = \text{const.} \\ \mu = \text{const.} \\ p = \text{const.} \end{cases}$$

$$\implies B = \underbrace{U - TS}_{F} - \mu N + \underbrace{pV}_{=0} = 0 \implies \begin{array}{\|c\|} \hline G = \mu N \\ \hline \end{array} \quad \mathbf{1}$$

$$\implies \begin{array}{\|c\|} \hline \Omega = -pV \\ \hline \end{array} \quad \mathbf{2}$$

$$d(\mathbf{1}) \implies dG = \mu dN + N d\mu$$


از طرفی دیفرانسیل کامل طبق تعریف گیبس:


$$dG = -S dT + V dp + \mu dN \implies \begin{array}{\|c\|} \hline d\mu = -\frac{S}{N} dT + \frac{V}{N} dp \\ \hline \end{array}$$

---

$$\mu = \mu(p, T) \quad \longleftarrow \text{تغییر مستقل پتانسیل شیمیایی اثر p و T}$$

$$\begin{array}{\|c\|} \hline d\mu = -s dT + v dp \\ \hline \end{array} \longrightarrow \text{رابطه گیبس - دوهم}$$

کمیت‌های ویژه یا شدتی:


$$\begin{cases} \frac{S}{N} \equiv s \longrightarrow \text{آنتروپی ویژه \vert{} Specific entropy} \\ \frac{V}{N} \equiv v \longrightarrow \text{حجم ویژه \vert{} Specific volume} \end{cases}$$

```
  +-------+       +---------------+
  |   N   |       |               |
  |       |       |      2N       | x 2
  +-------+       +---------------+
    T,p,u           T,u,p

```

> **زندگی:** چون $\mu$ تنها یک متغیر مشخص و جزئی مستقل از ذرات فاز موجود در ظرف جابه جایی است (مستقل از جرم). اگر چند جزء یا ذره داشته باشیم، آنگاه فرم کلی آن برابر با عبارت زیر خواهد بود:
> 
> $$G = \sum_i \mu_i N_i$$
> 
> 
> 
> مخلوط سیستم‌های چند جزئی

---

$$F, G, H, \dots \longrightarrow \begin{cases} dF \\ dG \\ dH \end{cases} \quad \text{:تغییرات طبیعی}$$

$$U = U(S, V, N)$$

$$F = F(T, V, N)$$

$$H = H(S, p, N)$$

$$G = G(T, p, N)$$

```
             /
            /
           /
          /
 ________/

```

---

## روابط ماکسول (Maxwell) : ارتباط مابین متغیرهای مختلف ترمودینامیکی

### یادآوری:

تابع خوش‌رفتار و پیوسته $f = f(x, y)$ (پیوسته مشتق‌پذیر یا دیفرانسیل جابجایی آن خوش‌تعریف است):


$$df = \left(\frac{\partial f}{\partial x}\right)_y dx + \left(\frac{\partial f}{\partial y}\right)_x dy$$

$$\begin{array}{\|c\|} \hline \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} \\ \hline \end{array} \quad \longleftarrow \text{قضیه کلرو / شوارتز}$$


(نسبت به جابجایی در متغیرهای مستقل مشتق جزئی مرتبه دوم یکسان است)


$$\left. \frac{\partial^2 f}{\partial x \partial y} \right\vert{}_p \equiv \frac{\partial}{\partial x} \left. \left( \frac{\partial f(x,y)}{\partial y} \right) \right\vert{}_{p:(x^*, y^*)}$$

**مثال:**


$$dG = -S dT + V dp \quad (N = \text{const.}) \implies \begin{cases} S = -\left(\frac{\partial G}{\partial T}\right)_{p, N} \\ V = \left(\frac{\partial G}{\partial p}\right)_{T, N} \end{cases}$$


با توجه به قضیه جابجایی مشتق کامل داریم:


$$\frac{\partial^2 G}{\partial T \partial p} = \frac{\partial^2 G}{\partial p \partial T} \implies$$

$$\begin{array}{\|c\|} \hline -\left(\frac{\partial S}{\partial p}\right)_T = \left(\frac{\partial V}{\partial T}\right)_p \\ \hline \end{array}$$

$$\implies \frac{\partial^2 (\text{پتانسیل ترمودینامیکی})}{\partial (\text{متغیر طبیعی دوم}) \partial (\text{متغیر طبیعی اول})} = \frac{\partial^2 (\text{پتانسیل ترمودینامیکی})}{\partial (\text{متغیر طبیعی اول}) \partial (\text{متغیر طبیعی دوم})}$$

---

$$\implies \begin{cases} \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial p}{\partial S}\right)_V \\ \left(\frac{\partial T}{\partial p}\right)_S = \left(\frac{\partial V}{\partial S}\right)_p \\ \left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V \\ \left(\frac{\partial S}{\partial p}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_p \end{cases} \quad \begin{array}{c\|c\|c} H & U & F \\ \hline & & \\ & & \\ & & \\ & & \end{array} \quad (\text{تمرین})$$

---

### برای روش حل هر مسئله عمومی ترمودینامیک:

a) کمیت‌های کل را برحسب متغیرها بنویسید:


$$f = f(x, y, z) \implies df = \left(\frac{\partial f}{\partial x}\right)_{y,z} dx + \left(\frac{\partial f}{\partial y}\right)_{x,z} dy + \left(\frac{\partial f}{\partial z}\right)_{x,y} dz$$

b) از روابط ماکسول (MR) برای تغییر مشتق‌های جزئی استفاده کنید که بتوان از روش‌ها یا کمیت‌هایی که برای آنها داده‌های تجربی در دست دارید استفاده کنید.

c) از قضیه مشتق جزئی معکوس استفاده کنید:


$$\left(\frac{\partial x}{\partial z}\right)_y = \frac{1}{\left(\frac{\partial z}{\partial x}\right)_y}$$


تا به کمک آن فرمول را به آن چیزی که می‌خواهید تبدیل کنید.


$$\vdots$$

---