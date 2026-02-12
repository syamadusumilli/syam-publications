# TAM Build Kit

Everything needed to deploy The Approximate Mind on Hugo/Congo/Cloudflare Pages.

## What's Included

```
tam-build/
├── README.md                          (this file)
├── TAM_Article_Mapping.md             (complete article-to-section reference)
├── build_tam_articles.py              (processes all 55 articles)
├── config/
│   └── _default/
│       ├── hugo.toml                  (main Hugo config)
│       ├── params.toml                (Congo theme params)
│       ├── languages.en.toml          (author info)
│       └── menus.en.toml              (navigation)
└── content/
    ├── _index.md                      (homepage)
    ├── about/
    │   └── index.md                   (about page)
    ├── the-approximation/_index.md    (section 1)
    ├── what-ai-becomes/_index.md      (section 2)
    ├── the-known-self/_index.md       (section 3)
    ├── the-shared-world/_index.md     (section 4)
    ├── growing-up-with-ai/_index.md   (section 5)
    └── the-structures-we-live-in/_index.md (section 6)
```

## Deployment Steps

### 1. Run the build script

From your local machine, with the source markdown articles in a folder:

```powershell
python build_tam_articles.py --source C:\path\to\source\articles --dest C:\Users\syama\onedrive\syam-publications\tam\content
```

This reads all 55 source articles, injects front matter, strips existing titles,
and places them in the correct Hugo page bundle structure.

### 2. Copy config files

```powershell
# Copy the config directory into tam/
Copy-Item -Recurse .\config\* C:\Users\syama\onedrive\syam-publications\tam\config\
```

### 3. Copy content files (homepage, about, section indexes)

```powershell
# Copy homepage
Copy-Item .\content\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\

# Copy about page
Copy-Item -Recurse .\content\about C:\Users\syama\onedrive\syam-publications\tam\content\

# Copy section indexes (run after build script so section dirs exist)
Copy-Item .\content\the-approximation\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\the-approximation\
Copy-Item .\content\what-ai-becomes\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\what-ai-becomes\
Copy-Item .\content\the-known-self\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\the-known-self\
Copy-Item .\content\the-shared-world\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\the-shared-world\
Copy-Item .\content\growing-up-with-ai\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\growing-up-with-ai\
Copy-Item .\content\the-structures-we-live-in\_index.md C:\Users\syama\onedrive\syam-publications\tam\content\the-structures-we-live-in\
```

### 4. Test locally

```powershell
cd C:\Users\syama\onedrive\syam-publications\tam
hugo server
```

Visit http://localhost:1313

### 5. Push to GitHub

```powershell
cd C:\Users\syama\onedrive\syam-publications
git add .
git commit -m "TAM: initial build with 55 articles across 6 sections"
git push
```

### 6. Create Cloudflare Pages project

Go to Cloudflare dashboard > Compute & AI > Pages > Import existing Git repository:

- Project name: approximatemind
- Repository: syam-publications
- Production branch: main
- Framework preset: Hugo
- Build command: hugo
- Build output directory: public
- Root directory (advanced): tam
- Environment variable: HUGO_VERSION = 0.155.3

### 7. Add custom domain

In the Cloudflare Pages project settings, add approximatemind.com as a custom domain.

## Still Needed

- Author photo at tam/assets/img/authors/syam-yagn.jpg
- Cover images for articles (generate via pipeline)
- Notion database for TAM
- Congo color scheme tuning (currently using default "congo" scheme)
- Verify Congo theme is installed as submodule at tam/themes/congo/
