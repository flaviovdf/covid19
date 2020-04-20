# Estimativas de R(t) por Estados do Brasil

1. [Brasil](#brasil)
1. [Centro Oeste](#centro-oeste)
1. [Nordeste](#nordeste)
1. [Norte](#norte)
1. [Sudeste](#sudeste)
1. [Sul](#sul)
    
- - -

## Metodologia

Esta página apresenta uma estimativa do número básico de reprodução (R0, pronunciado "R Zero"). O mesmo captura, ou é proporcional ao, número de outras pessoas que um indivíduo infectado vai contagiar. Um número básico de reprodução **R0 = 2** indica que uma pessoa infectada deve transmitir a doença para outras duas. Portanto, para conter uma doença é importante fazer com que **R0 < 1**, ou seja, na média a doença não se propaga mais entre pessoas. **Uma das formas de fazer isto é o isolamento social. Se você não entra em contato com ninguém, o vírus não espalha.**

Abaixo, apresento as estimativas do **R(t)**. Pode ser lido como a estimatica do número básico de reprodução em diferentes datas (em outras palavras "R0 ao longo do tempo"). Assim, podemos ter uma noção da eficácia do isolamento social.

Os dados foram gerados pelo [Brasil.IO](https://brasil.io) através de um esforço coletivo de interpretação dos relatórios da secretária de saúde de cada estado. O método utilizado é o mesmo que o [Centre for the Mathematical Modelling of Infectious Diseases (CMMID)](https://cmmid.github.io/) faz uso [4]. Aparenta ser o estado da arte. No geral, segui a metodologia dos autores para o COVID-19, os detalhes técnicos estão abaixo.

### Vídeo Aula

Para entender um pouco mais sobre o R0 fiz uma vídeo aula. A mesma está abaixo. Os primeiros minutos são suficientes.

[![Vídeo Aula](https://img.youtube.com/vi/VtSz59jez-Y/0.jpg)](https://www.youtube.com/watch?v=VtSz59jez-Y)

### Notas Técnicas (detalhes um pouco mais baixo nível)

Para fazer uso do método, é necessário estimar uma distribuição de probabilidade que captura o tempo entre casos consecutivos. Isto é, a distribuição captura a probabilidade de um caso **i** infectar outro **j** em um dado intervalo de tempo **x**. Para o COVID-19, [3] sugere uma distribuição Weibull com média 4.7 (95% CrI: 3.7, 6.0) e desvio padrão de 2.9 (95% CrI: 1.9, 4.9) dias, fiz uso dessa pois é a mesma utilizada pelo CMMID. É importante ressaltar que outros autores sugerem o uso de outras distribuições com outros parâmetros. Por exemplo, [1] sugere uma uma Weibull com média 5 e desvio 1.9. [2] uma Normal com média 6.70 e desvio 3.32 (estranhamente, aqui a Normal pode assumir valores negativos). Nos meus poucos experimentos, percebi que o uso da Weibull ou Lognormal gera plots similares.

### Sobre os Gráficos

Cada gráfico mostra a estimativa do R(t) além de um intervalo de credibilidade de 95%. De forma simples, interprete o intervalo como sendo uma faixa de incerteza onde podemos esperar o valor. Sendo o método Bayesiano, o mesmo captura a probabilidade a posteriori do R(t) nas amostras geradas.

### Limitações e Cuidados

A principal limitação deste estudo é na corretude dos dados. Com poucos testes sendo feitos, é impossível afirmar os resultados atuais não devem mudar nos próximos dias. Isto é, quando novos resultados de laboratório forem aparecendo. **No momento, acredito que é sensato manter a quarentena.**

Além do mais, as estimativas têm uma grande variabilidade no tempo capturando efeitos como fins de semanas, capacidade de testes, diferentes cidades. Minha estimativa é que apenas quando observamos um **R(t) < 1** por várias semanas é que estaremos mais seguros.

## Brasil

### R(t) no Brasil
![Brasil](plots/Brasil.png)

### Comparativo por Estado do último valor
![Comparativo](plots/comparativo.png)

## Centro Oeste

### Distrito Federal

#### Estado como um todo
![Distrito Federal](plots/Centro-Oeste/DF.png)

#### Capital
![Distrito Federal - Brasília](plots/Centro-Oeste/DF-Brasília.png)

### Goiás

#### Estado como um todo
![Goiás](plots/Centro-Oeste/GO.png)

#### Capital
![Goiás - Goiânia.png](plots/Centro-Oeste/GO-Goiânia.png)

### Mato Grosso do Sul

#### Estado como um todo
![Mato Grosso do Sul](plots/Centro-Oeste/MS.png)

#### Capital
![Mato Grosso do Sul - Campo Grande](plots/Centro-Oeste/MS-Campo Grande.png)

### Mato Grosso

#### Estado como um todo
![Mato Grosso](plots/Centro-Oeste/MT.png)

#### Capital
![Mato Grosso do Sul - Cuiabá](plots/Centro-Oeste/MT-Cuiabá.png)


## Nordeste

### Alagoas

#### Estado como um todo
![Alagoas](plots/Nordeste/AL.png)

#### Capital
![Alagoas - Maceió](plots/Nordeste/AL-Maceió.png)

### Bahia

#### Estado como um todo
![Bahia](plots/Nordeste/BA.png)

#### Capital
![Bahia - Salvador](plots/Nordeste/BA-Salvador.png)

### Ceará

#### Estado como um todo
![Ceará](plots/Nordeste/CE.png)

#### Capital
![Ceará - Fortaleza](plots/Nordeste/CE-Fortaleza.png)


### Maranhão

#### Estado como um todo
![Maranhão](plots/Nordeste/MA.png)

#### Capital
![Maranhão - São Luís](plots/Nordeste/MA-São Luís.png)

### Paraíba

#### Estado como um todo
![Paraíba](plots/Nordeste/PB.png)

#### Capital
![Paraíba - João Pessoa](plots/Nordeste/PB-João Pessoa.png)

### Pernambuco

#### Estado como um todo
![Pernambuco](plots/Nordeste/PE.png)

#### Capital
![Pernambuco - Recife](plots/Nordeste/PE-Recife.png)

### Piaui

#### Estado como um todo
![Piauí](plots/Nordeste/PI.png)

#### Capital
![Piauí - Teresina](plots/Nordeste/PI - Teresina.png)

### Rio Grande do Norte

#### Estado como um todo
![Rio Grande do Norte](plots/Nordeste/RN.png)

#### Capital
![Rio Grande do Norte - Natal](plots/Nordeste/RN-Natal.png)


### Sergipe

#### Estado como um todo
![Sergipe](plots/Nordeste/SE.png)

#### Capital
![Sergipe - Aracaju](plots/Nordeste/SE-Aracaju.png)


## Norte

### Acre

#### Estado como um todo
![Acre](plots/Norte/AC.png)

#### Capital
![Acre - Rio Branco](plots/Norte/AC-Rio%20Branco.png)


### Amazonas

#### Estado como um todo
![Amazonas](plots/Norte/AM.png)

#### Capital
![Amazonas - Manaus](plots/Norte/AM-Manaus.png)


### Amapá

#### Estado como um todo
![Amapá](plots/Norte/AP.png)

#### Capital
![Amapá - Macapá](plots/Norte/AP-Macapá.png)


### Pará

#### Estado como um todo
![Pará](plots/Norte/PA.png)

#### Capital
![Pará - Belém](plots/Norte/PA-Belém.png)


### Roraima

#### Estado como um todo
![Roraima](plots/Norte/RO.png)

#### Capital
![Roraima](plots/Norte/RO-Porto%20Velho.png)


### Tocantins

#### Estado como um todo
![Tocantins](plots/Norte/TO.png)

#### Capital
![Tocantins - Palmas](plots/Norte/TO-Palmas.png)


## Sudeste

### Espirito Santo

#### Estado como um todo
![Espirito Santo](plots/Sudeste/ES.png)

#### Capital
![Espirito Santo - Vitória](plots/Sudeste/ES-Vitória.png)


### Minas Gerais

#### Estado como um todo
![Minas Gerais](plots/Sudeste/MG.png)

#### Capital
![Minas Gerais - Belo Horizonte](plots/Sudeste/MG-Belo%20Horizonte.png)

### Rio de Janeiro

#### Estado como um todo
![Rio de Janeiro](plots/Sudeste/RJ.png)

#### Capital
![Rio de Janeiro - Rio de Janeiro](plots/Sudeste/RJ-Rio%20de%20Janeiro.png)


### São Paulo

#### Estado como um todo
![São Paulo](plots/Sudeste/SP.png)

#### Capital
![São Paulo](plots/Sudeste/SP-São%20Paulo.png)


## Sul

### Paraná

#### Estado como um todo
![Paraná](plots/Sul/PR.png)

#### Capital
![Paraná - Curitiba](plots/Sul/PR-Curitiba.png)


### Rio Grande do Sul

#### Estado como um todo
![Rio Grande do Sul](plots/Sul/RS.png)

#### Capital
![Rio Grande do Sul - Porto Alegre](plots/Sul/RS-Porto%20Alegre.png)


### Santa Catarina

#### Estado como um todo
![Santa Catarina](plots/Sul/SC.png)

#### Capital
![Santa Catarina - Florianópolis](plots/Sul/SC-Florianópolis.png)


## Refs

1. Ferretti L, Wymant C, Kendall M et al. Quantifying dynamics of SARS-CoV-2 transmission suggests that epidemic control and avoidance is feasible through instantaneous digital contact tracing. Online First: 2020. doi:https://doi.org/10.1101/2020.03.08.20032946
1. Ma S, Zhang J, Zeng M, et al. Epidemiological parameters of coronavirus disease 2019: a pooled analysis of publicly reported individual data of 1155 cases from seven countries. Online First: 2020. doi:https://doi.org/doi.org/10.1101/2020.03.21.20040329
1. Nishiura H, Linton NM, Akhmetzhanov AR. Serial interval of novel coronavirus (2019-nCoV) infections. medRxiv Published Online First: 2020. doi:https://doi.org/10.1101/2020.02.03.20019497
1. Thompson R, Stockwin J, Gaalen R van et al. Improved inference of time-varying reproduction numbers during infectious disease outbreaks. Epidemics 2019;29:100356. doi:https://doi.org/10.1016/j.epidem.2019.100356

