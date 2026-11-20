---
name: bia-paginas-porteiro
description: "Páginas da Bia no domínio dela: zona na conta Cloudflare do Rodrigo, ponte paginas.upcoproducoes.com.br no ar, porteiro-bia pronto esperando permissão"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-20T09:44:21.101Z
---

Estado em 20/11/2026:
- `fullconceptacademy.com.br` está na conta Cloudflare do Rodrigo (id 487c5435…). O login do Anderson (upcoproducoes) só tinha o papel "DNS" (leitura); não cria Worker nem mexe no Pages. O Anderson pediu ao Rodrigo (20/11) para trocar o papel dele para Administrador.
- Na conta do Anderson: o porteiro ganhou a ponte `paginas.upcoproducoes.com.br/<domínio>/<caminho>` (só lê o R2; commit b5bc454, no ar desde 19/11) e o pop-up de oferta ficou travado em pedrosachet.com.br.
- Falta criar o Worker `porteiro-bia` (arquivo `Up/cloudflare/porteiro-bia.js`) na conta do Rodrigo, com rotas `fullconceptacademy.com.br/*` e `www.fullconceptacademy.com.br/*`. Até lá, a página `/black-friday` publicada no Up (v3) responde 404 no domínio dela.
- O Worker do Rodrigo `paginas-beatriz-rotas` tem 47 rotas específicas (links-bio, combo-black-nov26, inscricao-black-nov26, black, black-live…); rota mais específica vence, então as páginas dele continuam. Página do Up não deve usar endereço dessa lista. As páginas dele vêm do projeto Pages `paginas-beatriz`; cópia local em `Full Concepty Academy/outputs/beatriz-vieira/cloudflare/paginas-beatriz/site` (de 13/11: comparar com o ar antes de editar).

**Why:** o Anderson quer publicar, despublicar e editar as páginas da Bia sem depender do Rodrigo. Independência de vez = trazer a zona para a conta dele (depois de 30/11, conferindo e-mail Hostinger, SES e site; ver titular no Registro.br).
**How to apply:** quando o Anderson avisar que o acesso mudou, conferir o papel (`/api/v4/memberships`), criar o porteiro-bia e as rotas, testar /black-friday e as páginas do Rodrigo. Ver [[vale-para-todos-os-projetos]].
