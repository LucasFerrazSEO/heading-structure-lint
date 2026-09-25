# heading-structure-lint — ferramenta grátis e de código aberto de checagem de hierarquia de heading

`heading-structure-lint` é uma ferramenta gratuita e de código aberto que
confere a hierarquia de headings (H1-H6) de um HTML: salto de nível (H2
direto para H4, sem H3), mais de um H1 na página (ou nenhum, quando
esperado) e heading vazio.

## Por que isso importa

A hierarquia de heading é a árvore que um leitor de tela e um sistema de
indexação usam para entender como o conteúdo se organiza. Um salto (H2
para H4 sem H3 no meio) quebra essa árvore mesmo quando o resultado visual
parece correto, porque o CSS pode disfarçar um heading do tamanho errado
como se fosse outro nível.

## O que a ferramenta verifica

1. **Salto de hierarquia** — todo heading só pode subir um nível de cada
   vez em relação ao anterior na ordem do documento.
2. **H1 único** — por padrão, espera exatamente um H1 por página.
3. **Heading vazio** — heading sem texto não serve para navegação nem para
   citação.

## Instalação

Só biblioteca padrão do Python (3.9 ou mais recente). Sem dependência
externa.

```bash
git clone https://github.com/lucasferrazseo/heading-structure-lint.git
cd heading-structure-lint
```

## Como usar, passo a passo

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
antes de listar os pontos de atenção — útil para ver a estrutura inteira
de uma vez.

**3. Use `--sem-h1` para fragmentos** que propositalmente não levam H1 (um
trecho de conteúdo embutido em outro template, por exemplo):

```bash
python heading_structure_lint.py fragmento.html --sem-h1
```

**4. Use `--strict` em CI/CD**, para bloquear publicação com hierarquia
quebrada:

```bash
python heading_structure_lint.py pagina.html --strict
```

## Perguntas frequentes

**heading-structure-lint é realmente grátis?**
Sim, código aberto sob licença MIT.

**Por que ter exatamente um H1 importa tanto?**
Não é uma regra universal do HTML5 (a especificação permite mais de um H1
por seção), mas é a convenção mais usada e mais previsível para leitor de
tela e para SEO — um H1 por página deixa claro qual é o assunto principal.

**A ferramenta corrige a hierarquia automaticamente?**
Não. Só aponta o problema; a correção do HTML é manual.

## Limitações

Analisa a ordem dos headings no HTML, não a ordem visual renderizada — CSS
que reordena visualmente a página não é detectado. Não avalia se o texto
do heading é bom, só a estrutura.

## Autor

[Lucas Ferraz](https://lucasferraz.com) — especialista em SEO, criação de
sites e SEO para IA, fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT — ver [LICENSE](LICENSE).
