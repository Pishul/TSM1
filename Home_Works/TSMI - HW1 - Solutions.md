پاسخ‌نامه‌ی سری تمرین اول
ترمودینامیک و مکانیک آماری ۱

بهار ۱۴۰۵

۱ مشتقات جزئی
الف) قضیه‌های وارون و وارونگی برای سه متغیر
طبق راهنمایی(درواقع قضیه‌ی تابع ضمنی) برای $dz$ و $dx$ می‌توانیم بنویسیم:

$$ x = x(y, z) \quad \Rightarrow \quad dx = \left(\frac{\partial x}{\partial y}\right)_z dy + \left(\frac{\partial x}{\partial z}\right)_y dz $$

$$ z = z(x, y) \quad \Rightarrow \quad dz = \left(\frac{\partial z}{\partial x}\right)_y dx + \left(\frac{\partial z}{\partial y}\right)_x dy $$

با قرار دادن تساوی دوم در تساوی اول خواهیم داشت:

$$ dx = \left(\frac{\partial x}{\partial y}\right)_z dy + \left(\frac{\partial x}{\partial z}\right)_y \left[ \left(\frac{\partial z}{\partial x}\right)_y dx + \left(\frac{\partial z}{\partial y}\right)_x dy \right] $$
$$ = \left(\frac{\partial x}{\partial y}\right)_z dy + \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y dx + \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x dy $$
$$ = \left[ \left(\frac{\partial x}{\partial y}\right)_z + \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x \right] dy + \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y dx $$

چون $x$ و $y$ را مستقل گرفتیم، رابطه‌ی بالا به ازای هر $dx$ و $dy$ دلخواه برقرار است. با اختیار کردن $dy = 0$ و $dx \neq 0$ ، خواهیم داشت:

$$ dy = 0 \quad \Rightarrow \quad dx = \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y dx \quad \Rightarrow \quad \boxed{ \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y = 1 } \quad \Rightarrow \quad \left(\frac{\partial x}{\partial z}\right)_y = \frac{1}{\left(\frac{\partial z}{\partial x}\right)_y} $$

که این همان چیزی است که می‌خواستیم نشان دهیم. مجدداً با اختیار کردن $dx = 0$ و $dy \neq 0$، خواهیم داشت:

$$ dx = 0 \quad \Rightarrow \quad \left[ \left(\frac{\partial x}{\partial y}\right)_z + \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x \right] dy = 0 $$

چون $dy$ ناصفر است، داریم:

$$ \Rightarrow \quad \left(\frac{\partial x}{\partial y}\right)_z = - \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x \quad \Rightarrow \quad \boxed{ \left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1 } $$

که در تساوی آخر از رابطه‌ی اثبات شده در بخش قبل استفاده کردیم. دومین رابطه‌ی مدنظر نیز ثابت شد.

۱

ب) قضیه‌های وارون و وارونگی برای چهار متغیر

مانند قسمت قبل و با توجه به راهنمایی(مجدداً همان قضیه‌ی تابع ضمنی) داریم:

$$ w = w(x, y, z) \quad \Rightarrow \quad dw = \left( \frac{\partial w}{\partial x} \right)_{y,z} dx + \left( \frac{\partial w}{\partial y} \right)_{x,z} dy + \left( \frac{\partial w}{\partial z} \right)_{x,y} dz $$

$$ x = x(w, y, z) \quad \Rightarrow \quad dx = \left( \frac{\partial x}{\partial w} \right)_{y,z} dw + \left( \frac{\partial x}{\partial y} \right)_{z,w} dy + \left( \frac{\partial x}{\partial z} \right)_{y,w} dz $$

روابط بالا و ترکیب آن‌ها به ازای $dx, dy, dz$ و $dw$ دلخواه برقرارند. که البته می‌دانیم سه تای این متغیرها مستقل از یکدیگرند.
به ازای $dy = 0$ و $dz = 0$ از ترکیب دو رابطه‌ی بالا داریم:

$$ dw = \left( \frac{\partial w}{\partial x} \right)_{y,z} dx = \left( \frac{\partial w}{\partial x} \right)_{y,z} \left[ \left( \frac{\partial x}{\partial w} \right)_{y,z} dw \right] \quad \Rightarrow \quad \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial w} \right)_{y,z} = 1 $$

پس داریم:

$$ \boxed{ \left( \frac{\partial w}{\partial x} \right)_{y,z} = \frac{1}{\left( \frac{\partial x}{\partial w} \right)_{y,z}} } $$

که این همان چیزی است که می‌خواستیم ثابت کنیم. حالا برای اثبات رابطه‌ی بعدی به ازای $dw = 0$ داریم:

$$ 0 = \left( \frac{\partial w}{\partial x} \right)_{y,z} dx + \left( \frac{\partial w}{\partial y} \right)_{x,z} dy + \left( \frac{\partial w}{\partial z} \right)_{x,y} dz $$

با جایگذاری $dx$ از رابطه‌ی دوم داریم:

$$ 0 = \left( \frac{\partial w}{\partial x} \right)_{y,z} \left[ \left( \frac{\partial x}{\partial y} \right)_{z,w} dy + \left( \frac{\partial x}{\partial z} \right)_{y,w} dz \right] + \left( \frac{\partial w}{\partial y} \right)_{x,z} dy + \left( \frac{\partial w}{\partial z} \right)_{x,y} dz $$
$$ = \left[ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial y} \right)_{z,w} + \left( \frac{\partial w}{\partial y} \right)_{x,z} \right] dy + \left[ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial z} \right)_{y,w} + \left( \frac{\partial w}{\partial z} \right)_{x,y} \right] dz $$

