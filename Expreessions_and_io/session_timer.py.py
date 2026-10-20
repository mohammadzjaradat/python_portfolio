#session_timmer.py
time_seconds = int(input("Enter the session duration in seconds: "))
time_minutes = time_seconds // 60
remaining_seconds = time_seconds % 60
messge = f"session duration = {time_minutes}m and {remaining_seconds}s"
print (messge)
# 15 and 5s = لما المستخدم يدخل بوقت الجلسة يساوي 905 ثانية
# 1m and 0s = لما المستخدم يدخل بوقت الجلسة يساوي 60 ثانية
# 0m and 59s = لما المستخدم يدخل بوقت الجلسة يساوي 59 ثانية
 