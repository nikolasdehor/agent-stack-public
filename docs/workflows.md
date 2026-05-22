# Workflows

Exemplos de como o stack é usado na prática, em formato público e sem dados privados.

## Large Implementation

1. Definir o objetivo e o risco.
2. Separar frentes independentes.
3. Delegar tarefas com escopo de escrita separado.
4. Integrar resultados no agente principal.
5. Rodar comandos reais de validação.
6. Reportar somente depois da verificação.

Skills comuns:

- agentic-engineering
- Codex-collaboration
- code-review
- verification-loop
- backend-patterns
- frontend-patterns

## Frontend Build And QA

1. Implementar a interface.
2. Rodar o servidor local.
3. Abrir via browser automation.
4. Checar desktop e mobile.
5. Capturar evidência visual quando necessário.
6. Corrigir sobreposição, responsividade e estados.

Plugins comuns:

- browser
- chrome
- playwright
- frontend-design
- build-web-apps

## Repo Review

1. Ler diff e contexto.
2. Priorizar bugs, regressões e riscos.
3. Verificar testes relevantes.
4. Reportar findings primeiro.
5. Sugerir próximos passos.

Plugins e skills comuns:

- GitHub
- CodeRabbit
- code-review
- pr-review-toolkit
- gh-address-comments
- gh-fix-ci

## Security Pass

1. Definir superfície analisada.
2. Procurar entradas, auth, dados sensíveis e integrações externas.
3. Separar finding confirmado de hipótese.
4. Validar exploitabilidade.
5. Propor correção mínima e teste.

Skills comuns:

- codex-security
- security-review
- threat-model
- finding-discovery
- fix-finding
- validation

## Deploy And Infra

1. Verificar framework e runtime.
2. Preferir integrações nativas da plataforma.
3. Isolar variáveis de ambiente.
4. Fazer deploy preview.
5. Inspecionar logs e health checks.
6. Documentar rollback.

Plugins comuns:

- Vercel
- Cloudflare
- Supabase
- GitHub
- Hostinger

## Knowledge Capture

1. Identificar decisão ou padrão reutilizável.
2. Remover detalhes privados.
3. Transformar em skill, nota ou checklist.
4. Reusar em tarefas semelhantes.

Princípio: memória operacional é útil, mas só vira conteúdo público depois de anonimização.