چون $dy$ و $dz$ دلخواه و مستقل هستند، ضرایب آن‌ها باید صفر باشد:

$$ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial y} \right)_{z,w} + \left( \frac{\partial w}{\partial y} \right)_{x,z} = 0 \quad \Rightarrow \quad \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial y} \right)_{z,w} = - \left( \frac{\partial w}{\partial y} \right)_{x,z} \quad (۱) $$
$$ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial z} \right)_{y,w} + \left( \frac{\partial w}{\partial z} \right)_{x,y} = 0 \quad \Rightarrow \quad \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial z} \right)_{y,w} = - \left( \frac{\partial w}{\partial z} \right)_{x,y} \quad (۲) $$

از رابطه (۲) و ترکیب آن با نتیجه‌ی بدست آمده از بخش قبل نتیجه می‌شود:

$$ \Rightarrow \quad \boxed{ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial z} \right)_{y,w} \left( \frac{\partial z}{\partial w} \right)_{y,x} = -1 } $$

که این همان چیزی است که می‌خواستیم ثابت کنیم.
در هر دو بخش الف و ب از آنجایی که از سه (و یا چهار) متغیر داده شده یکی از متغیرها وابسته به بقیه هستند، سعی کردیم در روابط
دیفرانسیلی یکی از متغیرها را حذف کرده و براساس بقیه بنویسیم. سپس متغیرهای باقی مانده مستقل رفتار می‌کنند. روابط بخش
ب به لحاظ شهودی تفاوتی با بخش الف ندارند. یعنی مادامی که متغیرهایی که اضافه می‌کنیم در روابط دیفرانسیلی ثابت بمانند،
انگار اصلاً متغیر نیستند و همانند اعداد ثابت عمل می‌کنند. این استدلال را در بخش زیادی از درس استفاده کرده‌ایم. در واقع تعداد
ذرات تشکیل‌دهنده‌ی یک گاز واقعاً یک متغیر ترمودینامیکی است؛ امّا از آنجایی که در تعداد زیادی از فرآیندها تعداد آن تغییر نمی‌کند،
اصلاً آن را بعنوان متغیر در نظر نگرفتیم. برای به خاطر سپردن این روابط پر کاربرد، می‌توان سه متغیر را پشت سر هم روی یک دایره
نوشت و مشتق‌گیری‌ها و متغیرهای ثابت در هر مشتق‌گیری را به ترتیب نوشته شده جلو برد. حاصل‌ضرب عدد منفی یک است.

۲

ج) دو قضیه‌ی کاربردی
از آنجایی که سه متغیر $x$، $y$ و $z$ مستقل نیستند و فقط دوتای آن‌ها مستقل‌اند، هر سه رابطه‌ی زیر برقرار است:
$$ x = x(y, z), \quad y = y(x, z), \quad z = z(x, y) $$

پس تابع $G$ را به هر یک از اشکال زیر می‌توان نوشت:
$$ G = G(x, y) = G(x(y, z), y) = G(y, z) = G(y(x, z), z) = G(x, z) = G(x, z(x, y)) $$

حالا یک تساوی مناسب را از بین آن‌ها انتخاب می‌کنیم. مثلاً داریم:
$$ G(x, y) = G(x, z(x, y)) $$

حالا برای اثبات رابطه‌های داده شده کافی است که از طرفین رابطه‌ی بالا یک بار تغییر تابع $G$ را برحسب تغییر متغیر $x$ و یک بار هم برحسب تغییر متغیر $y$ بنویسیم و از مشتق گیری زنجیره‌ای استفاده کنیم. اگر تغییرات $x$ را نگاه کنیم، خواهیم داشت:
$$ \left( \frac{\partial G}{\partial x} \right)_y = \left( \frac{\partial G}{\partial x} \right)_z + \left( \frac{\partial G}{\partial z} \right)_x \left( \frac{\partial z}{\partial x} \right)_y $$

که این یکی از روابطی است که باید ثابت می‌کردیم. رابطه‌ی بعدی نیز وقتی بدست می‌آید که تغییرات $y$ را نگاه کنیم:
$$ \left( \frac{\partial G}{\partial y} \right)_x = \left( \frac{\partial G}{\partial z} \right)_x \left( \frac{\partial z}{\partial y} \right)_x $$

که این هم رابطه‌ی دومی است که باید ثابت می‌کردیم. از این استدلال که متغیرها را می‌توان برحسب یکدیگر نوشت بسیار استفاده خواهیم کرد. برای مثال وقتی می‌خواهیم تفاوت ظرفیت گرمایی در فشار ثابت و ظرفیت گرمایی در حجم ثابت را محاسبه کنیم، از این روابط استفاده خواهیم کرد. نیازی به حفظ کردن این روابط نیست؛ کافیست متغیرهای مناسب را تشخیص دهید و از طرفین تساوی نسبت به متغیرها مشتق بگیرید. غالباً باید از قاعده‌ی مشتق گیری زنجیره‌ای نیز استفاده کرد.

د) یک مثال (امتیازی)
مطابق تعریف داریم:
$$ C = \frac{A}{B} \quad \Rightarrow \quad \ln C = \ln \left(\frac{A}{B}\right) = \ln A - \ln B $$

