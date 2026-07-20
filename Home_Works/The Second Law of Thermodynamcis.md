X1-190 (2025/08/03)

قانونِ دومِ ترمُدینامیک

محمد خرمی
mamwad@mailaps.org

بیان‌ی از قانونِ دومِ ترمُدینامیک ارائه میشود، که بر اساسِ ممنوع-کردنِ بعض‌ی چرخها ست.
بیانها‌یِ کِلوین-پْلانک [1] و کِلاوْزیوس [2] شکلهایی خاص از این بیانَ‌ند.

0 درآمد

چرخه فرایند‌ی ست که در آن حالتها‌یِ اولیه و نهاییِ سیستم یکسانَ‌ند. پس در یک چرخه، تغییرِ
انرژی-یِ-درونیِ سیستم صفر است. چرخه ای را بررسی میکنم که در آن سیستم با فقط دُ چشمه گرما
مبادله میکند. طیِ این چرخه، سیستم به اندازه یِ $W$ کار میگیرد، و از چشمه یِ گرم ($\mathrm{H}$) به اندازه یِ
$Q_{\mathrm{H}}$، و از چشمه یِ سرد ($\mathrm{C}$) به اندازه یِ $Q_{\mathrm{C}}$ گرما میگیرد. البته هر یک از اینها (گرماها و کار) ممکن
است منفی باشند. چون تغییرِ انرژی-یِ-درونیِ سیستم صفر است،

$$ 0 = Q_{\mathrm{H}} + Q_{\mathrm{C}} + W. \qquad (1) $$

قانونِ دومِ ترمُدینامیک                                                               ۲

پس میشود یک ی از این سه-کمیت را بر حسبِ دُ-تا یِ دیگر نوشت. از جمله،

$$
Q_H = -(Q_C + W). \qquad (2)
$$

از نظرِ تبادلِ گرما و کار، چرخه با دُ-تا از این کمیتها مشخّص میشود. اینجا با $(Q_C, W)$ کار میکنم. مجموعه یِ این دُتاییها (بردارها) را با $\mathbb{P}$ نشان میدهم. از نظرِ تبادلِ گرما و کار، هر چرخه با یک بردار در صفحه یِ $\mathbb{P}$ مشخّص میشود. البته تناظرِ بینِ بردارها یِ $\mathbb{P}$ و سیستمها یک-به-یک نیست: سیستمها یی هستند که یکسان نیستند، اما بردارها یِ شان یکسانَ ند. اما اینجا فقط تبادلها (یِ کار و گرما) را به کار میبَرَم. به هم ین خاطر چرخه را با بردارِ مشخّص-کننده یِ آن یکسان میگیرم: چرخه یِ $x$ یعنی چرخه ای که بردارِ مشخّص-کننده یِ آن $x$ است. تابعها یِ $Q_H$ و $Q_C$ و $W$ را چنین تعریف میکنم.

$$
x = [Q_C(x), W(x)]. \qquad (3)
$$

و البته،

$$
Q_H(x) = -[[Q_C(x) + W(x)]. \qquad (4)
$$

# 1 دست-کاری، هندسه

با بردارها یی در یک فضا-یِ-خطی یِ دُ-بُعدی یِ حقیقی ($\mathbb{P}$) کار میکنم. اما خیل ی از این کارها یا تعریفها به بُعدِ فضا وابسته نیستند. جاها یی که بُعد مهم است، صریحَن مینویسم.

چرخه (سیستم) را میشود مقیاس کرد: $\alpha$-برابر کرد. در این صورت همه یِ کمیتها یِ فزون‌وَر، از جمله گرماها و کارها، $\alpha$-برابر میشوند. پس $\alpha$-برابر-شده یِ چرخه یِ $x$، چرخه یِ $(\alpha x)$ است. از جمله چرخه یِ $(-x)$ هم ان چرخه یِ $x$ است که وارونه شده.

دُ چرخه را میشود با هم جمع کرد. چرخه یِ مجموع، متناظر است با سیستم ی که اجتماعِ سیستمها یِ (جدا-از-همِ) متناظر با چرخها یِ اولیه است.

با ترکیبِ مقیاس-کردن و جمع کردن، ترکیبِ -خطی یِ دُ چرخه تعریف میشود: ترکیبِ - خطی یِ چرخها یِ $x_1$ و $x_2$ با ضریبها یِ $\alpha^1$ و $\alpha^2$ چرخه یِ $(\alpha^1 x_1 + \alpha^2 x_2)$ است. span و spri

محمد خرمی (2025/08/03) X1-190
۳

را چنین تعریف میکنم.

$$ \operatorname{span}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n) = \{ \alpha^i \boldsymbol{x}_i \mid \alpha^1, \dots, \alpha^n \}. \tag{5} $$
$$ \operatorname{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n) = \{ \alpha^i \boldsymbol{x}_i \mid \alpha^1 \ge 0, \dots, \alpha^n \ge 0 \}. \tag{6} $$

