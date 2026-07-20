---
title: توزیع سرعت ماکسول-بولتزمن و سرعت‌های مشخصه
tags: [statistical-mechanics, kinetic-theory, maxwell-boltzmann, equipartition-theorem, root-mean-square]
sources: ["[[TSM I- n21.md]]"]
summary: استخراج تابع توزیع سرعت ماکسول-بولتزمن برای گاز ایده‌آل سه‌بعدی، محاسبه سرعت‌های مشخصه (rms, میانگین, بیشینه) و قضیه هم‌پاری انرژی.
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: intermediate
---

# توزیع سرعت ماکسول-بولتزمن

با استفاده از توزیع بولتزمن می‌توان توزیع سرعت ذرات یک گاز کلاسیک را استخراج کرد. انرژی جنبشی ذره برابر است با $E = \frac{1}{2} m (v_x^2 + v_y^2 + v_z^2)$.

## تابع توزیع در یک و سه بعد
در یک بعد، توزیع مولفه سرعت (مثلاً $v_x$) یک توزیع گوسی نرمال است:
$$ g(v_x) dv_x = \sqrt{\frac{m}{2\pi k_B T}} e^{-\frac{m v_x^2}{2 k_B T}} dv_x $$

برای یافتن توزیع **اندازه سرعت** $v = |\vec{v}|$ در فضای سه‌بعدی، المان حجم در فضای سرعت از $dv_x dv_y dv_z$ به حجم یک پوسته کروی $4\pi v^2 dv$ تبدیل می‌شود:
$$ f(v) dv = g(v_x)g(v_y)g(v_z) \times 4\pi v^2 dv $$
با جایگذاری و نرمال‌سازی، تابع توزیع نهایی ماکسول-بولتزمن حاصل می‌شود:
$$ f(v) dv = 4\pi \left( \frac{m}{2\pi k_B T} \right)^{3/2} v^2 e^{-\frac{m v^2}{2 k_B T}} dv $$

## سرعت‌های مشخصه
سه معیار مهم برای سرعت گاز وجود دارد:
1. **سرعت بیشینه (محتمل‌ترین سرعت - $v_{\text{max}}$):** نقطه‌ای که تابع $f(v)$ ماکسیمم است ($\frac{df}{dv}=0$):
   $$ v_{\text{max}} = \sqrt{\frac{2 k_B T}{m}} $$
2. **سرعت میانگین ($\langle v \rangle$):**
   $$ \langle v \rangle = \int_0^\infty v f(v) dv = \sqrt{\frac{8 k_B T}{\pi m}} \approx 1.59 \sqrt{\frac{k_B T}{m}} $$
3. **سرعت ریشه میانگین مربعات ($v_{\text{rms}}$):**
   $$ v_{\text{rms}} = \sqrt{\langle v^2 \rangle} = \sqrt{\int_0^\infty v^2 f(v) dv} = \sqrt{\frac{3 k_B T}{m}} \approx 1.73 \sqrt{\frac{k_B T}{m}} $$
همواره ترتیب زیر برقرار است: **$v_{\text{max}} < \langle v \rangle < v_{\text{rms}}$**

## قضیه هم‌پاری انرژی (Equipartition Theorem)
با استفاده از مقدار $\langle v^2 \rangle = \frac{3 k_B T}{m}$، میانگین انرژی جنبشی هر مولکول گاز تک‌اتمی برابر است با:
$$ \langle E_k \rangle = \frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T $$
این نشان می‌دهد که هر درجه آزادی انتقالی ($x, y, z$) به طور میانگین دارای انرژی $\frac{1}{2} k_B T$ است.
