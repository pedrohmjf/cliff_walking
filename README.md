# Cliff Walking Com Q-Learning

_Cliff Walking_ é um problema simples mas, ao mesmo tempo, muito interessante para testar a validade de modelos de _Reinforcement Learning_ (Aprendizagem por Reforço). Nele, há um _grid-world_ de tamanho 4x12. O objetivo do agente, que inicia na posição [4, 1] (ou [3, 0], se pensarmos que a indexação inicia em 0) é chegar ao prêmio, que se encontra na posição [4, 12] (ou [3, 11]). Porém, há um abismo, que se extende da posição [4, 2] até a posição [4, 11]. O agente deve chegar ao prêmio contornando o abismo.

Esse é um ótimo problema, que testa a convergência e a rapidez de métodos de Aprendizado por Reforço, como é o caso do _Q-Leaarning_.

![cliff](https://github.com/pedrohmjf/cliff_walking/assets/126244260/c4bd4048-56b9-4b7d-a586-d988f8ff9c3c)

O episódio termina quando o agente alcança o onjetivo. Sempre que ele cai no abismo, retorna para onde começou.