$\operatorname{span}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)$ را پهنه ی $(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)$ مینامم. $\operatorname{span}(\boldsymbol{x})$ یک خطِ گذرنده-از-مبدئ است. $\operatorname{span}(\boldsymbol{x})$ با یک راستا در $\mathbb{P}$ مشخص میشود.

$\operatorname{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)$ را کُنجه ی $(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)$ مینامم. $\operatorname{spri}(\boldsymbol{x})$ یک نیمخطِ بسته (با-ابتدا) است، که ابتدایِ ش مبدئ است. $\operatorname{spri}(\boldsymbol{x})$ با یک جهت در $\mathbb{P}$ مشخص میشود.

میگویم مجموعه ی $\mathbb{S}$ بیش-گوژ است، اگر کُنجه ی هر دُ-نقطه در $\mathbb{S}$ زیرمجموعه ی $\mathbb{S}$ باشد:

$$ (\boldsymbol{x}_1, \boldsymbol{x}_2) \in \mathbb{S}^2 \Rightarrow $$
$$ [\operatorname{spri}(\boldsymbol{x}_1, \boldsymbol{x}_2)] \subseteq \mathbb{S}. \tag{7} $$

دیده میشود $\operatorname{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)$ بیش-گوژ است: کوچکترین مجموعه ی بیش-گوژ ی که $\boldsymbol{x}_1$ تا $\boldsymbol{x}_n$ را در بر دارد.

دیده میشود

$$ \operatorname{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n, -\boldsymbol{x}_1, \dots, -\boldsymbol{x}_n) = \operatorname{span}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n). \tag{8} $$

پس اگر $\mathbb{S}$ بیش-گوژ باشد، و $\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_n \}$ و $\{ -\boldsymbol{x}_1, \dots, -\boldsymbol{x}_n \}$ زیرمجموعه ی $\mathbb{S}$ باشند،

$$ [\operatorname{span}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)] \subseteq \mathbb{S}. \tag{9} $$

اگر $\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_n \}$ یک زیرمجموعه ی خطی-مستقلِ فضا-یِ-خطی ی $n$-بُعدی ی $\mathbb{V}$ باشد،

$$ \operatorname{span}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n) = \mathbb{V}. \tag{10} $$

گیرم چنین است، و $\mathbb{S}$ یک زیرمجموعه ی بیش-گوژِ $\mathbb{V}$ است، و $\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_n \}$ و $\{ -\boldsymbol{x}_1, \dots, -\boldsymbol{x}_n \}$ زیرمجموعه ی $\mathbb{S}$ اند. در این صورت،

$$ \mathbb{S} = \mathbb{V}. \tag{11} $$

قانونِ دومِ ترمُدینامیک                                              ۴

گیرم $\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_{n+1} \}$ یک زیرمجموعه‌یِ $(n+1)$-عضویِ فضایِ-خطیِ $n$-بُعدیِ $\mathbb{V}$ است، و همه‌یِ زیرمجموعه‌هایِ $n$-عضویِ $\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_{n+1} \}$ خطی-مستقل‌ند. در این صورت عددهایِ ناصفرِ $\alpha^1$ تا $\alpha^{n+1}$ی هستند که
$$ \alpha^i \boldsymbol{x}_i = 0. \qquad (12) $$

