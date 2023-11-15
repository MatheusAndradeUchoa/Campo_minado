

# Requisitos Funcionais:

## R1: Inicialização do Jogo
O jogo deve ser inicializado com um tabuleiro em três dimensões.
- R1.1: (8x8)
- R1.2: (10x16)
- R1.3: (24x24)

### Testes:
- teste criar tabuleiro nas dimensões corretas
- facil
- medio 
- dificl
- invalidas 
- testes criar tabuleiro tamanho invalido 


## R2: Geração Aleatória de Bombas
O jogo deve gerar bombas aleatoriamente no tabuleiro no início de cada partida.
- R2.1: 10 bombas
- R2.2: 30 bombas
- R2.3: 100 bombas

### Testes:
- Teste: Verificar se o número de bombas geradas corresponde ao número configurado no modo fácil
- Teste: Verificar se o número de bombas geradas corresponde ao número configurado no modo intermediário
- Teste: Verificar se o número de bombas geradas corresponde ao número configurado no modo difícil
- test_posicoes_bombas__modo_intermediario
- test_posicoes_bombas__modo_dificil
- test_posicionar_bombas_posicao_invalida_modo_facil
- test_posicionar_bombas_posicao_invalida_modo_intermediario
- test_posicionar_bombas_posicao_invalida_modo_dificil
- test_tabuleiro_sem_bombas_facil
- test_tabuleiro_sem_bombas_intermediario
- test_tabuleiro_sem_bombas_dificl test_tabuleiro_apenas_bombas
- test_numero_bombas_maior_que_esperado
- test_numero_bombas_menor_que_esperado
- test_posicoes_validas_das_bombas_linha
- test_posicoes_validas_das_bombas_coluna


## R4: Revelação de Células
O jogador pode clicar em uma célula para revelar seu conteúdo. Se a célula contiver uma bomba, o jogo deve terminar, e o jogador perde.

### Testes:
- test_revelar_celula_com_bomba 
- test_revelar_celula_vazia 
- test_revelar_celula_com_bomba_intermediario 
- test_revelar_celula_vazia_intermediario 
- test_revelar_celula_com_bomba_dificil 
- test_revelar_celula_vazia_difi

## R6: Vitória
O jogador vence o jogo quando todas as células seguras forem reveladas.

### Testes:
- test_verificar_vitoria
- test_verificar_vitoria_intermediario
- test_verificar_vitoria_dificil
- test_verificar_vitoria_dificil_sem_bombas_facil
- test_verificar_vitoria_dificil_sem_bombas_intermediario
- test_verificar_vitoria_dificil_sem_bombas_dificil
- test_verificar_vitoria_dificil_apenas_bombas_facil
- test_verificar_vitoria_dificil_apenas_bombas_intermediario
- test_verificar_vitoria_dificil_apenas_bombas_dificil


## R7: Reiniciar o Jogo
O jogo deve permitir ao jogador reiniciar a partida após vitória ou derrota.

## R8: Contagem de Tempo
O jogo deve contar o tempo desde o início da partida até a sua conclusão (vitória ou derrota).

### Teste:
- Testar o registro correto do tempo durante a partida

## R9: Adicionar Bandeiras
O jogador pode colocar bandeiras em células para indicar onde acredita que há bombas.

### Testes:
- Testar se o jogador pode colocar uma bandeira em uma célula
- Testar adição de bandeira em diferentes níveis e posições

## R10: Remover Bandeiras
O jogador pode remover bandeiras.

### Testes:
- Testar se o jogador pode remover uma bandeira de uma célula
- Testar remoção de bandeira em diferentes níveis e posições

## R11: Atualização da Contagem de Bombas
A contagem de bombas vizinhas deve ser atualizada após a revelação de células.

### Testes:
- test_calcular_vizinhos_sem_bomba
- test_calcular_vizinhos_sem_bomba_intermediario
- test_calcular_vizinhos_sem_bomba_dificil
- test_calcular_vizinhos_facil_com_bombas(1-8 vizinhos)
- test_calcular_vizinhos_intermediario_com_bombas(1-8 vizinhos)
- test_calcular_vizinhos_dificil_com_bombas(1-8 vizinhos)
- 
- Canto superior esquerdo: Verificar se não há vizinhos com bombas.
- Canto superior direito: Verificar se não há vizinhos com bombas.
- Canto inferior esquerdo: Verificar se não há vizinhos com bombas.
- Canto inferior direito: Verificar se não há vizinhos com bombas.
- o centro: Verificar se não há vizinhos com bombas.


