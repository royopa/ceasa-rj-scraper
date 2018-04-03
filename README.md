# ceasa-rj-scraper
Captura das cotações diárias de preços no atacado de hortaliças, frutas, cereais, pescado, flores e plantas ornamentais do CEASA-RJ

## Links

http://www.ceasa.rj.gov.br/ceasa_portal/view/ListarCotacoes.asp

## Usando

```sh
> python main.py
```sh

O script lista primeiro todos os PDFs que deverão ser baixados e guarda no arquivo [urls.csv](urls.csv).

Depois o arquivo [urls.csv](urls.csv) é lido e os pdfs são baixados na pasta [downloads](downloads).

