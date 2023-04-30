#Automato celular
#Henrique Machado
#15-04-2023
 
Este projeto foi desenvolvido como trabalho prático para a disciplina de Algoritmos e Estruturas de Dados I no curso de Sistemas de Informação pela Universidade Federal dos Vales do Jequitinhonha e Mucuri. A primeira versão do projeto foi desenvolvida na linguagem C++ no ano de 2021 devido a uma das restrições do trabalho. Todavia, como forma de reforçar meus conhecimentos em Python, optei por refazer o projeto. 

O objetivo deste projeto é a simulação de um autômato celular no qual, a partir de uma situação inicial, é possível observar mudanças discretas ao longo do tempo. Essas mudanças criam novas linhas de células: as gerações. Ao utilizamos uma representação baseada somente em 0's e 1's, é possível notar a formação de padrões triangulares limpos sendo formados ao longo do surgimento de novas gerações, que estaria representando a auto-organização do autômato.

Portanto, o feito deste trabalho foi a construção de um autômato celular unidimensional e simples, caracterizado por apenas dois estados e vizinhanças formadas por trios. Devido a essa construção, observam-se 8 possíveis estados para cada vizinhança, levando a um total de 256 possíveis regras (2^8) de funcionamento dos autômatos, todas essas dadas pela representação binária em 8bits dos números inteiros dentro do intervalo de 0 a 255.

Na versão original do trabalho, foi encontrado um empecilho físico para a construção do código, uma vez que a utilização de gerações de muitas células nem sempre era adequada devido aos diferentes tamanhos de tela. Com isso, foram limitadas uma quantidade de gerações e células, dando enfoque à percepção dos padrões. Essa limitação foi, então, mantida nesta nova versão uma vez que o projeto possuía o intuito apenas de reforçar meus conhecimentos da linguagem. 




#Ferramentas utilizadas 
Linguagem: Python 3.11.1
IDE: VS Code
Sistema operacional: Windows 11
