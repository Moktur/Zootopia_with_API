import json
import data_fetcher  # Import our new module

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
    """Creates HTML for each animal"""
    return (
        '<li class="cards__item">'
        f'<div class="card__title">{a_name}</div>'
        f'<p class="card__text">'
        f'<strong>Diet:</strong> {a_diet}<br/>'
        f'<strong>Location:</strong> {a_location}<br/>'
        f'<strong>Type:</strong> {a_type}</br>'
        '</p>'
        '</li>'
    )

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
            animals_info = f'<div class="error-message">{name} wasn\'t found in the database 🚽</div>'
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