از دو طرف دیفرانسیل کامل می‌گیریم:
$$ d(\ln C) = d(\ln A) - d(\ln B) \quad \Rightarrow $$
$$ \frac{\partial (\ln C)}{\partial x} dx + \frac{\partial (\ln C)}{\partial y} dy = \left( \frac{\partial (\ln A)}{\partial x} dx + \frac{\partial (\ln A)}{\partial y} dy \right) - \left( \frac{\partial (\ln B)}{\partial x} dx + \frac{\partial (\ln B)}{\partial y} dy \right) $$

با کمی مرتب کردن، به رابطه‌ی زیر می‌رسیم:
$$ \Rightarrow \quad \frac{\partial (\ln C)}{\partial x} dx + \frac{\partial (\ln C)}{\partial y} dy = \left( \frac{\partial (\ln A)}{\partial x} - \frac{\partial (\ln B)}{\partial x} \right) dx + \left( \frac{\partial (\ln A)}{\partial y} - \frac{\partial (\ln B)}{\partial y} \right) dy $$

رابطه‌ی خواسته‌شده‌ی سوال در حالت $C$ ثابت است. مادامی که $C$ ثابت باشد، $\ln C$ هم ثابت خواهد بود:
$$ C = const \quad \Rightarrow \quad \ln C = const \quad \Rightarrow \quad d(\ln C) = 0 $$

با استفاده در رابطه‌ی بالا داریم:
$$ \left( \frac{\partial (\ln A)}{\partial x} - \frac{\partial (\ln B)}{\partial x} \right) dx + \left( \frac{\partial (\ln A)}{\partial y} - \frac{\partial (\ln B)}{\partial y} \right) dy = 0 \quad \Rightarrow \quad M dx + N dy = 0 $$

۳

پس داریم:

$$
\Rightarrow \quad \frac{dx}{dy} = \left(\frac{\partial x}{\partial y}\right)_C = -\frac{N}{M} \quad \Rightarrow \quad \boxed{ \left(\frac{\partial x}{\partial y}\right)_C = \frac{\left(\frac{\partial (\ln B)}{\partial y}\right)_x - \left(\frac{\partial (\ln A)}{\partial y}\right)_x}{\left(\frac{\partial (\ln A)}{\partial x}\right)_y - \left(\frac{\partial (\ln B)}{\partial x}\right)_y} }
$$

که این همان رابطه‌ای است که می‌خواستیم ثابت کنیم. عموماً برای اثبات این رابطه از روند بالا استفاده کرده بودید. اما اگر $z$ را به شکل زیر تعریف می‌کردید و از نتیجه‌ی بخش الف استفاده می‌کردید، سریعاً به رابطه‌ی مربوطه می‌رسیدید:

$$
z := \ln C = \ln A - \ln B
$$

که البته باید از این واقعیت هم استفاده می‌کردید که اگر $C$ ثابت باشد، $\ln C$ هم ثابت خواهد بود. این کار در واقع استفاده از روابطی است که قبلاً ثابت کردیم.

**۲ قضیه‌ی همگنی اویلر**

طبق تعریف تابع همگن داریم:

$$
F(\lambda x_1, \lambda x_2, \dots, \lambda x_k) = \lambda^p F(x_1, x_2, \dots, x_k)
$$

ابتدا از دو طرف تساوی نسبت به $\lambda$ مشتق جزئی می‌گیریم:

$$
\frac{\partial}{\partial \lambda} F(\lambda x_1, \lambda x_2, \dots, \lambda x_k) = \frac{\partial}{\partial \lambda} \left(\lambda^p F(x_1, x_2, \dots, x_k)\right)
$$

طبق قاعده‌ی زنجیره‌ای برای مشتق سمت چپ و مشتق عادی برای سمت راست داریم:

$$
\sum_{j=1}^k \frac{\partial F}{\partial x_j} (\lambda x_1, \lambda x_2, \dots, \lambda x_k) \frac{\partial (\lambda x_j)}{\partial \lambda} = p \lambda^{p-1} F(x_1, x_2, \dots, x_k)
$$

چون $\frac{\partial (\lambda x_j)}{\partial \lambda} = x_j$ برقرار است، پس داریم:

$$
p \lambda^{p-1} F(x_1, x_2, \dots, x_k) = \sum_{j=1}^k \frac{\partial F}{\partial x_j} (\lambda x_1, \lambda x_2, \dots, \lambda x_k) x_j
$$

این رابطه طبق صورت سوال به ازای همه‌ی $\lambda \in \mathbb{R}$ برقرار است. با مقداردهی $\lambda$ به صورت $\lambda = 1$ داریم:

$$
\boxed{ p F(x_1, x_2, \dots, x_k) = \sum_{j=1}^k \frac{\partial F}{\partial x_j} (x_1, x_2, \dots, x_k) x_j }
$$

که رابطه‌ی اخیر همان چیزی است که می‌خواستیم ثابت کنیم.

**۳ دیفرانسیل‌های کامل**

**الف** با بُرهانِ خُلف ثابت می‌کنیم این فُرم دیفرانسیلی کامل نیست. فرض کنید که این یک دیفرانسیل کامل باشد. پس:

$$
\exists F(x, y) : \mathrm{d}F = \frac{\partial F}{\partial x} \mathrm{d}x + \frac{\partial F}{\partial y} \mathrm{d}y = (x^2 + 2y) \mathrm{d}x + x \mathrm{d}y
$$

