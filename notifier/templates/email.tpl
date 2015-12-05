<!DOCTYPE html>
<html>
  <head></head>
    <body>
        <table align="center">
        {% for title, age, description, location, urls in data %}
            <tr>
                <td><center><h2>{{ title }} (Age: {{ age }})</h2></center></td>
            </tr>
            <tr>
                <td><center><h3>{{ description }}</h3></center></td>
            </tr>
            <tr>
                <td><center><h3><a href="{{ location }}">Link</a></h3></center></td>
            </tr>
            <tr>
                <td>
                {% for url in urls %}
                    <center><img src="{{ url }}"></center>
                {% endfor %}
                </td>
            </tr>
            <tr>
                <td><center><h5>---------------</h5></center></td>
            </tr>
        {% endfor %}
        </table>
    </body>
</html>

