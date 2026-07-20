---
title: توزیع و فاکتور بولتزمن
tags: [statistical-mechanics, boltzmann-distribution, boltzmann-factor, probability, thermal-equilibrium]
sources: ["[[TSM I- n21.md]]"]
summary: استخراج فاکتور بولتزمن برای سیستمی در تماس با مخزن گرمایی، و بیان احتمال یافتن سیستم در یک میکروحالت خاص.
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: intermediate
---

# توزیع بولتزمن

یکی از بنیادی‌ترین نتایج مکانیک آماری، یافتن احتمال حضور یک زیرسیستم در یک حالت خاص، هنگامی که در تماس با یک مخزن گرمایی بزرگ قرار دارد، است.

## استخراج فاکتور بولتزمن
فرض کنید یک سیستم کوچک $S$ با انرژی $\epsilon$ در تماس با یک مخزن گرمایی بزرگ $B$ با انرژی کل $E - \epsilon$ قرار دارد. انرژی کل $E$ ثابت است و فرض می‌شود $\epsilon \ll E$.

احتمال اینکه سیستم کوچک در میکروحالت $r$ با انرژی $\epsilon_r$ یافت شود، با تعداد میکروحالت‌های در دسترس مخزن گرمایی متناسب است:
$$ P(\epsilon_r) \propto \Omega_B(E - \epsilon_r) $$

با بسط تیلور لگاریتم تعداد حالت‌های مخزن ($\ln \Omega_B$) حول انرژی کل $E$:
$$ \ln \Omega_B(E - \epsilon_r) \approx \ln \Omega_B(E) - \epsilon_r \frac{\partial \ln \Omega_B}{\partial E} $$
با استفاده از رابطه بنیادی ترمودینامیک آماری $S_B = k_B \ln \Omega_B \implies \frac{\partial \ln \Omega_B}{\partial E} = \frac{1}{k_B T}$:
$$ \ln \Omega_B(E - \epsilon_r) \approx \ln \Omega_B(E) - \frac{\epsilon_r}{k_B T} $$
با به توان رساندن دو طرف:
$$ \Omega_B(E - \epsilon_r) \approx \Omega_B(E) e^{-\frac{\epsilon_r}{k_B T}} $$

بنابراین، احتمال $P(\epsilon_r)$ با عبارت نمایی **فاکتور بولتزمن** متناسب است:
$$ P(\epsilon_r) \propto e^{-\frac{\epsilon_r}{k_B T}} $$

## نرمال‌سازی و توزیع نهایی
برای اینکه جمع احتمالات برابر با ۱ شود ($\sum_i P(\epsilon_i) = 1$)، باید عبارت فوق را بر مجموع روی تمام حالت‌ها تقسیم کنیم. این مخرج به عنوان تابع پارش (Partition Function) شناخته می‌شود. توزیع نهایی بولتزمن:
$$ P(\epsilon_r) = \frac{e^{-\frac{\epsilon_r}{k_B T}}}{\sum_i e^{-\frac{\epsilon_i}{k_B T}}} $$

### مفهوم فیزیکی
- در دمای ثابت، حالت‌هایی که انرژی کمتری دارند، به صورت نمایی احتمال حضور بیشتری دارند.
- در دمای بالا ($T \to \infty$)، فاکتور نمایی به ۱ نزدیک شده و توزیع تمام حالت‌ها یکنواخت می‌شود.
- در دمای بسیار پایین ($T \to 0$)، احتمال حضور در حالت پایه به ۱ نزدیک شده و احتمال سایر حالت‌ها صفر می‌شود.
