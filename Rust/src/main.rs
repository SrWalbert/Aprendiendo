const ALFABETO: &str = "abcdefghijklmnopqrstuvwxyz";

fn en_cesar(key: &str, input: &str, checked: bool) -> String {
    let mut desplazamiento: usize = 0;
    let key = key.to_lowercase();
    let input = input.to_lowercase();

    if !checked {
        if key.len() == 1 && ALFABETO.contains(key.chars().next().unwrap()) {
            desplazamiento = ALFABETO.find(key.chars().next().unwrap()).unwrap() + 1;
        } else {
            return "Llave inválida, intente con una llave de un solo caracter alfabético".to_string();
        }
    } else {
        desplazamiento = ALFABETO.find(key.chars().next().unwrap()).unwrap() + 1;
    }

    let mut texto_cifrado = String::new();
    for letra in input.chars() {
        if ALFABETO.contains(letra) {
            let posicion_nueva = (ALFABETO.find(letra).unwrap() + desplazamiento) % 26;
            let letra_nueva = ALFABETO.chars().nth(posicion_nueva).unwrap();
            texto_cifrado.push(letra_nueva);
        } else {
            texto_cifrado.push(letra);
        }
    }
    texto_cifrado
}

fn desen_cesar(key: char, cifrado: &str, checked: bool) -> String {
    let alfabeto = "abcdefghijklmnopqrstuvwxyz";
    let mut desplazamiento = 0;

    if !checked {
        let key = key.to_lowercase().next().unwrap();
        let cifrado = cifrado.to_lowercase();

        if alfabeto.contains(key) {
            desplazamiento = -alfabeto.find(key).unwrap() as isize - 1;
        } else {
            return String::from("Llave inválida, intente con una llave de un solo caracter alfabético");
        }
    } else {
        desplazamiento = -alfabeto.find(key).unwrap() as isize - 1;
    }

    let mut texto_descifrado = String::new();

    for letra in cifrado.chars() {
        if alfabeto.contains(letra) {
            let posicion_actual = alfabeto.find(letra).unwrap() as isize;
            let posicion_nueva = ((posicion_actual + desplazamiento).rem_euclid(26)) as usize;
            let letra_nueva = alfabeto.chars().nth(posicion_nueva).unwrap();
            texto_descifrado.push(letra_nueva);
        } else {
            texto_descifrado.push(letra);
        }
    }

    texto_descifrado
}
fn main() {
    println!("Encriptado en cesar: {}", en_cesar("c", "Hola mundo"));
}
