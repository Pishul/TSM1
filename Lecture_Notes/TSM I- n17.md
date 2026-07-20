# جزوه ترمودینامیک – تبدیل لژاندر، پتانسیل‌های ترمودینامیکی و آنتروپی گاز ایده‌آل

---

## تصویر ۱: تبدیل لژاندر برای توابع چندمتغیره

$$
 f = f(x,y) \rightarrow df = \left(\frac{\partial f}{\partial x}\right)_y dx + \left(\frac{\partial f}{\partial y}\right)_x dy =: \alpha_x dx + \alpha_y dy 
$$

تبدیل لژاندر نسبت به متغیر $x$ به صورت زیر تعریف می‌شود:

$$
 h := f - \alpha_x x 
$$

دیفرانسیل $h$ به صورت زیر محاسبه می‌شود:

$$
 dh = df - d(\alpha_x x) = df - \alpha_x dx - x d\alpha_x 
$$
$$
 = \alpha_x dx + \alpha_y dy - \alpha_x dx - x d\alpha_x 
$$
$$
 = -x d\alpha_x + \alpha_y dy \Rightarrow h = h(\alpha_x, y) 
$$

اگر تابع $f$ به صورت $f = f(x,y)$ باشد، آنگاه تبدیل لژاندر نسبت به $x$ به صورت $h = f - \alpha_x x$ تعریف می‌شود که تابعی از متغیرهای جدید است: $h = h(\alpha_x, y)$.
در نتیجه روابط زیر برقرار خواهند بود:

$$
 \begin{cases} \left(\frac{\partial h}{\partial y}\right)_{\alpha_x} = \alpha_y \\ \left(\frac{\partial h}{\partial \alpha_x}\right)_y = -x \end{cases} 
$$

برای حالت کلی با بیش از دو متغیر:

$$
 f(x_1, x_2, \dots, x_n) \Rightarrow df = \sum_{i=1}^{n} \left( \frac{\partial f}{\partial x_i} \right)_{x_{j \neq i}} dx_i =: \sum_{i=1}^{n} \alpha_i dx_i 
$$

تبدیل لژاندر با حذف متغیر $x_k$:

$$
 h_k := f - \alpha_k x_k \Rightarrow dh_k = \sum_{i \neq k} \alpha_i dx_i - x_k d\alpha_k 
$$
$$
 h_k = h_k(x_1, x_2, \dots, \cancel{x_k}, \dots, x_n) 
$$

---

## تصویر ۲: مقایسه تبدیل لژاندر در مکانیک و ترمودینامیک

تبدیل لژاندر در مکانیک برای تبدیل لاگرانژین به همیلتونی استفاده می‌شود:

$$
 L(q, \dot{q}, t) \rightarrow H(q, p, t) = p\dot{q} - L = \left( \frac{\partial L}{\partial \dot{q}} \right) \dot{q} - L 
$$

که در آن تکانه تعمیم‌یافته به صورت زیر تعریف می‌شود:

$$
 \dot{q} \equiv \frac{dq}{dt}, \quad p = \frac{\partial L}{\partial \dot{q}} 
$$

نکته: این تبدیل، نوعی تبدیل لژاندر از متغیر $\dot{q}$ به متغیر $p$ است.

در ترمودینامیک، این تبدیل برای تعریف پتانسیل‌های ترمودینامیکی استفاده می‌شود. به عنوان مثال، پتانسیل شیمیایی $\mu$ به صورت زیر تعریف می‌شود:

$$
 dU = T dS - p dV + \mu dN = U(S, V, N) 
$$

به دلیل اینکه $\frac{\partial U}{\partial N}$ برابر با $\mu$ است.

**توصیف شکل (تصویر ۲):** یک خط موج‌دار افقی در وسط صفحه رسم شده است که بخش مکانیک را از بخش ترمودینامیک جدا می‌کند.

---

## تصویر ۳: تعریف پتانسیل شیمیایی و تعادل فازها

دیفرانسیل انرژی آزاد هلمهولتز ($F$) و انرژی آزاد گیبس ($G$) به صورت زیر است:

$$
 dF = -p dV - S dT + \mu dN 
$$
$$
 dG = V dp - S dT + \mu dN 
$$

در نتیجه پتانسیل شیمیایی به صورت زیر قابل محاسبه است:

$$
 \mu = \left(\frac{\partial F}{\partial N}\right)_{T,V} = \left(\frac{\partial G}{\partial N}\right)_{p,T} 
$$

