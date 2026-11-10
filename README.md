# Dr. Daniel Halls — Academic Portfolio Website

A fast, lightweight, and modern static academic website for **Dr. Daniel Halls** (Clinical Neuroscientist & Research Fellow at the University of Nottingham).

Built with **[Astro](https://astro.build/)** with an editorial dark theme (near-black ground, serif display type, hairline rules, one muted brass accent, no icons), instant hot-reloading local preview, and a single-folder content editing architecture.

---

## ⚡ Quick Start: Local Preview

To preview the website locally on your computer with instant live-reloading:

```bash
./preview.sh
```
*(or run `npm run dev`)*

Then open **[http://localhost:4321](http://localhost:4321)** in your browser. Whenever you edit any Markdown or JSON file in `content/`, your browser updates instantly.

*Press `Ctrl+C` in your terminal to stop the preview server.*

---

## 📝 How to Edit Website Content (No HTML Required!)

**All editable content lives inside a single directory: [`content/`](content/)**. You never have to touch HTML templates, CSS, or deep nested subdirectories:

| Webpage / Section | URL | File to Edit | What You Can Edit |
| :--- | :--- | :--- | :--- |
| **Home / Bio** | `/` | [`content/about.md`](content/about.md) | Hero banner, research paragraphs, imaging modalities, pillars, and skills stack |
| **CV** | `/cv/` | [`content/cv.md`](content/cv.md) | Academic appointments, clinical experience, education degrees, and thesis details |
| **Projects** | `/portfolio/` | [`content/projects.md`](content/projects.md) | Computational neuroimaging tools, pipelines, descriptions, and tags |
| **Teaching** | `/teaching/` | [`content/teaching.md`](content/teaching.md) | Teaching roles, university tutoring blocks, and student supervision |
| **Publications** | `/publications/` | [`content/publications.json`](content/publications.json) | Complete publication catalog (automatically indexed with live search) |
| **Profile & Links** | (Global) | [`content/profile.json`](content/profile.json) | Name, bio, email, Google Scholar, PubMed, ORCID, GitHub, and LinkedIn links |

---

### Editing Examples

#### 1. Editing Your Bio & Research Text
Open [`content/about.md`](content/about.md) and edit the text under `## About My Research` in plain Markdown:
```markdown
## About My Research

My work operates at the intersection of **psychological medicine**, **computational neuroimaging**, and **behavioural data analysis**...
```

#### 2. Adding a New Project / Pipeline
Open [`content/projects.md`](content/projects.md) and add a new item under `projects:`:
```yaml
  - title: "Diffusion Signal Decomposition Suite"
    image: "/images/thalamus_radiations.png"
    description: "Novel computational algorithms to extract subcortical pathway integrity metrics."
    tags: ["Python", "Diffusion MRI", "FSL", "Connectomics"]
```

#### 3. Adding a Publication
Open [`content/publications.json`](content/publications.json) and add an item at the top of the list:
```json
{
  "title": "Your New Paper Title",
  "venue": "Journal Name",
  "year": "2026",
  "date": "2026-03-01",
  "citation": "Halls, D., et al. (2026). Your New Paper Title. *Journal Name*.",
  "url": "https://doi.org/..."
}
```
*(The Publications page at `/publications/` will immediately index and display it with interactive search).*

#### 4. Updating Profile Links or Affiliation
Open [`content/profile.json`](content/profile.json) and edit the fields directly:
```json
{
  "name": "Dr. Daniel Halls",
  "title": "Clinical Neuroscientist & Research Fellow",
  "employer": "University of Nottingham",
  "email": "Daniel.Halls@Nottingham.ac.uk",
  "social": {
    "googlescholar": "https://scholar.google.com/citations?...",
    "orcid": "https://orcid.org/0000-0002-5372-3179"
  }
}
```

---

## 🌐 Custom Domain Setup

Because this site is built with modern static HTML/CSS, you can host it anywhere on your custom domain for **free** with automatic HTTPS/SSL:

### Option 1: Cloudflare Pages (Recommended)
1. Sign up / log in to [Cloudflare](https://pages.cloudflare.com/) (100% free).
2. Go to **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3. Select this GitHub repository.
4. Set build settings:
   - **Framework preset**: `Astro`
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
5. Click **Save and Deploy**.
6. In your Pages dashboard, click **Custom domains** > **Set up a custom domain**, enter your domain name, and follow the simple 2-click DNS prompt. Cloudflare provides global edge caching and free SSL automatically.

### Option 2: Vercel
1. Log in to [Vercel](https://vercel.com/) and click **Add New...** > **Project**.
2. Import this repository (Vercel automatically detects Astro).
3. Click **Deploy**.
4. In **Settings** > **Domains**, enter your domain name and point your DNS CNAME/A records as shown.

### Option 3: GitHub Pages with Your Custom Domain
If you want to keep hosting on GitHub:
1. Go to repository **Settings** > **Pages**.
2. Under **Build and deployment** > **Source**, select **GitHub Actions**. (The `.github/workflows/deploy.yml` file will automatically build the Astro site on every git push).
3. Under **Custom domain**, enter your domain name (e.g. `danielhalls.com`).
4. At your domain registrar, add a CNAME record pointing to `Daniel-Halls.github.io`.

---

## 📁 Repository Directory Structure

```text
├── content/               <-- THE ONLY FOLDER YOU NEED TO EDIT
│   ├── about.md           (Home page bio, imaging modalities, pillars, skills)
│   ├── cv.md              (Curriculum Vitae experience & education)
│   ├── projects.md        (Computational tools and pipelines)
│   ├── teaching.md        (Teaching appointments and supervision)
│   ├── publications.json  (Publication catalog)
│   └── profile.json       (Author name, affiliations, and social links)
├── public/                <-- Static assets
│   ├── images/            (Profile avatar and brain imaging scans)
│   └── files/             (Downloads, BibTeX files)
├── src/                   <-- Website layout & styling engine
│   ├── components/        (Header, Footer)
│   ├── layouts/           (Main Layout template)
│   ├── pages/             (Route endpoints: /, /cv/, /portfolio/, /teaching/, /publications/)
│   └── styles/            (Editorial dark theme, global.css)
├── preview.sh             <-- Run to preview changes locally: ./preview.sh
├── astro.config.mjs       <-- Astro static configuration
└── package.json           <-- Node dependencies and scripts
```
