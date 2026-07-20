---
title: دیفرانسیل پتانسیل‌های ترمودینامیکی با آلفا و کاپا
tags: [thermodynamics, thermodynamic-potentials, maxwell-relations]
sources: ["[[TSMI - HW3.md]]"]
summary: نمایش دیفرانسیل پتانسیل‌های ترمودینامیکی (U, H, F) بر حسب ضریب انبساط طولی و تراکم‌پذیری.
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: supporting
---

# دیفرانسیل پتانسیل‌های ترمودینامیکی با $\alpha$ و $\kappa$

با استفاده از روابط ماکسول و تعریف ظرفیت‌های گرمایی، می‌توان دیفرانسیل پتانسیل‌های ترمودینامیکی را به جای متغیرهای طبیعی‌شان، بر حسب متغیرهای قابل اندازه‌گیری فیزیکی مانند $P$ و $T$ و ثوابت ماده ($\alpha$ ضریب انبساط حجمی و $\kappa$ ضریب تراکم‌پذیری هم‌دما) نوشت.

## روابط پایه
دو رابطه بسیار مهم که از قانون اول و دوم (با استفاده از روابط ماکسول) استخراج می‌شوند عبارتند از:
$$ \left(\frac{\partial U}{\partial V}\right)_T = T \left(\frac{\partial P}{\partial T}\right)_V - P $$
$$ \left(\frac{\partial H}{\partial P}\right)_T = V - T \left(\frac{\partial V}{\partial T}\right)_P $$

## بیان دیفرانسیل‌ها
با توجه به تعاریف:
$\alpha = \frac{1}{V} \left(\frac{\partial V}{\partial T}\right)_P$
$\kappa = -\frac{1}{V} \left(\frac{\partial V}{\partial P}\right)_T$

می‌توان دیفرانسیل انرژی درونی ($dU$)، آنتالپی ($dH$) و انرژی آزاد هلمهولتز ($dF$) را به شکل زیر بازنویسی کرد:
$$ dU = (C_P - PV\alpha)dT + V(\kappa P - \alpha T)dP $$
$$ dH = C_P dT + V(1 - \alpha T)dP $$
$$ dF = -(PV\alpha + S)dT + PV\kappa dP $$

این روابط برای محاسبه تغییرات انرژی سیستم‌ها تحت فرآیندهایی که دما و فشار کنترل می‌شوند بسیار کاربردی است.