گیرم $\alpha^i$ ها هم-علامت‌ند. پس برایِ هر $i$،
$$ (-\boldsymbol{x}_i) \in [\text{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_{i-1}, \boldsymbol{x}_{i+1}, \dots, \boldsymbol{x}_{n+1})]. \qquad (13) $$

گیرم $\mathbb{S}$ یک زیرمجموعه‌یِ بیش-گوژِ $\mathbb{V}$ است، و $\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_{n+1} \}$ زیرمجموعه‌یِ $\mathbb{S}$ است. پس،
$$ [\text{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)] \subseteq \mathbb{S}. \qquad (14) $$
$$ [\text{spri}(-\boldsymbol{x}_1, \dots, -\boldsymbol{x}_n)] \subseteq \mathbb{S}. \qquad (15) $$

$\{ \boldsymbol{x}_1, \dots, \boldsymbol{x}_n \}$ هم خطی-مستقل است، پس $\mathbb{S}$ همان $\mathbb{V}$ است.

2 شدنی و نشدنی

همه‌یِ چرخه‌ها ممکن (شدنی) نیستند. مجموعه‌یِ چرخه‌هایِ شدنی را با $\mathbb{A}$ نشان می‌دهم. اگر $\boldsymbol{x}$ شدنی باشد، $(\alpha \boldsymbol{x})$ با $\alpha$یِ نامنفی هم شدنی ست:
$$ \boldsymbol{x} \in \mathbb{A} \Rightarrow $$
$$ [\text{spri}(\boldsymbol{x})] \subseteq \mathbb{A}. \qquad (16) $$

اگر $\boldsymbol{x}_1$ تا $\boldsymbol{x}_n$ شدنی باشند، $(\boldsymbol{x}_1 + \dots + \boldsymbol{x}_n)$ هم شدنی ست. به این ترتیب، اگر $\boldsymbol{x}_1$ تا $\boldsymbol{x}_n$ شدنی باشند، همه‌یِ چرخه‌هایِ $\text{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)$ هم شدنی‌یند:
$$ (\boldsymbol{x}_1, \dots, \boldsymbol{x}_n) \in (\mathbb{A}^n) \Rightarrow $$
$$ [\text{spri}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n)] \subseteq \mathbb{A}. \qquad (17) $$

۵
محمد خرمی (2025/08/03) X1-190

این یعنی $\mathbb{A}$ بیش-گوژ است.

اگر $x$ شدنی باشد و $\alpha$ منفی باشد، ممکن است $(\alpha x)$ نشدنی باشد. میگویم چرخه یِ (شدنی یِ) $x$ برگشت-پذیر است، اگر $(-x)$ شدنی باشد. دیده میشود چرخه یِ (شدنی یِ) $x$ برگشت-پذیر است، اگر و تنها اگر همه یِ چرخه هایِ $\text{span}(x)$ شدنی باشند. کلیتر، همه یِ چرخه هایِ (شدنی یِ) $x_1$ تا $x_n$ برگشت-پذیرند، اگر و تنها اگر همه یِ چرخه هایِ $\text{span}(x_1, \dots, x_n)$ شدنی باشند.

3 قانونِ دوم

چرخه هایِ $e_1$ و $e_2$ را چنین تعریف میکنم.

$$e_1 = (1, 0).$$ (18)
$$e_2 = (0, 1).$$ (19)

با $e_1$؛ سیستم از چشمه یِ سرد گرما میگیرد، این گرما را به چشمه یِ گرم میدهد، و کار مبادله نمیکند.
با $e_2$؛ سیستم کار میگیرد، این کار را به شکلِ گرما به چشمه یِ گرم میدهد، و با چشمه یِ سرد گرما مبادله نمیکند. عملن کار به گرما تبدیل میشود و چشمه یِ سرد حذف شده.

3.1 همواره-شدنی

با $(-e_1)$؛ چشمه یِ گرم به سیستم گرما میدهد، سیستم هم ان گرما را به چشمه یِ سرد میدهد، و کار مبادله نمیشود. عملن چشمه یِ گرم به چشمه یِ سرد گرما میدهد. $(-e_1)$ شدنی ست:

$$(-e_1) \in \mathbb{A}.$$ (20)

با $e_2$؛ سیستم عملن با فقط یک چشمه تماس دارد، کار میگیرد، و این کار را به شکلِ گرما به چشمه میدهد. $e_2$ شدنی ست:

$$e_2 \in \mathbb{A}.$$ (21)

۶                                                         قانونِ دومِ ترمُدینامیک

از (20) و (21) دیده میشود همه ی چرخها ی $\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2)$ شدنی یَند:

$$
[\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2)] \subseteq \mathbb{A}. \tag{22}
$$

رُشن است که

$$
\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2) = \{(q, w) \mid q \leq 0, w \geq 0\}. \tag{23}
$$

هر چرخه ای که در آن سیستم کار ندهد و از چشمه ی سرد گرما نگیرد شدنی ست. چنین-چرخه ای
همواره شدنی ست: مستقل از این که چشمها چه باشند شدنی ست.

3.2    گرما-گیر و کار-ده

میگویِم چرخه ی $\boldsymbol{x}$ گرما-گیر (یخچال) است، اگر

$$
Q_C(\boldsymbol{x}) > 0. \tag{24}
$$

میگویِم چرخه ی $\boldsymbol{x}$ کار-ده (مُتُر) است، اگر

$$
W(\boldsymbol{x}) < 0. \tag{25}
$$

رُشن است که $\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2)$ شاملِ هیچ چرخه ی گرما-گیر یا کار-ده ی نیست.

3.3    یک شرطِ کافی که همه ی چرخها شدنی باشند

گیرم چرخه ی $\boldsymbol{y}$، هم گرما-گیر است و هم کار-ده:

$$
Q_C(\boldsymbol{y}) > 0. \tag{26}
$$

$$
W(\boldsymbol{y}) < 0. \tag{27}
$$

دیده میشود

$$
\boldsymbol{y} + [Q_C(\boldsymbol{y})](-\boldsymbol{e}_1) + [-W(\boldsymbol{y})] \boldsymbol{e}_2 = 0. \tag{28}
$$

۷ محمد خرمی (2025/08/03) X1-190

$\{ \boldsymbol{y}, -e_1, e_2 \}$ یک مجموعه ی 3-عضوی از فضا-ی-خطی ی 2-بُعدی ی $\mathbb{P}$ است، و ضریبها ی $\boldsymbol{y}$
و $(-e_1)$ و $e_2$ در طرف-ِ-راستِ (28) مثبت‌اند. پس،
$$ \text{spri}(\boldsymbol{y}, -e_1, e_2) = \mathbb{P} . \qquad (29) $$

پس اگر $\boldsymbol{y}$ شدنی باشد، همه ی چرخها شدنی‌اند:
$$ \boldsymbol{y} \in \mathbb{A} \Rightarrow $$
$$ \mathbb{A} = \mathbb{P} . \qquad (30) $$

اگر یک چرخه که هم گرما-گیر و هم کار-ده است شدنی باشد، همه ی چرخها شدنی‌اند.
گیرم گرما-گیر $\boldsymbol{r}$ و کار-ده $\boldsymbol{m}$ شدنی‌اند. چرخه ی $\boldsymbol{s}$ در $\text{spri}(\boldsymbol{r}, \boldsymbol{m})$ را چنان میجوییم که $\boldsymbol{s}$ هم
گرما-گیر و هم کار-ده باشد:
$$ \boldsymbol{s} = \rho \boldsymbol{r} + \mu \boldsymbol{m} . \qquad (31) $$
$$ \rho \ge 0 . \qquad (32) $$
$$ \mu \ge 0 . \qquad (33) $$
$$ Q_C(\boldsymbol{s}) > 0 . \qquad (34) $$
$$ W(\boldsymbol{s}) < 0 . \qquad (35) $$

چون $\boldsymbol{r}$ گرما-گیر و $\boldsymbol{m}$ موتور است،
$$ Q_C(\boldsymbol{r}) > 0 . \qquad (36) $$
$$ W(\boldsymbol{m}) < 0 . \qquad (37) $$

