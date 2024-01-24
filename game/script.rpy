# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fabio = Character("Fabio Oya")

image fabioFoto = "Fabio-foto.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show fabioFoto :
        align (0.5, 0.5)

    # These display lines of dialogue.

    fabio "Olá, meu nome é Fabio Oya, e gostaria muito da oportunidade de trabalhar na Oppai-man "

    fabio "Sou formado em econômia pela Puc-SP, e nos ultimos 6 anos fui sócio de uma incorporadora. No momento estou buscando uma transição de carreira para desenvolvimento que acredito que sempre foi minha vocação."

    fabio "Tenho conhecimentos na linguagem Python utilizando o framework Django para desenvolvimento web porem é a primeira vez que utilizo o Renpy"

    fabio "Lendo a documentação do Renpy fiz essa simples visual novel como forma de me apresentar para a Oppai-man"

    fabio "Me ofereço para trabalhar de forma voluntária enquanto estudo toda a documentação do Renpy até que seja capaz de entregar valor a empresa desenvolvendo visual novels de qualidade!"

    fabio "Desde já agradeço a atenção!"


    # This ends the game.

    return
