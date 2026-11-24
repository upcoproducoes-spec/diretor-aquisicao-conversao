---
name: bia-paginas-porteiro
description: "Páginas da Bia no domínio dela: zona na conta Cloudflare do Rodrigo, Worker porteiro-up com rotas gerais (no ar desde 20/11), publicar pelo Up igual ao Pedro"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-20T23:20:52.227Z
---

Estado em 20/11/2026 (funcionando):
- `fullconceptacademy.com.br` está na conta Cloudflare do Rodrigo (id 487c5435…). Em 20/11 o Rodrigo deu ao login do Anderson os papéis Workers Admin, Cloudflare Pages Admin, Zone Settings Admin e DNS.
- O Rodrigo subiu o Worker **porteiro-up** (mesma lógica de `Up/cloudflare/porteiro-bia.js`: pergunta à ponte `paginas.upcoproducoes.com.br/<domínio>/<caminho>`; se o Up não tem a página, segue para o WordPress). Rotas: `fullconceptacademy.com.br/black-friday*` (dele) e, criadas por nós em 20/11, `fullconceptacademy.com.br/*` e `www.fullconceptacademy.com.br/*`, ambas com "falha ao abrir (continuar)" (se estourar a cota grátis de 100 mil/dia, o site segue pelo WordPress).
- Testado em 20/11: /black-friday e www/black-friday vêm do Up (x-served-by: up); home, /links-bio, /combo-black-nov26 (302), wp-admin, wp-login e 404 continuam como antes.
- O Worker `paginas-beatriz-rotas` do Rodrigo tem ~47 rotas específicas; rota mais específica vence, então as páginas dele continuam. Página do Up não deve usar endereço dessa lista.
- Gravar pela API do painel (POST com cookie) deu 403 em 20/11; rotas foram criadas pela tela (Domínio → Rotas de Workers → Adicionar rota). Leitura pela API do painel funciona.

Atualização em 24/11/2026:
- As 4 rotas do guia definitivo (`/guia-definitivo-pt`, `/guia-definitivo-pt/*`, `/guia-definitivo-pt-bio`, `/guia-definitivo-pt-bio/*`) passaram de `paginas-beatriz-rotas` para `porteiro-up` (pela tela; a API do painel segue dando 403). Testado: x-served-by: up; pixels 663381787741763 e 823602845323275 (PageView), GA4 G-T86JW6MJ5G (servidor appspot), Clarity e VTurb carregam; os links do checkout levam utm, src e sck.
- 10 páginas da Bia foram importadas para o Up (cópia fiel, aguardando aprovação): inscricao-black-nov26, obrigado-black-nov26, links-bio, links-bio-yt, up-1a/1b/2a/2b-gdpt, ds-gdpt e obrigado-gdpt. As rotas delas só mudam depois que o Anderson aprovar e publicar. Para desfazer qualquer troca: apontar a rota de volta para `paginas-beatriz-rotas`.
- Rastreio vem todo do GTM-PRTJDTX (embutido no HTML). Lead dispara em página cuja URL contém "obrigado". CompleteRegistration só dispara no clique em botão com o texto "QUERO ME INSCREVER AGORA". O formulário da Black posta em `paginas-beatriz.pages.dev/api/inscrever` (Function do Rodrigo), que é uma dependência.

**Why:** o Anderson quer publicar, despublicar e editar as páginas da Bia sem depender do Rodrigo. Agora é igual ao Pedro: aprovar e publicar no Up põe no ar. Independência total ainda = trazer a zona para a conta dele (depois de 30/11, conferindo e-mail Hostinger, SES e site; ver titular no Registro.br).
**How to apply:** página nova da Bia: só publicar no Up, sem rota nova. Se algo não abrir, conferir as rotas do porteiro-up e a ponte. Ver [[vale-para-todos-os-projetos]].