پس:

$$
\frac{\partial F}{\partial x} = x^2 + 2y \quad , \quad \frac{\partial F}{\partial y} = x
$$

۴

که به ترتیب نتیجه می‌دهند:

$$F(x, y) = \frac{1}{3} x^3 + 2xy + g(y) \quad , \quad F(x, y) = xy + h(x)$$

پس:

$$\frac{1}{3} x^3 + 2xy + g(y) = xy + h(x)$$

پس:

$$\frac{1}{3} x^3 + xy + g(y) = h(x)$$

نسبت به $y$ مشتق می‌گیرم:

$$x + g(y) = 0$$

که این معادله به ازای هر $x,y$ دلخواه باید برقرار باشد که غیرممکن است. بنابراین فرض دیفرانسیل کامل بودن فُرم مورد نظر نقض شد.

**ب** می‌خواهم ثابت کنم که برای فُرم دیفرانسیلی $\omega$

$$\omega := M(x, y) \mathrm{d}x + N(x, y) \mathrm{d}y$$

داریم:

$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \iff \exists F(x, y) : \mathrm{d}F = \omega$$

دو جهتِ این گزاره را نشان می‌دهم.

**اثبات $\impliedby$:**

$$M(x, y) \mathrm{d}x + N(x, y) \mathrm{d}y = \frac{\partial F}{\partial x} \mathrm{d}x + \frac{\partial F}{\partial y} \mathrm{d}y$$

پس:

$$M(x, y) = \frac{\partial F}{\partial x} \quad , \quad N(X, y) = \frac{\partial F}{\partial y}$$

از طرفی:

$$\frac{\partial^2 F}{\partial x \partial y} = \frac{\partial^2 F}{\partial y \partial x}$$

پس:

$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial y}$$

**اثبات $\implies$:** تابع $F(x, y)$ را چنین تعریف می‌کنم:

$$F(x, y) := \int_{x_0}^x M(s, y_0) \mathrm{d}s + \int_{y_0}^y N(x, s) \mathrm{d}s$$

که در آن $x_0, y_0$ یک نقطه‌ی دلخواه است. مشتقات این تابع را می‌نویسم:

$$\frac{\partial F}{\partial x} = M(x, y_0) + \int_{y_0}^y \frac{\partial N}{\partial x} (x, s) \mathrm{d}s$$

$$\frac{\partial F}{\partial y} = N(x, y)$$

حال از آن‌جایی که:

$$\frac{\partial N}{\partial x} = \frac{\partial M}{\partial y}$$

۵

می‌توان نوشت:
$$
\int_{y_{\circ}}^{y} \frac{\partial N}{\partial x} \mathrm{d}s = \int_{y_{\circ}}^{y} \frac{\partial M}{\partial y} \mathrm{d}s = M(x, y) - M(x, y_{\circ})
$$

پس:
$$
\frac{\partial F}{\partial x} = M(x, y) \quad , \quad \frac{\partial F}{\partial y} = N(x, y)
$$

**پ** می‌خواهم ثابت کنم که برای فُرم دیفرانسیلی $\omega$:
$$
\oint_{\text{هر مسیر بسته}} \omega = 0 \iff \exists F(x, y) : \mathrm{d}F = \omega
$$

دو جهت این گزاره را نشان می‌دهم.

**اثبات $\Longleftarrow$:** توجه کنید که انتگرالِ زیر از نقطه‌ی $A$ تا نقطه‌ی $B$ روی هر مسیری به صورت زیر است:
$$
\int_{A}^{B} \mathrm{d}F = F(B) - F(A)
$$

پس روی هر مسیر بسته:
$$
\oint \mathrm{d}F = \int_{A}^{A} \mathrm{d}F = F(A) - F(A) = 0
$$

**اثبات $\Longrightarrow$:** تابع $F$ را تعریف می‌کنم:
$$
F(x, y) := \int_{(x_{\circ}, y_{\circ})}^{(x, y)} \omega
$$

ابتدا نشان می‌دهم که مقدار این انتگرال به مسیر انتگرال‌گیری ربطی ندارد. دو مسیر $p_{1}$ و $p_{2}$ را برای این انتگرال‌گیری تصور کنید. همچنین $\bar{p}_{2}$ همان مسیر $p_{2}$ است که برعکس طی می‌شود (یعنی از $(x, y)$ به $(x_{\circ}, y_{\circ})$). می‌دانم انتگرال $\omega$ روی هر مسیر بسته صفر است. پس:
$$
\oint \omega = \int_{p_{1}} \omega + \int_{\bar{p}_{2}} \omega = 0
$$

از طرفی:
$$
\int_{\bar{p}_{2}} \omega = - \int_{p_{2}} \omega
$$

پس:
$$
\int_{p_{1}} \omega = \int_{p_{2}} \omega
$$

بنابراین، تعریف ارائه شده برای $F(x, y)$ خوش تعریف است و نیازی به تعیین مسیر انتگرال‌گیری ندارد. از این تعریف (مشابه قسمت قبل) واضح است که:
$$
\mathrm{d}F = \omega
$$

**ت** ابتدا ثابت می‌کنم دیفرانسیل کامل نیست:
$$
\frac{\partial}{\partial y}(3xy + y^{2}) = 3x + 2y \quad , \quad \frac{\partial}{\partial x}(x^{2} + xy) = 2x + y
$$

۶

