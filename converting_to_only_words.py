BACKGROUND_COLOR = "#B1DDC6"

with open("data/spanisz_words_temp..txt") as data_spanish:
    data = data_spanish.read()
    only_spanish_words = [data.split()[index] for index in range(len(data.split())) if index % 2 == 0]


with open("data/spanish_words.txt", "a") as new_data:
    for _ in only_spanish_words:
        new_data.write(f"{_}\n")
