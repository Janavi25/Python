has_high_income = True
has_good_credit = False
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligeble for loan")
else:
    print("Not Eligeble for loan")

if has_high_income or has_good_credit:
    print("Eligeble for loan")
else:
    print("Not Eligeble for loan")

if has_high_income and not has_criminal_record:
    print("Eligeble for loan")
else:
    print("Not Eligeble for loan")

# And : both true
# or : at least one true
# not : converts true to false
  