و شرطها بر $(\rho, \mu)$، علاوه بر (32) و (33)، چنین میشوند.
$$ \rho + \frac{Q_C(\boldsymbol{m})}{Q_C(\boldsymbol{r})} \mu > 0 . \qquad (38) $$
$$ \mu + \frac{-W(\boldsymbol{r})}{-W(\boldsymbol{m})} \rho > 0 . \qquad (39) $$

۸    قانون دوم ترمُدینامیک

برای $(\rho, \mu)$ جواب هست، اگر و تنها اگر

$$
[Q_C(\boldsymbol{m}), W(\boldsymbol{r})] \notin \mathbb{B}. \quad (40)
$$

$$
\mathbb{B} = \{(q, w) \mid q < 0, w > 0, (-q\, w) \geq [Q_C(\boldsymbol{r})] \, [-W(\boldsymbol{m})]\}. \quad (41)
$$

اگر برای $(\rho, \mu)$ جواب باشد، یک چرخه یِ شدنی هست ($s$) که هم گرما-گیر و هم کار-ده است، پس همه یِ چرخها شدنی یَند: اگر $[Q_C(\boldsymbol{m}), W(\boldsymbol{r})]$ در $\mathbb{B}$ نباشد، همه یِ چرخها شدنی یَند. پس، اگر چرخها یی باشند که نشدنی یَند، هیچ یک از اعضا یِ $\text{spri}(\boldsymbol{e}_1, -\boldsymbol{e}_2)$ شدنی نیستند، مگر $\boldsymbol{0}$:

$$
\mathbb{A} \neq \mathbb{P} \Rightarrow
$$

$$
\mathbb{A} \cap [\text{spri}(\boldsymbol{e}_1, -\boldsymbol{e}_2)] = \{\boldsymbol{0}\}. \quad (42)
$$

3.4 اصلها (چیزها یی که میدانیم؟) و پیامدِ شان

یک بیانِ قانونِ دومِ ترمُدینامیک این (سه-گزاره) است:
• همه یِ چرخها یِ $\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2)$ شدنی یَند.
◦ دست-ِ-کم یک چرخه هست که نشدنی ست.
⋆ دست-ِ-کم یک چرخه یِ شدنی (یِ ناصفر) هست، که برگشت-پذیر است.

از • و ◦ نتیجه میشود هیچ یک از اعضا یِ $\text{spri}(\boldsymbol{e}_1, -\boldsymbol{e}_2)$ شدنی نیستند، مگر $\boldsymbol{0}$. این، همراه با ⋆ نتیجه میدهد یک $\boldsymbol{e}$ در $\text{spri}(\boldsymbol{e}_1, \boldsymbol{e}_2)$ هست که در $\text{spri}(\boldsymbol{e}_1)$ نیست و در $\text{spri}(\boldsymbol{e}_2)$ هم نیست و $\boldsymbol{e}$ و $(-\boldsymbol{e})$، هر-دُ شدنی یَند:

$$
\boldsymbol{e} \in [\text{spri}(\boldsymbol{e}_1, \boldsymbol{e}_2)]. \quad (43)
$$

$$
\boldsymbol{e} \notin [\text{spri}(\boldsymbol{e}_1)]. \quad (44)
$$

$$
\boldsymbol{e} \notin [\text{spri}(\boldsymbol{e}_2)]. \quad (45)
$$

$$
\{\boldsymbol{e}, -\boldsymbol{e}\} \subseteq \mathbb{A}. \quad (46)
$$

از (20) و (21) و (46) نتیجه میشود

$$
\mathbb{A} \supseteq [\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e})]. \quad (47)
$$

۹                                         محمد خرمی (2025/08/03) X1-190

البته،

$$ \boldsymbol{e}_2 \in [\text{spri}(-\boldsymbol{e}_1, \boldsymbol{e})]. \tag{48} $$
$$ (-\boldsymbol{e}_1) \in [\text{spri}(\boldsymbol{e}_2, -\boldsymbol{e})]. \tag{49} $$

پس،

