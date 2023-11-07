## Requisitos

### R1: Inicialização do Jogo
- O jogo deve ser inicializado com um tabuleiro em três dimensões:
  - R1.1 - Fácil (8x8)
  - R1.2 - Intermediário (8x8)
  - R1.3 - Difícil (8x8)

#### Testes de Validação
- Teste: Criar tabuleiro nas dimensões corretas
  - Objetivo: Garantir que o tabuleiro seja criado com as dimensões corretas.
- Teste: Criar tabuleiro tamanho inválido
  - Objetivo: Verificar se o jogo lida adequadamente com tamanhos de tabuleiro inválidos.

### R2: Geração Aleatória de Bombas
- O jogo deve gerar bombas aleatoriamente no tabuleiro no início de cada partida.
- O número de bombas geradas deve corresponder ao número configurado.

#### Testes de Validação e Integração
- Teste: Verificar se o número de bombas geradas corresponde ao número configurado no modo fácil
- Teste: Verificar se o número de bombas geradas corresponde ao número configurado no modo intermediário
- Teste: Verificar se o número de bombas geradas corresponde ao número configurado no modo difícil
- Teste: Posições das bombas no modo intermediário
- Teste: Posições das bombas no modo difícil
- Teste: Posicionar bombas em posição inválida no modo fácil
- Teste: Posicionar bombas em posição inválida no modo intermediário
- Teste: Posicionar bombas em posição inválida no modo difícil
- Teste: Tabuleiro sem bombas no modo fácil
- Teste: Tabuleiro sem bombas no modo intermediário
- Teste: Tabuleiro sem bombas no modo difícil
- Teste: Tabuleiro apenas com bombas
- Teste: Número de bombas maior que o esperado
- Teste: Número de bombas menor que o esperado
- Teste: Posições válidas das bombas nas linhas
- Teste: Posições válidas das bombas nas colunas

### R4: Revelação de Células
- O jogador pode clicar em uma célula para revelar seu conteúdo.
- Se a célula contiver uma bomba, o jogador perde.

#### Testes de Unidade
- Teste: Revelar célula com bomba
- Teste: Revelar célula vazia
- Teste: Revelar célula com bomba no modo intermediário
- Teste: Revelar célula vazia no modo intermediário
- Teste: Revelar célula com bomba no modo difícil
- Teste: Revelar célula vazia no modo difícil

### R6: Vitória
- O jogador vence o jogo quando todas as células seguras forem reveladas.

#### Testes de Unidade
- Teste: Verificar vitória
- Teste: Verificar vitória no modo intermediário
- Teste: Verificar vitória no modo difícil
- Teste: Verificar vitória no modo difícil sem bombas no modo fácil
- Teste: Verificar vitória no modo difícil sem bombas no modo intermediário
- Teste: Verificar vitória no modo difícil sem bombas no modo difícil
- Teste: Verificar vitória no modo difícil apenas com bombas no modo fácil
- Teste: Verificar vitória no modo difícil apenas com bombas no modo intermediário
- Teste: Verificar vitória no modo difícil apenas com bombas no modo difícil

### R7: Reiniciar o Jogo

#### Testes de Regressão
- Teste: Reiniciar o jogo

### R8: Contagem de Tempo

#### Testes de Desempenho
- Teste: Tempo em jogo

### R9: Adicionar Bandeiras

#### Testes de Usabilidade
- Teste: Verificar se o jogador pode adicionar uma bandeira em uma célula
- Teste: Verificar se é possível adicionar bandeira em diferentes níveis e posições

### R10: Remover Bandeiras

#### Testes de Usabilidade
- Teste: Verificar se o jogador pode remover uma bandeira de uma célula
- Teste: Verificar se é possível remover bandeira em diferentes níveis e posições
- Teste: Contador de bandeira

### R11: Atualização da Contagem de Bombas

#### Testes de Caixa Branca
- Teste: Calcular vizinhos sem bomba
- Teste: Calcular vizinhos sem bomba no modo intermediário
- Teste: Calcular vizinhos sem bomba no modo difícil
- Teste: Calcular vizinhos no modo fácil com bombas (1-8 vizinhos)
- Teste: Calcular vizinhos no modo intermediário com bombas (1-8 vizinhos)
- Teste: Calcular vizinhos no modo difícil com bombas (1-8 vizinhos)
- Teste: Verificar se não há vizinhos com bombas no canto superior esquerdo
- Teste: Verificar se não há vizinhos com bombas no canto superior direito
- Teste: Verificar se não há vizinhos com bombas no canto inferior esquerdo
- Teste: Verificar se não há vizinhos com bombas no canto inferior direito
- Teste: Verificar se não há vizinhos com bombas no centro

### R12: Revelação Automática de Áreas Vazias

#### Testes de Caixa Branca
- Teste: Revelar célula sem bomba com vizinhos no modo fácil
- Teste: Revelar célula sem bomba com vizinhos no modo intermediário
- Teste: Revelar célula sem bomba com vizinhos no modo Difícil

### R13: Finalização do Jogo ao Clicar em Bomba

#### Testes de Caixa Branca
- Teste: Finalizar o jogo ao clicar em uma célula com bomba no modo fácil
- Teste: Finalizar o jogo ao clicar em uma célula com bomba no modo intermediário
- Teste: Finalizar o jogo ao clicar em uma célula com bomba no modo difícil

### R14: Opção de Reiniciar Durante o Jogo

#### Testes de Regressão
- Teste: Reiniciar o jogo

### R15: Opção de Sair do Jogo

#### Testes de Regressão
- Teste: Sair do jogo

### R16: Mensagem de Vitória

#### Testes de Aceitação do Usuário
- Teste: Exibir mensagem de vitória
- Teste: Não exibir mensagem de vitória

### R17: Mensagem de Derrota

#### Testes de Aceitação do Usuário
- Teste: Exibir mensagem de derrota
- Teste: Não exibir mensagem de derrota

### R18: Derrota ao Revelar Bomba

#### Testes de Aceitação do Usuário
- Teste: Verificar derrota nos extremos do tabuleiro (cantos superiores e inferiores, centro)

### Interface R18: Seleção de Nível de Dificuldade

#### Testes de Aceitação do Usuário
- Teste: Iniciar jogo no modo fácil
- Teste: Iniciar jogo no modo intermediário
- Teste: Iniciar jogo no modo difícil

### R19: Início de um Novo Jogo

#### Testes de Aceitação do Usuário
- Teste: Iniciar um novo jogo

### R20: Finalização de um Jogo

#### Testes de Aceitação do Usuário
- Teste: Sair do jogo

### R21: Visualização das Bombas

#### Testes de Aceitação do Usuário
- Teste: Mostrar localização das bombas após derrota

### R22: Revelar célula com botão esquerdo

### R23: Adicionar e remover bandeira com botão direito

### R24: Contador de bandeira

#### Testes de Usabilidade
- Teste: Contador de bandeira
