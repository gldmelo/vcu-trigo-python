## Visualização de dados de VCU 

Este código demonstra a visualização de dados de Regiões Homogêneas de Adaptação de Cultivares de Trigo utilizando a linguagem Python com a biblioteca geobr.

Para simplicidade foi renderizada apenas a região Sul do Brasil.

## Como utilizar o código

1) Crie uma pasta local para salvar o arquivo png gerado. Ex. ``C:\var\vcu``

2) Monte uma imagem Docker a partir da pasta do Clone do repositório com o comando:

  ```docker build -t vcu-trigo-python -f Dockerfile .```

3) Utilize o comando abaixo para criar um container docker que executará o script:

  ``docker run -it -v "C:\var\vcu:/var/vcu" --rm vcu-trigo-python``

  Mude o ``C:\var\vcu`` para o diretório do seu computador criado no passo 1. Se estiver em linux utilize um path linux.

## Mapa gerado pelo script
![Mapa gerado pelo Script](https://raw.githubusercontent.com/gldmelo/vcu-trigo-python/main/vcu-trigo.png?raw=true)

## Fonte de dados / Bibliografia
Embrapa Trigo - [Informações técnicas para trigo e triticale: safra 2023](https://www.embrapa.br/busca-de-publicacoes/-/publicacao/1153536/informacoes-tecnicas-para-trigo-e-triticale-safra-2023)