که برابر نیستند پس دیفرانسیل مورد نظر، کامل نیست. حال فرض کنید تابع $\mu(x)$ در این دیفرانسیل ضرب شود. شرط
دیفرانسیل کامل بودن را مجدداً می‌نویسم:

$$
\mu(x)(3x + 2y) = \mu'(x)(x^2 + xy) + \mu(x)(2x + y)
$$

جملات آن را مرتب می‌کنم:

$$
\mu(x)(x + y) = \mu'(x)x(x + y)
$$

که ساده می‌شود به:

$$
\mu(x) = \mu'(x)x
$$

پس یک انتخاب برای $\mu(x)$ به صورت نمایی است:

$$
\mu(x) \sim e^x
$$

با ضرب این عامل در دیفرانسیل، یک دیفرانسیل کامل ساخته خواهد شد.

**۴ انتگرال گاوسی و حد سری هندسی**
**الف) انتگرال گاوسی**
طبق صورت سوال، نیاز به قضیه‌ی تغییر متغیر برای انتگرال‌های دوگانه داریم. از درس ریاضی ۲، قضیه‌ی زیر که به آن قضیه‌ی تغییر
متغیر می‌گویند را داریم:
فرض کنید $f$ یک نگاشت یک‌به‌یک و پوشا میان ناحیه $S$ در صفحه $uv$ و ناحیه $D$ در صفحه $xy$ باشد:

$$
x = x(u, v), \quad y = y(u, v)
$$

همچنین فرض کنید که تابع‌های فوق و مشتقات جزئی مرتبه‌ی اول آن‌ها در $S$ پیوسته هستند. اگر تابع $f(x, y)$ روی $D$ انتگرال‌پذیر
باشد، آن‌گاه تابع $g(u, v) := f(x(u, v), y(u, v))$ نیز انتگرال‌پذیر بوده و داریم:

$$
\iint_D f(x, y) dx dy = \iint_S g(u, v) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| du dv
$$

که در آن $\left| \frac{\partial(x, y)}{\partial(u, v)} \right|$ دترمینان ژاکوبی بوده و برابر است با:

$$
\frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}
$$

همچنین می‌دانیم:

$$
if: \frac{\partial(u, v)}{\partial(x, y)} \neq 0 \quad \Rightarrow \quad \frac{\partial(x, y)}{\partial(u, v)} = \frac{1}{\frac{\partial(u, v)}{\partial(x, y)}}
$$

این نتایج برای متغیرهای بیشتر هم قابل تعمیم است؛ اما ما در این مسئله با همین تابع دو متغیره کار داریم. در نتیجه در تغییر
مختصات قطبی(یک نگاشت ویژه‌ی مفید) با روابط $r = \sqrt{x^2 + y^2}$ و $\theta = \tan^{-1}\left(\frac{y}{x}\right)$ یا معادلاً $x = r \cos\theta$ و
$y = r \sin\theta$ داریم:

$$
\iint_D f(x, y) dx dy = \iint_S g(r, \theta) \left| \frac{\partial(x, y)}{\partial(r, \theta)} \right| dr d\theta
$$

با محاسبه‌ی ژاکوبی برای مختصات قطبی، مقدار دترمینان آن برابر $r$ می‌شود و خواهیم داشت:

$$
\Rightarrow \quad \iint_D f(x, y) dx dy = \iint_S g(r, \theta) r dr d\theta
$$

۷

حالا با این مقدمات به حل مسئله‌ی اصلی یعنی محاسبه‌ی انتگرال گاوسی می‌پردازیم:

$$ I = \int_{-\infty}^{+\infty} e^{-x^2} dx $$

مطابق راهنمایی این انتگرال را به توان دو می‌رسانیم و از این واقعیت استفاده می‌کنیم که نام متغیری که روی آن انتگرال گرفته می‌شود مهم نیست؛ زیرا همانند یک متغیر دامی عمل می‌کند و در نهایت از بین می‌رود. پس داریم:

$$ I^2 = \left( \int_{-\infty}^{+\infty} e^{-x^2} dx \right) \left( \int_{-\infty}^{+\infty} e^{-x^2} dx \right) = \left( \int_{-\infty}^{+\infty} e^{-x^2} dx \right) \left( \int_{-\infty}^{+\infty} e^{-y^2} dy \right) $$

$$ = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} e^{-x^2-y^2} dx dy = \int_0^{2\pi} \int_0^{+\infty} e^{-r^2} r dr d\theta $$

که در تساوی آخر از تغییر متغیر قطبی استفاده شده است. با جداکردن متغیرها (زیرا از هم مستقل هستند) خواهیم داشت:

$$ \Rightarrow \quad I^2 = \left( \int_0^{2\pi} d\theta \right) \left( \int_0^{+\infty} r e^{-r^2} dr \right) = 2\pi \times \left( \int_0^{+\infty} r e^{-r^2} dr \right) $$

با تغییر متغیر:

$$ r^2 = t \quad \Rightarrow \quad 2r dr = dt $$

انتگرال دوم به صورت زیر حل می‌شود:

$$ \int_0^{+\infty} \frac{1}{2} e^{-t} dt = \frac{1}{2} \left( -e^{-t} \right) \Big|_0^{+\infty} = \frac{1}{2} $$

$$ \Rightarrow \quad I^2 = \pi \quad \Rightarrow \quad I = \sqrt{\pi} \quad \Rightarrow \quad \boxed{ \int_{-\infty}^{+\infty} e^{-x^2} dx = \sqrt{\pi} } $$

