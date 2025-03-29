import pytest

def fix_phone_num(phone_num_to_fix):
  # Check for invalid chars
  valid_chars = "0123456789- "
  if any(char not in valid_chars for char in phone_num_to_fix):
    raise ValueError("Invalid characters in phone number")
  
  # Remove all the non-digit chars
  cleaned_num = []
  for char in phone_num_to_fix:
      if char.isdigit():
          cleaned_num.append(char)
  phone_num_to_fix = "".join(cleaned_num)
  
  # can only handle numbers that are exactly 10 digits long
  if (len(phone_num_to_fix) != 10):
    raise ValueError("Can only format numbers that are exactly 10 digits long")

  # given "5125558823". Split the parts, then recombine and return
  area_code = phone_num_to_fix[0:3] # 512 (first three digits)
  three_part = phone_num_to_fix[3:6] # 555 (next three digits)
  four_part = phone_num_to_fix[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'
  
# Now check that a too short string gives a ValueError
def test_fix_phone_num_invalid_length():
    with pytest.raises(ValueError):
        fix_phone_num("51")

def test_fix_phone_num_with_special_chars():
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761")
    with pytest.raises(ValueError):
        fix_phone_num("(321) 654 3333")

def test_fix_phone_num_non_digit_input():
    with pytest.raises(ValueError):
        fix_phone_num("512-abc-8823")
