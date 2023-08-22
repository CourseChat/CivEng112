import yaml

with open("_data/pdf_urls.yml", "r") as yaml_file:
    data = yaml.safe_load(yaml_file)

with open("output.html", "w") as html_file:
    for key, value in data.items():
        html_button = f'<a class="button" href="{value}">Visit PDF for page {key}</a>'
        html_file.write(html_button + "\n")
