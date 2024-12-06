
! [[File:{{faction_info.logo}}|link={{faction_info.link}}|75px]] 
[[{{faction_info.link}}|{{faction_info.name}}]]
| {% for weapon in weapons -%}
[[ Weapons|{{weapon}} ]]</br>
{%- endfor %}
| {% for ammunition in ammunitions -%}
[[ Ammunition|{{ ammunition }}]]</br>
{%- endfor %}
| {% for gear in gears -%}
[[{{ gear }}]]</br>
{%- endfor %}
| {% for mech in mechs -%}
[[{{ mech }}]]</br>
{%- endfor %}
| {% for vehicle in vehicles -%}
[[{{ vehicle }}]]</br>
{%- endfor %}
| {% for battlearmor in battlearmors -%}
[[{{ battlearmor }}]]</br>
{%- endfor %}
| {% for contract in contracts -%}
[[ Contracts|{{ contract }}]]</br>
{%- endfor %}
|-