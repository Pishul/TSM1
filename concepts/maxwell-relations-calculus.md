---
title: روابط ماکسول و حسابان ترمودینامیکی
tags: [thermodynamics, maxwell-relations, clairaut-theorem, reciprocity-theorem, thermodynamic-calculus]
sources: ["[[TSM I- n16.md]]", "[[TSM I- n17.md]]"]
summary: آموزش استخراج روابط ماکسول با استفاده از قضیه کلرو، معرفی قضیه وارونگی و چرخه مشتقات، و معرفی ضرایب ترمودینامیکی بتا و کاپا.
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: intermediate
---

# روابط ماکسول و حسابان ترمودینامیکی

ترمودینامیک پر از مشتقات جزئی است. برای ارتباط دادن کمیت‌های غیرقابل اندازه‌گیری (مانند آنتروپی) به کمیت‌های قابل اندازه‌گیری (دما، فشار، حجم)، از ریاضیات توابع چندمتغیره استفاده می‌کنیم.

## ۱. قضیه کلرو/شوارتز و روابط ماکسول
برای هر تابع خوش‌رفتار $f(x, y)$ که دارای دیفرانسیل کامل $df = M dx + N dy$ باشد، مشتقات جزئی دوم آن تعویض‌پذیرند:
$$ \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} \implies \left( \frac{\partial M}{\partial y} \right)_x = \left( \frac{\partial N}{\partial x} \right)_y $$

با اعمال این قضیه بر پتانسیل‌های ترمودینامیکی، **روابط ماکسول** استخراج می‌شوند:
- از $dU = T dS - p dV \implies \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial p}{\partial S}\right)_V$
- از $dH = T dS + V dp \implies \left(\frac{\partial T}{\partial p}\right)_S = \left(\frac{\partial V}{\partial S}\right)_p$
- از $dF = -S dT - p dV \implies \left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V$
- از $dG = -S dT + V dp \implies -\left(\frac{\partial S}{\partial p}\right)_T = \left(\frac{\partial V}{\partial T}\right)_p$

*(رابطه ناشی از $F$ و $G$ در عمل بسیار پرکاربردترند زیرا متغیرهای ثابت آن‌ها $T, p, V$ در آزمایشگاه قابل کنترل‌اند).*

## ۲. قضیه وارونگی و چرخه (Reciprocity and Inversion Theorem)
برای یک تابع ضمنی $f(x,y,z) = 0$ (مثل معادله حالت گاز):
1. **رابطه وارونگی:**
   $$ \left(\frac{\partial x}{\partial y}\right)_z = \frac{1}{\left(\frac{\partial y}{\partial x}\right)_z} $$
2. **رابطه چرخه (Reciprocity):**
   $$ \left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1 \implies \left(\frac{\partial x}{\partial y}\right)_z = - \frac{\left(\frac{\partial z}{\partial y}\right)_x}{\left(\frac{\partial z}{\partial x}\right)_y} $$
   *(دقت کنید که برخلاف مشتقات معمولی، حاصلضرب چرخه‌ای سه مشتق جزئی برابر $1$ نیست، بلکه $-1$ است).*

## ۳. ضرایب ترمودینامیکی پاسخ
برای توصیف رفتار مواد، از ضرایبی که مشتقات استاندارد هستند استفاده می‌شود:
- **ضریب انبساط حجمی ($\beta_p$):** 
  $$ \beta_p \equiv \frac{1}{V} \left(\frac{\partial V}{\partial T}\right)_p $$
  (نشان می‌دهد حجم ماده با افزایش دما چقدر منبسط می‌شود).
- **تراکم‌پذیری هم‌دما ($\kappa_T$):** 
  $$ \kappa_T \equiv -\frac{1}{V} \left(\frac{\partial V}{\partial p}\right)_T $$
  (نشان می‌دهد حجم ماده با افزایش فشار چقدر فشرده می‌شود. علامت منفی برای این است که مقدار $\kappa_T$ مثبت باشد).

### روش کلی حل مسائل ترمودینامیک:
1. دیفرانسیل کامل کمیت مطلوب را بنویسید.
2. از روابط ماکسول استفاده کنید تا مشتقات حاوی آنتروپی را به مشتقات $p, V, T$ تبدیل کنید.
3. با کمک قضیه چرخه، مشتقات باقی‌مانده را بر حسب داده‌های تجربی ($\beta_p, \kappa_T, C_p, C_V$) ساده کنید.
