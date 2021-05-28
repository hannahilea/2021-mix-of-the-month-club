---
title: "MotM2021: Table of Contents"
---

### :mailbox_with_mail: :notes: Currently published mixes:
<ul>
{% for month in site.months %}
    <li>
        <a href="{{ site.baseurl }}/{{ month.permalink }}">{{ month.title }}</a><br>
        <img src="{{ site.baseurl }}/assets/radar_plot_{{ month.spotify_link_embedded }}.png" alt="Radar chart" width="300"/>
    </li>
{% endfor %}
</ul>
