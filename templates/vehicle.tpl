|rowspan="1"|
[[File:Vehicle_{{icon}}.png|125px|border|center]]

'''[[{{icon}}#{{uiname}}|{{name.upper()}}]]'''

| {{uiname}}
| {{tonnage}}
| yes
| {{propulsion}}
| lmao
| {{enginetype}}
| {{enginecore}}
| {{armortotal}}
| {{structuretotal}}
| {{frontarmor}}
| {{leftarmor}}
| {{rightarmor}}
| {{reararmor}}
| {{turretarmor}}
| {% for gear in gears -%}
[[{{ gear }}]]</br>
{%- endfor %}
| {% for weapon in weapons -%}
[[ Weapons|{{weapon}} ]]</br>
{%- endfor %}
| {% for ammunition in ammunitions -%}
[[ Ammunition|{{ ammunition }}]]</br>
{%- endfor %}
|-