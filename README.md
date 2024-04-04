# Relatório do Servidor Web

## Introdução
Servidor web desenvolvido em Python utilizando sockets. O servidor é capaz de atender solicitações HTTP GET, retornando os recursos solicitados aos clientes, bem como lidar com casos de recursos não encontrados.

## Funcionalidades
O servidor possui as seguintes funcionalidades:
- Recebe solicitações HTTP GET de clientes.
- Retorna os recursos solicitados aos clientes.
- Lida com casos de recursos não encontrados, retornando o código de status "404 Not Found".
- Suporta diferentes tipos de conteúdo, como HTML, JPEG e texto.

## Teste do Servidor
O servidor foi testado utilizando um navegador web. Os seguintes testes foram realizados:

1. **Acesso à Página Principal:**
   - Abriu-se um navegador.
   - Digitou-se o endereço IP e a porta do servidor na barra de endereços.
   - Verificou-se se a página principal foi carregada corretamente, incluindo imagens e texto.

2. **Recursos Não Encontrados:**
   - Tentou-se acessar arquivos que não existiam para verificar se o servidor retornava corretamente a mensagem de erro "404 Not Found".

## Observações
Durante os testes, observou-se o seguinte:
- Os cabeçalhos HTTP foram enviados corretamente, incluindo os cabeçalhos de resposta "Content-Type".
- O servidor respondeu corretamente às solicitações GET, retornando os recursos solicitados.
- Quando um recurso não foi encontrado, o servidor retornou corretamente a mensagem de erro "404 Not Found".

## Conclusão
O servidor web foi desenvolvido com sucesso e passou nos testes realizados. Ele é capaz de atender solicitações HTTP GET, retornando os recursos solicitados, e lida adequadamente com casos de recursos não encontrados. O código fonte está disponível nesse repositório.
