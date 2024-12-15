text = input("Matn kiriting: ")
vowel_count = 0
consonant_count = 0
vowels = "aeiouAEIOU"

# Har bir belgi ustida ishlash
for char in text:
    if char.isalpha(): 
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
            
print(f"Unli harflar soni: {vowel_count}")
print(f"Undosh harflar soni: {consonant_count}")