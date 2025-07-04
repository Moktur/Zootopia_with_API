import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def animal_data_to_html(animals_json_load):
    animal_info = ""
    for animal in animals_json_load:
        a_name, a_diet, a_location, a_type = extract_json_data(animal)
        if a_name and a_diet and a_location and a_type:
            animal_info += serialize_animal(a_name, a_diet, a_location, a_type)
    return animal_info


def extract_json_data(animal_dict):
    a_name = animal_dict.get("name")
    a_diet = animal_dict.get("characteristics", {}).get("diet")
    a_locations = animal_dict.get("locations", [])
    a_location = a_locations[0] if a_locations else None
    a_type = animal_dict.get("characteristics", {}).get("type")
    return a_name, a_diet, a_location, a_type


def serialize_animal(a_name, a_diet, a_location, a_type):
    """append information to each string for html"""
    animal_info = ""
    animal_info += '<li class="cards__item">'
    animal_info += (
        f"<div class=\"card__title\">{a_name}</div>\n"
        f"<p class=\"card__text\">\n"
        f"<strong>Diet:</strong> {a_diet}<br/>\n"
        f"<strong>Location:</strong> {a_location}<br/>\n"
        f"<strong>Type:</strong> {a_type}</br>\n"
        f"</p>"
        f"</li>"
    )
    animal_info += '</li>'
    return animal_info


def main():
    animals_data = load_data('animals_data.json')
    # print(animals_data)
    animal_data_to_html(animals_data)
    htmlfile = ""
    with open("animals_template.html", "r", encoding="utf-8") as at:
        template = at.read()
        htmlfile = template.replace(
            "__REPLACE_ANIMALS_INFO__",
            animal_data_to_html(animals_data)
        )
    with open("animals_template.html", "w", encoding="utf-8") as at:
        at.write(htmlfile)


if __name__ == '__main__':
    main()