**توصیف شکل (تصویر ۳):** یک مستطیل با خطوط افقی و عمودی در وسط صفحه رسم شده است که دو فاز یا دو بخش از یک سیستم را با برچسب‌های I و II و همچنین دو بخش کوچک‌تر با برچسب‌های a و b نشان می‌دهد. در کنار این شکل، شرایط تعادل (برابری دما، فشار و پتانسیل شیمیایی) نوشته شده است.

شرایط تعادل ترمودینامیکی بین فازهای I و II به صورت زیر است:

$$
 \begin{cases} T_I = T_{II} \\ \frac{M_I}{N_I} = \frac{M_{II}}{N_{II}} \\ \frac{p_I}{T_I} = \frac{p_{II}}{T_{II}} \end{cases} \Rightarrow \begin{cases} T_I = T_{II} \\ M_I = M_{II} \\ p_I = p_{II} \end{cases} 
$$

در مورد یک واکنش شیمیایی مانند $2 H_2 + O_2 \rightarrow 2 H_2O$، پتانسیل شیمیایی $\mu$ نقش مهمی در تعادل واکنش ایفا می‌کند.

---

## تصویر ۴: شرط تعادل و حداقل‌سازی انرژی آزاد

اگر سیستم در تعادل باشد، انرژی آزاد آن کمینه خواهد شد. برای یک سیستم با حجم و دمای ثابت ($V=\text{const.}$ و $T=\text{const.}$)، شرط تعادل به صورت زیر است:

$$
 A = F \quad \Rightarrow \quad \frac{\partial F}{\partial N} \bigg|_{V,T} = 0 \quad \Rightarrow \quad \mu = 0 
$$

**توصیف شکل (تصویر ۴):** یک مکعب با برچسب V در بالای صفحه رسم شده است که نشان‌دهنده یک ظرف با حجم ثابت است. در داخل این ظرف، چهار دایره توخالی قرمز رنگ رسم شده است که نشان‌دهنده ذرات (اتم‌ها یا مولکول‌ها) هستند. با فلش‌های آبی رنگ، حرکت احتمالی این ذرات به سمت مرزهای ظرف نشان داده شده است.

---

## تصویر ۵: روابط ریاضی و مشتقات جزئی

**قضیه وارونگی:**
برای متغیرهای $x, y, z$ که رابطه‌ای بین آن‌ها برقرار است، داریم:

$$
 \left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1 \Rightarrow \left(\frac{\partial x}{\partial y}\right)_z = - \frac{\left(\frac{\partial z}{\partial x}\right)_y}{\left(\frac{\partial z}{\partial y}\right)_x} 
$$

**ظرفیت‌های گرمایی:**

$$
 \begin{cases} \frac{C_V}{T} = \left(\frac{\partial S}{\partial T}\right)_V \\ \frac{C_p}{T} = \left(\frac{\partial S}{\partial T}\right)_p \end{cases} 
$$

**روابط ماکسول:**

$$
 \begin{cases} T = \left(\frac{\partial U}{\partial S}\right)_V \\ p = -\left(\frac{\partial U}{\partial V}\right)_S \end{cases} \Rightarrow \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial p}{\partial S}\right)_V 
$$

**ضریب انبساط حجمی و تراکم‌پذیری:**

$$
 \begin{cases} \beta_p \equiv \frac{1}{V} \left(\frac{\partial V}{\partial T}\right)_p \\ \beta_S \equiv \frac{1}{V} \left(\frac{\partial V}{\partial T}\right)_S \end{cases} 
$$
$$
 \begin{cases} \kappa_T \equiv -\frac{1}{V} \left(\frac{\partial V}{\partial p}\right)_T > 0 \\ \kappa_S \equiv -\frac{1}{V} \left(\frac{\partial V}{\partial p}\right)_S > 0 \end{cases} 
$$

---

## تصویر ۶: رابطه مایر و اثبات آن

$$
 C_p - C_V = TV \frac{\beta_p^2}{\kappa_T} > 0 
$$

برای اثبات این رابطه، از دیفرانسیل آنتروپی $S = S(T, V)$ شروع می‌کنیم:

$$
 dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV 
$$

با تقسیم دو طرف بر $dT$ در فشار ثابت:

$$
 \left(\frac{dS}{dT}\right)_p = \left(\frac{\partial S}{\partial T}\right)_V + \left(\frac{\partial S}{\partial V}\right)_T \left(\frac{dV}{dT}\right)_p 
