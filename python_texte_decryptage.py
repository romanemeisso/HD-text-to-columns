text = """
 

"""

per_sentence_text = text.replace(". ",".\n")
new_text = per_sentence_text.replace("\n\n","")

print(new_text)