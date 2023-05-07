# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
my_age = int(age)
end_age = 90
all_days = 365
all_weeks = 52
all_month = 12

my_age_days = all_days * my_age
my_age_weeks = all_weeks * my_age
my_age_month = all_month * my_age

end_age_days = all_days * end_age
end_age_weeks = all_weeks * end_age
end_age_month = all_month * end_age

print(f"Вам осталось жить\n{end_age_days - my_age_days} - дней\n{end_age_month - my_age_month}-месяцев\n"
      f"{end_age_weeks - my_age_weeks} - недель")
