---
layout: page
title: Staff
description: A listing of all the course staff members.
---

# Staff

Staff information is stored in the `_staffers` directory and rendered according to the layout file, `_layouts/staffer.html`.

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Teaching Assistants

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign eng_lect = site.staffers | where: 'role', 'Engineer Lecturer' %}
{% assign num_eng_lect = eng_lect | size %}
{% if num_eng_lect != 0 %}
## Engineer Lecturer
{% for staffer in eng_lect %}
{{ staffer }}
{% endfor %}
{% endif %}