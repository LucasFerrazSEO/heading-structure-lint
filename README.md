**English** · [Português (Brasil)](README.pt-BR.md)

# heading-structure-lint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`heading-structure-lint` is a free, open source tool that checks the
heading hierarchy (H1 to H6) of an HTML file: skipped levels (H2 straight
to H4, with no H3), more than one H1 on the page (or none, when one is
expected) and empty headings. It runs locally on an HTML file. The tool
prints its report in Brazilian Portuguese.

## Contents

- [Background](#background)
- [What it checks](#what-it-checks)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [FAQ](#faq)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Background

The heading hierarchy is the tree that a screen reader and an indexing
system use to understand how the content is organized. A skipped level
(H2 to H4 with no H3 in between) breaks that tree even when the page
looks right, because CSS can make a heading of the wrong level look like
another one.

## What it checks

1. **Skipped levels.** Each heading can only go one level deeper than the
   previous one, in document order.
2. **Single H1.** By default, it expects exactly one H1 per page.
3. **Empty headings.** A heading with no text is useless for navigation
   and for citation.

## Requirements

Python 3.9 or newer. Standard library only, no external dependencies.

## Installation

```bash
git clone https://github.com/LucasFerrazSEO/heading-structure-lint.git
cd heading-structure-lint
```

## Usage

**1. Run it on the HTML you want to audit.**

```bash
python heading_structure_lint.py pagina.html
```

**2. Read the report.** A real example, from a page with a skipped level
and an empty heading:

```
=== heading-structure-lint: headings.html ===
4 heading(s) | ATENÇÃO 2

  H1  Título da página
  H2  Seção 1
  H4  Subseção pulando H3
  H2

  ATENÇÃO  salto de hierarquia: H2 -> H4 ("Subseção pulando H3") sem heading intermediário
  ATENÇÃO  heading H2 vazio (sem texto)
```

The tool lists every heading it found, in document order, before the
ATENÇÃO (warning) lines, so you can see the whole structure at once.

**3. Use `--sem-h1` for fragments** that deliberately have no H1 (a piece
of content embedded in another template, for example). With this flag,
any H1 found is flagged.

```bash
python heading_structure_lint.py fragmento.html --sem-h1
```

**4. Use `--strict` in CI/CD** to block publishing with a broken
hierarchy. The exit code is 1 when there is any warning.

```bash
python heading_structure_lint.py pagina.html --strict
```

## FAQ

**Is heading-structure-lint really free?**
Yes. It is open source under the MIT license.

**Why does having exactly one H1 matter so much?**
It is not a universal HTML rule (the HTML specification allows more than
one H1 in a document), but it is the most common and most predictable
convention for screen readers and for SEO. One H1 per page makes the main
topic clear.

**Does the tool fix the hierarchy automatically?**
No. It only flags the problem. Fixing the HTML is manual.

## Limitations

It analyzes the order of headings in the HTML, not the rendered visual
order. CSS that visually reorders the page is not detected. It does not
judge whether the heading text is good, only the structure.

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/LucasFerrazSEO/heading-structure-lint/issues).

## Author

[Lucas Ferraz](https://lucasferraz.com) is an SEO, website development and Generative Engine Optimization specialist and the founder of [Lucas Ferraz SEO](https://lucasferrazseo.com).

## License

MIT. See [LICENSE](LICENSE).
