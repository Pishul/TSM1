---
title: ضریب ژول-تامسون و وابستگی انرژی داخلی به حجم
tags: [thermodynamics, joule-thomson, internal-energy, van-der-waals, free-expansion, non-ideal-gas]
sources: ["[[TSM I- n18.md]]"]
summary: اثبات وابستگی انرژی درونی گازهای واقعی به حجم، و معرفی ضریب ژول-تامسون برای محاسبه تغییرات دما در انبساط آزاد.
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: intermediate
---

# ضریب ژول-تامسون و انبساط گازهای حقیقی

در یک فرآیند انبساط آزاد (محیط عایق و دیواره‌های صلب بیرونی)، کاری انجام نمی‌شود و گرمایی مبادله نمی‌گردد ($\Delta U = 0$). برای یک گاز ایده‌آل، از آنجا که انرژی درونی فقط تابع دما است ($U=U(T)$)، نتیجه می‌گیریم که $\Delta T = 0$. اما برای گازهای واقعی، انرژی درونی به حجم نیز بستگی دارد و انبساط باعث تغییر دما می‌شود.

## وابستگی انرژی درونی به حجم
با استفاده از رابطه اول ترمودینامیک ($dU = T dS - p dV$):
$$ \left(\frac{\partial U}{\partial V}\right)_T = T \left(\frac{\partial S}{\partial V}\right)_T - p $$
با استفاده از رابطه ماکسول ($(\frac{\partial S}{\partial V})_T = (\frac{\partial p}{\partial T})_V$):
$$ \left(\frac{\partial U}{\partial V}\right)_T = T \left(\frac{\partial p}{\partial T}\right)_V - p $$
- برای **گاز ایده‌آل** ($p = \frac{RT}{v}$): مشتق $(\frac{\partial p}{\partial T})_V = \frac{R}{v}$. با جایگذاری، حاصل براکت صفر می‌شود. پس انرژی درونی گاز ایده‌آل به حجم ربطی ندارد.
- برای **گاز واندروالس**: با جایگذاری معادله حالت واندروالس، حاصل مثبت می‌شود ($\frac{a}{v^2}$)، یعنی انرژی درونی گاز واقعی با افزایش حجم (در دمای ثابت) افزایش می‌یابد (به دلیل غلبه بر انرژی پتانسیل جاذبه بین مولکولی).

## تعریف ضریب ژول-تامسون مکرر ($m_J$)
*توضیح: در این جزوه، ضریب ژول-تامسون به جای فرآیند هم‌آنتالپی (اختناق)، برای فرآیند انبساط هم‌انرژی (انبساط آزاد) در نظر گرفته شده است و با $m_J$ نشان داده می‌شود.*

این ضریب نشان‌دهنده‌ی تغییر دما نسبت به تغییر حجم در یک فرآیند با انرژی درونی ثابت است:
$$ m_J \equiv \left(\frac{\partial T}{\partial V}\right)_U $$
با استفاده از مشتق زنجیره‌ای چرخه‌ای:
$$ \left(\frac{\partial T}{\partial V}\right)_U \left(\frac{\partial V}{\partial U}\right)_T \left(\frac{\partial U}{\partial T}\right)_V = -1 \implies \left(\frac{\partial T}{\partial V}\right)_U = -\frac{\left(\frac{\partial U}{\partial V}\right)_T}{\left(\frac{\partial U}{\partial T}\right)_V} = -\frac{1}{C_v} \left(\frac{\partial U}{\partial V}\right)_T $$
با جایگذاری رابطه قبلی:
$$ m_J = -\frac{1}{C_v} \left[ T \left(\frac{\partial p}{\partial T}\right)_V - p \right] $$

### محاسبه $\Delta T$ در انبساط آزاد
برای پیدا کردن تغییر کل دمای گاز پس از انبساط آزاد:
$$ \Delta T = \int_{V_i}^{V_f} m_J dV $$
- **گاز ایده‌آل:** $m_J = 0 \implies \Delta T = 0$
- **گاز واندروالس:** $m_J = -\frac{a}{C_v v^2}$. با انتگرال‌گیری: 
  $$ \Delta T = -\frac{a}{C_v} \left( \frac{1}{v_i} - \frac{1}{v_f} \right) < 0 \quad (\text{چون } v_f > v_i) $$
  گاز واندروالس در انبساط آزاد همواره **سرد** می‌شود.

*(توجه: در گاز واقعی مدل‌شده با ضرایب ویریال $B_2(T)$، اگر $\frac{dB_2}{dT} > 0$ باشد، گاز در انبساط آزاد خنک می‌شود).*