که این همان چیزی است که می‌خواستیم ثابت کنیم. در قسمت بعد می‌خواهیم روابط زیر را به کمک نتایجی که بدست آوردیم اثبات کنیم:

$$ 1) \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} dx = \sqrt{\frac{2\pi}{a}}, \quad 2) \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2+bx} dx = \sqrt{\frac{2\pi}{a}} e^{\frac{b^2}{2a}} $$

برای اثبات (۱)، با تغییر متغیر:

$$ y = \sqrt{\frac{a}{2}} x \quad \Rightarrow \quad dy = \sqrt{\frac{a}{2}} dx $$

و استفاده از نتایج بخش قبل خواهیم داشت:

$$ \int_{-\infty}^{+\infty} e^{-y^2} dy = \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} \sqrt{\frac{a}{2}} dx = \sqrt{\pi} \quad \Rightarrow \quad \boxed{ \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} dx = \sqrt{\frac{2\pi}{a}} } $$

که این همان چیزی است که می‌خواستیم ثابت کنیم. برای اثبات (۲)، ابتدا عبارت توان را مربع کامل می‌کنیم:

$$ -\frac{1}{2}ax^2+bx = -\frac{1}{2}a \left( x^2 - \frac{2b}{a}x \right) = -\frac{a}{2} \left[ \left( x - \frac{b}{a} \right)^2 - \left( \frac{b}{a} \right)^2 \right] = -\frac{a}{2} \left( x - \frac{b}{a} \right)^2 + \frac{b^2}{2a} $$

بنابراین با تغییر متغیر:

$$ x - \frac{b}{a} = u \quad \Rightarrow \quad dx = du $$

خواهیم داشت:

$$ \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2+bx} dx = e^{\frac{b^2}{2a}} \int_{-\infty}^{+\infty} e^{-\frac{a}{2} \left( x - \frac{b}{a} \right)^2} dx = e^{\frac{b^2}{2a}} \int_{-\infty}^{+\infty} e^{-\frac{a}{2}u^2} du = \sqrt{\frac{2\pi}{a}} e^{\frac{b^2}{2a}} $$

۸

که در رابطه‌ی آخر از نتایج بخش قبل استفاده کردیم، پس داریم:

$$
\Rightarrow \quad \boxed{ \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2+bx} dx = \sqrt{\frac{2\pi}{a}} e^{\frac{b^2}{2a}} }
$$

که این همان رابطه‌ای است که می‌خواستیم ثابت کنیم.
مطابق تعریف گشتاورهای این تابع توزیع به صورت:

$$
\langle x^n \rangle = \int_{-\infty}^{+\infty} x^n P(x) dx
$$

هستند. پس برای محاسبه‌ی گشتاور اول مطابق تعریف داریم:

$$
\langle x \rangle = \int_{-\infty}^{+\infty} x P(x) dx = \int_{-\infty}^{+\infty} \sqrt{\frac{a}{2\pi}} x e^{-\frac{1}{2}ax^2} dx = \sqrt{\frac{a}{2\pi}} \int_{-\infty}^{+\infty} x e^{-\frac{1}{2}ax^2} dx
$$

چون تابع درون انتگرال فرد است و بازه‌ی انتگرال‌گیری متقارن است، حاصل انتگرال برابر صفر می‌شود. پس اصلاً نیازی به محاسبه نیست. امّا محاسبه‌ی این انتگرال نیز کار دشواری نبوده و با یک تغییر متغیر به شکل زیر در می‌آید:

$$
\langle x \rangle = \sqrt{\frac{a}{2\pi}} \left[ \lim_{\alpha \to +\infty} \int_{-\alpha}^{0} x e^{-\frac{1}{2}ax^2} dx + \lim_{\alpha \to +\infty} \int_{0}^{\alpha} x e^{-\frac{1}{2}ax^2} dx \right]
$$

همان‌طور که گفته شد این انتگرال‌گیری‌ها به راحتی با تغییر متغیر حل می‌شوند. جواب آن‌ها به شکل زیر خواهد بود:

$$
\langle x \rangle = \sqrt{\frac{a}{2\pi}} \left[ -\frac{1}{a} \left( \lim_{\alpha \to +\infty} e^{-\frac{1}{2}ax^2} \Big|_{-\alpha}^{0} + \lim_{\alpha \to +\infty} e^{-\frac{1}{2}ax^2} \Big|_{0}^{\alpha} \right) \right] = 0 \quad \Rightarrow \quad \boxed{\langle x \rangle = 0}
$$

که این حدود مطابق تعریف انتگرال‌های ناسره نوشته شده است. این همان چیزی است که دنبالش بودیم. در ادامه برای محاسبه $\langle x^2 \rangle$ مطابق تعریف داریم:

$$
\langle x^2 \rangle := \int_{-\infty}^{+\infty} x^2 P(x) dx = \sqrt{\frac{a}{2\pi}} \int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx
$$

مجدداً برای محاسبه‌ی این انتگرال ناسره، انتگرال را به دو بخش منفی و مثبت باز می‌کنیم:

$$
\int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx = \lim_{\alpha \to +\infty} \int_{-\alpha}^{0} x^2 e^{-\frac{1}{2}ax^2} dx + \lim_{\alpha \to +\infty} \int_{0}^{\alpha} x^2 e^{-\frac{1}{2}ax^2} dx
$$

