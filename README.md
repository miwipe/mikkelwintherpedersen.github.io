# Mikkel Winther Pedersen — personal homepage

A bilingual, responsive static website for GitHub Pages. No JavaScript, tracking, external fonts or runtime dependencies are required.

Website: https://mikkelwintherpedersen.dk/

## Pages and languages

Danish is the default at the root; matching English pages are in `en/`. The language switch preserves the current page.

- `index.html`: introduction and six selected publications with short explanations
- `about.html`: background, research initiatives, LinkedIn and November 2026 CV
- `group.html`: five group members with portraits, biographies and profile links
- `talks.html`: speaking topics, seven previous talks and enquiries
- `press.html`: contact information, eight downloadable photographs, biography, CV and nine outreach examples

The CV is the supplied English PDF, copied without modification. Short biographies are downloadable in Danish and English.

## Editing and validation

Edit the source files, then regenerate the HTML:

- `scripts/build.py`: page templates and publication selection
- `scripts/da.json`: Danish translations
- `people.json`: group roster and profile links
- `talks.json`: previous talks and supporting links
- `outreach.json`: outreach examples and supporting links
- `press-photos.json`: press images, dimensions, credits and source provenance
- `seo.json`: page titles and descriptions
- `assets/style.css`: styles

```sh
python3 scripts/build.py
python3 scripts/check_languages.py
python3 scripts/check_seo.py
git diff --check
```

The builder uses only Python's standard library and does not modify images or the CV. Preview with `python3 -m http.server 8765`, then open http://localhost:8765/.

## GitHub Pages

Publish `main` from the repository root. `.nojekyll` serves the generated HTML without a Jekyll build. The older Markdown starter files and original `images/` directory are retained, but the redesigned pages use the HTML and `assets/` files.

The custom domain is recorded in `CNAME`. The generated pages use its HTTPS URL above for canonical, Open Graph, structured data, sitemap and alternate-language URLs. If the domain or hosting path changes, update `base` in `scripts/build.py`, `_config.yml` and the GitHub Pages domain settings, then rebuild.

## Sources and image credits

Content was reviewed with Mikkel in November 2026. The supplied CV and confirmed group biographies are the principal sources for the background and roster. Four group cards link to LinkedIn; Nare Ngoepe's card links to her University of Copenhagen profile.

- Personal research profile: https://researchprofiles.ku.dk/en/persons/mikkel-winther-pedersen/
- Group: https://globe.ku.dk/research/geogenetics/paleo-environmental-genomics-group/
- AEGIS: https://aegisearth.bio/en
- CAEG: https://globe.ku.dk/research/caeg/
- Nare's profile: https://researchprofiles.ku.dk/en/persons/dora-nare-ngoepe/

Each selected publication links to its DOI. Talk and outreach sources are recorded alongside the entries in their JSON files. The Vienna and Oulu talks link to the supplied CV. The Videnskab.dk article and PBS NOVA Q&A link to explanatory posts because direct destination URLs were not verified. Event programme links are not labelled as recordings. The 2022 Gisselfeld heading is a descriptive summary rather than a verbatim lecture title.

The homepage portrait and four press portraits are credited to Nicolai West. The two Arktisk Festival photos are credited to Mads Lumholt. At Mikkel's request, the two workshop images have no displayed credit; their original embedded photographer metadata is preserved.

The approved Arktisk Festival stage image is cropped and retouched around the speaker's eyes. The press gallery identifies that edit; its downloadable PNG is the approved image unchanged at 1672 × 941 pixels. Website JPG previews are derived from it. Original photos and earlier edited versions remain in the separate local source workspace.

Source paths in `press-photos.json` document the supplied files; they are not runtime dependencies. Press downloads otherwise preserve supplied JPG/PNG files, with HEIC converted to JPG as needed. Portraits, press photographs and CV content are not covered by an implied software or Creative Commons licence.

## Search readiness

Each page has its own title and description, canonical URL and language-alternate links. JSON-LD describes Mikkel as a Person; the About page uses ProfilePage. `scripts/check_seo.py` validates this metadata locally.

The custom domain serves `robots.txt` at its root and points crawlers to https://mikkelwintherpedersen.dk/sitemap.xml. After deployment, use Google Search Console to submit that sitemap and inspect indexing. Search Console and external profile updates are separate account actions.
