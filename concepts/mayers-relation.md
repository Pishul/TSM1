---
title: رابطه مایر برای ظرفیت‌های گرمایی
tags: [thermodynamics, mayers-relation, heat-capacity, thermodynamic-calculus]
sources: ["[[TSM I- n17.md]]"]
summary: اثبات رابطه مایر که نشان می‌دهد همیشه ظرفیت گرمایی در فشار ثابت بزرگتر از ظرفیت گرمایی در حجم ثابت است (Cp > Cv).
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: intermediate
---

# رابطه مایر (Mayer's Relation)

یکی از نتایج مهم روابط ترمودینامیکی، تعیین ارتباط دقیق بین ظرفیت گرمایی در فشار ثابت ($C_p$) و حجم ثابت ($C_v$) است. 

## اثبات رابطه
ظرفیت‌های گرمایی بر حسب آنتروپی به این صورت تعریف می‌شوند:
$$ C_p = T \left(\frac{\partial S}{\partial T}\right)_p \quad , \quad C_v = T \left(\frac{\partial S}{\partial T}\right)_V $$

دیفرانسیل کامل آنتروپی با در نظر گرفتن $T$ و $V$ به عنوان متغیرهای مستقل:
$$ dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV $$

با مشتق‌گیری از کل این رابطه نسبت به دما ($T$) در فشار ثابت ($p = \text{const}$):
$$ \left(\frac{\partial S}{\partial T}\right)_p = \left(\frac{\partial S}{\partial T}\right)_V + \left(\frac{\partial S}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_p $$

با ضرب کردن کل معادله در $T$:
$$ T\left(\frac{\partial S}{\partial T}\right)_p = T\left(\frac{\partial S}{\partial T}\right)_V + T\left(\frac{\partial S}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_p $$
$$ \implies C_p = C_v + T\left(\frac{\partial S}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_p $$

با استفاده از رابطه ماکسول از انرژی آزاد هلمهولتز $\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V$:
$$ C_p - C_v = T \left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial V}{\partial T}\right)_p $$

با استفاده از قضیه چرخه، مشتق $\left(\frac{\partial p}{\partial T}\right)_V$ را ساده می‌کنیم:
$$ \left(\frac{\partial p}{\partial T}\right)_V = - \frac{\left(\frac{\partial V}{\partial T}\right)_p}{\left(\frac{\partial V}{\partial p}\right)_T} $$

با جایگذاری:
$$ C_p - C_v = - T \frac{\left[ \left(\frac{\partial V}{\partial T}\right)_p \right]^2}{\left(\frac{\partial V}{\partial p}\right)_T} $$

حالا ضرایب ترمودینامیکی (انبساط حجمی $\beta_p$ و تراکم‌پذیری هم‌دما $\kappa_T$) را وارد می‌کنیم:
$$ \beta_p = \frac{1}{V} \left(\frac{\partial V}{\partial T}\right)_p \implies \left(\frac{\partial V}{\partial T}\right)_p = V \beta_p $$
$$ \kappa_T = -\frac{1}{V} \left(\frac{\partial V}{\partial p}\right)_T \implies \left(\frac{\partial V}{\partial p}\right)_T = -V \kappa_T $$

با جایگذاری این مقادیر، **رابطه نهایی مایر** به دست می‌آید:
$$ C_p - C_v = - T \frac{(V \beta_p)^2}{-V \kappa_T} = TV \frac{\beta_p^2}{\kappa_T} $$

## نتیجه‌گیری فیزیکی
از آنجا که دما ($T$) بر حسب کلوین، حجم ($V$) و تراکم‌پذیری ($\kappa_T$) برای سیستم‌های پایدار همواره مثبت هستند، و عبارت $\beta_p^2$ نیز به دلیل توان دوم همواره مثبت است:
$$ TV \frac{\beta_p^2}{\kappa_T} > 0 \implies C_p > C_v $$
این نشان می‌دهد که برای هر ماده‌ای (در حالت پایدار)، گرم کردن در فشار ثابت همواره نیازمند انرژی بیشتری نسبت به گرم کردن در حجم ثابت است (زیرا بخشی از گرما صرف انجام کار انبساط در مقابل محیط می‌شود). برای آب در دمای ۴ درجه سانتی‌گراد که $\beta_p = 0$ است، $C_p = C_v$ خواهد بود.