با استفاده از روش جزء به جزء ($\int u dv = uv - \int v du$) با فرض $u = x$ و $dv = x e^{-\frac{1}{2}ax^2} dx$ برای بازه‌ی منفی داریم:

$$
\lim_{\alpha \to +\infty} \int_{-\alpha}^{0} x^2 e^{-\frac{1}{2}ax^2} dx = \lim_{\alpha \to +\infty} \left( -\frac{1}{a} x e^{-\frac{1}{2}ax^2} \Big|_{-\alpha}^{0} + \frac{1}{a} \int_{-\alpha}^{0} e^{-\frac{1}{2}ax^2} dx \right) = \frac{1}{a} \lim_{\alpha \to +\infty} \int_{-\alpha}^{0} e^{-\frac{1}{2}ax^2} dx
$$

به طور مشابه برای بازه مثبت خواهیم داشت:

$$
\lim_{\alpha \to +\infty} \int_{0}^{\alpha} x^2 e^{-\frac{1}{2}ax^2} dx = \frac{1}{a} \lim_{\alpha \to +\infty} \int_{0}^{\alpha} e^{-\frac{1}{2}ax^2} dx
$$

در نتیجه حاصل کل انتگرال برابر است با:

$$
\int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx = \frac{1}{a} \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} dx = \frac{1}{a} \sqrt{\frac{2\pi}{a}}
$$

۹

که از نتایج بخش‌های قبلی استفاده شده است. با ضرب در ضریب پشت انتگرال $(\sqrt{\frac{a}{2\pi}})$ مقدار نهایی گشتاور دوم به شکل زیر بدست می‌آید:

$$
\langle x^2 \rangle = \frac{1}{a}
$$

که این همان چیزی است که می‌خواستیم محاسبه کنیم. همچنین یک روش دیگر برای حل انتگرال‌هایی به شکل $\int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx$
این است که از طرفین تساوی $\int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} dx = \sqrt{\frac{2\pi}{a}}$ که در ابتدا ثابت کردیم، نسبت به متغیر $a$ مشتق بگیرید. خواهیم داشت:

$$
\frac{\partial}{\partial a} \left( \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} dx \right) = \frac{\partial}{\partial a} \left( \sqrt{\frac{2\pi}{a}} \right)
$$

محاسبه‌ی طرف راست که بسیار ساده است. برای محاسبه‌ی طرف چپ هم از این واقعیت استفاده می‌کنیم که چون انتگرال گیری نسبت به متغیر $x$ است، مشتق گیری نسبت به $a$ از آن عبور می‌کند و به شکل زیر نوشته می‌شود:

$$
\frac{\partial}{\partial a} \left( \int_{-\infty}^{+\infty} e^{-\frac{1}{2}ax^2} dx \right) = \int_{-\infty}^{+\infty} \frac{\partial}{\partial a} \left( e^{-\frac{1}{2}ax^2} \right) dx = \int_{-\infty}^{+\infty} -\frac{1}{2}x^2 e^{-\frac{1}{2}ax^2} dx = -\frac{1}{2} \int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx
$$

طرف راست نیز به شکل زیر است:

$$
\frac{\partial}{\partial a} \left( \sqrt{\frac{2\pi}{a}} \right) = \frac{\partial}{\partial a} \left( \sqrt{2\pi}a^{-\frac{1}{2}} \right) = -\frac{1}{2}\sqrt{2\pi}a^{-\frac{3}{2}}
$$

از تساوی این دو رابطه خواهیم داشت:

$$
-\frac{1}{2} \int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx = -\frac{1}{2}\sqrt{2\pi}a^{-\frac{3}{2}} \quad \Rightarrow \quad \int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx = \sqrt{2\pi}a^{-\frac{3}{2}}
$$

که با ضرب طرفین در ضریب پشت انتگرال $(\sqrt{\frac{a}{2\pi}})$ مقدار نهایی گشتاور دوم به شکل زیر بدست می‌آید:

$$
\langle x^2 \rangle = \sqrt{\frac{a}{2\pi}} \int_{-\infty}^{+\infty} x^2 e^{-\frac{1}{2}ax^2} dx = \sqrt{\frac{a}{2\pi}} \sqrt{2\pi}a^{-\frac{3}{2}} = \frac{1}{a}
$$

که همان نتیجه‌ای است که از روش جزء به جزء بدست آمد. این روش بسیار مفید است و در جاهای زیادی استفاده می‌شود. پیشنهاد می‌شود این روش را به خوبی یاد بگیرید. قضیه‌ی ویک نیز به کمک انتگرال گیری جزء به جزء و یا همین روش ارائه شده در بالا اثبات می‌شود. سعی کنید خودتان آن را ثابت کنید.

ب) حد سری هندسی

بدست آوردن سری هندسی را در دبیرستان آموخته‌اید. روش اثبات به این شکل است که سری را در قدر نسبت آن ضرب می‌کنیم:

$$
S_n = a + ar + \cdots + ar^{n-1} \quad \Rightarrow \quad rS_n = ar + ar^2 + \cdots + ar^n
$$

حالا از تفاضل دو تساوی بالا خواهیم داشت:

$$
\Rightarrow \quad rS_n - S_n = a(r + r^2 + \cdots + r^n) - a(1 + r + \cdots + r^{n-1})
$$

تمامی جملات بجز جمله‌ی اول و آخر ساده می‌شوند. با کمی ساده سازی داریم:

