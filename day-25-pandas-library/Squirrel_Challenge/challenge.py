import pandas

data = pandas.read_csv("day-25-pandas-library/Squirrel_Challenge/squirrel_data.csv")

colors = data["Primary Fur Color"]

gray = 0
cinnamon = 0
black = 0

for color in colors.to_list():
    match color:
        case "Gray":
            gray += 1
        case "Cinnamon":
            cinnamon += 1
        case "Black":
            black += 1

data_dict = {
    "colours": ["Gray", "Cinnamon", "Black"],
    "amount": [gray,cinnamon,black]
}
    
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("day-25-pandas-library/Squirrel_Challenge/ColorData.csv")
