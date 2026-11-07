# Instala o Diretor de Aquisicao e Conversao num computador (skills, agentes e memoria).
#
# Uso (PowerShell, dentro da pasta do repositorio):
#   .\instalar.ps1
#   .\instalar.ps1 -PastaProjeto "C:\Users\SeuUsuario\Documents\Claude\Sistema"
#
# Skills e agentes: copiados para %USERPROFILE%\.claude (substitui os arquivos de mesmo nome).
# Memoria: copiada SOMENTE se informar -PastaProjeto (a memoria do Claude Code fica por pasta de
# projeto). Arquivos de memoria que ja existem NAO sao sobrescritos, a menos que use -SobrescreverMemoria.

param(
    [string]$PastaProjeto = "",
    [switch]$SobrescreverMemoria
)

$ErrorActionPreference = "Stop"
$raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
$claude = Join-Path $env:USERPROFILE ".claude"

$skillsDestino = Join-Path $claude "skills"
$agentsDestino = Join-Path $claude "agents"
New-Item -ItemType Directory -Force $skillsDestino, $agentsDestino | Out-Null

Copy-Item -Recurse -Force (Join-Path $raiz "skills\*") $skillsDestino
Copy-Item -Force (Join-Path $raiz "agents\*") $agentsDestino
$nSkills = (Get-ChildItem (Join-Path $raiz "skills") -Directory).Count
$nAgents = (Get-ChildItem (Join-Path $raiz "agents") -File).Count
Write-Host "Skills instaladas: $nSkills  |  Agentes instalados: $nAgents"

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
Write-Host "Lembretes: (1) recrie a chave da OpenAI em $claude\openai.env se for usar o agente de design;"
Write-Host "(2) reinstale as skills de design de terceiros listadas em docs\skills-de-design-necessarias.md."
