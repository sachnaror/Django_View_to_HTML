# Django View to HTML

This Django application demonstrates how to render HTML templates using Django views. It includes a simple example of a view that renders a template and passes context data to it.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sachnaror/Django_View_to_HTML.git
   pip install -r requirements.txt
   python manage.py runserver
   Visit http://127.0.0.1:8000/ in your web browser to see the rendered HTML template.
    ```

## Usage

The `render_template` view in `app/views.py` demonstrates how to render an HTML template using the `render` function provided by Django. The `template_name` argument specifies the path to the HTML template file relative to the `templates` directory in the app.

The `context` argument is a dictionary containing data to be passed to the template. In this example, the `name` key is passed to the template, which can be accessed using Django's template language (e.g., `{{ name }}`).

## Contributing

Contributions are welcome! If you find any issues or would like to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

Feel free to use and modify this markdown template for your `README.md` file.