$$
$$
 \left(\frac{\partial S}{\partial T}\right)_p = \left(\frac{\partial S}{\partial T}\right)_V + \left(\frac{\partial S}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_p 
$$

با جایگذاری تعاریف ظرفیت‌های گرمایی و استفاده از رابطه ماکسول $(\frac{\partial S}{\partial V})_T = (\frac{\partial p}{\partial T})_V$ و روابط مربوط به $\beta_p$ و $\kappa_T$، رابطه مایر به دست می‌آید:

$$
 C_p - C_V = V T \frac{\beta_p^2}{\kappa_T} 
$$

---

## تصویر ۷: آنتروپی گاز ایده‌آل

برای گاز ایده‌آل، معادلات حالت به صورت زیر است:

$$
 \begin{cases} pV = N k_B T \\ U = U(N, T) \Rightarrow U = N u(T) \end{cases} 
$$

از رابطه $dU = T dS - p dV + \mu dN$ و تعریف $C_V$:

$$
 \left(\frac{\partial U}{\partial T}\right)_{N,V} = T \left(\frac{\partial S}{\partial T}\right)_{N,V} = C_V(T, N) = N c_V(T) 
$$
$$
 \Rightarrow \frac{d}{dT} u(T) = c_V(T) 
$$

برای گاز ایده‌آل تک‌اتمی، $U(N,T) = \alpha N R T \Rightarrow c_V = \alpha k_B$. همچنین، از تعریف آنتروپی:

$$
 \left(\frac{\partial S}{\partial T}\right)_{N,V} = \frac{C_V}{T} 
$$

با انتگرال‌گیری نسبت به دما:

$$
 S = C_V \ln \frac{T}{T_0} + A(N, V) 
$$

---

## تصویر ۸: به دست آوردن وابستگی حجمی آنتروپی

با استفاده از رابطه ماکسول ناشی از دیفرانسیل انرژی آزاد هلمهولتز ($dF = -S dT - p dV + \mu dN$):

$$
 \left(\frac{\partial S}{\partial V}\right)_{T,N} = \left(\frac{\partial p}{\partial T}\right)_{V,N} 
$$

برای گاز ایده‌آل، $ (\frac{\partial p}{\partial T})_{V,N} = \frac{N k_B}{V} $. بنابراین:

$$
 \left(\frac{\partial S}{\partial V}\right)_{T,N} = \frac{N k_B}{V} 
$$

با انتگرال‌گیری از این رابطه نسبت به حجم:

$$
 \Delta S = C_V \ln \frac{T}{T_0} + A(N, V) = C_V \ln \frac{T}{T_0} + N k_B \ln \frac{V}{V_0} + D(N) 
$$
$$
 \Rightarrow S = N k_B \left\{ \alpha \ln \frac{T}{T_0} + \ln \frac{V}{V_0} + \gamma \right\} 
$$

برای اینکه آنتروپی یک کمیت **واسعه** (Extensive) باشد، یعنی با جرم سیستم متناسب باشد ($S \propto N$)، وابستگی آن به حجم باید به صورت زیر باشد:

$$
 S = N k_B \ln \left( \frac{V T^\alpha}{\gamma' N} \right) 
$$

**نتیجه‌گیری نهایی:** آنتروپی یک سیستم بسته در حالت تعادل به صورت زیر است:

$$
 S = \text{const.} = N k_B \ln \left( \frac{V T^\alpha}{\text{const.}} \right) 
$$

---

## تصویر ۹: محاسبه پتانسیل‌های ترمودینامیکی و پتانسیل شیمیایی گاز ایده‌آل

از معادله حالت گاز ایده‌آل، رابطه زیر برقرار است:

$$
 V T^\alpha = \text{const.} 
$$

**محاسبه انرژی آزاد هلمهولتز ($F$):**

$$
 F = U - TS = N k_B T \left[ \alpha - \ln \left( \frac{V T^\alpha}{\eta' N} \right) \right] 
$$

**محاسبه انرژی آزاد گیبس ($G$):**

$$
 G = F + pV = N k_B T \left[ 1 + \alpha - \ln \left( \frac{V T^\alpha}{\eta' N} \right) \right] 
$$

**محاسبه پتانسیل شیمیایی ($\mu$):**

$$
 \mu = \frac{G}{N} = k_B T \left[ 1 + \alpha - \ln \left( \frac{V T^\alpha}{\eta' N} \right) \right] 
$$
$$
 \Rightarrow \mu = k_B T \left[ 1 + \alpha - \ln \left( \frac{k_B T^{\alpha+1}}{\eta' p} \right) \right] = \mu(T, p) 
$$

**نتیجه‌گیری:** پتانسیل شیمیایی گاز ایده‌آل فقط به دما و فشار بستگی دارد و به حجم وابسته نیست. رابطه دیفرانسیلی آن نیز به صورت زیر است:

$$
 d\mu = -\frac{S}{N} dT + \frac{V}{N} dp 
$$