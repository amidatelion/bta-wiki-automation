# bta-wiki-generation
Automatic updates to mediawiki based on HBS Battletech json.

# How this works
This repo is intended to be used with Github Actions, specifically those in the main BTA repo. It can be adjusted for other usecases with little issue.

The core of this work is using jinja to create the final web document via [templates](templates/). This lets us pivot to hosting solutions that are not Mediawiki easily, as the data generation and and user interfaces are logically separated.

The actions require a little settings setup in the main BTA repo, namely creating repo variables and secrets for the wiki. Further documentation is in the main repo's [.github](https://github.com/BattleTech-Advanced-3062/BattleTech-Advanced/tree/development/.github/) directory. The actions call the Renderer scripts, which call the Parser scripts, which iterate through the desired data structures, gathering the desired information. The Renderer scripts then, uh, render the pages from the jinja templates and post them to the wiki. 

The pages that are rendered are Mediawiki *templates*, and so must still be inserted into the final webpages. This follows the wiki's development philosophy of ["good enough"](https://www.bta3062.com/index.php?title=Wiki_Team_Hub#Coding_Philosophy) whereby work is done piecemeal, in small, easily updateable chunks rather than attempts to build a large wholesale solution. 

Once the templates are inserted, they automatically update and can be forced to update with a cache purge. However, when new templated items are added, i.e. new factions or factories, those must be inserted manually still. The pages that need to be updated are listed below. There is a [ticket](https://github.com/BattleTech-Advanced-3062/bta-wiki-automation/issues/2) to diff those pages with the generated data to highlight any missing entires. Certain scripts (currently just the factory one) alert if they notice a lack of entries in their main page. 

# Local development
To test locally (that is to say, only write out .wiki files), nothing needs to be done. This is the default to avoid fucky updates going out. Once written out to the various files you can inspect them yourself and/or write them to a test page on the wiki to make sure they work right. Don't forget to `rm *.wiki` when you're done (the .gitignore doesn't let them be uploaded, but its a lot of clutter)

To post from you local for whatever reason, you need to export a valid WIKI_USER and WIKI_PASS and also export LOCAL_OVERRIDE=true. This force the scripts to post to the wiki. 

# Pages to update
- [Faction Stores](https://www.bta3062.com/index.php?title=Faction_Stores)
- [Factories](https://www.bta3062.com/index.php?title=Factory_Worlds)