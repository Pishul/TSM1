---
title: وابستگی ظرفیت‌های گرمایی به متغیرهای حالت
tags: [thermodynamics, heat-capacity, maxwell-relations]
sources: ["[[TSMI - HW3.md]]"]
summary: مشتقات ظرفیت‌های گرمایی نسبت به حجم و فشار.
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: supporting
---

# وابستگی ظرفیت‌های گرمایی به متغیرهای حالت

ظرفیت‌های گرمایی $C_V$ و $C_P$ علاوه بر دما، می‌توانند به متغیرهای دیگر مانند حجم و فشار نیز وابسته باشند (برای گاز ایده‌آل این وابستگی صفر است، اما برای گازهای حقیقی این‌گونه نیست).

## مشتقات ظرفیت گرمایی
با استفاده از این حقیقت که ظرفیت‌های گرمایی با مشتقات دوم پتانسیل‌های ترمودینامیکی (انرژی آزاد هلمهولتز و گیبس) مرتبط هستند:
$$ C_V = -T \left( \frac{\partial^2 F}{\partial T^2} \right)_V, \quad C_P = -T \left( \frac{\partial^2 G}{\partial T^2} \right)_P $$
و با بهره‌گیری از تقارن مشتقات متقاطع، به دو رابطه کلیدی می‌رسیم:

۱. **تغییرات $C_V$ با حجم (در دمای ثابت):**
$$ \left( \frac{\partial C_V}{\partial V} \right)_T = T \left( \frac{\partial^2 P}{\partial T^2} \right)_V $$
برای گاز ایده‌آل، $P \propto T$ است، بنابراین مشتق دوم آن نسبت به $T$ صفر می‌شود و $C_V$ مستقل از $V$ است.

۲. **تغییرات $C_P$ با فشار (در دمای ثابت):**
$$ \left( \frac{\partial C_P}{\partial P} \right)_T = -T \left( \frac{\partial^2 V}{\partial T^2} \right)_P = -TV \left[ \alpha^2 + \left( \frac{\partial \alpha}{\partial T} \right)_P \right] $$
که در آن $\alpha$ ضریب انبساط حجمی است. 

این معادلات به ما اجازه می‌دهند تغییرات ظرفیت گرمایی را تنها با استفاده از معادله حالت ($P-V-T$) پیش‌بینی کنیم، بدون آنکه نیاز به اندازه‌گیری مستقیم کالریمتری در فشارهای مختلف باشد.
