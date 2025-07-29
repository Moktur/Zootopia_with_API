import json
import data_fetcher  # Import our new module


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def animal_data_to_html(animals_json_load):
    """
    extracts all animal data from a json file
    returns a html string for all animals
    """
    animal_info = ""
    for animal in animals_json_load:
        a_name, a_diet, a_location, a_type = extract_json_data(animal)
        # if a_name and a_diet and a_location and a_type:
        animal_info += serialize_animal(a_name, a_diet, a_location, a_type)
    return animal_info


def extract_json_data(animal_dict):
    """
    extract data from a single animal
    returns four values about the animals
    """
    a_name = animal_dict.get("name")
    if animal_dict.get("characteristics", {}).get("diet") is not None:
        a_diet = animal_dict.get("characteristics", {}).get("diet")
    else:
        a_diet = ""
    if animal_dict.get("locations", []) is not None:
        a_location = animal_dict.get("locations", [])[0]
    else:
        a_location = ""
    if animal_dict.get("characteristics", {}).get("type") is not None:
        a_type = animal_dict.get("characteristics", {}).get("type")
    else:
        a_type = ""
    return a_name, a_diet, a_location, a_type


def serialize_animal(a_name, a_diet, a_location, a_type):
    """Creates HTML for each animal"""
    html_string = '<li class="cards__item">' \
        f'<div class="card__title">{a_name}</div>' \
        f'<p class="card__text">'
    if a_diet != "":
        html_string += f'<strong>Diet:</strong> {a_diet}<br/>'
    if a_location != "":
        html_string += f'<strong>Location:</strong> {a_location}<br/>'
    if a_type != "":
        html_string += f'<strong>Type:</strong> {a_type}</br>'
    html_string += '</p>' \
        '</li>'
    return html_string


def write_html(animals_info):
    """Writes the final HTML file"""
    with open("animals_template.html", "r", encoding="utf-8") as at:
        template = at.read()

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals_output.html", "w", encoding="utf-8") as at:
        at.write(html_content)


def main():
    try:
        name = input("What animal are you searching for? ")
        animals_data = data_fetcher.fetch_data(name)

        if not animals_data:
            animals_info = f'<div class="error-message">' \
                f'{name} wasn\'t found in the database 🚽</div>'
        else:
            animals_info = animal_data_to_html(animals_data)
        write_html(animals_info)
        print("HTML file generated successfully!")
    except Exception as e:
        animals_info = f'<div class="error-message">Error: {str(e)}</div>'
        write_html(animals_info)
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
