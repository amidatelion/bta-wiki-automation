{{ '{{' }}InfoboxPilot
|callsign = {{callsign}}
|pilotimage = Pilot {{callsign}}.png
|pilotname = {{firstname}} {{lastname}}
|age = {{age}}
|gender = {{gender}}
|faction = {{faction}}
|health = {{health}}
|gunnery = {{gunnery}}
|piloting = {{piloting}}
|guts = {{guts}}
|tactics = {{tactics}}
# Should work, if jank - requires variable contain the name of the variable
{% if multitarget %}|{{multitarget}} = yes{% else %}{% endif %}
{% if battlelord %}|{{battlelord}} = yes{% else %}{% endif %}
{% if precisionmaster %}|{{precisionmaster}} = yes{% else %}{% endif %}
{% if ballisticmaster %}|{{ballisticmaster}} = yes{% else %}{% endif %}
{% if energymaster %}|{{energymaster}} = yes{% else %}{% endif %}
{% if missilemaster %}|{{missilemaster}} = yes{% else %}{% endif %}
{% if stonecold %}|{{stonecold}} = yes{% else %}{% endif %}
{% if surefooting %}|{{surefooting}} = yes{% else %}{% endif %}
{% if phantom %}|{{phantom}} = yes{% else %}{% endif %}
{% if acepilot %}|{{acepilot}} = yes{% else %}{% endif %}
{% if invisibletarget %}|{{invisibletarget}} = yes{% else %}{% endif %}
{% if sprinter %}|{{sprinter}} = yes{% else %}{% endif %}
{% if bulwark %}|{{bulwark}} = yes{% else %}{% endif %}
{% if shieldedstance %}|{{shieldedstance}} = yes{% else %}{% endif %}
{% if juggernaut %}|{{juggernaut}} = yes{% else %}{% endif %}
{% if brawler %}|{{brawler}} = yes{% else %}{% endif %}
{% if defensiveformation %}|{{defensiveformation}} = yes{% else %}{% endif %}
{% if sensorlock %}|{{sensorlock}} = yes{% else %}{% endif %}
{% if targetprediction %}|{{targetprediction}} = yes{% else %}{% endif %}
{% if mastertactician %}|{{mastertactician}} = yes{% else %}{% endif %}
{% if knifefighter %}|{{knifefighter}} = yes{% else %}{% endif %}
{% if eagleeye %}|{{eagleeye}} = yes{% else %}{% endif %}
{% if intensifyfirepower %}|{{intensifyfirepower}} = yes{% else %}{% endif %}
{% if perfecttargeting %}|{{perfecttargeting}} = yes{% else %}{% endif %}
{% if overwhelmingaggression %}|{{overwhelmingaggression}} = yes{% else %}{% endif %}
{% if sideslip %}|{{sideslip}} = yes{% else %}{% endif %}
{% if streetracer %}|{{streetracer}} = yes{% else %}{% endif %}
{% if spotter %}|{{spotter}} = yes{% else %}{% endif %}
{% if redundantcomponents %}|{{redundantcomponents}} = yes{% else %}{% endif %}
{% if bruteforce %}|{{bruteforce}} = yes{% else %}{% endif %}
{% if hulldown %}|{{hulldown}} = yes{% else %}{% endif %}
{% if sensorsweep %}|{{sensorsweep}} = yes{% else %}{% endif %}
{% if targetpainting %}|{{targetpainting}} = yes{% else %}{% endif %}
{% if commandandcontrol %}|{{commandandcontrol}} = yes{% else %}{% endif %}
{{pilottags}}
# above will need extra processing to assemble something that looks like the below
|pilottag1 = Military
|pilottag2 = Command Experience
|pilottag3 = Solaris Gladiator
|pilottag4 = Federal
{{ '}}' }}


===Biography:===
{% if biography %}
{{ biography }}
{% else %}
None
{% endif %}


===Bonuses:===

None


===Availability:===
Can be found as a random starting pilot or in hiring halls. 

[[Category:Pilots]]
