from workflow import extract_location_speciality,summary

user_query = input("Enter Text\t")
extracted_text = extract_location_speciality(user_query)
print(summary(user_query,extracted_text))