$$ \text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e}) = \text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}, -\boldsymbol{e}). \tag{50} $$
$$ \text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e}) = \text{spri}(\boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e}). \tag{51} $$

گیرم $\boldsymbol{y}$ در $\text{spri}(\boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e})$ نیست. دیده میشود

$$ \boldsymbol{y} = a \boldsymbol{e}_2 + b \boldsymbol{e}. \tag{52} $$
$$ a < 0. \tag{53} $$

به این ترتیب،

$$ -\boldsymbol{e}_2 = (-a)^{-1} \boldsymbol{y} + a^{-1} b \boldsymbol{e}. \tag{54} $$

پس اگر $\boldsymbol{y}$ در $\mathbb{A}$ باشد، $(-\boldsymbol{e}_2)$ هم در $\mathbb{A}$ است. در این صورت $\mathbb{A}$ شامل $\text{span}(\boldsymbol{e}_2, \boldsymbol{e})$ میشود، که $\mathbb{P}$
است. این نتیجه میدهد $\mathbb{A}$ برابر $\mathbb{P}$ است، که درست نیست، چون چرخه ی نشدنی هم هست. پس همه ی
چرخها ی شدنی در $\text{spri}(\boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e})$ اند. این، همراه با (47) و (51) نتیجه میدهد

$$ \mathbb{A} = \text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e}). \tag{55} $$

و البته،

$$ \mathbb{A} = \text{spri}(-\boldsymbol{e}_1, \boldsymbol{e}, -\boldsymbol{e}). \tag{56} $$
$$ \mathbb{A} = \text{spri}(\boldsymbol{e}_2, \boldsymbol{e}, -\boldsymbol{e}). \tag{57} $$

قانونِ دومِ ترمُدینامیک                                                                          ۱۰

4 بیان‌های دیگر

از بیان‌های معمول‌ترِ قانونِ دومِ ترمُدینامیک، بیانِ کلوین-پلانک [1] و بیانِ کلاوزیوس [2] است.

4.1 بیانِ کلوین-پلانک

چرخه‌ای که از فقط یک چشمه گرما بگیرد و همه‌ی این گرما را به شکلِ کار بدهد ممکن نیست.
چون در این چرخه (ی نشدنی) سیستم با فقط یک چشمه تبادلِ گرما دارد، این چشمه را میشود
چشمه‌ی گرم یا سرد گرفت. در حالتِ اول، بیانِ کلوین-پلانک [1] این میشود.

$$ (-e_2) \notin \mathbb{A}. \quad (58) $$

در حالتِ دوم، بیانِ کلوین-پلانک [1] این میشود.

$$ (e_1 - e_2) \notin \mathbb{A}. \quad (59) $$

البته، در هر-دُ-حالت، گزاره‌های $\bullet$ و $\star$ هم ضمنی فرض شده‌اند.

4.2 بیانِ کلاوزیوس

چرخه‌ای که از چشمه‌ی سرد گرما بگیرد و همه‌ی این گرما را به چشمه‌ی گرم بدهد ممکن نیست.
بیانِ کلاوزیوس [2] این میشود.

$$ e_1 \notin \mathbb{A}. \quad (60) $$

البته گزاره‌های $\bullet$ و $\star$ هم ضمنی فرض شده‌اند.

4.3 مقایسه

بیانی از قانونِ دومِ ترمُدینامیک که شاملِ سه-گزاره‌ی $\bullet$ و $\circ$ و $\star$ است، شکلی کلی‌ست، که بیان‌های
کلوین-پلانک [1] و کلاوزیوس [2] حالت- -خاص‌هایی از آن‌ند. در همه‌ی این بیان‌ها دُ-گزاره‌ی $\bullet$ و
$\star$ مشترک‌ند (فرض شده‌اند). در بیانِ کلی، گزاره‌ی $\circ$ به گزاره‌های $\bullet$ و $\star$ اضافه میشود. در بیان‌های
کلوین-پلانک [1] و کلاوزیوس [2]، گزاره‌ی $\circ$ با شکل‌هایی خاص‌تر جای-گزین شده.

۱۱	محمد خرمی X1-190 (2025/08/03)

