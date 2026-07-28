---
title: All pages
---

# All pages

An overview of the whole manual. This list is generated automatically, so it stays up to date even as new pages are added.

📄 [Download the manual as PDF](../assets/pdf/nattfjarilar-manual.pdf) — a print-friendly snapshot of the page. Video links are shown as clickable addresses instead of embedded players, and some of the layout (page breaks, image sizes) is a compromise between how it looks online and the ability to print it.

{% for p in site.html_pages %}
{% if p.url contains "/en/" %}
{% unless p.url == "/en/" or p.url == "/en/index.html" %}
- [{{ p.title }}]({{ p.url | relative_url }})
{% endunless %}
{% endif %}
{% endfor %}
