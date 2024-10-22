# Neste problema, você terá acesso aos registros de banco de dados referentes ao acervo
# de livros e membros de uma biblioteca pertencente à uma instituição de ensino. Cada
# livro é composto por um título, lista de autores, edição, e quantidade de exemplares
# disponíveis na biblioteca. Implemente as funcionalidades de locação e entrega de
# exemplares do programa. Atente-se que, durante o processo de locação, é registrado a
# matrícula do membro da biblioteca que está alocando o livro, o dia da locação e o dia da
# devolução, 15 dias corridos após a data de locação. Já no processo de devolução,
# implemente as funcionalidades de verificação do título do livro devolvido, existência de
# atraso e a reposição das quantidades alocadas. Caso haja atraso na entrega, o membro
# deverá ser multado em R$ 10,00 por dia de atraso. Membros não pertencentes à
# instituição não podem alocar livros. Por fim, dê a opção do usuário do sistema informar
# uma data de início e fim para obter um relatório das alocações, devoluções, quantidades
# de atrasos e o total em reais pago em multas por cada membro.
import datetime

livros = [
  
  {
    
    "titulo": 1984,
    "autores": "George Orwell",
    "edicao": 1,
    "quantidade": 5
  },
  {
    "titulo": "Cem Anos de Solidão",
    "autores": "Gabriel García Márquez",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Dom Quixote",
    "autores": "Miguel de Cervantes",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "A Metamorfose",
    "autores": "Franz Kafka",
    "edicao": 3,
    "quantidade": 6
  },
  {
    "titulo": "O Pequeno Príncipe",
    "autores": "Antoine de Saint-Exupéry",
    "edicao": 1,
    "quantidade": 7
  },
  {
    "titulo": "Crime e Castigo",
    "autores": "Fiódor Dostoiévski",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Senhor dos Anéis",
    "autores": "J.R.R. Tolkien",
    "edicao": 3,
    "quantidade": 5
  },
  {
    "titulo": "Orgulho e Preconceito",
    "autores": "Jane Austen",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "O Grande Gatsby",
    "autores": "F. Scott Fitzgerald",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Ulisses",
    "autores": "James Joyce",
    "edicao": 1,
    "quantidade": 2
  },
  {
    "titulo": "Moby Dick",
    "autores": "Herman Melville",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "A Divina Comédia",
    "autores": "Dante Alighieri",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Hamlet",
    "autores": "William Shakespeare",
    "edicao": 3,
    "quantidade": 5
  },
  {
    "titulo": "O Apanhador no Campo de Centeio",
    "autores": "J.D. Salinger",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "O Processo",
    "autores": "Franz Kafka",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "A Revolução dos Bichos",
    "autores": "George Orwell",
    "edicao": 1,
    "quantidade": 6
  },
  {
    "titulo": "O Retrato de Dorian Gray",
    "autores": "Oscar Wilde",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Morro dos Ventos Uivantes",
    "autores": "Emily Brontë",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Os Miseráveis",
    "autores": "Victor Hugo",
    "edicao": 2,
    "quantidade": 5
  },
  {
    "titulo": "Madame Bovary",
    "autores": "Gustave Flaubert",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Anna Karenina",
    "autores": "Lev Tolstói",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Coração das Trevas",
    "autores": "Joseph Conrad",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Lolita",
    "autores": "Vladimir Nabokov",
    "edicao": 2,
    "quantidade": 2
  },
  {
    "titulo": "As Vinhas da Ira",
    "autores": "John Steinbeck",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "O Som e a Fúria",
    "autores": "William Faulkner",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Velho e o Mar",
    "autores": "Ernest Hemingway",
    "edicao": 1,
    "quantidade": 5
  },
  {
    "titulo": "O Estrangeiro",
    "autores": "Albert Camus",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Hobbit",
    "autores": "J.R.R. Tolkien",
    "edicao": 1,
    "quantidade": 6
  },
  {
    "titulo": "A Ilíada",
    "autores": "Homero",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "A Odisseia",
    "autores": "Homero",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Nome da Rosa",
    "autores": "Umberto Eco",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Lobo da Estepe",
    "autores": "Hermann Hesse",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Jogo da Amarelinha",
    "autores": "Julio Cortázar",
    "edicao": 2,
    "quantidade": 2
  },
  {
    "titulo": "O Amor nos Tempos do Cólera",
    "autores": "Gabriel García Márquez",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "A Insustentável Leveza do Ser",
    "autores": "Milan Kundera",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Os Irmãos Karamázov",
    "autores": "Fiódor Dostoiévski",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Conde de Monte Cristo",
    "autores": "Alexandre Dumas",
    "edicao": 2,
    "quantidade": 5
  },
  {
    "titulo": "O Vermelho e o Negro",
    "autores": "Stendhal",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Retrato da Senhora",
    "autores": "Henry James",
    "edicao": 2,
    "quantidade": 2
  },
  {
    "titulo": "As Flores do Mal",
    "autores": "Charles Baudelaire",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Idiota",
    "autores": "Fiódor Dostoiévski",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "A Montanha Mágica",
    "autores": "Thomas Mann",
    "edicao": 1,
    "quantidade": 2
  },
  {
    "titulo": "O Castelo",
    "autores": "Franz Kafka",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Estranho Caso do Dr. Jekyll e Mr. Hyde",
    "autores": "Robert Louis Stevenson",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "O Homem Sem Qualidades",
    "autores": "Robert Musil",
    "edicao": 2,
    "quantidade": 2
  },
  {
    "titulo": "O Leopardo",
    "autores": "Giuseppe Tomasi di Lampedusa",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Ficções",
    "autores": "Jorge Luis Borges",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Mestre e Margarida",
    "autores": "Mikhail Bulgákov",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "A Peste",
    "autores": "Albert Camus",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "Crônica de uma Morte Anunciada",
    "autores": "Gabriel García Márquez",
    "edicao": 1,
    "quantidade": 5
  },
  {
    "titulo": "O Segundo Sexo",
    "autores": "Simone de Beauvoir",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Memórias Póstumas de Brás Cubas",
    "autores": "Machado de Assis",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "Dom Casmurro",
    "autores": "Machado de Assis",
    "edicao": 2,
    "quantidade": 5
  },
  {
    "titulo": "Grande Sertão: Veredas",
    "autores": "João Guimarães Rosa",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Vidas Secas",
    "autores": "Graciliano Ramos",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "Capitães da Areia",
    "autores": "Jorge Amado",
    "edicao": 1,
    "quantidade": 5
  },
  {
    "titulo": "O Cortiço",
    "autores": "Aluísio Azevedo",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "Macunaíma",
    "autores": "Mário de Andrade",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "A Hora da Estrela",
    "autores": "Clarice Lispector",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Guarani",
    "autores": "José de Alencar",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Iracema",
    "autores": "José de Alencar",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "Quincas Borba",
    "autores": "Machado de Assis",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Ateneu",
    "autores": "Raul Pompeia",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "A Moreninha",
    "autores": "Joaquim Manuel de Macedo",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "Memórias de um Sargento de Milícias",
    "autores": "Manuel Antônio de Almeida",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Mulato",
    "autores": "Aluísio Azevedo",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Triste Fim de Policarpo Quaresma",
    "autores": "Lima Barreto",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "São Bernardo",
    "autores": "Graciliano Ramos",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Angústia",
    "autores": "Graciliano Ramos",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "A Paixão Segundo G.H.",
    "autores": "Clarice Lispector",
    "edicao": 1,
    "quantidade": 2
  },
  {
    "titulo": "Laços de Família",
    "autores": "Clarice Lispector",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "Sagarana",
    "autores": "João Guimarães Rosa",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Quinze",
    "autores": "Rachel de Queiroz",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "Fogo Morto",
    "autores": "José Lins do Rego",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Terras do Sem Fim",
    "autores": "Jorge Amado",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Mar Morto",
    "autores": "Jorge Amado",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "A Bagaceira",
    "autores": "José Américo de Almeida",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Tempo e o Vento",
    "autores": "Érico Veríssimo",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "Incidente em Antares",
    "autores": "Érico Veríssimo",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Memórias Sentimentais de João Miramar",
    "autores": "Oswald de Andrade",
    "edicao": 1,
    "quantidade": 2
  },
  {
    "titulo": "Serafim Ponte Grande",
    "autores": "Oswald de Andrade",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Brás, Bexiga e Barra Funda",
    "autores": "Antônio de Alcântara Machado",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "A Escrava Isaura",
    "autores": "Bernardo Guimarães",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "O Seminarista",
    "autores": "Bernardo Guimarães",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Gaúcho",
    "autores": "José de Alencar",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Tronco do Ipê",
    "autores": "José de Alencar",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Lucíola",
    "autores": "José de Alencar",
    "edicao": 2,
    "quantidade": 4
  },
  {
    "titulo": "A Viuvinha",
    "autores": "José de Alencar",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Til",
    "autores": "José de Alencar",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Sertanejo",
    "autores": "José de Alencar",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "O Cabeleira",
    "autores": "Franklin Távora",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "O Alienista",
    "autores": "Machado de Assis",
    "edicao": 1,
    "quantidade": 5
  },
  {
    "titulo": "Esaú e Jacó",
    "autores": "Machado de Assis",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Memorial de Aires",
    "autores": "Machado de Assis",
    "edicao": 1,
    "quantidade": 3
  },
  {
    "titulo": "Casa Velha",
    "autores": "Machado de Assis",
    "edicao": 2,
    "quantidade": 3
  },
  {
    "titulo": "Helena",
    "autores": "Machado de Assis",
    "edicao": 1,
    "quantidade": 4
  },
  {
    "titulo": "Ressurreição",
    "autores": "Machado de Assis",
    "edicao": 2,
    "quantidade": 3
  }
]
membros = [
  {
    "matricula": 20230001,
    "nome": "João Silva"
  },
  {
    "matricula": 20230002,
    "nome": "Maria Santos"
  },
  {
    "matricula": 20230003,
    "nome": "Pedro Oliveira"
  },
  {
    "matricula": 20230004,
    "nome": "Ana Rodrigues"
  },
  {
    "matricula": 20230005,
    "nome": "Carlos Ferreira"
  },
  {
    "matricula": 20230006,
    "nome": "Mariana Costa"
  },
  {
    "matricula": 20230007,
    "nome": "José Pereira"
  },
  {
    "matricula": 20230008,
    "nome": "Fernanda Almeida"
  },
  {
    "matricula": 20230009,
    "nome": "Antonio Carvalho"
  },
  {
    "matricula": 20230010,
    "nome": "Juliana Martins"
  },
  {
    "matricula": 20230011,
    "nome": "Lucas Souza"
  },
  {
    "matricula": 20230012,
    "nome": "Beatriz Lima"
  },
  {
    "matricula": 20230013,
    "nome": "Rafael Gomes"
  },
  {
    "matricula": 20230014,
    "nome": "Camila Barbosa"
  },
  {
    "matricula": 20230015,
    "nome": "Marcelo Ribeiro"
  },
  {
    "matricula": 20230016,
    "nome": "Larissa Alves"
  },
  {
    "matricula": 20230017,
    "nome": "Gabriel Pinto"
  },
  {
    "matricula": 20230018,
    "nome": "Isabela Correia"
  },
  {
    "matricula": 20230019,
    "nome": "Thiago Fernandes"
  },
  {
    "matricula": 20230020,
    "nome": "Aline Mendes"
  },
  {
    "matricula": 20230021,
    "nome": "Bruno Castro"
  },
  {
    "matricula": 20230022,
    "nome": "Carolina Nunes"
  },
  {
    "matricula": 20230023,
    "nome": "Diogo Ramos"
  },
  {
    "matricula": 20230024,
    "nome": "Elisa Cardoso"
  },
  {
    "matricula": 20230025,
    "nome": "Fábio Teixeira"
  },
  {
    "matricula": 20230026,
    "nome": "Gabriela Moreira"
  },
  {
    "matricula": 20230027,
    "nome": "Henrique Dias"
  },
  {
    "matricula": 20230028,
    "nome": "Inês Cavalcanti"
  },
  {
    "matricula": 20230029,
    "nome": "Júlio Melo"
  },
  {
    "matricula": 20230030,
    "nome": "Kátia Nascimento"
  },
  {
    "matricula": 20230031,
    "nome": "Leandro Aragão"
  },
  {
    "matricula": 20230032,
    "nome": "Mônica Borges"
  },
  {
    "matricula": 20230033,
    "nome": "Nuno Coelho"
  },
  {
    "matricula": 20230034,
    "nome": "Olga Rezende"
  },
  {
    "matricula": 20230035,
    "nome": "Paulo Xavier"
  },
  {
    "matricula": 20230036,
    "nome": "Quitéria Uchoa"
  },
  {
    "matricula": 20230037,
    "nome": "Renato Vieira"
  },
  {
    "matricula": 20230038,
    "nome": "Sandra Duarte"
  },
  {
    "matricula": 20230039,
    "nome": "Tiago Fonseca"
  },
  {
    "matricula": 20230040,
    "nome": "Úrsula Barros"
  },
  {
    "matricula": 20230041,
    "nome": "Vitor Nogueira"
  },
  {
    "matricula": 20230042,
    "nome": "Wanda Esteves"
  },
  {
    "matricula": 20230043,
    "nome": "Xavier Peixoto"
  },
  {
    "matricula": 20230044,
    "nome": "Yasmin Guimarães"
  },
  {
    "matricula": 20230045,
    "nome": "Zélio Monteiro"
  },
  {
    "matricula": 20230046,
    "nome": "Amanda Lopes"
  },
  {
    "matricula": 20230047,
    "nome": "Bernardo Cunha"
  },
  {
    "matricula": 20230048,
    "nome": "Carla Freitas"
  },
  {
    "matricula": 20230049,
    "nome": "Daniel Rocha"
  },
  {
    "matricula": 20230050,
    "nome": "Eduarda Vasconcelos"
  },
  {
    "matricula": 20230051,
    "nome": "Flávio Neves"
  },
  {
    "matricula": 20230052,
    "nome": "Gisele Andrade"
  },
  {
    "matricula": 20230053,
    "nome": "Hugo Medeiros"
  },
  {
    "matricula": 20230054,
    "nome": "Iris Pires"
  },
  {
    "matricula": 20230055,
    "nome": "Jonas Quadros"
  },
  {
    "matricula": 20230056,
    "nome": "Kelly Torres"
  },
  {
    "matricula": 20230057,
    "nome": "Leonardo Brito"
  },
  {
    "matricula": 20230058,
    "nome": "Michele Campos"
  },
  {
    "matricula": 20230059,
    "nome": "Nelson Guerra"
  },
  {
    "matricula": 20230060,
    "nome": "Otávia Siqueira"
  },
  {
    "matricula": 20230061,
    "nome": "Péricles Dantas"
  },
  {
    "matricula": 20230062,
    "nome": "Quênia Galvão"
  },
  {
    "matricula": 20230063,
    "nome": "Ricardo Braga"
  },
  {
    "matricula": 20230064,
    "nome": "Sabrina Tavares"
  },
  {
    "matricula": 20230065,
    "nome": "Tomás Pacheco"
  },
  {
    "matricula": 20230066,
    "nome": "Ulisses Bandeira"
  },
  {
    "matricula": 20230067,
    "nome": "Valéria Magalhães"
  },
  {
    "matricula": 20230068,
    "nome": "Wagner Leal"
  },
  {
    "matricula": 20230069,
    "nome": "Ximena Cordeiro"
  },
  {
    "matricula": 20230070,
    "nome": "Yuri Figueiredo"
  },
  {
    "matricula": 20230071,
    "nome": "Zara Pessoa"
  },
  {
    "matricula": 20230072,
    "nome": "Adriano Sampaio"
  },
  {
    "matricula": 20230073,
    "nome": "Bianca Maia"
  },
  {
    "matricula": 20230074,
    "nome": "Cássio Aguiar"
  },
  {
    "matricula": 20230075,
    "nome": "Débora Vargas"
  },
  {
    "matricula": 20230076,
    "nome": "Edmundo Viana"
  },
  {
    "matricula": 20230077,
    "nome": "Flávia Queiroz"
  },
  {
    "matricula": 20230078,
    "nome": "Gustavo Padilha"
  },
  {
    "matricula": 20230079,
    "nome": "Helena Paiva"
  },
  {
    "matricula": 20230080,
    "nome": "Ivan Mota"
  },
  {
    "matricula": 20230081,
    "nome": "Joana Bastos"
  },
  {
    "matricula": 20230082,
    "nome": "Kleber Gonzaga"
  },
  {
    "matricula": 20230083,
    "nome": "Lúcia Bezerra"
  },
  {
    "matricula": 20230084,
    "nome": "Maurício Abreu"
  },
  {
    "matricula": 20230085,
    "nome": "Natália Vidal"
  },
  {
    "matricula": 20230086,
    "nome": "Osvaldo Damasceno"
  },
  {
    "matricula": 20230087,
    "nome": "Priscila Rangel"
  },
  {
    "matricula": 20230088,
    "nome": "Quirino Botelho"
  },
  {
    "matricula": 20230089,
    "nome": "Raquel Prado"
  },
  {
    "matricula": 20230090,
    "nome": "Sérgio Frota"
  },
  {
    "matricula": 20230091,
    "nome": "Tatiana Portela"
  },
  {
    "matricula": 20230092,
    "nome": "Ulisses Mesquita"
  },
  {
    "matricula": 20230093,
    "nome": "Viviane Farias"
  },
  {
    "matricula": 20230094,
    "nome": "Wellington Rego"
  },
  {
    "matricula": 20230095,
    "nome": "Xuxa Batista"
  },
  {
    "matricula": 20230096,
    "nome": "Yago Domingues"
  },
  {
    "matricula": 20230097,
    "nome": "Zélia Falcão"
  },
  {
    "matricula": 20230098,
    "nome": "Artur Mendonça"
  },
  {
    "matricula": 20230099,
    "nome": "Bruna Holanda"
  },
  {
    "matricula": 20230100,
    "nome": "César Junqueira"
  }
]

