<!DOCTYPE html>
<html>
  <head></head>
    <body>
        <table align="center">
        {% for title, description, urls in data %}
            <tr>
                <td><center><h2>{{ title }}</h2></center></td>
            </tr>
            <tr>
                <td><center><h3>{{ description }}</h3></center></td>
            </tr>
            <tr>
                <td>
                {% for url in urls %}
                    <center><img src="{{ url }}"></center>
                {% endfor %}
                </td>
            </tr>
        {% endfor %}
        </table>
    </body>
</html>

