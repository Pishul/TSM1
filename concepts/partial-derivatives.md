---
title: مشتقات جزئی در ترمودینامیک
tags: [math, partial-derivatives, implicit-function]
sources: ["[[TSMI - HW1.md]]"]
summary: قضایای کاربردی مشتقات جزئی برای روابط بین متغیرهای ترمودینامیکی وابسته.
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: "2026-07-20"
tier: supporting
---

# مشتقات جزئی در ترمودینامیک

در ترمودینامیک، معمولاً با سیستم‌هایی سروکار داریم که متغیرهای حالت آن‌ها ($x, y, z$) از طریق معادلات حالت (به فرم $f(x,y,z)=0$) به هم وابسته‌اند. این امر منجر به روابط ریاضی مفیدی می‌شود که از قضیه تابع ضمنی استخراج می‌گردند.

## قضیه‌های وارون و چرخه‌ای (سه متغیر)
برای سه متغیر وابسته که رابطه $f(x,y,z)=0$ را ارضا می‌کنند:
$$ \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y = 1 $$
$$ \left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1 $$
رابطه دوم به عنوان قضیه چرخه‌ای (Cyclic Relation) شناخته می‌شود و علامت منفی آن بسیار حائز اهمیت است.

## تعمیم به چهار متغیر
اگر متغیری مانند $w$ به سه متغیر وابسته $x, y, z$ مرتبط باشد:
$$ \left( \frac{\partial w}{\partial x} \right)_{y,z} = \frac{1}{\left( \frac{\partial x}{\partial w} \right)_{y,z}} $$
$$ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial z} \right)_{y,w} \left( \frac{\partial z}{\partial w} \right)_{y,x} = -1 $$

## قضایای کاربردی برای توابع ترمودینامیکی
برای تابع دلخواهی مانند $G(x,y,z)$ با قید وابسته بودن متغیرها:
$$ \left( \frac{\partial G}{\partial x} \right)_{y} = \left( \frac{\partial G}{\partial x} \right)_{z} + \left( \frac{\partial G}{\partial z} \right)_{x} \left( \frac{\partial z}{\partial x} \right)_{y} $$
$$ \left( \frac{\partial G}{\partial y} \right)_{x} = \left( \frac{\partial G}{\partial z} \right)_{x} \left( \frac{\partial z}{\partial y} \right)_{x} $$
این روابط برای تغییر متغیرهای مستقل در مشتق‌گیری‌ها (مثلاً از حجم به فشار) مستقیماً استفاده می‌شوند.

## مفاهیم مرتبط
- [[exact-differentials]]

## تمرین‌ها و پاسخ‌ها (بر اساس تکالیف)

### تمرین ۱: اثبات قضایای مشتقات جزئی
**سوال الف)** با استفاده از متغیرهای $x=x(y,z)$ و $z=z(x,y)$ روابط چرخه‌ای و وارون را ثابت کنید.
**پاسخ:**
مطابق دیفرانسیل کامل داریم:
$$ dx = \left(\frac{\partial x}{\partial y}\right)_z dy + \left(\frac{\partial x}{\partial z}\right)_y dz $$
$$ dz = \left(\frac{\partial z}{\partial x}\right)_y dx + \left(\frac{\partial z}{\partial y}\right)_x dy $$
با قرار دادن دومی در اولی و فرض $dy=0$ و سپس $dx=0$ ثابت می‌شود که:
$$ \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y = 1 $$
$$ \left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1 $$

**سوال ب)** همین قضایا را برای چهار متغیر وابسته بسط دهید.
**پاسخ:**
با استفاده از روش مشابه و دیفرانسیل سه‌متغیره، برای $w=w(x,y,z)$ بدست می‌آید:
$$ \left( \frac{\partial w}{\partial x} \right)_{y,z} \left( \frac{\partial x}{\partial z} \right)_{y,w} \left( \frac{\partial z}{\partial w} \right)_{y,x} = -1 $$

**سوال ج)** نشان دهید برای تابعی مثل $G(x,y)$:
$$ \left( \frac{\partial G}{\partial y} \right)_{x} = \left( \frac{\partial G}{\partial z} \right)_{x} \left( \frac{\partial z}{\partial y} \right)_{x} $$
**پاسخ:** 
با در نظر گرفتن $G=G(x,z(x,y))$ و گرفتن مشتق زنجیره‌ای نسبت به $y$ (در $x$ ثابت) مستقیماً به رابطه فوق می‌رسیم.
