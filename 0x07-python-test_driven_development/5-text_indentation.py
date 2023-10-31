def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    line = ""

    for char in text:
        # Append the character to the current line
        line += char

        # Check if the character is '.', '?', or ':'
        if char in ".?:":
            # Print the current line without leading/trailing spaces and add two new lines
            print(line.strip())
            print()
            line = ""

    # Print any remaining text in the last line
    print(line.strip())

if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