locacoes = [
    {
        "livro": "1984",
        "membro": 20230001,
        "data_locacao": "2023-11-20",
        "data_devolucao": "2023-12-05"
    },
    # ... outras locações
]

def menu():
    print("1. Realizar locação")
    print("2. Realizar devolução")
    print("3. Gerar relatório")
    print("4. Sair")

def locar_livro(livro, membro, data_locacao):
    for livro_info in livros:
        if livro_info["titulo"] == livro:
            for membro_info in membros:
                if membro_info["matricula"] == membro:
                    print("Membro não pertence à instituição.")
                    return
            if livro_info["quantidade"] == 0:
                print("Não há exemplares disponíveis deste livro.")
                return

            locacoes.append({
                "livro": livro,
                "membro": membro,
                "data_locacao": data_locacao,
                "data_devolucao": (datetime.datetime.strptime(data_locacao, "%Y-%m-%d") + datetime.timedelta(days=15)).strftime("%Y-%m-%d")
            })
            livro_info["quantidade"] -= 1
            print("Livro locado com sucesso!")
            return 

    print("Livro não encontrado.")
def devolver_livro(livro, membro, data_devolucao):
    for locacao in locacoes:
        if locacao["livro"] == livro and locacao["membro"] == membro:
            data_devolucao_esperada = locacao["data_devolucao"]
            if data_devolucao > data_devolucao_esperada:
                dias_atraso = (datetime.datetime.strptime(data_devolucao, "%Y-%m-%d") - datetime.datetime.strptime(data_devolucao_esperada, "%Y-%m-%d")).days
                multa = dias_atraso * 10
                print(f"Livro devolvido com {dias_atraso} dias de atraso. Multa de R$ {multa:.2f}.")
            else:
                print("Livro devolvido com sucesso.")
            locacoes.remove(locacao)
            livros[livro]["quantidade"] += 1
            return
    print("Locação não encontrada.")

