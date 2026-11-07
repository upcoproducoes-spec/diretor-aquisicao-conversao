# Instala o Diretor de Aquisicao e Conversao num computador (skills, agentes e memoria).
#
# Uso (PowerShell, dentro da pasta do repositorio):
#   .\instalar.ps1
#   .\instalar.ps1 -PastaProjeto "C:\Users\SeuUsuario\Documents\Claude\Sistema"
#
# Skills e agentes: copiados para %USERPROFILE%\.claude (substitui os arquivos de mesmo nome).
# Memoria: copiada SOMENTE se informar -PastaProjeto (a memoria do Claude Code fica por pasta de
# projeto). Arquivos de memoria que ja existem NAO sao sobrescritos, a menos que use -SobrescreverMemoria.

#
# Opcional: -CriarAmbienteAds cria o ambiente Python da skill "ads" (precisa de Python 3.12+ instalado;
# baixa pacotes da internet via pip a partir de requirements.lock). Sem isso, as skills ads-* funcionam
# no modo de leitura/planejamento, mas os scripts de apoio (landing page, relatorio PDF, screenshots) nao.

param(
    [string]$PastaProjeto = "",
    [switch]$SobrescreverMemoria,
    [switch]$CriarAmbienteAds
)

$ErrorActionPreference = "Stop"
$raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
$claude = Join-Path $env:USERPROFILE ".claude"

$skillsDestino = Join-Path $claude "skills"
$agentsDestino = Join-Path $claude "agents"
New-Item -ItemType Directory -Force $skillsDestino, $agentsDestino | Out-Null

Copy-Item -Recurse -Force (Join-Path $raiz "skills\*") $skillsDestino
Copy-Item -Recurse -Force (Join-Path $raiz "skills-terceiros\*") $skillsDestino
Copy-Item -Force (Join-Path $raiz "agents\*") $agentsDestino
Copy-Item -Force (Join-Path $raiz "agents-terceiros\*") $agentsDestino
$nSkills = (Get-ChildItem (Join-Path $raiz "skills") -Directory).Count
$nTerc = (Get-ChildItem (Join-Path $raiz "skills-terceiros") -Directory).Count
$nAgents = (Get-ChildItem (Join-Path $raiz "agents") -File).Count
$nAgentsT = (Get-ChildItem (Join-Path $raiz "agents-terceiros") -File).Count
Write-Host "Skills do sistema: $nSkills  |  Skills de terceiros: $nTerc  |  Agentes do sistema: $nAgents  |  Agentes de terceiros: $nAgentsT"

if ($CriarAmbienteAds) {
    $adsDir = Join-Path $skillsDestino "ads"
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) {
        Write-Host "Python nao encontrado: instale o Python 3.12+ e rode de novo com -CriarAmbienteAds."
    } else {
        & python -m venv (Join-Path $adsDir ".venv")
        & (Join-Path $adsDir ".venv\Scripts\python.exe") -m pip install -r (Join-Path $adsDir "requirements.lock")
        Write-Host "Ambiente Python da skill ads criado em $adsDir\.venv"
    }
}

if ($PastaProjeto -ne "") {
    # O Claude Code guarda a memoria em .claude\projects\<caminho do projeto com tudo que nao e letra/numero trocado por ->\memory
    $nome = ($PastaProjeto.TrimEnd('\') -replace '[^A-Za-z0-9]', '-')
    $memDestino = Join-Path $claude ("projects\" + $nome + "\memory")
    New-Item -ItemType Directory -Force $memDestino | Out-Null
    $copiados = 0; $mantidos = 0
    foreach ($f in Get-ChildItem (Join-Path $raiz "memoria") -File) {
        $alvo = Join-Path $memDestino $f.Name
        if ((Test-Path $alvo) -and (-not $SobrescreverMemoria)) { $mantidos++; continue }
        Copy-Item -Force $f.FullName $alvo
        $copiados++
    }
    Write-Host "Memoria em: $memDestino  |  copiados: $copiados  |  ja existiam (mantidos): $mantidos"
} else {
    Write-Host "Memoria NAO instalada (informe -PastaProjeto para instalar). Veja o README."
}

Write-Host ""
Write-Host "Pronto. Feche e abra o Claude Code para carregar as skills e os agentes."
Write-Host "Lembrete: recrie a chave da OpenAI em $claude\openai.env se for usar o agente de design (cole voce mesmo, nunca no chat)."
Write-Host "Contas de anuncios (Meta, Google etc.) e outros conectores sao configurados por voce no Claude; nada disso vai no repositorio."
