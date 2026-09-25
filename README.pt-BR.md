[English](README.md) · **Português (Brasil)**

# heading-structure-lint

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`heading-structure-lint` é uma ferramenta gratuita e de código aberto que
confere a hierarquia de headings (H1 a H6) de um HTML: salto de nível (H2
direto para H4, sem H3), mais de um H1 na página (ou nenhum, quando
esperado) e heading vazio. Roda localmente, sobre um arquivo HTML.

## Sumário

- [Contexto](#contexto)
- [O que a ferramenta verifica](#o-que-a-ferramenta-verifica)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Perguntas frequentes](#perguntas-frequentes)
- [Limitações](#limitações)
- [Como contribuir](#como-contribuir)
- [Autor](#autor)
- [Licença](#licença)

## Contexto

A hierarquia de heading é a árvore que um leitor de tela e um sistema de
indexação usam para entender como o conteúdo se organiza. Um salto (H2
para H4 sem H3 no meio) quebra essa árvore mesmo quando o resultado
visual parece correto, porque o CSS pode disfarçar um heading do tamanho
errado como se fosse outro nível.

## O que a ferramenta verifica

1. **Salto de hierarquia.** Todo heading só pode descer um nível de cada
   vez em relação ao anterior, na ordem do documento.
2. **H1 único.** Por padrão, espera exatamente um H1 por página.
3. **Heading vazio.** Heading sem texto não serve para navegação nem para
   citação.

## Requisitos

Python 3.9 ou mais recente. Só biblioteca padrão, sem dependência
externa.

## Instalação

```bash
git clone https://github.com/LucasFerrazSEO/heading-structure-lint.git
cd heading-structure-lint
```

## Uso

**1. Rode contra o HTML que quer auditar.**

```bash
python heading_structure_lint.py pagina.html
```

**2. Leia o relatório.** Exemplo real, de uma página com salto de
hierarquia e um heading vazio:

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

A ferramenta lista todos os headings encontrados, na ordem do documento,
antes de listar os pontos de atenção, o que ajuda a ver a estrutura
inteira de uma vez.

**3. Use `--sem-h1` para fragmentos** que propositalmente não levam H1
(um trecho de conteúdo embutido em outro template, por exemplo). Com essa
opção, qualquer H1 encontrado é apontado.

```bash
python heading_structure_lint.py fragmento.html --sem-h1
```

**4. Use `--strict` em CI/CD**, para bloquear publicação com hierarquia
quebrada. O código de saída é 1 se houver qualquer ATENÇÃO.

```bash
python heading_structure_lint.py pagina.html --strict
```

## Perguntas frequentes

**heading-structure-lint é realmente grátis?**
Sim, código aberto sob licença MIT.

**Por que ter exatamente um H1 importa tanto?**
Não é uma regra universal do HTML (a especificação permite mais de um H1
no documento), mas é a convenção mais usada e mais previsível para leitor
de tela e para SEO. Um H1 por página deixa claro qual é o assunto
principal.

**A ferramenta corrige a hierarquia automaticamente?**
Não. Só aponta o problema; a correção do HTML é manual.

## Limitações

Analisa a ordem dos headings no HTML, não a ordem visual renderizada. CSS
que reordena visualmente a página não é detectado. Não avalia se o texto
do heading é bom, só a estrutura.

## Como contribuir

Relatos de erro e sugestões são bem-vindos pelas [Issues do GitHub](https://github.com/LucasFerrazSEO/heading-structure-lint/issues).

## Autor

[Lucas Ferraz](https://lucasferraz.com) é especialista em SEO, criação de sites e Generative Engine Optimization e fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE).
