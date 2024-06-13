#2 - Normalmente um jogo da NBA tem em média um total de 200 pontos
#por jogo, sabe-se que o jogo tem 4 quartos de 12 minutos. Enquanto um
#jogo de futebol do campeonato brasileiro tem em média 2,53 gols por jogo.
#Um jogo de futebol se considerarmos 3 minutos de acréscimos em cada um
#dos tempos, teremos 96 minutos de jogo no total.
#Quantos pontos a mais são marcados proporcionalmente ao tempo em um
#jogo da NBA, do que gols marcados no campeonato brasileiro

pontosNBA = 200
tempoNBA = 4 * 12

pontoFutebol = 2.53
tempoFutebol = 96

mediaNBD = pontosNBA / tempoNBA
mediaFutebol = pontoFutebol / tempoFutebol

print("a quantidade media de pontos em um jogo de NBA", round(mediaNBD,2), "a media de pontos em um jogo de futebol é", round(mediaFutebol,2))
print("sendo assim em um jogo de NBA são marcados", round((mediaNBD - mediaFutebol),2), "a mais por minuto do que em um jogo de futebol")