## R12: Revelação Automática de Áreas Vazias
Se o jogador revelar uma célula vazia, todas as células vizinhas também devem ser reveladas automaticamente.

### Testes:
- Teste: Revelar célula sem bomba com vizinhos no modo fácil
- Teste: Revelar célula sem bomba com vizinhos no modo intermediário
- Teste: Revelar célula sem bomba com vizinhos no modo Difícil


## R13: Finalização do Jogo ao Clicar em Bomba
Se o jogador clicar em uma célula contendo uma bomba, o jogo deve finalizar e mostrar todas as bombas no tabuleiro.

### Testes:
- Testar finalização do jogo ao clicar em célula com bomba em modos fácil, intermediário e difícil

## R14: Opção de Sair do Jogo
O jogador deve ter a opção de sair do jogo a qualquer momento.

### Teste:
- Testar saída do jogo durante uma partida em andamento

## R15: Mensagem de Vitória
Quando o jogador vence o jogo, uma mensagem de vitória deve ser exibida.

### Testes:
- Testar exibição da mensagem de vitória com e sem bombas

## R16: Mensagem de Derrota
Quando o jogador perde o jogo, uma mensagem de derrota deve ser exibida.

### Testes:
- Testar exibição da mensagem de derrota ao clicar em bomba nos modos fácil, intermediário e difícil

## R17: Derrota ao Revelar Bomba
O jogo deve verificar se uma célula com uma bomba foi revelada, encerrando a partida e exibindo uma mensagem de derrota.

### Testes:
- Testar derrota ao revelar bomba nos extremos do tabuleiro e no centro

## R18: Não deve ser possível clicar em área já revelada.
Testar se é impossível clicar em uma célula já revelada.

### Testes:
- Testar impossibilidade de clicar em células já reveladas nos modos fácil, intermediário e difícil

## R19: Não deve ser possível adicionar bandeira em uma área já revelada.
Testar se é impossível adicionar uma bandeira em uma célula já revelada.

### Testes:
- Testar impossibilidade de adicionar bandeira em células já reveladas nos modos fácil, intermediário e difícil

# Requisitos de Interface:

## R25: Seleção de Nível de Dificuldade
1.1 Selecionar Fácil
1.2 Selecionar Médio
1.3 Selecionar Difícil

### Testes:
- Testar a seleção de níveis Fácil, Intermediário e Difícil e verificar se o tabuleiro é configurado corretamente.

## R26: Início de um Novo Jogo
- Testar o início de um novo jogo após selecionar um nível de dificuldade.

## R27: Finalização de um Jogo
- Testar a finalização de um jogo durante uma partida em andamento.

## R28: Revelar Célula com Botão Esquerdo
- Testar a revelação de células ao clicar com o botão esquerdo do mouse.

## R29: Adicionar Bandeira com Botão Direito
- Testar a adição de bandeira ao clicar com o botão direito do mouse.

## R30: Deve Aparecer na Tela a Quantidade de Bandeira
- Testar se o contador de bandeiras é atualizado adequadamente.

## R31: Botão "Reiniciar" no Pop-up de Vitória
- Testar o reinício do jogo ao clicar no botão "Reiniciar" após a vitória.

## R32: Botão "Sair" no Pop-up de Vitória
- Testar o fechamento da aplicação ao clicar no botão "Sair" após a vitória.

## R33: Botão "Reiniciar" no Pop-up de Derrota
- Testar o reinício do jogo ao clicar no botão "Reiniciar" após a derrota.

## R34: Botão "Sair" no Pop-up de Derrota
- Testar o fechamento da aplicação ao clicar no botão "Sair" após a derrota.

## R35: Clicar para Voltar ao Menu
- Testar se é apresentada uma mensagem ao tentar fechar a janela do jogo.

## R36: Bandeiras Iniciais Igual a Zero
- Testar se a contagem inicial de bandeiras é zero no início do jogo.

## R37: Atualizar Contador
- A interface deve atualizar o contador de bandeira.
