
# Automatizando Playlists do Spotify Para Utilizar Como Despertador

Recentemente descobri que através do app de relógio do Google é possível utilizar o Spotify como despertador. O problema é que se você escolher uma playlist para tocar ele irá tocar todo dia a primeira música da playlist, então eu resolvi criar um programa para criar e atualizar uma playlist que será utilizada no meu despertador. 

Minha playlist: [Anthony_alarm](https://open.spotify.com/playlist/15wuKoew9XJovVsZJS4TNI?si=SYbOr83nTJ2-K6UH0RfbSw)

## Descrição

Este é um programa simples que automatiza criação de playlists no Spotify. As funções permitem criação de playlists através da função de recomendação de músicas do Spotify, que usa como seed outros artistas, músicas, gêneros e parâmetros como 'energia' da música. O programa gera uma playlist nova a cada semana, baseada em diferentes artistas, a playlist é composta por sete músicas e a cada 24h ocorre uma permutação cíclica na ordem das músicas de forma que a primeira música mude diariamente.

## Execução

Para rodar o programa é necessário criar um aplicativo na página de desenvolvedor do Spotify e usar as credenciais para configurar um arquivo `.env` com as seguintes configurações:

```
SPOTIPY_CLIENT_ID = "..."
SPOTIPY_CLIENT_SECRET = "..."
SPOTIPY_REDIRECT_URI = "..."
```

Ao executar o programa na primeira vez você terá que logar em sua conta do spotify pelo navegador, depois você será redirecionad@ para para uma página e deve copiar o link desta página no terminal. Caso queira manter o programa na nuvem, basta executar o programa simultaneamente na máquina e no seu computador e então copiar o link da página que você for redirecionad@ para a outra máquina. Se houver uma maneira mais direta para fazer isso eu gostaria de saber, obrigado :).
