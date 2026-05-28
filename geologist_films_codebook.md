# CODEBOOK: Foreign Geologist Films Screening Checklist
# Extending Sturkell et al. (Geology Today, 2026)
# ─────────────────────────────────────────────────

## STEP 1: ELIGIBILITY TRIAGE
Fill these columns first. A film must pass ALL THREE to proceed.

is_fiction
  Y = narrative fiction film
  N = documentary, short, animated (unless animated narrative fiction)
  ? = unclear, needs investigation

theatrical_release
  Y = released theatrically in cinemas
  N = TV movie, direct-to-video, short film
  ? = unclear

geologist_explicitly_named_on_screen
  Y = a character is called "geologist" or equivalent in dialogue/title card
  N = geology is just the setting/topic, no named geologist character
  ? = unclear, needs viewing

ELIGIBLE
  Y = passes all three criteria above
  N = fails one or more
  ? = needs more research

notes_on_eligibility
  Brief note on why eligible/ineligible, or what you need to find out.


## STEP 2: CHARACTER DATA
(Only fill if ELIGIBLE = Y)
One row per geologist character. Add rows if a film has multiple geologists.

character_name
  Name as given in film. "Unknown" if unnamed.

gender
  M / F / NB / ?

race_ethnicity
  Use descriptive terms, not codes. e.g. "Japanese", "white Norwegian",
  "Soviet/Russian", "Indigenous" etc.
  ? if unclear

main_or_supporting
  MAIN = central protagonist or deuteragonist
  SUPPORTING = significant supporting role
  MINOR = brief appearance, few scenes

morally_good
  Y = acts ethically, aligned with audience sympathy
  N = villain, corrupt, or harmful actor
  MIXED = ambiguous
  ? = unclear

performs_heroic_act
  Y = explicitly sacrifices or risks self for others
  N = no heroic act
  ? = unclear

survives
  Y = alive at end of film
  N = dead by end of film
  ? = unclear / ambiguous ending

cause_of_death
  MURDER / GEOLOGICAL / ACCIDENT / HEALTH / EXTRATERRESTRIAL /
  SUICIDE / UNKNOWN / N/A (if survives)

death_on_screen
  Y = death depicted on screen
  N = found dead / implied
  N/A = survives


## STEP 3: NARRATIVE ROLE
(Your analytical additions — not in Sturkell)

narrative_role
  WARNER = warns of geological danger, believed or not
  EXTRACTOR = seeks resources, often in conflict with local populations
  BUILDER = state/nation-building mission (esp. Soviet tradition)
  INVESTIGATOR = solving a geological mystery
  VICTIM = geology or humans kill them, not their primary function
  OTHER = describe in notes

ignored_by_society
  Y = character's warnings or expertise are explicitly dismissed
  N = expertise is accepted/acted upon
  PARTIAL = partially heeded
  N/A = not applicable to narrative role

expertise_validated_before_death
  Y = shown to be right before dying
  N = dies without vindication
  N/A = survives or not applicable

notes_on_characterization
  Free text. Note anything interesting — tone, genre, ideological context,
  how geology itself is portrayed, relationship to landscape/land,
  colonial or anti-colonial dynamics, anything that diverges from
  the Anglo-American template.


## PRELIMINARY TRIAGE NOTES (from CSV metadata alone)

LIKELY ELIGIBLE (fiction, theatrical, geologist character):
  - The Skin of the South (1952, Japan) — drama, geologists vs. lumber baron
  - Letter Never Sent (1960, USSR) — drama, four geologists in Siberia
  - Papaya: Love Goddess of the Cannibals (1978, Italy) — horror, geologist team
  - Focusing on the Turquoise Mountain (1978, Czechoslovakia) — adventure/comedy
  - A Place in the World (1992, Argentina) — drama, geological engineer
  - The Wave (2015, Norway) — disaster thriller, geologist protagonist
  - Beyond Sleep (2016, Norway) — drama, geologist protagonist
  - The Quake (2018, Norway) — disaster thriller, geologist protagonist

NEEDS INVESTIGATION:
  - Where the Green Ants Dream (1984, Herzog) — mining company focus,
    is there an explicitly named geologist character?
  - Do Rocks Dream of Flying? (2025, Argentina) — 8 min, sci-fi/doc hybrid,
    "acoustic geologist" — theatrical? eligible?

INELIGIBLE (documentaries):
  - Diplom-Geologe (1990, Germany) — 8 min career documentary
  - Big Bang in Tunguska (2008, Germany) — documentary
  - Alice's Birthday (2009, Russia) — animated family sci-fi (archaeologist,
    not geologist — verify)
  - Living Stones of Sacsayhuamán (2014, Russia) — documentary
  - Jules Verne / Centre of the Earth (2023, France) — documentary
  - Great Natural Monuments Iceland (2023, France) — documentary
  - Grand Canyon (2025, France) — documentary (geologists appear but as
    real scientists, not characters)