def gerar_relatorio(data_inicio, data_fim):
    relatorio = {}
    for locacao in locacoes:
        data_loc = datetime.datetime.strptime(locacao["data_locacao"], "%Y-%m-%d")
        if data_inicio <= data_loc <= data_fim:
            membro = locacao["membro"]
            if membro not in relatorio:
                relatorio[membro] = {
                    "locacoes": 1,
                    "devolucoes": 0,
                    "atrasos": 0,
                    "multa": 0
                }
            else:
                relatorio[membro]["locacoes"] += 1
            # ... calcular devoluções, atrasos e multas

    # Imprimir o relatório formatado
    for membro, dados in relatorio.items():
        print(f"Membro {membro}:")
        print(f"  Locações: {dados['locacoes']}")
        # ... imprimir outros dados
while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        livro = input("Digite o título do livro: ")
        membro = input("Digite a matrícula do membro: ")
        data_locacao = input("Digite a data da locação (YYYY-MM-DD): ")
        locar_livro(livro, membro, data_locacao)
    elif opcao == 2:
        livro = input("Digite o título do livro: ")
        membro = input("Digite a matrícula do membro: ")
        data_devolucao = input("Digite a data da devolução (YYYY-MM-DD): ")
        devolver_livro(livro, membro, data_devolucao)
    elif opcao == 3:
        data_inicio = input("Digite a data de início do relatório (YYYY-MM-DD): ")
        data_fim = input("Digite a data de fim do relatório (YYYY-MM-DD): ")
        gerar_relatorio(data_inicio, data_fim)
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")