5 پیامدها

از (55)، همارز با آن (56) و (57)، دیده میشود مجموعه ی چرخها ی شدنی یک نیم-صفحه (شاملِ مرزِ ش) است. مرزِ این نیم-صفحه پهنه ی $e$ است. $\text{span}(e)$ یک خط است که از مبدئ میگذرد. شیبِ این خط را با $\xi$ نشان میدهم:

$$
\xi > 0. \tag{61}
$$

$$
\text{span}(e) = \{ (q, w) \mid \xi q - w = 0 \} . \tag{62}
$$

و مجموعه ی چرخها ی شدنی چنین میشود.

$$
\mathbb{A} = \{ (q, w) \mid \xi q - w \leq 0 \} . \tag{63}
$$

پس چرخه ی $x$ شدنی ست، اگر و تنها اگر

$$
\xi Q_C(x) - W(x) \leq 0 . \tag{64}
$$

که، با توجه به (1)، همارز است با این دُ-رابطه ی همارز-با-هم.

$$
(1 + \xi) Q_C(x) + Q_H(x) \leq 0. \tag{65}
$$

$$
(1 + \xi) W(x) + \xi Q_H(x) \geq 0. \tag{66}
$$

در (64) تا (66)، برابری برقرار است، اگر و تنها اگر $x$ برگشت-پذیر باشد، یعنی در $\text{span}(e)$ باشد.
رُشن است که $\xi$ به فقط چشمها بستگی دارد. $\xi$ ی متناظر با چشمها ی $i$ (گرم) و $j$ (سرد) را با $\xi_{ij}$ نشان میدهم: شرطِ لازم و کافی برا ی این که چرخه ی برگشت-پذیرِ $e_{ij}$، که با فقط چشمها ی $i$ و $j$ تبادل- -گرما دارد، شدنی باشد این است.

$$
(1 + \xi_{ij}) Q_j(e_{ij}) + Q_i(e_{ij}) = 0 . \tag{67}
$$

سه چشمه ی $i$ و $j$ و $k$ را در نظر میگیرم که $i$ گرمتر از $j$ است و $j$ گرمتر از $k$ است. مشابه با (67)،

$$
(1 + \xi_{jk}) Q_k(e_{jk}) + Q_j(e_{jk}) = 0 . \tag{68}
$$

قانون دوم ترمُدینامیک
۱۲

چرخه ی برگشت-پذیر $e_{jk}$ را به چرخه ی برگشت-پذیر $\tilde{e}_{jk}$ مقیاس میکنم:

$$ \tilde{e}_{jk} = -\frac{Q_j(e_{ij})}{Q_j(e_{jk})} e_{jk}. \qquad (69) $$

دیده میشود

$$ Q_j(\tilde{e}_{jk}) = -Q_j(e_{ij}). \qquad (70) $$
$$ Q_k(\tilde{e}_{jk}) = -\frac{Q_j(e_{ij})}{Q_j(e_{jk})} Q_k(e_{jk}) \qquad (71) $$

اجتماع سیستمها یی که چرخه-ی-برگشت-پذیرها ی $e_{ij}$ و $\tilde{e}_{jk}$ را میپیمایند، یک چرخه ی برگشت-پذیر را میپیماید که با فقط چشمهها ی $i$ و $j$ و $k$ تبادل-گرما دارد. گرماها و کار مبادله-شده هم جمع کمیتها ی متناظر با چرخها ی $e_{ij}$ و $\tilde{e}_{jk}$ اند. گرماها ی متناظر با این چرخه را با $\mathfrak{Q}$، و کار متناظر با این چرخه را با $\mathfrak{W}$ نشان میدهم:

$$ \mathfrak{Q}_i = Q_i(e_{ij}). \qquad (72) $$
$$ \mathfrak{Q}_j = Q_j(e_{ij}) + Q_j(\tilde{e}_{jk}). \qquad (73) $$
$$ \mathfrak{Q}_k = Q_k(\tilde{e}_{jk}). \qquad (74) $$
$$ \mathfrak{W} = W(e_{ij}) + W(\tilde{e}_{jk}). \qquad (75) $$