$$
\Rightarrow \quad (r - 1)S_n = a(r^n - 1) \quad \Rightarrow \quad S_n = a\frac{r^n - 1}{r - 1}
$$

البته اگر قدر نسبت برابر یک باشد، سری به شکل زیر می‌شود:

$$
S_n = na
$$

۱۰

که این همان چیزی است که می‌خواستیم بدست آوریم. حالا اگر $|r| < 1$ باشد، حد مجموع در بی‌نهایت برابر است با:

$$ \lim_{n \to +\infty} S_n = \lim_{n \to +\infty} a \frac{r^n - 1}{r - 1} = \frac{-a}{r - 1} = \frac{a}{1 - r} \quad \Rightarrow \quad \boxed{ \lim_{n \to +\infty} S_n = \frac{a}{1 - r} } $$

که این همان نتیجه‌ای است که می‌خواستیم به آن برسیم. از این حد سری هندسی در مکانیک آماری استفاده‌ی فراوان می‌شود. خوب
است که آن را به خاطر بسپارید.

۵ بیشترین دما

الف بیشترین دما زمانی به دست می‌آید که ابتدا جسم ۱ را با ۲ و سپس با ۳ تماس دهیم. پس از تماس با ۲ دمایش به $۲۵^\circ$
می‌رسد و سپس با تماس با ۳ دمایش به $۶۲٫۵^\circ$ می‌رسد و این بیشترین دماییست که می‌توان به آن رسید. می‌توانید
جایگشت‌های دیگر را هم محاسبه کنید و بفهمید که این مورد بیشترین دما را دارد.

ب در هر تماس، دماها میانگین گرفته می‌شوند. پس دمای نهایی جسم یکم، یک ترکیب خطی از دماهای اولیه است:

$$ T_{1,f} = \sum_{i=1}^N w_i T_i $$

که $w_i$ها تنها به ترتیب تماس‌دهی ربط دارند و نه به دماها. با توجه به این که $T_{i+1} > T_i$، هدف نهایی این است که
وزن‌های مربوط به اجسام گرم‌تر را بیشینه کنیم (دقت کنید که $w_i$ها همگی دلخواه نیستند).
اگر جسم ۱ در تمام تماس‌ها حضور داشته باشد، دمای نهایی آن می‌شود:

$$ T_f = \frac{\frac{\frac{T_1 + T_2}{2} + \cdots}{2} + T_N}{2} $$
$$ = 2^{-(N-1)} T_1 + 2^{-(N-1)} T_2 + 2^{-(N-2)} T_3 + \cdots + 2^{-1} T_N $$

واضح است که اگر جرم‌ها را به ترتیبی بچینیم که $T_1$ کم‌ترین و $T_N$ بیشترین دما را داشته باشد، این جمع بیشینه خواهد
شد.
حال باید ثابت کنم که در حالت بهینه، حتماً جسم ۱ در همه‌ی تماس‌ها شرکت دارد. دنباله‌ای از تماس‌ها را در نظر بگیرید.
دمای نهایی جسم ۱ را می‌نویسم:

$$ T_f = \sum_{i=1}^N w_i T_i $$

اگر دو جسم $i$-اُم و $j$-اُم را پیش از تماسشان به جسم یکم به هم تماس دهیم:

$$ w_i, w_j \to \frac{w_i + w_j}{2} $$

دمای نهایی جسم ۱ به میزان $\Delta T$ تغییر می‌کند:

$$ \Delta T = \frac{w_i + w_j}{2} (T_i + T_j) - w_i T_i - w_j T_j = \frac{1}{2} (w_i - w_j)(T_j - T_i) $$

اگر $T_j \ge T_i$ باشد، واضح است که در حالت بهینه، $w_j \ge w_i$. پس $w_i - w_j$ و $T_j - T_i$ حتماً علامت مخالف
دارند. بنابراین $\Delta T \le 0$ است. بنابراین، در حالت بهینه، نباید دو جسمی که هیچکدام جسم ۱ نیستند را با هم تماس
دهیم. پس بیشینه دمای جسم ۱ به دست می‌آید:

$$ T_{1,max} = 2^{-(N-1)} T_1 + \sum_{i=2}^N 2^{-(N+1-i)} T_i $$

۱۱

۶ چند سوال کیفی
الف: روی سیستم کار انجام داده‌ایم پس انرژی آن بیشتر شده و دمایش بالا می‌رود و گرم‌تر می‌شود. برای شهود فیزیکی، می‌توانید به این سیستم شبیه گازی با فشار منفی نگاه کنید، یک گاز در یک انبساط بی‌درو سرد می‌شود. پس این سیستم که فشار منفی دارد گرم‌تر خواهد شد.

ب: با توجه به استدلال قسمت قبل، پس از تعادل انرژی سیستم کم‌تر شده پس باید سردتر شود.

پ» مطابق استدلال دو قسمت پیشین، افزایش دمای هم‌فشار باعث انقباض نوار می‌شود.

ت: اگر خوب ترمودینامیک بلد باشید، باید با ایده‌ی او مخالفت کنید. یک یخچال گرما را از جسم سرد به جسم گرم می‌دهد یعنی در ازای گرم شدن موتور، داخل یخچال سرد می‌شود. با باز گذاشتن یخچال این عمل هیچ اثری نخواهد داشت ولی اتلاف و گرمای ناشی از ایده‌آل نبودن موتور و برق، باعث افزایش دمای بیشتر اتاق می‌شود.

۱۲
