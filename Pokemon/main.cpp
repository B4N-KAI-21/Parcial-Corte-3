#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

class Pokemon {
    string nombre;
    int vida;
    string ataque1;
    int golpe1;
    string ataque2;
    int golpe2;
    string ataque3;
    int golpe3;

public:
    Pokemon(string nombre, int vida, string ataque1, int golpe1, string ataque2, int golpe2, string ataque3, int golpe3)
        : nombre(nombre), vida(vida), ataque1(ataque1), golpe1(golpe1), ataque2(ataque2), golpe2(golpe2), ataque3(ataque3), golpe3(golpe3) {}

    string getNombre() { return nombre; }
    int getVida() { return vida; }
    bool estaVivo() { return vida > 0; }
    void restaurarVida() { vida = 30; }

    void mostrarAtaques() {
        cout << "1. " << ataque1 << " (Impacto: " << golpe1 << ")\n";
        cout << "2. " << ataque2 << " (Impacto: " << golpe2 << ")\n";
        cout << "3. " << ataque3 << " (Impacto: " << golpe3 << ")\n";
    }

    int usarAtaque(int opcion) {
        while (opcion < 1 || opcion > 3) {
            cout << "Opcion invalida. Vuelve a intentarlo: \n";
            mostrarAtaques();
            cin >> opcion;
        }

        switch (opcion) {
            case 1: return golpe1;
            case 2: return golpe2;
            case 3: return golpe3;
        }
        return 0;
    }

    string getNombreAtaque(int opcion) {
        switch (opcion) {
            case 1: return ataque1;
            case 2: return ataque2;
            case 3: return ataque3;
        }
        return "Ataque desconocido";
    }

    void recibirGolpe(int cantidad) {
        vida -= cantidad;
        if (vida < 0) vida = 0;
    }
};

void mostrarMenuObjetos(int pokebolas, int curas, vector<string> pokemonsCapturados) {
    cout << "\n--- MENU DE OBJETOS ---\n";
    cout << "Pokebolas: " << pokebolas << "/3\n";
    cout << "Objetos de curacion: " << curas << "/3\n";
    cout << "Pokemon capturados: ";
    if (pokemonsCapturados.empty()) cout << "Ninguno";
    else for (auto& p : pokemonsCapturados) cout << p << " ";
    cout << "\n------------------------\n";
}

bool intentarCaptura(string nombre, int vecesDerrotado, int& pokebolas, vector<string>& capturados) {
    if (pokebolas <= 0) {
        cout << "No tienes pokebolas suficientes.\n";
        return false;
    }
    pokebolas--;
    int probabilidad = min(20 * vecesDerrotado, 80); // 20%, 40%, 60%, 80%, 100%
    int chance = rand() % 100;
    if (chance < probabilidad) {
        capturados.push_back(nombre);
        cout << "\n\t*** Has capturado a " << nombre << "! ***\n";
        return true;
    } else {
        cout << "\n\t*** El Pokemon ha escapado! ***\n";
        return false;
    }
}

int main() {
    srand(time(0));

    // Pokemons disponibles
    Pokemon pikachu("Pikachu", 30, "Impactrueno", 7, "Cola de hierro", 9, "Rayo", 10);
    Pokemon charmander("Charmander", 30, "Ascuas", 6, "Cuchillada", 6, "Lanzallamas", 9);
    Pokemon squirtle("Squirtle", 30, "Pistola Agua", 6, "Burbuja", 7, "Hidro Bomba", 10);
    Pokemon bulbasaur("Bulbasaur", 30, "Latigo Cepa", 7, "Drenadoras", 5, "Rayo Solar", 10);

    vector<Pokemon> rivales = {charmander, squirtle, bulbasaur};
    vector<int> derrotas(3, 0);
    vector<string> pokemonsCapturados;
    int pokebolas = 0;
    int curas = 0;

    // Elegir tu Pokemon
    cout << "Elige tu Pokemon:\n1. Pikachu\n2. Charmander\n3. Squirtle\n4. Bulbasaur\n";
    int eleccion;
    cin >> eleccion;
    Pokemon jugador = pikachu;
    switch (eleccion) {
        case 1: jugador = pikachu; break;
        case 2: jugador = charmander; break;
        case 3: jugador = squirtle; break;
        case 4: jugador = bulbasaur; break;
        default: cout << "Opcion invalida. Se asigno Pikachu.\n";
    }

    cout << "\nHas elegido a " << jugador.getNombre() << "!\n";

    for (size_t i = 0; i < rivales.size(); ++i) {
        cout << "\n\nComienza el combate contra " << rivales[i].getNombre() << "!\n";
        rivales[i].restaurarVida();
        jugador.restaurarVida();

        int turno = 1;
        while (jugador.estaVivo() && rivales[i].estaVivo()) {
            cout << "\n---- Turno " << turno << " ----\n";
            cout << "1. Atacar\n2. Usar objeto\n";
            int opcion;
            cin >> opcion;
            if (opcion == 2) {
                mostrarMenuObjetos(pokebolas, curas, pokemonsCapturados);
                cout << "Deseas usar curacion? (1=Si, 0=No): ";
                int usar;
                cin >> usar;
                if (usar && curas > 0) {
                    jugador.restaurarVida();
                    curas--;
                    cout << "Tu Pokemon ha sido curado!\n";
                    continue;
                } else if (usar) {
                    cout << "No tienes objetos de curacion.\n";
                    continue;
                }
            }

            cout << jugador.getNombre() << " ataca. Elige ataque:\n";
            jugador.mostrarAtaques();
            int ataque;
            cin >> ataque;
            int golpe = jugador.usarAtaque(ataque);
            cout << jugador.getNombre() << " usa " << jugador.getNombreAtaque(ataque) << " y causa " << golpe << " de impacto.\n";
            rivales[i].recibirGolpe(golpe);
            cout << rivales[i].getNombre() << " tiene " << rivales[i].getVida() << " de vida.\n";
            if (!rivales[i].estaVivo()) break;

            // Turno rival
            ataque = (rand() % 3) + 1;
            golpe = rivales[i].usarAtaque(ataque);
            cout << rivales[i].getNombre() << " usa " << rivales[i].getNombreAtaque(ataque) << " y causa " << golpe << " de impacto.\n";
            jugador.recibirGolpe(golpe);
            cout << jugador.getNombre() << " tiene " << jugador.getVida() << " de vida.\n";

            turno++;
        }

        if (jugador.estaVivo()) {
            cout << "\nHas derrotado a " << rivales[i].getNombre() << "!\n";
            derrotas[i]++;
            if (rand() % 2 == 0 && pokebolas < 3) {
                pokebolas++;
                cout << "Recibiste una Pokebola!\n";
            } else {
            if (curas < 3) {
                curas++;
                cout << "Recibiste un objeto de curacion!\n";
            }
            }

            cout << "\nQuieres intentar capturar a " << rivales[i].getNombre() << "? (1=Si, 0=No): ";
            int intentar;
            cin >> intentar;
            if (intentar == 1) {
                intentarCaptura(rivales[i].getNombre(), derrotas[i], pokebolas, pokemonsCapturados);
            }
        } else {
            cout << "\nTu Pokemon fue derrotado. Fin del juego.\n";
            break;
        }
    }

    if (pokemonsCapturados.size() == 3) {
        cout << "\n*** Felicidades! Has capturado a todos los Pokemon enemigos! ***\n";
    }

    return 0;
}
