# razrv3telegram.py
O sucessor desse projeto é https://github.com/bolander2000/razrv3telegram

## Descrição
Protótipo da interface web do telegram para o motorola v3, feita em python e bash, diferentemente da interface feita em php, esse servidor usava-se do método Webhook da API do telegram, foi utilizado também o ngrok (tunel ssh para localhost) para facilitar o prototipagem. 

A biblioteca usada para montar o servidor web para python foi a biblioteca bottle e diferentemente da interface php, não foi utilizado nenhum banco de dados mySQL, os dados em estrutura JSON eram todos processados por scripts bash (usando o comando sed) e pelo comando jq (sed para json), quando processados eram armazenados em arquivos textos que eram assim upados para o localhost (com acesso pelo ngrok) pelo servidor bottle.

Esse servidor somente exibia mensagens, não mandava mensagens para o telegram.

Por ser um emaranhado de código, ser lento para processar os dados e por não ter acesso ao serviço pago do ngrok, decide reescrever a interface em php e mySQL e montar um servidor LAMP.


