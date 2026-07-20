---
title: شرایط تعادل ترمودینامیکی (حرارتی، مکانیکی و شیمیایی)
tags: [thermodynamics, equilibrium, thermal-equilibrium, mechanical-equilibrium, chemical-equilibrium, entropy-maximization]
sources: ["[[TSM I- n16.md]]", "[[TSM I- n19.md]]"]
summary: استخراج شرایط تعادل حرارتی، مکانیکی و شیمیایی از اصل بیشینه شدن آنتروپی برای یک سیستم منزوی متشکل از دو زیرسیستم.
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: intermediate
---

# شرایط تعادل ترمودینامیکی

بر اساس قانون دوم ترمودینامیک، یک سیستم منزوی (Isolated) زمانی به حالت تعادل پایدار می‌رسد که آنتروپی کل آن بیشینه شود. 
فرض کنید دو زیرسیستم $1$ و $2$ در تماس با یکدیگر یک سیستم منزوی را تشکیل می‌دهند. آنتروپی کل برابر است با $S_{\text{tot}} = S_1 + S_2$.
در حالت تعادل: $dS_{\text{tot}} = 0$.

## استخراج شرایط تعادل
معادلات بقای سیستم منزوی عبارتند از:
- بقای انرژی: $U_1 + U_2 = \text{const} \implies dU_1 = -dU_2$
- بقای حجم: $V_1 + V_2 = \text{const} \implies dV_1 = -dV_2$
- بقای ذرات: $N_1 + N_2 = \text{const} \implies dN_1 = -dN_2$

دیفرانسیل کل آنتروپی:
$$ dS_{\text{tot}} = \left( \frac{\partial S_1}{\partial U_1} dU_1 + \frac{\partial S_1}{\partial V_1} dV_1 + \frac{\partial S_1}{\partial N_1} dN_1 \right) + \left( \frac{\partial S_2}{\partial U_2} dU_2 + \frac{\partial S_2}{\partial V_2} dV_2 + \frac{\partial S_2}{\partial N_2} dN_2 \right) = 0 $$

با جایگذاری دیفرانسیل‌های زیرسیستم ۲ بر حسب ۱ و فاکتورگیری:
$$ dS_{\text{tot}} = \left( \frac{\partial S_1}{\partial U_1} - \frac{\partial S_2}{\partial U_2} \right) dU_1 + \left( \frac{\partial S_1}{\partial V_1} - \frac{\partial S_2}{\partial V_2} \right) dV_1 + \left( \frac{\partial S_1}{\partial N_1} - \frac{\partial S_2}{\partial N_2} \right) dN_1 = 0 $$

چون متغیرهای $U_1, V_1, N_1$ مستقل از هم هستند، برای اینکه حاصل جمع صفر شود، باید ضریب هر یک به صورت جداگانه صفر باشد:

### ۱. تعادل حرارتی (Thermal Equilibrium)
از برابر صفر قرار دادن ضریب $dU_1$:
$$ \frac{\partial S_1}{\partial U_1} = \frac{\partial S_2}{\partial U_2} \implies \frac{1}{T_1} = \frac{1}{T_2} \implies T_1 = T_2 $$
سیستم‌ها در صورت امکان تبادل گرما، هم‌دما می‌شوند.

### ۲. تعادل مکانیکی (Mechanical Equilibrium)
از برابر صفر قرار دادن ضریب $dV_1$:
$$ \frac{\partial S_1}{\partial V_1} = \frac{\partial S_2}{\partial V_2} \implies \frac{p_1}{T_1} = \frac{p_2}{T_2} \implies p_1 = p_2 $$
سیستم‌ها در صورت امکان تغییر حجم متقابل (جابجایی دیواره)، هم‌فشار می‌شوند.

### ۳. تعادل شیمیایی (Chemical Equilibrium)
از برابر صفر قرار دادن ضریب $dN_1$:
$$ \frac{\partial S_1}{\partial N_1} = \frac{\partial S_2}{\partial N_2} \implies -\frac{\mu_1}{T_1} = -\frac{\mu_2}{T_2} \implies \mu_1 = \mu_2 $$
سیستم‌ها در صورت امکان تبادل ذرات، پتانسیل شیمیایی برابر خواهند داشت.

## نتیجه‌گیری
تعادل کل ترمودینامیکی تنها زمانی حاصل می‌شود که هر سه شرط ($T_1=T_2$, $p_1=p_2$, $\mu_1=\mu_2$) همزمان برقرار باشند. این نشان می‌دهد که دما، فشار و پتانسیل شیمیایی به ترتیب پتانسیل‌های محرک تبادل گرما، حجم و جرم هستند.
