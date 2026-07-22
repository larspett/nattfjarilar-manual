---
title: Alla sidor
---

# Alla sidor

En översikt över hela manualen. Listan genereras automatiskt, så den hålls uppdaterad även när nya sidor läggs till.

{% assign pages_by_dir = site.html_pages | where_exp: "p", "p.url != '/' and p.url != '/index.html'" | group_by: "dir" %}
{% for group in pages_by_dir %}
{% assign section_name = group.name | remove_first: "/" | remove: "/" | replace: "-", " " %}
{% if section_name == "" %}{% assign section_name = "Övrigt" %}{% endif %}

## {{ section_name }}

{% for p in group.items %}
- [{{ p.title | default: p.name }}]({{ p.url | relative_url }})
{% endfor %}
{% endfor %}
