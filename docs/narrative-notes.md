# Notas de narrativa pública

Estas notas sugerem como apresentar um stack Codex + Claude Code de forma pública, útil e segura. A ideia central não é publicar um dump do ambiente local, mas explicar uma arquitetura de trabalho: como agentes, skills, plugins, MCPs e automações se combinam para transformar tarefas abertas em execução verificável.

## Tese do repositório

O repositório pode ser apresentado como um mapa editorial de um stack de agentes para desenvolvimento, pesquisa e operações locais. Ele mostra categorias, padrões de uso e exemplos anonimizados, sem expor configurações privadas, histórico de trabalho, credenciais, caminhos locais ou dados de clientes.

Frase curta possível:

> Um guia público para organizar um stack de agentes com Codex, Claude Code, skills, plugins e ferramentas MCP, com foco em colaboração, verificação e segurança operacional.

## Narrativa principal

1. **Do chat para o sistema operacional de trabalho**: mostrar que o valor não está em uma lista enorme de ferramentas, mas na combinação entre contexto, regras, skills especializadas e verificação.
2. **Agentes como colaboradores delimitados**: explicar que cada agente deve ter escopo, entregável, comandos de validação e fronteiras de escrita.
3. **Skills como memória operacional reutilizável**: apresentar skills como playbooks versionáveis, não como prompts soltos.
4. **Plugins e MCPs como capacidades externas**: descrever plugins por capacidade, origem e risco, sem copiar configurações locais.
5. **Publicação com higiene**: separar catálogo público, exemplos sintéticos e detalhes privados.

## Categorias a mostrar

- **Orquestração**: regras para dividir trabalho, integrar resultados e fazer revisão final.
- **Desenvolvimento**: frontend, backend, mobile, testes, refactors, revisão de código e documentação.
- **Browser e QA visual**: abertura de apps locais, screenshots, validação responsiva e fluxos manuais reproduzíveis.
- **Segurança**: auditorias, threat modeling, validação de findings e cuidados com segredos.
- **Infra e deploy**: Vercel, Cloudflare, Supabase, VPS e automações de ambiente, descritos por papel e não por credenciais.
- **Conhecimento e memória**: como o stack preserva decisões reutilizáveis sem publicar dados sensíveis.
- **Produtividade local**: scripts, checklists e rotinas que reduzem atrito sem depender de estado privado.

## Como apresentar skills e plugins

Evitar publicar um inventário cru. Em vez disso, usar um catálogo curado com campos públicos:

| Campo | Como usar |
| --- | --- |
| Nome público | Nome da skill ou plugin quando não revelar informação privada. |
| Categoria | Agrupar por capacidade, como testes, segurança, frontend ou deploy. |
| Função | Uma frase sobre o problema que resolve. |
| Origem | Oficial, comunidade, local-publicável ou exemplo sintético. |
| Nível de risco | Baixo, médio ou alto, conforme acesso a arquivos, rede, navegador ou credenciais. |
| Exemplo seguro | Um comando ou cenário anônimo, sem caminhos pessoais e sem tokens. |

Não publicar:

- Caminhos locais completos.
- Arquivos de configuração reais.
- Variáveis de ambiente.
- Tokens, chaves, cookies, sessões ou histórico de login.
- Dumps de memória, transcrições privadas ou logs brutos.
- Nomes de clientes, projetos fechados ou repositórios privados.
- Conteúdo completo de skills privadas quando a própria skill for propriedade intelectual ou contexto sensível.

## Seções recomendadas para o README

1. **Título e proposta**: nome do projeto e uma frase clara sobre o que ele documenta.
2. **Para quem é**: engenheiros, operadores de agentes, builders solo e times pequenos.
3. **Visão geral da arquitetura**: diagrama simples ligando agente principal, subagentes, skills, plugins, MCPs, browser e validação.
4. **Princípios de uso**: escopo claro, menor privilégio, validação real, contexto mínimo e publicação segura.
5. **Catálogo público**: tabela por categorias, com links para notas detalhadas.
6. **Workflows exemplares**: exemplos anonimizados de auditoria, implementação, QA visual e deploy.
7. **Modelo de privacidade**: o que fica fora do repo e por que.
8. **Como reproduzir sem copiar estado privado**: templates, exemplos sintéticos e comandos seguros.
9. **Como contribuir**: critérios para adicionar uma skill, plugin ou workflow ao catálogo.
10. **Licença e limites**: deixar claro que o repo documenta padrões, não distribui credenciais nem ambientes completos.

## Tom editorial

O README deve soar prático e investigativo: "aqui está como organizamos capacidades", não "aqui está tudo que existe no computador". A curiosidade vem da arquitetura e dos trade-offs, não da exposição de detalhes privados.

Preferir:

- "Este workflow usa um agente orquestrador e dois agentes delimitados para acelerar auditorias extensas."
- "Skills são descritas por intenção, gatilho e validação esperada."
- "Plugins com acesso a rede, browser ou credenciais aparecem com aviso de risco."

Evitar:

- "Aqui está a cópia completa do meu ambiente."
- "Basta importar estes arquivos locais."
- "Lista completa de memória, histórico e configuração."

## Estrutura possível do repo

```text
agent-stack-public/
  README.md
  docs/
    narrative-notes.md
    architecture.md
    catalog-format.md
    privacy-boundaries.md
    workflows.md
  examples/
    skill-card.example.md
    plugin-card.example.md
    workflow.example.md
  data/
    public-catalog.example.json
```

## Próxima decisão editorial

A decisão mais importante é escolher o nível de detalhe do catálogo:

- **Resumo curto**: melhor para README público e leitura rápida.
- **Catálogo por cards**: melhor para explicar capacidades sem dumping.
- **Manifest JSON público**: melhor para tooling, desde que seja gerado por allowlist e revisado antes de publicar.

Recomendação: usar os três em camadas. O README conta a história, `docs/` explica os princípios, e `data/` guarda apenas manifestos públicos gerados a partir de uma allowlist.