از (70) و (73) دیده میشود چرخه ی متناظر با اجتماع، با چشمه ی $j$ گرما مبادله نمیکند. پس این چرخه ($e$) با فقط چشمهها ی $i$ و $k$ تبادل-گرما دارد. در نتیجه، مشابه با (67)،

$$ (1 + \xi_{ik}) Q_k(e) + Q_i(e) = 0. \qquad (76) $$

به این ترتیب،

$$ 1 + \xi_{ik} = \frac{Q_i(e_{ij})}{Q_j(e_{ij})} \frac{Q_j(e_{jk})}{Q_k(e_{jk})}. \qquad (77) $$

که یعنی،

$$ 1 + \xi_{ik} = (1 + \xi_{ij})(1 + \xi_{jk}). \qquad (78) $$

محمد خرمی (2025/08/03) X1-190                               ۱۳

یک چشمه ی دلخواه (چشمه ی استاندارد $s$) و یک ثابتِ دلخواه ($T_s$) میگیرم، و برایِ هر چشمه ی $i$ کمیتِ $T_i$ را چنین تعریف میکنم.

$$ T_i = (1 + \xi_{is}) \, T_s. \quad (79) $$

این را در (78) میگذارم. دیده میشود

$$ 1 + \xi_{ij} = \frac{T_i}{T_j}. \quad (80) $$

این یعنی برایِ $\xi$ ی متناظر با چشمه-ی-گرم H و چشمه-ی-سرد C،

$$ 1 + \xi = \frac{T_H}{T_C}. \quad (81) $$

به $T$ دما ی مطلق میگویند. $T$ یکتا نیست. اما رُشن است که تا حدِ یک ثابتِ ضربی یکتا ست: نسبتِ دُ تابع که هر-دُ دما-ی-مطلق اند، یک ثابت است. ثابت-ِ-ضربی ی دلخواه ی که در $T$ هست، با چشمه-ی-استاندارد $s$ و ثابت-ِ-دلخواه $T_s$ تعیین میشود. البته اثرِ $s$ و $T_s$ بر $T$ مستقل از هم نیست: در $T$ فقط یک پارامترِ آزاد هست.

شرطِ (64) را برایِ گرما-گیرِ $r$ به کار میبرم. $Q_C(r)$ مثبت است: رابطه ی (36). پس (64) نتیجه میدهد $W(r)$ هم مثبت است و

$$ \frac{Q_C(r)}{W(r)} \le \frac{1}{\xi}. \quad (82) $$

نسبتِ گرما یی که از چشمه ی سرد گرفته میشود به کار ی که به گرما-گیر داده میشود را با $\nu$ نشان میدهم و به آن شاخصِ گرما-گیر میگویم. هر چه این شاخص بزرگتر باشد، گرما-گیر بهتر است. دیده میشود

$$ \nu(r) \le \frac{T_C}{T_H - T_C}. \quad (83) $$

۱۴
قانونِ دومِ ترمودینامیک

برابری (بهترین گرما-گیر) رخ میدهد، اگر و تنها اگر چرخه برگشت-پذیر باشد.

شرطِ (66) را برایِ کار-دهِ $m$ به کار میبرم. $W(m)$ منفی ست: رابطه یِ (37). پس (66)
نتیجه میدهد $Q_\text{H}(m)$ مثبت است و

$$ \frac{-W(m)}{Q_\text{H}(m)} \leq \frac{\xi}{1+\xi}. \quad (84) $$

نسبتِ کاری که از کار-ده گرفته میشود به گرمایی که از چشمه یِ گرم گرفته میشود را با $\eta$ نشان
میدهم و به آن بازدهِ کار-ده میگویم. هر چه این شاخص بزرگتر باشد، کار-ده بهتر است. دیده میشود

$$ \eta(m) \leq 1 - \frac{T_\text{C}}{T_\text{H}}. \quad (85) $$

برابری (بهترین کار-ده) رخ میدهد، اگر و تنها اگر چرخه برگشت-پذیر باشد.

6  پانوشت‌ها

[1] Kelvin-Planck
[2] Clausius
