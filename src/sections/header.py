# -*- coding: utf-8 -*-
def generate(sections):
    html = ""

    max_i = len(sections)
    for i, section in enumerate(sections):
        html += f'<a href="#{section.lower().replace(" ", "-")}">{section}</a>'

        if i < max_i - 1:
            html += " • "

    return f"""<h1 align="center">
  <br>
  <a href="http://www.example.com"><img src="https://foo.png" alt="TODO" width="200"></a>
  <br>
  TODO
  <br>
</h1>

<h4 align="center">TODO - Title.</h4>

<p align="center">
    TODO BADGES
</p>

<p align="center">
  {html}
</p>"""
