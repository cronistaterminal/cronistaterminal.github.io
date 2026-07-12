+++
title = 'Quando o BASIC era a língua franca dos quartos'
date = 2026-06-22
draft = false
num = 1233
epoca = '1980–1991'
tldr = 'Antes do framework, antes do pacote, havia o prompt piscando e um manual de 300 páginas. Era assim que se aprendia.'
tldr_long = 'A década em que digitar um jogo a partir de uma revista era um rito de passagem. Cada erro de digitação virava uma aula de depuração — e de paciência.'
tags = ['retrocomputacao', 'c64']
+++

{{< figure src="demo/crt-monitor.jpg" pos="inline-right" w="320px"
    alt="Monitor CRT âmbar de um Commodore 64 ligado, exibindo o cursor piscando no prompt READY."
    cap="Um C64 recém-ligado: o prompt READY antes de qualquer fita carregar." >}}

A máquina ligava direto no interpretador. Não havia área de trabalho, não havia
menu, não havia nada entre a pessoa e a linguagem — só um cursor piscando e a
promessa de que qualquer linha digitada ali seria levada a sério.

Ligar o computador e cair no interpretador era a coisa mais natural do mundo, e
hoje é quase inconcebível: a máquina começava disposta a conversar.

{{< clear >}}

```basic {file="ola.bas"}
10 REM O PRIMEIRO PROGRAMA DE TODA UMA GERACAO
20 PRINT "QUAL O SEU NOME"
30 INPUT N$
40 FOR I = 1 TO 10
50   PRINT "OLA, "; N$; " -- LINHA "; I
60 NEXT I
70 GOTO 20
```

Dez linhas, e o computador já sabia o seu nome. O `GOTO` da linha 70 é o pecado
original de que Dijkstra reclamaria a vida inteira — mas era também a primeira
vez que alguém de doze anos via um laço infinito acontecer por culpa própria.

O que se perdeu não foi o BASIC: foi a distância curta. Hoje o mesmo impulso
sobrevive no terminal, que continua sendo o único lugar onde a máquina responde
sem intermediários.

```fish {file="retro.fish"}
function retro --description 'lista os .prg do diretorio, do maior pro menor'
    set -l dir (path resolve $argv[1])
    test -d "$dir"; or begin
        echo "nao é um diretorio: $dir" >&2
        return 1
    end
    for f in $dir/*.prg
        printf '%8d  %s\n' (path basename $f) (stat -c %s $f)
    end | sort -rn
end
```

A sintaxe mudou. O contrato — digito, ele obedece, eu vejo — é o mesmo de 1982.

{{< figure src="demo/keyboard-macro.jpg" pos="break-box" w="520px"
    alt="Teclado mecânico vintage visto de cima, teclas de função numeradas em vermelho."
    cap="As teclas de função coloridas — atalhos antes de atalhos serem padrão." >}}

Ninguém chamava aquilo de *developer experience*. Era só o teclado, e o que ele
fazia quando você o apertava.
