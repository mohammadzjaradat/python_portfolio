# fix_the_stats.py
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1 Fix: نقلنا تعريف وتصفير العداد failed ليصبح خارج الحلقة (قبلها)،
# لئلا يتم تصفيره في كل دورة تكرار داخل الfor loop.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

# Bug 3 Fix: نقلنا تصفير total و count ليصبحا قبل الحلقة بدلاً من وضعهما داخلها،
# لكي يتم تجميع البيانات عبر جميع عناصر القائمة بشكل صحيح.
total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2 Fix: استبدلنا القسمة الصحيحة (//) بالقسمة العادية (/) 
# للحصول على ناتج دقيق وعشري (float) مثل 30.0 بدلاً من 30.
print(f"Average session: {total / count} minutes")

# Bug 4 Fix: عدلنا نطاق range من (1, 4) إلى (1, 5) 
# لكي يتوقف عند الرقم 5 ويشمل طباعة Level 4 تماماً كما يطلب الهدف.
for level in range(1, 5):
    print(f"Level {level}")