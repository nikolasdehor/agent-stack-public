# Privacy Boundaries

Este repositório publica um mapa do stack, não o ambiente em si.

## Seguro Para Publicar

- Nomes públicos de plugins.
- Versões públicas de plugins.
- Repositórios de origem públicos.
- Categorias de uso.
- Descrições sanitizadas de skills.
- MCPs por nome e transporte, sem argumentos ou variáveis de ambiente.
- Workflows anonimizados.

## Nunca Publicar

- `auth.json`, tokens, cookies, sessões ou credenciais.
- `.env`, chaves privadas, PATs, API keys, SSH keys ou secrets.
- `config.toml`, `settings.json` ou MCP configs reais.
- Args de comandos MCP, headers, URLs privadas ou env vars.
- Logs, histórico, transcrições, memórias e bancos `.sqlite` ou `.db`.
- Plugin cache bruto, `node_modules`, `.git`, backups e dumps de estado.
- Paths locais, IPs privados, e-mails pessoais, nomes de clientes e repositórios privados.

## Política Para Skills

Skills podem parecer "só documentação", mas muitas carregam:

- caminhos locais;
- decisões de projeto;
- nomes de clientes;
- comandos internos;
- padrões pessoais de trabalho;
- contexto de memória.

Por isso, este repo publica inventário e categorias. O conteúdo completo de uma skill customizada só deve entrar aqui depois de revisão manual.

## Política Para Plugins

Listar nomes de plugins públicos é geralmente aceitável. Publicar o cache do plugin não é.

O cache pode conter dependências, exemplos, metadados de instalação, paths locais, hooks e integração com credenciais. Este repo usa nomes, versões e fontes públicas em vez do conteúdo bruto.

## Política Para MCPs

MCPs são documentados somente por:

- nome;
- transporte aproximado;
- categoria;
- nota pública.

Comandos, argumentos, variáveis de ambiente, tokens, URLs específicas e auth state ficam fora.

## Checklist Antes De Publicar

```bash
bash scripts/privacy_check.sh
```

Além disso, revisar manualmente alterações em:

- `README.md`
- `docs/`
- `data/*.json`

Se uma alteração menciona um caminho local, conta, cliente, segredo ou estado de execução, ela não pertence ao repo público.
