## Aqui estão as descrição do uso das tecnicas 

## Tópicos

- [Agrupamento - Testes separados por tecnicas](./testes_por_tecnica.md)

## Classe de Equivalência

### Criar tabuleiro nas dimensões corretas:
- **Uso:** Testando diferentes tamanhos de tabuleiros (pequeno, médio, grande) para garantir que a criação do tabuleiro funcione corretamente em cada categoria.

### Criar tabuleiro tamanho inválido:
- **Uso:** Verificar como o jogo lida com tamanhos de tabuleiro que não são permitidos, garantindo que o sistema trate corretamente casos de entrada inválidos.

### Posicionar bombas em posição inválida nos diferentes modos de dificuldade:
- **Uso:** Ao testar diferentes modos de dificuldade (fácil, intermediário, difícil), garantimos que o jogo reaja corretamente quando alguém tenta posicionar bombas em lugares não permitidos.

### Tabuleiro sem bombas nos diferentes modos de dificuldade:
- **Uso:** Utilizando Classe de Equivalência, verificamos se o jogo se comporta conforme esperado quando o tabuleiro não contém bombas, em diferentes níveis de dificuldade.

### Tabuleiro apenas com bombas:
- **Uso:** Testando a resposta do jogo quando o tabuleiro é composto apenas por bombas.

### Posições válidas das bombas nas linhas e colunas:
- **Uso:** Ao testar posições válidas das bombas nas linhas e colunas, utilizamos Classe de Equivalência para verificar a validade das posições, abrangendo diferentes orientações no tabuleiro.

## Análise de Valor Limite

### Revelar célula com bomba, vazia e nos diferentes modos de dificuldade:
- **Uso:** Aplicamos Análise de Valor Limite para explorar situações extremas ao revelar células, verificando se o jogo responde corretamente em diferentes modos de dificuldade.

### Verificar vitória nos diferentes modos de dificuldade:
- **Uso:** Utilizando Análise de Valor Limite, testamos os limites dos cenários de vitória para garantir que o sistema reconheça corretamente quando o jogador vence, independentemente do modo de dificuldade escolhido.

### Game over - Sim e Não:
- **Uso:** Aplicamos Análise de Valor Limite para explorar situações extremas de vitória e derrota, garantindo que o sistema responda conforme o esperado em ambos os resultados.

## Relação de Vizinhança

### Uso:
- **Uso:** Testamos a relação de vizinhança para explorar cenários extremos relacionados à contagem de vizinhos com bombas. Isso ajuda a garantir que o sistema se comporte corretamente em condições limite em termos de vizinhança de bombas.
